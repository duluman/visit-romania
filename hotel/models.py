from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils import timezone
# Create your models here.


class Hotel(models.Model):
    name = models.CharField(max_length=255, default="Hotel")
    location = models.CharField(max_length=255, default=None)
    owner = models.CharField(max_length=255, default=None)
    administrator = models.ForeignKey(settings.AUTH_USER_MODEL,
                                      on_delete=models.CASCADE,
                                      related_name='proprietar',
                                      default=1)
    review = models.CharField(max_length=1000, default=None)
    hotel_picture = models.ImageField(upload_to='hotel_picture/', blank=True, null=True)
    youtube_video = models.CharField(max_length=255, default=None, blank=True)

    def __str__(self):
        return self.name


class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=100, default=None)
    room_type = models.CharField(max_length=40, default='Double')
    bathroom = models.BooleanField(default=True)
    balcony = models.BooleanField(default=False)
    room_picture = models.ImageField(upload_to='room_picture/', blank=True, null=True)
    room_youtube_video = models.CharField(max_length=255, default=None, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=149.99)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # return reverse('hotel:room', str(self.hotel.id))
        return reverse('hotel:list')


class Period(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    price = models.DecimalField(max_digits=7, decimal_places=2, default=149.99)
    days = models.PositiveIntegerField(default=1)
    total = models.DecimalField(max_digits=9, decimal_places=2, default=149.99)
    available = models.BooleanField(default=True)

    SEASON_CHOICE = [("spring", "spring"),
                     ("summer", "summer"),
                     ("autumn", "autumn"),
                     ("winter", "winter")]

    seasons = models.CharField(
        max_length=100,
        choices=SEASON_CHOICE,
        default=None,
        blank=True)

    def __str__(self):
        return str(self.price)

    def get_absolute_url(self):
        return reverse('hotel:list')


class CustomerReview(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 on_delete=models.CASCADE,
                                 related_name='client',
                                 default=1)

    hotel_to_review = models.ForeignKey(Hotel,
                                        on_delete=models.CASCADE,
                                        default=None)

    comment = models.TextField(default=None)

    date = models.DateTimeField(default=timezone.now)

    CHOICE = [("* * * * *","5"),
              ("* * * *", "4"),
              ("* * *", "3"),
              ("* *", "2"),
              ("*", "1")]

    stars = models.CharField(max_length=10, choices=CHOICE, default="*****")

    def __str__(self):
        return str(self.hotel_to_review)
