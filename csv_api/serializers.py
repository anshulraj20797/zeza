from django.db.models import fields
from rest_framework import serializers
from .models import CustomerMaster


class CustomerMasterSerializer(serializers.ModelSerializer):
    class Meta():
        model = CustomerMaster
        fields = ('id', 'name', 'email', 'address', 'phone')

        

