

from django.db import models


class inventory(models.Model):
    machine = models.CharField(max_length=100, default="Not Specified")
    room = models.CharField(max_length=100, default="Not Specified")
    mac = models.CharField(max_length=100, default="Not Specified", unique=True)
    ip = models.CharField(max_length=100, default="Not Specified")
    vlan = models.CharField(max_length=100, default="Not Specified")
    manufacturer = models.CharField(max_length=100, default="Not Specified")
    model = models.CharField(max_length=100, default="Not Specified")
    serial = models.CharField(max_length=100, default="Not Specified", unique=True)
    user = models.CharField(max_length=100, default="Not Specified")
    os = models.CharField(max_length=100, default="Not Specified")
    department = models.CharField(max_length=100, default="Not Specified")
    sponsor = models.CharField(max_length=100, default="Not Specified")
    notes = models.CharField(max_length=100, default="Not Specified")
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.machine