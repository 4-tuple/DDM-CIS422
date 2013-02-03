from django.shortcuts import *
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from polls.models import Choice, Poll, Voter, VoterForm
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
        form = VoterForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            voter = authenticate(username=username, password=password)
            if voter is not None:
                    login(request, voter)
                    polls_list = Polls.objects.all().filter(avoter=voter)
                    return render_to_response('polls/index.html',
                          {'voter': voter, 'polls': polls_list})
        else:#no user?
            print "oops"
    else:
        form = VoterForm()
    return render(request, 'auth.html', {'form': form})

def register_voter(request):
   #logged in?  No user creation for you
    if request.method == 'POST': # If the form has been submitted...
        form = VoterForm(request.POST) # A form bound to the POST data
        if form.is_valid() and (form.cleaned_data['password'] == form.cleaned_data['confirm_password']): # All validation rules pass
            def_username = form.cleaned_data['username']
            def_password = form.cleaned_data['password']
            def_email = form.cleaned_data['email']
            try:
                name_user = User.objects.get(username = def_username)
                return error_out(request,"User name collision.")
            except User.DoesNotExist:
                try:
                    email_user = User.objects.get(email = def_email)
                    return error_out(request,"Email collision.")
                except User.DoesNotExist:
                    user = User.objects.create_user(username = def_username,
                                    email=def_email,
                                    password=def_password)
                    voter = authenticate(username=def_username, password=def_password)
                    if voter is not None:
                        login(request, voter)
                    # Redirect after POST
                        return render(request, 'polls/index.html',
                                  {'voter': voter})

        else:
            print "oh crap"
            #return error_out(request, "Bad user creation styuff")
    else:
        form = VoterForm() # An unbound form
        return render(request, 'reg.html', {'form': form})


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