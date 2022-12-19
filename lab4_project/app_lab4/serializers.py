from rest_framework import serializers 
from app_lab4.models import Student
 
 
class StudentSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Student
        fields = ('univ_id',
                  'first_name',
                  'last_name',
                  'course',
                  'age')