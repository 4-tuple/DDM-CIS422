from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from polls.models import Choice, Poll
from django.core.context_processors import csrf
from django.contrib.auth import authenticate, login, logout

def main_page(request):
    return render_to_response('index.html')

def logout_page(request):
    # Log users out and re-direct them to the main page.
    logout(request)
    return HttpResponseRedirect('/')

def login_voter(request):
    if request.method == 'POST': # If the form has been submitted...
        form = LoginForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            voter = authenticate(username=username, password=password)
            if voter is not None:
                    login(request, voter)
                    poll_list = Polls.objects.all().filter(avoter=voter)
                    return render_to_response('polls/detail.html',
                          {'Voter': voter, 'Polls': poll_list})
        return render(request, 'polls/login.html', {'form': form})

#
#- Only allow one vote on assigned polls.
#- Add visual cues: 
#    Poll in progess 
#    Poll finished (show results)
#    You've already voted, no more votes allowed


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