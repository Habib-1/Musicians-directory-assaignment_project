from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.

class Musicians(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=11)
    instrument=models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class Album(models.Model):
    album_name=models.CharField(max_length=50)
    musician=models.ForeignKey(Musicians, on_delete=models.CASCADE)
    realise_date=models.DateTimeField(auto_now_add=True)
    rating=models.IntegerField(validators=[
        MinValueValidator(1), MaxValueValidator(5)
    ],
    help_text="Enter A rating between 1 to 5"
    )
    def __str__(self):
        return f"Album :{self.album_name}  musician : {self.musician.first_name}"
