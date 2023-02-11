from django.db import models


class ModelCategory(models.Model):
    name_category = models.CharField(max_length=50, verbose_name="category_name")
    logo_category = models.ImageField(blank=False, null=False, upload_to='logo_category', verbose_name="category_logo")
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name_category
