from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Category(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField()

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)


class Board(models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField()
    description = models.CharField(max_length=1024)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Board, self).save(*args, **kwargs)


class Pin(models.Model):
    title = models.CharField(max_length=256, unique=True)
    description = models.CharField(max_length=1024)
    image = models.ImageField(title)
    likes = models.IntegerField(default=0)
    category = models.ForeignKey(Category)
    board = models.ForeignKey(Board)

    def __unicode__(self):
        return self.title

