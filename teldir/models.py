from django.db import models

# Create your models here.
class Category(models.Model):
    category = models.CharField(unique=True, max_length=15)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.category


class Contact(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    address = models.CharField(max_length=50, blank=True, null=True)
    category_id = models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET(0))
    landline_no = models.CharField(max_length=30, blank=True, null=True)
    mobile_no = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return "{0} {1}".format(self.name, self.address)
