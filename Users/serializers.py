from rest_framework import serializers
from .models import Student, Tutor

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'pronouns']

class TutorSerializer(serializers.ModelSerializer):
    tickets = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Tutor
        fields = ['id', 'name', 'pronouns', 'photo', 'tickets']