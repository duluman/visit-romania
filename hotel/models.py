from django.db import models
# Create your models here.


class Hotel(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255, default=None)

    def __str__(self):
        return ' Hotel - ID: {} - Name: {}'.format(self.id, self.name)
