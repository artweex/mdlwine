# from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import (
    post_save,
    pre_save,
    post_delete
)
from django.dispatch import receiver
from django.utils.text import slugify

from .utils import create_slug

try:
    # from ckeditor.fields import RichTextField as ContentArea
    from ckeditor_uploader.fields import RichTextUploadingField as ContentArea
except ImportError as e:
    print('(Products) Can\'t import: ckeditor')
    from django.db.models import TextField as ContentArea


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.titlepip 

    # def get_absolute_url(self):
    # 	return reverse("category_detail", kwargs={ "slug": self.slug })


@receiver(pre_save, sender=Category)
def pre_save_page_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(sender, instance)


class Product(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    images = models.ImageField(upload_to='images')
    details = models.TextField(blank=True, null=True)
    description = ContentArea(blank=True, null=True)
    item_price = models.DecimalField(
        decimal_places=2, max_digits=20, default=0)
    box_price = models.DecimalField(decimal_places=2, max_digits=20, default=0)
    active = models.BooleanField(default=True)
    quantity_in_box = models.IntegerField(default=6)
    # quantity_in_pallet = models.IntegerField(default = 18)
    # thumbnail = models.ImageField(upload_to=thumbnail_upload_to, null=True, blank=True)
    categories = models.ManyToManyField('Category', blank=True)
    default_category = models.ForeignKey(
        'Category',
        related_name='default_category',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    # objects = ProductManager()

    class Meta:
        ordering = ["-title"]

    def __str__(self):
        return self.title

    # @property
    # def get_absolute_url(self):
    # 	return reverse("product_detail", kwargs={ "pk": self.pk })
