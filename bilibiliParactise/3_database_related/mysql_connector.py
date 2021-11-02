
import pymysql
import pandas as pd

def mysql_con(host,port,user,passwd,db,sql):
    conn = pymysql.connect(host=host,port=port,user=user,passwd=passwd,database=db)  # 连接mysql
    cursor = conn.cursor()  # 创建游标
    cursor.execute(sql)  # 执行sql语句
    result = cursor.fetchall()  # 获取执行结果
    result = [list(x) for x in result]  # 推导式
    col_result = cursor.description  # 获取查询结果的字段描述
    columns = [x[0] for x in col_result]
    print(columns)
    for res in result:
        print(res)

    cursor.close()
    conn.close()

# 将查询结果保存到本地
def mysql_result_save(host,port,user,passwd,db,sql,annex_path):
    conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, database=db)  # 连接mysql
    cursor = conn.cursor()  # 创建游标
    cursor.execute(sql)  # 执行sql语句
    result = cursor.fetchall()  # 获取执行结果
    result = [list(x) for x in result]  # 推导式
    col_result = cursor.description  # 获取查询结果的字段描述
    columns = [x[0] for x in col_result]
    data = pd.DataFrame(result,columns=columns)
    print(data)
    data.to_excel(annex_path,index=False)  # 将数据库数据保存到excel中

    cursor.close()
    conn.close()

def main():
    '''数据库信息'''
    host = 'localhost'
    port = 3306
    user = 'root'
    passwd = '123456'
    db = 'student'
    sql = "select age,name,id,birthday from student;"
    annex_path = 'G:/desktop/pythonProject/bilibiliParactise/3_database_related/student.xls'

    # mysql_con(host,port,user,passwd,db,sql)
    mysql_result_save(host, port, user, passwd, db, sql, annex_path)
if __name__ == '__main__':
    main()