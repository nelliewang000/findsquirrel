from django.db import models

class Squirrel(models.Model):
    latitude = models. DecimalField(max_digits=10,decimal_places=6)
    longitude = models. DecimalField(max_digits=10,decimal_places=6)
    unique_squirrel_id = models. CharField(max_length=250)

    AM = 'AM'
    PM = 'PM'
    SHIFT_CHOICES = ((AM,'AM'),(PM,'PM'),)

    shift = models. CharField(max_length=250,choices=SHIFT_CHOICES,)

    date = models. DateField()
    
    ADULT = 'Adult'
    JUVENILE = 'Juvenile'

    AGE_CHOICES = ((ADULT,'Adult'),(JUVENILE,'Juvenile'),)

    age = models. CharField(max_length=250,choices= AGE_CHOICES,)

    GRAY = 'Gray'
    CINNAMON = 'Cinnamon'
    BLACK = 'Black'

    FUR_CHOICES = ((GRAY,'Gray'),(CINNAMON,'Cinnamon'),(BLACK,'Black'),)

    primary_fur_color = models.CharField(max_length=250,choices= FUR_CHOICES,)

    GROUNDPLANE = 'Ground Plane'
    ABOVEGROUND = 'Above Ground'

    LOCATION_CHOICES = ((GROUNDPLANE,'Ground Plane'),(ABOVEGROUND,'Above Ground'),)

    location = models.CharField(max_length=250,choices = LOCATION_CHOICES,)
    specific_location = models.CharField(max_length=250,blank=True)
    running = models.BooleanField()
    chasing = models.BooleanField()
    climbing = models.BooleanField()
    eating = models.BooleanField()
    foraging = models.BooleanField()
    other_activities = models.CharField(max_length=250,blank=True)
    kuks = models.BooleanField()
    quaas = models.BooleanField()
    moans = models.BooleanField()
    tail_flags = models.BooleanField()
    tail_twitches = models.BooleanField()
    approaches = models.BooleanField()
    indifferent = models.BooleanField()
    runs_from = models.BooleanField()






# Create your models here.
