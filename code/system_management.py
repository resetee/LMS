"""
    系统管理模块
    １．用户的增删改查
    ２．权限的增删改查
"""
import pymysql

HOST = "localhost"
USER = "root"
PASSWD = "123456"
DBNAME = "lsm"

db = pymysql.connect(HOST, USER, PASSWD, DBNAME)
cursor = db.cursor()

def add_user(staff_id,user_name,user_pwd):
    sql = "insert into user (staff_id, user_name, " \
          "user_pwd) values('%s','%s','%s')"%(staff_id,
            user_name,user_pwd)
    try:
        cursor.execute(sql)
        db.commit()
        return True
    except Exception:
        db.rollback()
        return False

def delete_user(staff_id):
    sql = "delete * from user where staff_id = '%s'"%staff_id
    try:
        cursor.execute(sql)
        db.commit()
        return True
    except Exception:
        db.rollback()
        return False

def update_user_pwd(user_pwd,staff_id):
    sql = "update user set user_pwd = '%s' where staff_id='%s'"%(user_pwd,staff_id)
    try:
        cursor.execute(sql)
        db.commit()
        return True
    except:
        db.rollback()
        return False

def qurey_user(user_name):
    """
    查询用户密码
    :return:
    """
    sql = "select user_pwd from user where user_name = '%s'"%user_name
    cursor.execute()
    return cursor.fetchall()


# 权限管理
def add_role_name(role_name):
    """
    增加新角色
    :param role_name:
    :return:
    """
    sql = "insert into permission role_name values '%s'"%role_name
    try:
        cursor.execute(sql)
        db.commit()
        return False
    except Exception:
        db.rollback()
        return False

def add_permission():
    """
    增加权限
    :return:
    """
    pass

def delete_permission():
    """
    删除权限
    :return:
    """
    pass

def query_permission():
    """
    查询权限
    :return:
    """
    pass

def update_permission():
    """
    修改权限
    :return:
    """
    pass

