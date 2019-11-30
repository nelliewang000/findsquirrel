# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from django.db.models import Count, Q

from .models import Squirrel

def map(request):
    s = Squirrel.objects.all()
    context = {
            's':s,
    }
    return render(request, 'squirrel/map.html', context)

def stats(request):
    dataset = Squirrel.objects \
        .values('shift') \
        .annotate(running_count=Count('shift', filter=Q(running=True)),
                  not_running_count=Count('shift', filter=Q(running=False)),
                  chasing_count=Count('shift', filter=Q(chasing=True)),
                  not_chasing_count=Count('shift', filter=Q(chasing=False)),
                  climbing_count=Count('shift', filter=Q(climbing=True)),
                  not_climbing_count=Count('shift', filter=Q(climbing=False)),
                  eating_count=Count('shift', filter=Q(eating=True)),
                  not_eating_count=Count('shift', filter=Q(eating=False)),
                  foraging_count=Count('shift', filter=Q(foraging=True)),
                  not_foraging_count=Count('shift', filter=Q(foraging=False))) \
        .order_by('shift')
    return render(request, 'squirrel/sightings/stats.html', {'dataset': dataset})
