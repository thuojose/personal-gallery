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

class Location(models.Model):
    name=models.CharField(max_length=30)


    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    # @classmethod
    # def update_location(cls,location,update):
    #     updated = cls.objects.filter(image_name=location).update(name=update)
    #     return updated