
from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete all existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Sample users (super heroes)
        users = [
            User(name='Clark Kent', email='superman@dc.com', team='dc'),
            User(name='Bruce Wayne', email='batman@dc.com', team='dc'),
            User(name='Diana Prince', email='wonderwoman@dc.com', team='dc'),
            User(name='Peter Parker', email='spiderman@marvel.com', team='marvel'),
            User(name='Tony Stark', email='ironman@marvel.com', team='marvel'),
            User(name='Steve Rogers', email='captainamerica@marvel.com', team='marvel'),
        ]
        User.objects.bulk_create(users)

        # Teams
        teams = [
            Team(name='marvel', members=['Peter Parker', 'Tony Stark', 'Steve Rogers']),
            Team(name='dc', members=['Clark Kent', 'Bruce Wayne', 'Diana Prince']),
        ]
        Team.objects.bulk_create(teams)

        # Activities
        activities = [
            Activity(user='Clark Kent', activity='Flying', duration=60),
            Activity(user='Bruce Wayne', activity='Martial Arts', duration=45),
            Activity(user='Diana Prince', activity='Training', duration=50),
            Activity(user='Peter Parker', activity='Web Slinging', duration=40),
            Activity(user='Tony Stark', activity='Suit Testing', duration=30),
            Activity(user='Steve Rogers', activity='Shield Practice', duration=35),
        ]
        Activity.objects.bulk_create(activities)

        # Leaderboard
        leaderboard = [
            Leaderboard(team='marvel', points=105),
            Leaderboard(team='dc', points=155),
        ]
        Leaderboard.objects.bulk_create(leaderboard)

        # Workouts
        workouts = [
            Workout(user='Clark Kent', workout='Strength', reps=100),
            Workout(user='Bruce Wayne', workout='Endurance', reps=80),
            Workout(user='Diana Prince', workout='Agility', reps=90),
            Workout(user='Peter Parker', workout='Flexibility', reps=70),
            Workout(user='Tony Stark', workout='Cardio', reps=60),
            Workout(user='Steve Rogers', workout='Power', reps=85),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data using Django ORM.'))
