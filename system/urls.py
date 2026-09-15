from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import (
    StudentViewSet, TeacherViewSet, CourseViewSet,
    AttendanceViewSet, AcademicRecordViewSet, dashboard,
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
]
