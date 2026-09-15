from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Students, Teacher, Courses, Attendances, AcademicRecords
from .serializers import (
    StudentSerializer, TeacherSerializer, CourseSerializer,
    AttendanceSerializer, AcademicRecordSerializer,
)


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Courses.objects.select_related("teacher").all()
    serializer_class = CourseSerializer


class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendances.objects.select_related("students", "courses").all()
    serializer_class = AttendanceSerializer


class AcademicRecordViewSet(viewsets.ModelViewSet):
    queryset = AcademicRecords.objects.select_related("student", "course").all()
    serializer_class = AcademicRecordSerializer


@api_view(["GET"])
def dashboard(request):
    return Response({
        "students": Students.objects.count(),
        "teachers": Teacher.objects.count(),
        "courses": Courses.objects.count(),
        "attendance_records": Attendances.objects.count(),
        "academic_records": AcademicRecords.objects.count(),
    })
