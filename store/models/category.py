from django.db import models

class Category(models.Model):
    name= models.CharField(max_length=50)
    recommendedSkinColor = models.fields.CharField(max_length=100)
    recommendedGender = models.fields.CharField(max_length=100)
    recommendedWearingArea = models.fields.CharField(max_length=100)
    recommendedFaceShape = models.fields.CharField(max_length=100)

    

    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    def __str__(self):
        return self.name
    def register(self):
        self.save()
