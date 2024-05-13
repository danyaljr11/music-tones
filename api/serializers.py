from rest_framework import serializers
from .models import Section, Item
from fcm_django.models import FCMDevice


class Sections_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ['pk', 'text', 'icon']


class Items_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ['pk', 'text', 'link']


class FCMDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FCMDevice
        fields = ['registration_id', 'type']