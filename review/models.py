from django.db import models

# Create your models here.


class Review(models.Model):
    name = models.CharField(max_length=255, default=None)
    customer = models.CharField(max_length=255, default=None)
    comment = models.CharField(max_length=1000, default=None)
    rating = models.CharField(max_length=10, default=None)

    def __str__(self):
        return 'Review ID: {} Name {}'.format(self.id, self.name, self.customer, self.comment, self.rating)

