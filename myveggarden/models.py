from django.db import models



class GardenSet(models.Model):
    concentration_set = models.CharField(max_length=140, default='')
    cycle_time_set = models.CharField(max_length=140, default='')
    plant_pump_set = models.CharField(max_length=140, default='')
    recirculation_pump_set = models.CharField(max_length=140, default='')
    solution_pump_set = models.CharField(max_length=140, default='')

class Garden(models.Model):
    concentration = models.CharField(max_length=140, default='')
    luminosity = models.CharField(max_length=140, default='')
    temperature = models.CharField(max_length=140, default='')
    next_cycle = models.CharField(max_length=140, default='')
    last_update = models.CharField(max_length=140, default='')
    plant_pump = models.CharField(max_length=140, default='')
    recirculation_pump = models.CharField(max_length=140, default='')
    solution_pump = models.CharField(max_length=140, default='')

