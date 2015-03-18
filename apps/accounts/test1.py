else:
		print 'rrrrrrrrrrrrrrrrrrrrrrr'
    	form = RegistrationForm()
	variables = RequestContext(request, {
   		'form' : form
       	})
	return render_to_response('registration/register.html',
     variables)