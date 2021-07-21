from django.urls import path
from monthly_challenges.apps.challenges.views import challenge_list, challenge_detail, challenge_by_number

urlpatterns = [
    path('challenges/<int:month_number>', view=challenge_by_number,
         name='challenge-by-number'),
    path('challenges/<str:month>', view=challenge_detail, name='challenge-detail'),
    path('challenges/', view=challenge_list, name='challenge-list')
]
