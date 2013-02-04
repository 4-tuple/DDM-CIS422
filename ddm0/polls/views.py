from django.template import Context, loader
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from polls.models import Choice, Poll
from django.core.context_processors import csrf
from django.contrib.auth import authenticate, login, logout


def main_page(request):
    return render_to_response('index.html')

"""
def list(request):
    if request.method == "POST":
        poll = Poll.objects.filter(pin = request.POST['pin'])
    return render_to_response('polls/index.html')
"""


def list(request):
    if 'p' in request.POST:
        p = request.POST['p']
    polls = Poll.objects.filter(pin = p)
    return render_to_response('polls/index.html',
                {'polls': polls, 'pin': p})


def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render_to_response('polls/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        }, context_instance=RequestContext(request))
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('poll_results', args=(p.id,)))


