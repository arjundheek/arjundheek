from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=20, default='', blank=True)
    phone = models.IntegerField(default=0, blank=True)
    age = models.IntegerField(default=0, blank=True)
    picture = models.ImageField(default='', blank=True, upload_to='static/uploads/profiles')
    gender = models.CharField(max_length=15, default='', blank=True)
    skin = models.CharField(max_length=15, default='', blank=True)
    height = models.FloatField(max_length=2, default=0, blank=True)
    size = models.CharField(max_length=3, default='', blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return str(f"{self.user.username} - {self.name}")


class ProfileSettings(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    main_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    active = models.IntegerField()

    def __str__(self):
        return str(f"{self.user.username} - {self.main_profile.name}")
