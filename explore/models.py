from django.db import models

# Create your models here.


class Destination(models.Model):
    
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Image(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')

    def __str__(self):
        return self.name

class Festival(models.Model):
    name = models.CharField(max_length=100)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    desc = models.TextField()
    # destination_id = models.IntegerField()
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Hotspot(models.Model):

    name = models.CharField(max_length=100)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    desc = models.TextField()
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Stay(models.Model):

    name = models.CharField(max_length=100)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    desc = models.TextField()
    number_of_rooms = models.IntegerField()
    price = models.IntegerField()
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class PopularFood(models.Model):

    name = models.CharField(max_length=100)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)

    def __str__(self):
        return self.name