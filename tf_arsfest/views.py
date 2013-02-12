from django.template import RequestContext
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render_to_response, get_object_or_404
from forms import GuestForm, RegistrationForm
from models import Event, Guest, Registration
from django.utils import timezone
from django.template.loader import render_to_string

    
def register(request, year):
    
    event = get_object_or_404(Event, pk=year);
    
    places = event.places - len(Guest.objects.filter(event=event))
    
    
    now = timezone.now()
    if now < event.round1_opens or (now > event.round1_closes and now < event.round2_opens) or now > event.round2_closes or not places > 0:
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
                    avec = avec_form.save(commit=False)
                    avec.event = event
                    avec.save()
                    registration.avec = avec
                else:
                    return render_to_response('registration_form.html', {'registration': registration_form,
                                                             'guest': guest_form,
                                                             'avec': avec_form,
                                                             'year': year,
                                                             'desc': event.registration_description}
                                  , context_instance=RequestContext(request))
            
            # All good, save                   
            guest = guest_form.save(commit=False)
            guest.event = event
            guest.save()
            registration.guest = guest                 
            registration.event = event
            registration.save()
            
            data = registration.get_dictionary()
            send_registration_email(data)
            return render_to_response('registration_done.html', {'year': year, 'data': data}, context_instance=RequestContext(request))
        
    # If not POST    
    else:
        registration = Registration()
        registration.event = event
        registration_form = RegistrationForm(instance=registration)
        guest_form = GuestForm(prefix='guest')
        avec_form = GuestForm(prefix='avec')
        
        if places <= 1:
            registration_form.fields['avecbutton'].widget.attrs['disabled'] = True

    
    # If forms not valid or not POST
    return render_to_response('registration_form.html', {'registration': registration_form,
                                                             'guest': guest_form,
                                                             'avec': avec_form,
                                                             'year': year,
                                                             'desc': event.registration_description}
                              , context_instance=RequestContext(request))
        
def send_registration_email(data):
         
    subject, from_email, to = 'Registrering mottagen', 'TF<arsk@teknolog.fi>', data['guest']['email']
    content = render_to_string('email.txt', {'data': data})
     
    msg = EmailMultiAlternatives(subject, content, from_email, [to])
    msg.send()

