from django.db import models


class BloodPressure(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    systolic = models.PositiveSmallIntegerField()
    diastolic = models.PositiveSmallIntegerField()
    pulse = models.PositiveSmallIntegerField()
    record_datetime = models.DateTimeField()
    notes = models.TextField(null=True, blank=True)
