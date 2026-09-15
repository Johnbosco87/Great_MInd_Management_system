from rest_framework import serializers
from .models import Students, Teacher, Courses, Attendances, AcademicRecords


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = "__all__"


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    teacher_name = serializers.CharField(source="teacher", read_only=True)

    class Meta:
        model = Courses
        fields = "__all__"


class AttendanceSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source="students", read_only=True)
    course_name = serializers.CharField(source="courses", read_only=True)

    class Meta:
        model = Attendances
        fields = "__all__"


class AcademicRecordSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source="students", read_only=True)
    course_name = serializers.CharField(source="courses", read_only=True)
    total_score = serializers.ReadOnlyField()
    grade = serializers.ReadOnlyField()

    class Meta:
        model = AcademicRecords
        fields = "__all__"

    def validate(self, attrs):
        ca = attrs.get("ca_score", 0)
        exam = attrs.get("exam_score", 0)
        if ca < 0 or exam < 0:
            raise serializers.ValidationError("Scores cannot be negative.")
        if ca > 40:
            raise serializers.ValidationError("CA score cannot exceed 40.")
        if exam > 60:
            raise serializers.ValidationError("Exam score cannot exceed 60.")
        return attrs
