from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="category")
    logo = models.ImageField(blank=False, null=False, upload_to='logo', verbose_name="category_logo")
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Products(models.Model):
    category_id = models.ForeignKey(Category, verbose_name="category_id", on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name="name")
    description = models.TextField(verbose_name="description")
    image = models.ImageField(blank=True, null=True, upload_to='image')
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Instruction(models.Model):
    product_id = models.ForeignKey(Products, verbose_name="product_id", on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=255, verbose_name="name")
    text = models.TextField(verbose_name="text")
    image = models.ImageField(null=True, blank=True, upload_to='image')
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name
