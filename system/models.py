from django.db import models

# Create your models here.
class Students(models.Model):
    GENDER_CHOICES = [
        ("M", "Male"),
        ("F", "Female"),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    admission_number = models.CharField(max_length=50, unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    class_name = models.CharField(max_length=100)
    guardian_name = models.CharField(max_length=150, blank=True)
    guardian_phone = models.CharField(max_length=30, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["last_name", "first_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    employee_number = models.CharField(max_length=50, unique=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=30, blank=True)
    subject = models.CharField(max_length=100, blank=True)

    class Meta:
        ordering = ["last_name", "first_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Courses(models.Model):
    name = models.CharField(max_length=150)
    code = models.CharField(max_length=30, unique=True)
    teacher = models.ForeignKey(
        Teacher, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="courses"
    )
    class_name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.code} - {self.name}"


class Attendances(models.Model):
    STATUS_CHOICES = [
        ("present", "Present"),
        ("absent", "Absent"),
        ("late", "Late"),
    ]

    students = models.ForeignKey(
        Students, on_delete=models.CASCADE, related_name="attendance"
    )
    courses = models.ForeignKey(
        Courses, on_delete=models.CASCADE, related_name="attendance"
    )
    date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    class Meta:
        ordering = ["-date"]
        constraints = [
            models.UniqueConstraint(
                fields=["students", "courses", "date"],
                name="unique_student_course_date",
            )
        ]

    def __str__(self):
        return f"{self.students} - {self.date} - {self.status}"


class AcademicRecords(models.Model):
    students = models.ForeignKey(
        Students, on_delete=models.CASCADE, related_name="academic_records"
    )
    courses = models.ForeignKey(
        Courses, on_delete=models.CASCADE, related_name="academic_records"
    )
    session = models.CharField(max_length=30)
    term = models.CharField(max_length=30)
    ca_score = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    exam_score = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    class Meta:
        ordering = ["students", "courses"]

    @property
    def total_score(self):
        return self.ca_score + self.exam_score

    @property
    def grade(self):
        total = float(self.total_score)
        if total >= 70:
            return "A"
        if total >= 60:
            return "B"
        if total >= 50:
            return "C"
        if total >= 45:
            return "D"
        if total >= 40:
            return "E"
        return "F"

    def __str__(self):
        return f"{self.students} - {self.courses}"