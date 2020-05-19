#教师子系统
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db import connection

def teacher1(request):#个人信息
    return render(request,'teacher1.html')

def teacher2(request):#授课信息
    return render(request,'teacher2.html')

def teacher3(request):#学生成绩
    return render(request,'teacher3.html')

def indexTeacher(request):
    print("查询教师自己的信息")
    if 'sessionid' in request.COOKIES and request.session['role'] == 'teacher': 
        teacher_id = request.session['id']
        connection.connect()  
        cursor = connection.cursor()
        cursor.execute("select * from teacher where teacher_id='%s'" % (teacher_id))
        result = cursor.fetchall()
        connection.close()
        result_list = []
        for r in result:
            result_list.append({"teacher_id":r[0],'teacher_name':r[2],'dept':r[3]})
        print(result_list)
        return redirect('/pro/teacher1')
    else:
        print("用户身份不合法")
        return redirect('/pro/login/')

def indexTCourse(request):
    print("查询教师教授的课程")
    if 'sessionid' in request.COOKIES and request.session['role'] == 'teacher': 
        teacher_id = request.session['id']
        connection.connect()    
        cursor = connection.cursor()
        cursor.execute("select course.course_id,course_name,credits \
                        from course natural join teach \
                        where teacher_id='%s'" % (teacher_id))
        result = cursor.fetchall()
        connection.close()
        result_list = []
        for r in result:
            result_list.append({"course_id":r[0],'course_name':r[1],'credits':r[2]})
        print(result_list)
        return redirect('/pro/teacher1')
    else:
        print("用户身份不合法")
        return redirect('/pro/login/')

def indexTGrade(request):
    print("查询学生的成绩")
    if 'sessionid' in request.COOKIES and request.session['role'] == 'teacher': 
        teacher_id = request.session['id']
        connection.connect()    
        cursor = connection.cursor()
        cursor.execute("select take.student_id,student_name,take.course_id,course_name,credits,grade \
                        from student natural join course natural join take natural join teach \
                        where teacher_id ='%s'" % (teacher_id))
        result = cursor.fetchall()
        connection.close()
        result_list = []
        for r in result:
            result_list.append({"student_id":r[0],'student_name':r[1],'course_id':r[2],\
                                'course_name':r[3],'credits':r[4],'grade':r[5]})
        print(result_list)
        return redirect('/pro/teacher1')
    else:
        print("用户身份不合法")
        return redirect('/pro/login/')

def indexTDist(request):
    print("查询学生成绩分布")

