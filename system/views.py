from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes

from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str


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
    queryset = AcademicRecords.objects.select_related("students", "courses").all()
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

@api_view(["POST"])
def forgot_password(request):
    email = request.data.get("email")

    if not email:
        return Response(
            {"error": "Email is required"},
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return Response(
            {"message": "If that email exists, a reset link has been sent."}
        )

    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = default_token_generator.make_token(user)

    reset_link = (
        f"http://localhost:5173/reset-password/{uid}/{token}/"
    )

    send_mail(
        "Great Mind Password Reset",
        f"Click this link to reset your password:\n\n{reset_link}",
        "noreply@greatmind.com",
        [user.email],
    )

    return Response({
        "message": "Password reset link sent."
    })
    
@api_view(["POST"])
def reset_password(request, uidb64, token):
    new_password = request.data.get("password")

    if not new_password:
        return Response(
            {"error": "Password is required"},
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        return Response(
            {"error": "Invalid reset link"},
            status=status.HTTP_400_BAD_REQUEST
        )

    if not default_token_generator.check_token(user, token):
        return Response(
            {"error": "Invalid or expired reset link"},
            status=status.HTTP_400_BAD_REQUEST
        )

    user.set_password(new_password)
    user.save()

    return Response({
        "message": "Password reset successful. You can now login."
    })
    
@api_view(["POST"])
def register(request):
    username = request.data.get("username")
    email = request.data.get("email")
    password = request.data.get("password")

    if not username or not email or not password:
        return Response(
            {"error": "Username, email and password are required"},
            status=status.HTTP_400_BAD_REQUEST
        )

    if User.objects.filter(username=username).exists():
        return Response(
            {"error": "Username already exists"},
            status=status.HTTP_400_BAD_REQUEST
        )

    if User.objects.filter(email=email).exists():
        return Response(
            {"error": "Email already exists"},
            status=status.HTTP_400_BAD_REQUEST
        )

    user = User.objects.create_user(
        username=username,
        email=email,
        password=password
    )

    return Response(
        {"message": "Registration successful"},
        status=status.HTTP_201_CREATED
    )