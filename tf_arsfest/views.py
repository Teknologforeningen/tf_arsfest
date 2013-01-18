from django.shortcuts import render_to_response
from django.forms.formsets import formset_factory
from django.template import RequestContext
from forms import RegistrationForm


def add_participant(request):
    ParticipantFormSet = formset_factory(RegistrationForm, extra=2, max_num=2)
    if request.method == 'POST':
        formset = ParticipantFormSet(request.POST, request.FILES)
        if formset.is_valid():
            # do something with the formset.cleaned_data
            pass
    else:
        formset = ParticipantFormSet()
    return render_to_response('participant_form.html', {'formset': formset}, context_instance=RequestContext(request))