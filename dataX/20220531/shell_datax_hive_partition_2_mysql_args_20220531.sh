#!/bin/sh

# 如果需要，可以调用python将原mysql的目标表清空
python ./truncate_mysql_data.py $1 $2 $3 $4 $5

for dt in `hdfs dfs -ls /user/hive/warehouse/datax.db/hive_partition_source_orc/ | awk -F '=' '{print $2}' | tail -n +2`
do
echo ${dt}
sleep 5
#sed -i 's/partition_column_args/'${dt}'/g' ./datax/job/hive_partition_source_orc_hive_2_mysql_by_shell_args.json

# 通过传参${dt}给json文件，指定分区信息（优化了修改json文件的内容，简洁！）
./datax/bin/datax.py -p "-Ddt=${dt}" ./datax/job/hive_partition_source_orc_hive_2_mysql_by_shell_dy_args_20220531.json

sleep 10
# 执行完毕后将参数重新改回原来的参数
#sed -i 's/'${dt}'/partition_column_args/g' ./datax/job/hive_partition_source_orc_hive_2_mysql_by_shell_args.json
#cat ./datax/job/hive_partition_source_orc_hive_2_mysql_by_shell_args.json
done

