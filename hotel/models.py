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


class BadgeHotel(models.Model):
    hotel_k = models.ForeignKey(Hotel, on_delete=models.CASCADE, default=None)
    ICON_CHOICES = [("camera-retro", "camera-retro"),
                    ("heart", "heart"),
                    ("brain", "brain"),
                    ("calendar-check", "calendar-check"),
                    ("pen", "pen"),
                    ("eye", "eye"),
                    ("car", "car"),
                    ("plane", "plane"),
                    ("hotel", "hotel"),
                    ("key", "key"),
                    ("sun", "sun"),
                    ("music", "music"),
                    ("clock", "clock"),
                    ("user-check", "user-check"),
                    ("yin-yang", "yin-yang")]

    icon = models.CharField(
        max_length=100,
        choices=ICON_CHOICES,
        default=None,
        blank=True)

    text = models.CharField(max_length=255, default="new feature", blank=True, null=True)

    COLOR_CHOICE = [("info", "cyan"),
                    ("danger", "red"),
                    ("success", "green"),
                    ("warning", "amber"),
                    ("black", "black")]

    color = models.CharField(
        max_length=100,
        choices=COLOR_CHOICE,
        default=None,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.icon


class BestFeature(models.Model):
    hotel_feature = models.ForeignKey(Hotel, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=255, default=None)
    ICON_CHOICES = [("camera-retro", "camera-retro"),
                    ("heart", "heart"),
                    ("bicycle", "bicycle"),
                    ("lightning", "bolt"),
                    ("bug", "bug"),
                    ("bell", "bell"),
                    ("birthday-cake", "birthday-cake"),
                    ("gift", "gift"),
                    ("magic", "magic"),
                    ("accusoft", "accusoft"),
                    ("artstation", "artstation"),
                    ("award", "award"),
                    ("balance-scale", "balance-scale"),
                    ("battery-full", "battery-full"),
                    ("bible", "bible"),
                    ("blogger", "blogger"),
                    ("book", "book"),
                    ("brain", "brain"),
                    ("calendar-check", "calendar-check"),
                    ("charging-station", "charging-station"),
                    ("check-square", "check-square"),
                    ("dice-d20", "dice-d20"),
                    ("dna", "dna"),
                    ("dog", "dog"),
                    ("dove", "dove"),
                    ("dragon", "dragon"),
                    ("envira", "envira"),
                    ("envelope-open-text", "envelope-open-text"),
                    ("eye", "eye"),
                    ("feather-alt", "feather-alt"),
                    ("fighter-jet", "fighter-jet"),
                    ("fire", "fire"),
                    ("firs-aid", "first-aid"),
                    ("fish", "fish"),
                    ("flag", "flag"),
                    ("diamant", "gem"),
                    ("gifts", "gifts"),
                    ("globe", "globe"),
                    ("graduation-cap", "graduation-cap"),
                    ("gravity", "grav"),
                    ("smile face", "grin"),
                    ("smile face 2", "grin-alt"),
                    ("smile face star", "grin-stars"),
                    ("smile face hearts", "grin-hearts"),
                    ("smile face wink", "grin-wink"),
                    ("smile face tears", "grin-tears"),
                    ("grip fire", "gripfire"),
                    ("guitar", "guitar"),
                    ("home", "home"),
                    ("handshake", "handshake"),
                    ("hat-wizard", "hat-wizard"),
                    ("heart music foto", "icons"),
                    ("hotel", "hotel"),
                    ("key", "key"),
                    ("leaf", "leaf"),
                    ("lock", "lock"),
                    ("map", "map"),
                    ("music", "music"),
                    ("pencil-alt", "pencil-alt"),
                    ("atom", "react"),
                    ("pergament", "scroll"),
                    ("diamond 2", "sketch"),
                    ("snowflake", "snowflake"),
                    ("spa", "spa"),
                    ("star", "star"),
                    ("store-alt", "store-alt"),
                    ("pro", "themeco"),
                    ("trophy", "trophy"),
                    ("umbrella", "umbrella"),
                    ("umbrella-beach", "umbrella-beach"),
                    ("user", "user"),
                    ("user-check", "user-check"),
                    ("user-circle", "user-circle"),
                    ("user-clock", "user-clock"),
                    ("user-config", "user-cog"),
                    ("user-edit", "user-edit"),
                    ("user-friends", "user-friends"),
                    ("user-graduate", "user-graduate"),
                    ("user-plus", "user-plus"),
                    ("user-tie", "user-tie"),
                    ("user-tag", "user-tag"),
                    ("users", "users"),
                    ("wrench", "wrench"),
                    ("yin-yang", "yin-yang")]

    icon = models.CharField(
        max_length=100,
        choices=ICON_CHOICES,
        default=None,
        blank=True
    )
    size = models.CharField(max_length=100, default="4x", blank=True, null=True)

    COLOR_CHOICES = [("cyan", "cyan"),
                     ("indigo", "indigo"),
                     ("blue", "blue"),
                     ("blue-violet", "blue-violet"),
                     ("red", "red"),
                     ("green", "green"),
                     ("amber", "amber"),
                     ("pink", "pink"),
                     ("black", "black")]

    color = models.CharField(
        max_length=100,
        choices=COLOR_CHOICES,
        default=None,
        blank=True,
        null=True
    )

    body = models.TextField(default=None)

    def __str__(self):
        return self.icon


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
