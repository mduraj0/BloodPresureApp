from django.db import models


class Glucose(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    value = models.PositiveSmallIntegerField()
    record_datetime = models.DateTimeField()
    notes = models.TextField(null=True, blank=True)

