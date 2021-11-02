#!/bin/python
# -*- coding = UTF-8 -*-

import os

filename='student.txt'
def main():
    menu()
    while True:
        choice = int(input('请输入您的选择：'))
        if choice in [0, 1, 2, 3, 4, 5, 6, 7]:
            if choice == 0:
                answer = input('您确定退出系统吗？y/n')
                if answer == 'Y' or answer == 'y':
                    print('谢谢您的使用！祝您生活愉快！')
                    break
                else:
                    continue
            elif choice == 1:
                insert()
            elif choice == 2:
                search()
            elif choice == 3:
                delete()
            elif choice == 4:
                modify()
            elif choice == 5:
                sort()
            elif choice == 6:
                total()
            elif choice == 7:
                show()

def insert():
    student_list=[]
    while True:
        id=input('请输入ID（如10001）：')
        if not id:
            break
        name=input('请输入姓名')
        if not name:
            break
        try:
            english=int(input('请输入英语成绩：'))
            python=int(input('请输入Python成绩：'))
            java=int(input('请输入Java成绩：'))
        except:
            print('成绩无效，不是整数类型，请重新输入')
            continue
        #将录入的信息保存到字典中
        student={'id':id,'name':name,'english':english,'python':python,'java':java}
        student_list.append(student)
        answer=input('是否继续添加?y/n\n')
        if answer=='y' or answer=='Y':
            continue
        else:
            break
    #输入完毕，退出循环后，调用save()函数保存信息
    save(student_list)
    print('信息录入完毕')
    menu()
def save(lst):
    try:
        stu_txt=open(filename,'a',encoding='utf-8')
    except:
        stu_txt=open(filename,'w',encoding='utf-8')
    for item in lst:
        stu_txt.write(str(item)+'\n')
    stu_txt.close()
    menu()
def search():
    student_query=[]
    while True:
        id=''
        name=''
        if os.path.exists(filename):
            mode=input('按ID查找请输入1，按姓名查找请输入2，请输入：')
            if mode == '1':
                id=input('请输入学生ID：')
            elif mode =='2':
                name=input('请输入学生姓名：')
            else:
                print('您的输入有误，请重新输入：')
                continue
                #或者重复调用本函数
                # search()
            with open(filename,'r',encoding='utf-8') as rfile:
                students=rfile.readlines()
                for item in students:
                    d = dict(eval(item))
                    if id != '':
                        if d['id'] == id:
                            student_query.append(d)
                    if name != '':
                        if d['name'] == name:
                            student_query.append(d)
            show_student(student_query)
            # 清空列表，用于第二次查询
            student_query.clear()
            answer=input('还继续查询吗?y/n\n')
            if answer == 'y' or answer == 'Y':
                continue
            else:
                break

        else:
            print('暂未有学生信息!!!')
            break
            # return
    menu()
def show_student(lst):
    if len(lst) == 0:
        print('没有查询到学生信息，无数据显示!!!')
        return
    #定义标题显示格式
    format_title='{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^6}\t{:^6}'
    print(format_title.format('ID','姓名','英语成绩','Python成绩','Java成绩','总成绩'))
    #定义内容的显示格式
    format_data='{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^13}'
    for item in lst:
        print(format_data.format(item['id'],
                                 item.get('name'),
                                 item.get('english'),
                                 item.get('python'),
                                 item.get('java'),
                                 int(item['english'])+int(item['python'])+int(item['java'])
                                 ))
    menu()
