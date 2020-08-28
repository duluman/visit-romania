from django.db import models


class Job(models.Model):
    image = models.ImageField(upload_to='jobs/', blank=True, null=True)
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=755)
    date = models.CharField(max_length=100)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title


class Education(models.Model):
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=755)
    date = models.CharField(max_length=100)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title


