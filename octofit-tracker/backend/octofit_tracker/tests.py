from django.test import TestCase
from .models import Team, User, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team')
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpass', team=self.team)
        self.workout = Workout.objects.create(name='Test Workout', description='desc', duration=30)
        self.activity = Activity.objects.create(user=self.user, type='run', duration=20, distance=5)
        self.leaderboard = Leaderboard.objects.create(user=self.user, points=50)

    def test_team_str(self):
        self.assertEqual(str(self.team), 'Test Team')
    def test_user_str(self):
        self.assertEqual(self.user.username, 'testuser')
    def test_activity_str(self):
        self.assertIn('run', str(self.activity))
    def test_workout_str(self):
        self.assertEqual(str(self.workout), 'Test Workout')
    def test_leaderboard_str(self):
        self.assertIn('testuser', str(self.leaderboard))
