
from pyhive import hive


def hive_connection(hql):
    conn = hive.Connection(host='HiveServer2 host', port=10000, database='default')
    cursor = conn.cursor()
    cursor.execute(hql)
    # 获取查询结果
    result = cursor.fetchall()
    for res in result:
        print(res)

    # import pip._internal
    # print(pip._internal.pep425tags.get_supported())
def main(hql):
    hive_connection(hql)

if __name__ == '__main__':
    hql ="select name,orderdate,cost from business;"
    main(hql)