
from django.core.management.base import BaseCommand
import csv

Class Command(BaseCommand):
    def add_arguments(self,parser):
        parser.add_argument('csv_file')
    
    def handle(self, *args, **options):
        with open(options['csv_file']) as fp:
            reader = csv.DictReader(fp)
            data=list(reader)

        for item in data:
            s= Squirrel(
            	latitude = item['Y'],
    			longitude = item['X'],
    			unique_squirrel_id = item['Unique Squirrel ID'],
    			shift = item['Shift'],
    			date = item['Date'],
    			age = item['Age'],
    			primary_fur_color = item['Primary Fur Color'],
    			location = item['Location'],
			    specific_location = item['Specific Location'],
			    running = item['Running'],
			    chasing = item['Chasing'],
			    climbing = item['Climbing'],
			    eating = item['Eating'],
			    foraging = item['Foraging'],
			    other_activities = item['Other Activities'],
			    kuks = item['Kuks'],
			    quaas = item['Quaas'],
			    moans = item['Moans'],
			    tail_flags = item['Tail flags'],
			    tail_twitches = item['Tail twitches'],
			    approaches = item['Approaches'],
			    indifferent = item['Indifferent'],
			    runs_from =item['Runs from'],
			    )
            s.save()

