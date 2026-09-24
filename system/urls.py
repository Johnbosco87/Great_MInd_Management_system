from django.urls import include, path

from rest_framework.routers import DefaultRouter
from .views import (
    StudentViewSet, TeacherViewSet, CourseViewSet,
    AttendanceViewSet, AcademicRecordViewSet, dashboard,forgot_password, reset_password,  register,
)

router = DefaultRouter()
router.register("students", StudentViewSet)
router.register("teachers", TeacherViewSet)
router.register("courses", CourseViewSet)
router.register("attendance", AttendanceViewSet)
router.register("academic-records", AcademicRecordViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("dashboard/", dashboard),
    path("forgot-password/", forgot_password),
    path("reset-password/<uidb64>/<token>/", reset_password),
    path("register/", register),
]
