from django.db import models

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