def delete():
    while True:
        student_id = input("请输入您要删除的学生id")
        if student_id != '':
            if os.path.exists(filename):
                with open(filename, 'r', encoding='utf-8') as file:
                    student_old = file.readlines()
            else:
                student_old = []
            flag = False  # 标记是否删除
            if student_old:
                with open(filename, 'w', encoding='utf-8') as wfile:
                    d = {}
                    for item in student_old:
                        d = dict(eval(item))
                        if d['id'] != student_id:
                            wfile.write(str(d) + '\n')
                        else:
                            flag = True
                    if flag:
                        print(f'id为{student_id}的学生信息已被删除')
                    else:
                        print(f"没有找到ID为{student_id}的学生信息")
            else:
                print('无学生信息')
                break
            show()
            answer = input('是否继续删除学生信息？y/n')
            if answer == 'y' or answer == 'Y':
                continue
            else:
                break
    menu()
def modify():
    show()
    #判断文件是否存在，存在即做修改，不存在就反馈没有学生信息
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            #存在：读取所有信息，存入列表中
            student_old = rfile.readlines()
    else:
        print('没有学生信息，无法修改')
        return
    student_id = input('请输入要修改的学员id:')
    with open(filename,'w',encoding='utf-8') as wfile:
        for item in student_old:
            # 将每条数据转为字典
            d = dict(eval(item))
            if d['id'] == student_id:
                print('查到学生信息，可以修改')
                while True:
                    try:
                        d['id'] = input('请输入姓名：')
                        d['english'] = input('请输入英语成绩：')
                        d['python'] = input('请输入python成绩：')
                        d['java'] = input('请输入java成绩：')
                    except:
                        print('您的输入有误，请重新输入！！！')
                    else:
                        break
                wfile.write(str(d) + '\n')
                print('修改成功！！！')
            else:
                wfile.write(str(d)+'\n')
        answer=input('是否继续修改其他学生信息？y/n')
        if answer=='y' or answer =='Y':
            modify()
    menu()
def sort():
    show()
    student_list=[]
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            student=rfile.readlines()
        for item in student:
            d=dict(eval(item))
            student_list.append(d)

    else:
        return
    asc_or_desc=input('请选择（0：升序；1：降序）')
    if asc_or_desc == '0':
        asc_or_desc_bool=False
    elif asc_or_desc == '1':
        asc_or_desc_bool=True
    else:
        print('您的输入有误，请重新输入：')
        student_list.clear()
        sort()
    while True:
        mode = input('请选择排序方式（1.按英文成绩排序；2.按Python成绩排序；3.按Java成绩排序；0.按总成绩排序）')
        if mode == '1':
            student_list.sort(key=lambda d:int(d['english']),reverse=asc_or_desc_bool)
            break
        elif mode == '2':
            student_list.sort(key=lambda d:int(d['python']),reverse=asc_or_desc_bool)
            break
        elif mode == '3':
            student_list.sort(key=lambda d:int(d['java']),reverse=asc_or_desc_bool)
            break
        elif mode == '0':
            student_list.sort(key=lambda d:int(d['english'])+int(d['python'])+int(d['java']),reverse=asc_or_desc_bool)
            break
        else:
            print('输入有误，请重新输入')
            break
    show_student(student_list)
    menu()
def total():
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            students=rfile.readlines()
            if students:
                # print('一共有{}名学生。'.format(len(students)))
                # 或者这样表达
                print(f'一共有{len(students)}名学生。')
            else:
                print('还没录入学生信息。')
    else:
        print('暂未录入过学生信息...')
    menu()
def show():
    student_list=[]
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            student = rfile.readlines()
            if student:
                for item in student:
                    student_list.append(eval(item))
                show_student(student_list)
    else:
        print('暂无学生信息!!!')
    menu()
def menu():
    print('=========================学生管理系统===========================')
    print('========================== 功能菜单============================')
    print('\t\t\t1.录入学生信息')
    print('\t\t\t2.查找学生信息')
    print('\t\t\t3.删除学生信息')
    print('\t\t\t4.修改学生信息')
    print('\t\t\t5.排序')
    print('\t\t\t6.统计学生总人数')
    print('\t\t\t7.显示所有学生信息')
    print('\t\t\t0.退出系统')
    print('---------------------------------------------------------------')


if __name__ == '__main__':
    main()