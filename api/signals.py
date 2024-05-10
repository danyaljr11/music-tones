# signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from api.models import Item, Section
import requests


@receiver(post_save, sender=Item)
def item_created(sender, instance, created, **kwargs):
    if created:
        send_notification("تم إضافة عنصر جديد: " + instance.text + "طلو شرفوناn/")


@receiver(post_save, sender=Section)
def section_created(sender, instance, created, **kwargs):
    if created:
        send_notification("تم إضافة قسم جديد:" + instance.text)


def send_notification(message):
    # Make HTTP request to OneSignal API to send push notification
    # Replace 'YOUR_APP_ID' and 'YOUR_REST_API_KEY' with your OneSignal app ID and REST API key
    url = "https://onesignal.com/api/v1/notifications"
    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "Authorization": "Basic OTFiZTRlOGYtN2EzMC00YjA3LTlkZDAtZWFhOWIxNmI4NjRi"
    }
    payload = {
        "app_id": "7f337be9-b299-4aaf-b537-38a46e312eea",
        "included_segments": ["All"],
        "contents": {"en": message}
    }
    response = requests.post(url, json=payload, headers=headers)
    print(response.text)  # Check response for errors
