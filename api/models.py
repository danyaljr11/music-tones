from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from fcm_django.models import FCMDevice
from firebase_admin.messaging import Message, Notification
import firebase_admin
from firebase_admin import credentials


cred = credentials.Certificate('serviceAccountKey.json')
firebase_admin.initialize_app(cred)

# Create your models here.


class Section (models.Model):
    text = models.CharField(max_length=30)
    icon = models.ImageField(upload_to='images/sections/')

    class Meta:
        ordering = ['pk']

    def __str__(self):
        return self.text


class Item (models.Model):
    section = models.ForeignKey('Section', on_delete=models.CASCADE)
    text = models.CharField(max_length=30)
    link = models.URLField()

    class Meta:
        ordering = ['pk']

    def __str__(self):
        return self.text


@receiver(post_save, sender=Item)
def send_notification_Items(sender, instance, created, **kwargs):
    if created:
        message = Message(
            notification=Notification(
                title="New Item Added",
                body=instance.text,
            ),
        )
        devices = FCMDevice.objects.all()
        devices.send_message(message)


@receiver(post_save, sender=Section)
def send_notification_Sections(sender, instance, created, **kwargs):
    if created:
        message = Message(
            notification=Notification(
                title="New Section Added",
                body=instance.text,
            ),
        )
        devices = FCMDevice.objects.all()
        devices.send_message(message)

