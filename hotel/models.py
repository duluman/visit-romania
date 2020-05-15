from django.db import models
# Create your models here.


class Hotel(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255, default=None)
    owner = models.CharField(max_length=255, default=None)
    room = models.CharField(max_length=10, default=None)
    review = models.CharField(max_length=1000, default=None)

    def __str__(self):
        return ' Hotel - ID: {} - Name: {}'.format(self.id, self.name, self.location, self.owner, self.room, self.review)

