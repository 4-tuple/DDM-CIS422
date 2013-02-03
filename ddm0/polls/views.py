from django.shortcuts import *
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from polls.models import Choice, Poll
from django.core.context_processors import csrf
from django.contrib.auth import authenticate, login, logout

from django import forms
from django.contrib.auth.forms import UserCreationForm

def main_page(request):
    return render_to_response('index.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/polls")
    else:
        form = UserCreationForm()
    return render_to_response("reg.html", {
        'form': form,
    })

def user_page(request):
    if request.user is not None:
        name = request.user.username
    return render_to_response('polls/index.html')  
#
#- Only allow one vote on assigned polls.
#- Add visual cues: 
#    Poll in progess 
#    Poll finished (show results)
#    You've already voted, no more votes allowed


# @login_required
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