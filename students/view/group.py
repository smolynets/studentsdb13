from django.utils.translation import ugettext as _
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from ..models.group import Group
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from ..models.student import Student
from django.contrib.auth.decorators import login_required



def grup(request):
   groups = Group.objects.all()
   # try to order grup list
   order_by = request.GET.get('order_by', '')
   if order_by in ('group', 'leader', '#'):
     groups = groups.order_by(order_by)
     if request.GET.get('reverse', '') == '1':
       groups = groups.reverse()
   # paginate groups
   paginator = Paginator(groups, 3)
   page = request.GET.get('page')
   try:
     groups = paginator.page(page)
   except PageNotAnInteger:
   # If page is not an integer, deliver first page.
     groups = paginator.page(1)
   except EmptyPage:
     # If page is out of range (e.g. 9999), deliver
     # last page of results.
     groups = paginator.page(paginator.num_pages)
   return render(request, 'students/grup.html',
{'groups': groups})







@login_required
def groups_add(request):
  # was form posted?
  if request.method == "POST":
    # was form add button clicked?
    if request.POST.get('add_button') is not None:
      # errors collection
      errors = {}
      # data for group object
      data = {'notes': request.POST.get('notes'),'leader': request.POST.get('leader')}
      # validate user input
      title = request.POST.get('title', '').strip()
      if not title:
        errors['title'] = _(u"Name of group is mandatory.")
      else:
        data['title'] = title
      
      # save student
      if not errors:
        group = Group(**data)
        group.save()
        # redirect to students list
        return HttpResponseRedirect( u'%s?status_message=%!'  % (reverse('groups'), _(u'Group added succefully')))
      else:
        # render form with errors and previous user input
        return render(request, 'students/groups_add_edit.html',
        {'students': Student.objects.all().order_by('last_name'),'errors': errors})
    elif request.POST.get('cancel_button') is not None:
      # redirect to home page on cancel button
      return HttpResponseRedirect( u'%s?status_message=%s' % (reverse('groups'), _(u'adding group canceled')))
  else:
   # initial form render
   return render(request, 'students/groups_add_edit.html',
   {'students': Student.objects.all().order_by('last_name')})







@login_required
def groups_edit(request, pk):
    groups = Group.objects.filter(pk=pk)
    students = Student.objects.filter(student_group_id=groups)
    
    if request.method == "POST":
      data = Group.objects.get(pk=pk)
      students = Student.objects.all()
      # was form add button clicked?
      if request.POST.get('add_button') is not None:
        # errors collection
        errors = {}
        # data for group object
        
        data.notes = request.POST.get('notes', '').strip()
        
        
        # validate user input
        title = request.POST.get('title', '').strip()
        if not title:
          errors['title'] = _(u"Name is mandatory.")
        else:
          data.title = title

        leader = request.POST.get('leader', '').strip()
        if not leader:
          errors['leader'] = _(u"Name of leader is mandatory.")
        else:
          try:
            st = Student.objects.filter(pk=leader)
            data.leader = st[0]
          except:
            return HttpResponseRedirect( u'%s?status_message=%s' % (reverse('groups'), _(u'Editing of group canceled. Group hasnt student')))
          
        
        # save student
        if not errors:
          
          data.save()
          # redirect to students list
          return HttpResponseRedirect( u'%s?status_message=%s'  % (reverse('groups'), _(u'Group edited succefully')))
        else:
          # render form with errors and previous user input
          return render(request, 'students/groups_add_edit.html',
          {'pk': pk,'students': Student.objects.all().order_by('last_name'),'errors': errors})
      elif request.POST.get('cancel_button') is not None:
        # redirect to home page on cancel button
        return HttpResponseRedirect( u'%s?status_message=%s' % (reverse('groups'), _('Editing group canceled')))
    else:
     # initial form render
     return render(request, 'students/groups_add_edit.html',
     {'pk': pk, 'group': groups[0], 'students': students})







@login_required
def groups_delete(request, pk):
    groups = Group.objects.filter(pk=pk)
    
    if request.method == "POST":
        if request.POST.get('yes') is not None:
          try:
            groups.delete()
            return HttpResponseRedirect( u'%s?status_message=%s'  % (reverse('groups'), _(u'Group deleted succefully')))
          except:
            return HttpResponseRedirect( u'%s?status_message=%s'  % (reverse('groups'), _u('Remove impossible because in the group are students. You must first remove students')))
        elif request.POST.get('cancel_button') is not None:
          return HttpResponseRedirect( u'%s?status_message=%s'  % (reverse('groups'), _(u'Deleting group canceled')))
        
    else:
        return render(request,
                      'students/groups_delete.html',
                      {'pk': pk, 'group': groups[0]})



def groups_one(request, pk):
   gp = Group.objects.filter(pk=pk)
   students = Student.objects.filter(student_group_id=gp)
   if len(students) > 0:
     # try to order students list
     order_by = request.GET.get('order_by', '')
     if order_by in ('last_name', 'first_name', 'ticket', '#'):
       students = students.order_by(order_by)
       if request.GET.get('reverse', '') == '1':
         students = students.reverse()
     # paginate students
     paginator = Paginator(students, 3)
     page = request.GET.get('page')
     try:
       students = paginator.page(page)
     except PageNotAnInteger:
       # If page is not an integer, deliver first page.
       students = paginator.page(1)
     except EmptyPage:
       # If page is out of range (e.g. 9999), deliver
       # last page of results.
       students = paginator.page(paginator.num_pages)
     return render(request, 'students/groups_one.html',
       {'students': students, 'pk': pk, 'group': gp[0],})
   else:
     return render(request, 'students/groups_one_null.html',
       {'students': students, 'pk': pk, 'group': gp[0],})
