from rest_framework import serializers


class DesignationSerializer(serializers.Serializer):
    name = serializers.CharField()

    def validate(self, attrs):
        print(attrs)
        if attrs['name'] == '':
            raise serializers.ValidationError("name required")
        return attrs