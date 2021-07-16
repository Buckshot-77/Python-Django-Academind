from django.urls import reverse
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.
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


def get_month_by_number(month_number):
    if month_number >= 1 and month_number <= 12:
        months = list(CHALLENGES_BY_MONTH.keys())

        month = months[month_number - 1]

        return month

    else:
        raise ValueError('Invalid month number given!')


def challenge_detail(request, month):
    try:
        month_lowercase = month.lower()
        challenge = CHALLENGES_BY_MONTH[month_lowercase]
        return HttpResponse(challenge, status=200)
    except KeyError:
        return HttpResponseNotFound('An invalid month was given')


def challenge_by_number(request, month_number):
    try:
        month = get_month_by_number(month_number)
    except ValueError:
        return HttpResponseNotFound('Invalid month!')

    return HttpResponseRedirect(reverse('challenge-detail', args=[month]))


def challenge_list(request):
    list_items = ''
    for month in CHALLENGES_BY_MONTH.keys():
        list_items += f'''
                            <li>
                                <a href="{reverse('challenge-detail', args=[month])}">
                                    {month}
                                </a>
                            </li>\n
                        '''

    sent_html = f'<ul>{list_items}</ul>'

    return HttpResponse(sent_html, status=200)
