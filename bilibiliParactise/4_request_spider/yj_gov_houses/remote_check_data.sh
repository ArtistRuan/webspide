#!/bin/sh

# 连接远程机器获取数据传输状态（远程只有nohup.out）
ssh 192.168.174.110 <<EOF
if [ -f /export/servers/nohupa.out ];then
    echo "ok"
else
    echo -e "\e[1;41mno ok file\e[0m\e[1;31m contact the supplier\e[0m `date +"%Y-%m-%d %H%M%S"`"
    exit 1
fi
>>EOF

echo "没有文件，不应该执行这里"
echo $?
