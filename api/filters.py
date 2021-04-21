import django_filters

from .models import *

class ScheduleFilter(django_filters.FilterSet):
    class Meta:
        model = Schedule
        fields = ["train_from", "train_to", "date"]
