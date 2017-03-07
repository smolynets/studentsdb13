from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime
from django.contrib import messages
from PIL import Image
from django.contrib.auth.decorators import login_required








def users_list(request):
	users = User.objects.all()
	return render(request, 'users_list.html',
    {'users': users})







def users_one(request, pk):
   use = User.objects.get(id=pk)
   return render(request, 'user_one_profile.html',
   {'user_one': use})





def user_edit(request, pk):
    use = User.objects.get(pk=pk)
    
    if request.method == "POST":
      data = User.objects.get(pk=pk)
      if request.POST.get('add_button') is not None:

        errors = {}

        username = request.POST.get('username', '').strip()
        if not username:
          errors['username'] = _(u"Name is mandatory.")
        else:
          data.username = username

        password = request.POST.get('password', '').strip()
        if not password:
          errors['password'] = _(u"Name is mandatory.")
        else:
          data.password = password

        email = request.POST.get('email', '').strip()
        if not email:
          errors['email'] = _(u"Name is mandatory.")
        else:
          data.email = email

        if not errors:
          
          data.save()
          return HttpResponseRedirect( u'%s?status_message=%s'  % (reverse('users_list'), _(u'User edited succefully')))
        else:
          # render form with errors and previous user input
          return render(request, 'user_edit.html',
          {'pk': pk,'errors': errors})
      elif request.POST.get('cancel_button') is not None:
        # redirect to home page on cancel button
        return HttpResponseRedirect( u'%s?status_message=%s' % (reverse('users_list'), _('Editing user canceled')))
    else:
     # initial form render
     return render(request, 'user_edit.html',
     {'use': use, 'pk': pk})






@login_required
def user_one_edit(request, pk):
    use = User.objects.get(pk=pk)
    
    if request.method == "POST":
      data = User.objects.get(pk=pk)
      if request.POST.get('add_button') is not None:

        errors = {}

        username = request.POST.get('username', '').strip()
        if not username:
          errors['username'] = _(u"Name is mandatory.")
        else:
          data.username = username

        password = request.POST.get('password', '').strip()
        if not password:
          errors['password'] = _(u"Name is mandatory.")
        else:
          data.password = password

        email = request.POST.get('email', '').strip()
        if not email:
          errors['email'] = _(u"Name is mandatory.")
        else:
          data.email = email

        language = request.POST.get('language', '').strip()
        if not language:
          errors['language'] = _(u"Language is mandatory")
        else:
          data.stprofile.mobile_phone = language

        if not errors:
          
          data.save()
          return HttpResponseRedirect( u'%s?status_message=%s'  % (reverse('users_list'), _(u'User edited succefully')))
        else:
          # render form with errors and previous user input
          return render(request, 'user_edit.html',
          {'pk': pk,'errors': errors})
      elif request.POST.get('cancel_button') is not None:
        # redirect to home page on cancel button
        return HttpResponseRedirect( u'%s?status_message=%s' % (reverse('users_list'), _('Editing user canceled')))
    else:
     # initial form render
     return render(request, 'user_one_edit.html',
     {'use': use, 'pk': pk})