from rest_framework import serializers


class EmployeeSerializer(serializers.Serializer):
    name = serializers.CharField()
    year_of_experience = serializers.IntegerField()

    def validate(self, attrs):
        print(attrs)
        if attrs['year_of_experience'] < 0:
            raise serializers.ValidationError("Year of experience cannot be negative")
        return attrs