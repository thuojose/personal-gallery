from django.db import models

# Create your models here.



class Category(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Categories"


    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()
