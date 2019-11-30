# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.template import loader
from django.http import HttpResponse
from django.db.models import Count, Q

from .models import Squirrel
from .form import ArticleForm

def index(request):
    return render(request, 'squirrel/index.html')

def map(request):
    s = Squirrel.objects.all()
    return render(request, 'squirrel/map.html',{'s':s})

def list(request):
    s = Squirrel.objects.all()
    return render(request, 'squirrel/list.html',{'s':s})

def add(request):
    if request.method == 'POST':
        add = ArticleForm(request.POST)
        if add.is_valid():
            add.save()
            return redirect("/squirrel/sightings/") 
        else:
            for key,value in request.POST.items():
                print(key,value)
            print(add.errors)
    return render(request, 'squirrel/add.html')

def detail(request,sq_id):
    sq = Squirrel.objects.get(unique_squirrel_id=sq_id)
    if request.method=='POST':
        if 'delete' in request.POST:
            sq.delete()
            return redirect("/squirrel/sightings/")
        else:
            sq = ArticleForm(instance=sq, data=request.POST)
            if sq.is_valid():
                sq.save()
                return redirect("/squirrel/sightings/")
            else:
                print(sq.errors)

    return render(request, 'squirrel/detail.html',{'sq':sq})
    
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
