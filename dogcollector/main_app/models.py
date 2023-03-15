from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Toy(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("toys_detail", kwargs={"pk": self.id})
    

class Dog(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    image = models.ImageField(upload_to = 'main_app/static/uploads/', max_length=100, default= 'dogs')
    toy = models.ManyToManyField(Toy)

    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def get_absolute_url(self):
        return reverse('detail', kwargs={"dog_id": self.id})
    
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

class Feeding(models.Model):
    date = models.DateField()
    meal = models.CharField(
        max_length = 1,
        choices = MEALS,
        default = MEALS[0][0]
    )
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
    class Meta:
        ordering = ['-date']