from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rest/sections/', views.SectionList.as_view()),
    path('rest/items/<int:pk>', views.ItemList.as_view()),
    path('fcm-device/', views.FCMDeviceView.as_view()),

]
