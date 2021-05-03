from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.conf import settings
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
CATEGORY_CHOICES = (
    ('P', 'Physical'),
    ('E', 'Ebook'),
)
genre_list = (
    ("F", "Fantasy"),
    ("D", "Dystopian"),
    ("S", "Science fiction"),
    ("M", "Mystery"),
    ("H", "Horror"),
    ("R", "Romance"),
)


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Books(models.Model):
    user1 = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    Title = models.CharField(max_length=100,unique=True)
    Author = models.CharField(max_length=100)
    Genre = models.CharField(choices=genre_list,max_length=40)
    Type = models.CharField(choices=CATEGORY_CHOICES,max_length=1)
    Rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    Review = models.CharField(max_length=100)
    Favorite = models.BooleanField(default=False)


def userprofile_receiver(sender, instance, created, *args, **kwargs):
    if created:
        userprofile = UserProfile.objects.create(user=instance)


post_save.connect(userprofile_receiver, sender=settings.AUTH_USER_MODEL)
