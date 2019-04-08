from rest_framework import serializers
from .models import Employee
from issues.models import Issue
from rest_auth.serializers import UserDetailsSerializer
from phonenumber_field.serializerfields import PhoneNumberField


class EmployeeSerializer(UserDetailsSerializer):
    name = serializers.CharField()
    phone = serializers.CharField()
    email = serializers.EmailField()
    admin = serializers.BooleanField()   


    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + ('email', 'name', 'admin', 'phone', )

    def update(self, instance, validated_data):
        name = validated_data.get('name', instance.name)
        phone = validated_data.get('phone', instance.phone)
        email = validated_data.get('email', instance.email)
        admin = validated_data.get('admin', instance.admin)

        instance = super(EmployeeSerializer, self).update(instance, validated_data)

        # get and update user profile
        employee = instance
        if validated_data:
            employee.name = name
            employee.phone = phone
            employee.email = email
            employee.admin = admin
            employee.save()
        return instance
 