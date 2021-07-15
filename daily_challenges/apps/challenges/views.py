from django.urls import reverse
from django.http import HttpResponse

# Create your views here.


class MonthlyChallenges():
    CHALLENGES_BY_MONTH = {
        'january': 'Eat one apple a day',
        'february': 'Do 30 pushups every day',
        'march': 'Read a new book every week',
        'april': 'Try a new sport',
        'may': 'Try a different food every week',
        'june': 'Experiment learning the Go programming language',
        'july': '30 minutes of walking every day',
        'august': 'Learn how to dance',
        'september': 'Learn 10 magic tricks',
        'october': 'Make a new recipe every week',
        'november': 'Play a new computer game every week',
        'december': 'Participate on a Tekken 7 tournament'
    }

    @classmethod
    def challenge_list(cls, request):
        sent_html = ''

        for month in cls.CHALLENGES_BY_MONTH.keys():
            sent_html += f'''
                         <ul>
                            <li>
                                {month}
                            </li>
                         </ul>
                        '''

        return HttpResponse(sent_html, status=200)
