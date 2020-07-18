from django.db import models
# Create your models here.


class Hotel(models.Model):
    name = models.CharField(max_length=255, default="Hotel")
    location = models.CharField(max_length=255, default=None)
    owner = models.CharField(max_length=255, default=None)
    review = models.CharField(max_length=1000, default=None)
    hotel_picture = models.ImageField(upload_to='hotel_picture/', blank=True, null=True)
    youtube_video = models.CharField(max_length=255, default=None)

    def __str__(self):
        return self.name


class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=100, default=None)
    room_type = models.CharField(max_length=40, default=None)
    bathroom = models.BooleanField(default=True)
    balcony = models.BooleanField(default=False)
    room_picture = models.ImageField(upload_to='room_picture/', blank=True, null=True)
    room_youtube_video = models.CharField(max_length=255, default=None)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=149.99)

    def __str__(self):
        return self.name


class Period(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=149.99)
    days = models.PositiveIntegerField(default=1)
    total = models.DecimalField(max_digits=9, decimal_places=2, default=149.99)
    # pay = int(days)*int(price)
    # total = days * price
    # email = models.EmailField()
    # address = models.CharField(max_length=250)
    # postal_code = models.CharField(max_length=50)
    def __str__(self):
        return self.room
