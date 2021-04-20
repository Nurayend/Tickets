from datetime import datetime
from django.db import models

# Create your models here.

class Schedule(models.Model):
    date = models.DateTimeField(default=datetime.now)
    DAY_OF_WEEK = [
        ('MON', 'Monday'),
        ('TUE', 'Tuesday'),
        ('WED', 'Wednesday'),
        ('THU', 'Thursday'),
        ('FRI', 'Friday'),
        ('SAT', 'Saturday'),
        ('SUN', 'Sunday')
    ]
    day = models.CharField(
        max_length=3,
        choices=DAY_OF_WEEK,
        default='MON'
    )
    train_from = models.CharField(max_length=50) #cities
    train_to = models.CharField(max_length=50)
    name = models.CharField(max_length=20) #name of train

    class Meta:
        verbose_name = 'Schedule of Trains'
        verbose_name_plural = 'Schedules of Trains'

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

    def to_json(self):
        return{
            'id': self.id,
            'name': self.name,
            'date': self.date,
            'day': self.day,
            'train_from': self.train_from,
            'train_to': self.train_to
        }
