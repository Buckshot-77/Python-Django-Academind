from django.urls import path
from daily_challenges.apps.challenges.views import MonthlyChallenges

urlpatterns = [
    path('challenges/', view=MonthlyChallenges.challenge_list, name='challenge-list')
]
