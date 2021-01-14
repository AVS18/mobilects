from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('addStudent',views.addStudent,name="addStudent"),
    path('listStudent',views.listStudent,name="listStudent"),
    path('updateStudent/<int:sid>',views.updateStudent,name="updateStudent"),
    path('deleteStudent/<int:sid>',views.deleteStudent,name="deleteStudent")
]
