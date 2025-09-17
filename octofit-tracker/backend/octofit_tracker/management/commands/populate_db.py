from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Borrar datos existentes
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Crear equipos
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='DC', description='DC superheroes')

        # Crear usuarios
        users = [
            User.objects.create(email='ironman@marvel.com', username='Iron Man', team=marvel),
            User.objects.create(email='spiderman@marvel.com', username='Spider-Man', team=marvel),
            User.objects.create(email='captainamerica@marvel.com', username='Captain America', team=marvel),
            User.objects.create(email='batman@dc.com', username='Batman', team=dc),
            User.objects.create(email='superman@dc.com', username='Superman', team=dc),
            User.objects.create(email='wonderwoman@dc.com', username='Wonder Woman', team=dc),
        ]

        # Crear actividades
        Activity.objects.create(user=users[0], type='run', duration=30, date=date.today())
        Activity.objects.create(user=users[1], type='cycle', duration=45, date=date.today())
        Activity.objects.create(user=users[3], type='swim', duration=60, date=date.today())

        # Crear workouts
        w1 = Workout.objects.create(name='Cardio Blast', description='High intensity cardio')
        w2 = Workout.objects.create(name='Strength Training', description='Build muscle')
        w1.suggested_for.add(marvel)
        w2.suggested_for.add(dc)

        # Crear leaderboard
        Leaderboard.objects.create(team=marvel, points=150)
        Leaderboard.objects.create(team=dc, points=120)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully!'))
