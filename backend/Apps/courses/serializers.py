from rest_framework import serializers
from .models import Course, Instructor, Enrollment

class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = "__all__"

class CourseSerializer(serializers.ModelSerializer):
    instructor = InstructorSerializer(read_only=True)
    instructor_id = serializers.PrimaryKeyRelatedField(
        queryset=Instructor.objects.all(), source="instructor", write_only=True
    )

    class Meta:
        model = Course
        fields = ["id", "title", "code", "description", "instructor", "instructor_id", "start_date", "end_date"]

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = "__all__"
