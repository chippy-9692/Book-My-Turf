from django.db import models

# Create your models here.
class turfs(models.Model):
    img =models.ImageField(upload_to="pic")
    name =models.CharField(max_length=50)
    description =models.CharField(max_length=500)
    location=models.CharField(max_length=50)
    time =models.CharField(max_length=20)
    perhour=models.CharField(max_length=50)
    def __str__(self):
        return self.name
    



class Booking(models.Model):
    turf = models.ForeignKey(turfs, on_delete=models.CASCADE)
    user = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"{self.user} booked {self.turf} from {self.start_time} to {self.end_time}"