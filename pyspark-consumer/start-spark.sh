#start-spark.sh
#!/bin/bash
. "/opt/spark/bin/load-spark-env.sh"
# When the spark work_load is master run class org.apache.spark.deploy.master.Master
if [ "$SPARK_WORKLOAD" == "master" ];
then

export SPARK_MASTER_HOST=`hostname`

cd /opt/spark/bin && ./spark-class org.apache.spark.deploy.master.Master --ip $SPARK_MASTER_HOST --port $SPARK_MASTER_PORT --webui-port $SPARK_MASTER_WEBUI_PORT >> $SPARK_MASTER_LOG

elif [ "$SPARK_WORKLOAD" == "worker" ];
then
# When the spark work_load is worker run class org.apache.spark.deploy.master.Worker
cd /opt/spark/bin && ./spark-class org.apache.spark.deploy.worker.Worker --webui-port $SPARK_WORKER_WEBUI_PORT $SPARK_MASTER >> $SPARK_WORKER_LOG

elif [ "$SPARK_WORKLOAD" == "submit" ];
then
    echo "SPARK SUBMIT"
    
cd /stock-app && 
/opt/spark/bin/spark-submit  --master spark://spark-master:7077 --total-executor-cores $SPARK_WORKER_CORES --driver-memory $SPARK_DRIVER_MEMORY --executor-memory $SPARK_EXECUTOR_MEMORY --jars kafka-clients-2.4.1.jar,spark-token-provider-kafka-0-10_2.12-3.2.0.jar,commons-pool2-2.6.2.jar,spark-sql-kafka-0-10_2.12-3.2.0.jar --files=configs/config.ini,configs/ticker_schema.json --py-files application.zip data_application.py

else

    echo "Undefined Workload Type $SPARK_WORKLOAD, must specify: master, worker, submit"
fi