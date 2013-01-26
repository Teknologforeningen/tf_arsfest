from django.template import RequestContext
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render_to_response, get_object_or_404
from django.forms.models import model_to_dict
from django.template.loader import get_template
from django.template import Context
from forms import *
from models import Event
from django.utils import timezone

    
def register(request, year):
    
    event = get_object_or_404(Event, pk=year);
    
    places = event.places - len(Guest.objects.filter(event=event))
    
    
    now = timezone.now()
    if now < event.round1_opens or (now > event.round1_closes and now < event.round2_opens) or now > event.round2_closes or guests >= event.places:
        return render_to_response('registration_closed.html', {'event': event, 'places': places}, context_instance=RequestContext(request))
        
    
    # If posting a filled out form
    if request.POST:
        
        # Get the forms from the POST data
        registration_form = RegistrationForm(request.POST)
        guest_form = GuestForm(request.POST, prefix='guest')
        avec_form = GuestForm(request.POST, prefix='avec')
        
        # If the main guest form and registration specific info was correct
        if guest_form.is_valid() and registration_form.is_valid():
            
            registration = registration_form.save(commit=False)   
            
            # If there was an avec
            if registration.avecbutton:
                # If the avec was filled out correctly
                if avec_form.is_valid():
                    avec = avec_form.save()
                    avec.event = event
                    registration.avec = avec
                else:
                    return render_to_response('registration_form.html', {'registration': registration_form,
                                                             'guest': guest_form,
                                                             'avec': avec_form,
                                                             'year': year,
                                                             'desc': event.registration_description}
                                  , context_instance=RequestContext(request))
            
            # All good, save                   
            guest = guest_form.save()
            guest.event = event
            registration.guest = guest                 
            registration.event = event
            registration.save()
            
            data = registration.get_dictionary()
            
            return render_to_response('registration_done.html', {'year': year, 'data': data}, context_instance=RequestContext(request))
        
    # If not POST    
    else:
        registration = Registration()
        registration.event = event
        registration_form = RegistrationForm(instance=registration)
        guest_form = GuestForm(prefix='guest')
        avec_form = GuestForm(prefix='avec')

    
    # If forms not valid or not POST
    return render_to_response('registration_form.html', {'registration': registration_form,
                                                             'guest': guest_form,
                                                             'avec': avec_form,
                                                             'year': year,
                                                             'desc': event.registration_description}
                              , context_instance=RequestContext(request))
        
def send_registration_email(reciever, data):
    template = get_template('email.txt')
     
    subject, from_email, to = 'Registrering mottagen', 'arsk@teknolog.fi', reciever
    content = template.render(Context())
     
    msg = EmailMultiAlternatives(subject, content, from_email, [to])
    msg.send()
