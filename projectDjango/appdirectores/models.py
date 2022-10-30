from django.db import models

class Director(models.Model):
    Name = models.CharField(max_length=20, help_text='Name')
    Last_Name = models.CharField(max_length=20, help_text='Last Name')
    Name_Movie = models.CharField(max_length=64, help_text='Movie')
    Description =  models.TextField(help_text='Description Movie')

    def __str__(self):
        return f'{self.Name} {self.Last_Name}'

    def pelicula_y_descripcion(self):
        return f'{self.Name_Movie}\n Descripcion: {self.Description}'