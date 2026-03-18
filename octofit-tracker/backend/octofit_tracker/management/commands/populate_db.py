from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        # Create users
        ironman = User.objects.create(email='ironman@marvel.com', name='Iron Man', team='Marvel', is_superhero=True)
        captain = User.objects.create(email='captain@marvel.com', name='Captain America', team='Marvel', is_superhero=True)
        batman = User.objects.create(email='batman@dc.com', name='Batman', team='DC', is_superhero=True)
        superman = User.objects.create(email='superman@dc.com', name='Superman', team='DC', is_superhero=True)

        # Create activities
        Activity.objects.create(user=ironman, type='Running', duration=30, date='2026-03-18')
        Activity.objects.create(user=batman, type='Cycling', duration=45, date='2026-03-18')

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=200)
        Leaderboard.objects.create(team=dc, points=180)

        # Create workouts
        Workout.objects.create(name='Pushups', description='Upper body workout', suggested_for='Marvel')
        Workout.objects.create(name='Squats', description='Lower body workout', suggested_for='DC')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
