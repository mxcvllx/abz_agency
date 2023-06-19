from rest_framework import serializers
from employee.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ("id", "name", "employment_position", "employment_start_date", "salary", "date_added", "parent")
