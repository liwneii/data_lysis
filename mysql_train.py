from pymysql import *

def main():

    # connection
    conn = connect(host='master', port=3306, user='root', password='', database='mysql_py1', charset='utf8')
    # get Cursor object
    cs1 = conn.cursor()

    # cs1.execute('select * from student;')
    # line_content = cs1.fetchone()
    # print(line_content)
    # print(line_content[0], line_content[1])
    # for tmp in line_content:
    # # (1, 'swk', 18, 'male', 0, None, b'\x00')
    # # 1
    # # swk
    # # 1
    # # swk
    # # 18
    # # male
    # # 0
    # # None
    # # b'\x00'


    # execute select, return rows of selected
    # count = cs1.execute('select id,name from student where id > 1')
    # print("the numbers of rows is %d" % count)
    # data = cs1.fetchone()
    # print(data)
    # data1 = cs1.fetchmany(2)
    # print(data1)
    # data2 = cs1.fetchall()
    # print(data2)
    # # the numbers of rows is 3
    # # (2, 'zbj')
    # # ((3, 'zbj'), (4, 'shs'))
    # # ()


    cs1.execute('select * from student;')
    line_content = cs1.fetchmany(size=2)
    print(line_content)
    print(line_content[0], line_content[1])
    for tmp in line_content:
        print(tmp)
        for tmp_1 in tmp:
            print(tmp_1)
    # ((1, 'swk', 18, 'male', 0, None, b'\x00'), (2, 'zbj', 28, 'male', 0, datetime.date(1999, 9, 9), b'\x01'))
    # (1, 'swk', 18, 'male', 0, None, b'\x00')(2, 'zbj', 28, 'male', 0, datetime.date(1999, 9, 9), b'\x01')
    # (1, 'swk', 18, 'male', 0, None, b'\x00')
    # 1
    # swk
    # 18
    # male
    # 0
    # None
    # b'\x00'
    # (2, 'zbj', 28, 'male', 0, datetime.date(1999, 9, 9), b'\x01')
    # 2
    # zbj
    # 28
    # male
    # 0
    # 1999 - 0
    # 9 - 0
    # 9
    # b'\x01'




    # close Cursor object
    cs1.close()
    conn.close()

if __name__ == '__main__':
    main()














