from django.db import models

# Create your models here.


class FamilyMember(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    birth_date = models.DateField()
    description = models.TextField(blank=True, null=True)
    thumbnail = models.CharField(max_length=200)

    def __str__(self):
        return self.name
