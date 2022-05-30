#!/bin/sh

# 将hive的分区表通过datax同步到mysql

# 本脚本为程序的开始，调用方式为：
# sh shell_datax_hive_partition_2_mysql.sh '192.168.174.100' 3306 'datax' 'root' '123456

# 如果需要，可以调用python将原mysql的目标表清空
python ./truncate_mysql_data.py $1 $2 $3 $4 $5

for dt in `hdfs dfs -ls /user/hive/warehouse/datax.db/hive_partition_source_orc/ | awk -F '=' '{print $2}' | tail -n +2`
do
echo ${dt}
sleep 5
sed -i 's/partition_column_args/'${dt}'/g' ./datax/job/hive_partition_source_orc_hive_2_mysql_by_shell_args.json
./datax/bin/datax.py ./datax/job/hive_partition_source_orc_hive_2_mysql_by_shell_args.json


sleep 10
# 执行完毕后将参数重新改回原来的参数
sed -i 's/'${dt}'/partition_column_args/g' ./datax/job/hive_partition_source_orc_hive_2_mysql_by_shell_args.json
cat ./datax/job/hive_partition_source_orc_hive_2_mysql_by_shell_args.json
done

