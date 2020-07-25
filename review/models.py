from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils import timezone
# Create your models here.


class AppReview(models.Model):
    name = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    comment = models.TextField(default=None)
    CHOICE = [("* * * * *", "5"),
              ("* * * *", "4"),
              ("* * *", "3"),
              ("* *", "2"),
              ("*", "1")]
    stars = models.CharField(max_length=10, choices=CHOICE, default="*****")
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("review:app_review")
