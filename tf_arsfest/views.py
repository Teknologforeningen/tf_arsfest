from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from forms import *
from models import Event

    
def register(request, year):
    
    event = get_object_or_404(Event, pk=year);
    
    # If posting a filled out form
    if request.POST:
        
        # Get the forms from the POST data
        registration_form = RegistrationForm(request.POST)
        guest_form = GuestForm(request.POST, prefix='guest')
        avec_form = GuestForm(request.POST, prefix='avec')
        
        # If the main guest form and registration specific info was correct
        if guest_form.is_valid() and registration_form.is_valid():
            
            # Save, but do not commit to database before everything else is ok
            guest = guest_form.save(commit=False)
            
            # Save, but do not commit until the guest is added and avec checks out
            registration = registration_form.save(commit=False)

            # Add guest to registration
            registration.guest = guest
            
            # If there was an avec
            if registration.avecbutton:
                # If the avec was filled out correctly
                if avec_form.is_valid():
                    avec = avec_form.save(commit=False)
                    registration.avec = avec
                    avec.save()
                else:
                    return render_to_response('registration_form.html', {'registration': registration_form,
                                                             'guest': guest_form,
                                                             'avec': avec_form,
                                                             'year': year}
                                  , context_instance=RequestContext(request))
            
            # All good, save          
            guest.save()
            
            # Save all the relations    
            registration_form.save_m2m()
            
            return render_to_response('registration_done.html', {'year': year}, context_instance=RequestContext(request))
        
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
                                                             'year': year}
                              , context_instance=RequestContext(request))
        
        
