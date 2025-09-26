from django.core.management.base import BaseCommand
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Drop collections if they exist
        for col in ['users', 'teams', 'activities', 'leaderboard', 'workouts']:
            db[col].drop()

        # Create unique index on email for users
        db['users'].create_index('email', unique=True)

        # Sample users (super heroes)
        users = [
            {'name': 'Clark Kent', 'email': 'superman@dc.com', 'team': 'dc'},
            {'name': 'Bruce Wayne', 'email': 'batman@dc.com', 'team': 'dc'},
            {'name': 'Diana Prince', 'email': 'wonderwoman@dc.com', 'team': 'dc'},
            {'name': 'Peter Parker', 'email': 'spiderman@marvel.com', 'team': 'marvel'},
            {'name': 'Tony Stark', 'email': 'ironman@marvel.com', 'team': 'marvel'},
            {'name': 'Steve Rogers', 'email': 'captainamerica@marvel.com', 'team': 'marvel'},
        ]
        db['users'].insert_many(users)

        # Teams
        teams = [
            {'name': 'marvel', 'members': ['Peter Parker', 'Tony Stark', 'Steve Rogers']},
            {'name': 'dc', 'members': ['Clark Kent', 'Bruce Wayne', 'Diana Prince']},
        ]
        db['teams'].insert_many(teams)

        # Activities
        activities = [
            {'user': 'Clark Kent', 'activity': 'Flying', 'duration': 60},
            {'user': 'Bruce Wayne', 'activity': 'Martial Arts', 'duration': 45},
            {'user': 'Diana Prince', 'activity': 'Training', 'duration': 50},
            {'user': 'Peter Parker', 'activity': 'Web Slinging', 'duration': 40},
            {'user': 'Tony Stark', 'activity': 'Suit Testing', 'duration': 30},
            {'user': 'Steve Rogers', 'activity': 'Shield Practice', 'duration': 35},
        ]
        db['activities'].insert_many(activities)

        # Leaderboard
        leaderboard = [
            {'team': 'marvel', 'points': 105},
            {'team': 'dc', 'points': 155},
        ]
        db['leaderboard'].insert_many(leaderboard)

        # Workouts
        workouts = [
            {'user': 'Clark Kent', 'workout': 'Strength', 'reps': 100},
            {'user': 'Bruce Wayne', 'workout': 'Endurance', 'reps': 80},
            {'user': 'Diana Prince', 'workout': 'Agility', 'reps': 90},
            {'user': 'Peter Parker', 'workout': 'Flexibility', 'reps': 70},
            {'user': 'Tony Stark', 'workout': 'Cardio', 'reps': 60},
            {'user': 'Steve Rogers', 'workout': 'Power', 'reps': 85},
        ]
        db['workouts'].insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
