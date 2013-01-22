from django.template import RequestContext
from django.shortcuts import render_to_response
from forms import *

    
def register(request, year):
    
    if request.POST:
        registration_form = RegistrationForm(request.POST)
        
        g = Guest()
        guest_form = GuestForm(request.POST, instance=g, prefix='guest')
        
        a = Guest()
        avec_form = GuestForm(request.POST, instance=a, prefix='avec')
        
        if guest_form.is_valid() and registration_form.is_valid():
            guest = guest_form.save(commit=False)
            
            registration = registration_form.save(commit=False)
               
            guest.save()
            registration.guest = guest
            
            if avec_form.is_valid():
                avec = avec_form.save(commit=False)
                if len(avec.name) != 0: 
                    registration.avec = avec
                    avec.save()
                else:
                    return render_to_response('registration_form.html', {'registration': registration_form,
                                                             'guest': guest_form,
                                                             'avec': avec_form,
                                                             'year': year}
                                  , context_instance=RequestContext(request))
                
            registration.save()
               
            return render_to_response('registration_done.html', {'year': year}, context_instance=RequestContext(request))
        
        return render_to_response('registration_form.html', {'registration': registration_form,
                                                             'guest': guest_form,
                                                             'avec': avec_form,
                                                             'year': year}
                                  , context_instance=RequestContext(request))
        
    else:
        registration_form = RegistrationForm()
        guest_form = GuestForm(prefix='guest')
        avec_form = GuestForm(prefix='avec')
        return render_to_response('registration_form.html', {'registration': registration_form,
                                                             'guest': guest_form,
                                                             'avec': avec_form,
                                                             'year': year}
                                  , context_instance=RequestContext(request))
