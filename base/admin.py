from django.contrib import admin

# Register your models here.
from .models import Student

class StudentRef(admin.ModelAdmin):
    list_display = ['sid','name','branch','semester']
    list_filter = ['branch','semester']

admin.site.register(Student,StudentRef)