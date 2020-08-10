from django.urls import path
from .view import add, admin, enroll, stat, student, teacher
urlpatterns = [
    path('welcome/',enroll.welcome),
    path('login/', enroll.login),
    path('admin/',admin.admin),
    path('student/',student.student),
    path('teacher/',teacher.teacher),
    path('indexStudent',student.indexStudent),
    path('indexSCourse',student.indexSCourse),
    path('indexSGPA',student.indexSGPA),
    path('indexSGPADIST',student.indexSGPADIST),
    path('indexTeacher',teacher.indexTeacher),
    path('indexTCourse',teacher.indexTCourse),
    path('indexTGrade',teacher.indexTGrade),
    path('indexTDist',teacher.indexTDist),
    path('indexAdmin',admin.indexAdmin),
    path('indexAllStu',admin.indexAllStu),
    path('indexAllTeacher',admin.indexAllTeacher),
    path('indexAllCourse',admin.indexAllCourse),
]