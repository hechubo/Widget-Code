"""""
递归查询指定数据库中某个表的外键关系
"""""
import mysql.connector

def recursive_foreign_keys(database_name, table_name):
    # 创建数据库连接
    connection = mysql.connector.connect(
        host="127.0.0.1",
        port="4306",
        user="root",
        password="123456",
        database=database_name
    )

    # 创建游标对象
    cursor = connection.cursor(dictionary=True)

    # 查询给定表的外键约束
    query = f"""
    SELECT
        CONSTRAINT_NAME,
        COLUMN_NAME,
        REFERENCED_TABLE_NAME,
        REFERENCED_COLUMN_NAME
    FROM
        INFORMATION_SCHEMA.KEY_COLUMN_USAGE
    WHERE
        TABLE_SCHEMA = '{database_name}'
        AND TABLE_NAME = '{table_name}'
        AND REFERENCED_TABLE_NAME IS NOT NULL;
    """

    # 执行查询语句，获取外键约束结果
    cursor.execute(query)
    foreign_keys = cursor.fetchall()

    # 递归查询被引用的表的外键关系
    for foreign_key in foreign_keys:
        referenced_table_name = foreign_key['REFERENCED_TABLE_NAME']
        referenced_column_name = foreign_key['REFERENCED_COLUMN_NAME']
        print(f"Table: {table_name}, Foreign Key: {foreign_key['COLUMN_NAME']} -> Referenced Table: {referenced_table_name}.{referenced_column_name}")

        # 递归调用，继续查询被引用表的外键关系
        recursive_foreign_keys(database_name, referenced_table_name)

    # 关闭游标和数据库连接
    cursor.close()
    connection.close()

# 调用递归查询函数
recursive_foreign_keys('weshare', 'lab_vessel')