from django.contrib import admin
from .models import Students, Teacher, Courses, Attendances, AcademicRecords

# Register your models here.
admin.site.register(Students)
admin.site.register(Teacher)
admin.site.register(Courses)
admin.site.register(Attendances)
admin.site.register(AcademicRecords)