from django.core.management.base import BaseCommand
from students.models.student import Student
from students.models.group import Group
from students.models.exam import Exam
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _


class Command(BaseCommand):
	args = '<model_name model_name ...>'
	help = "Prints to console number of student related objects in a database."

	def handle(self, *args, **options):
		if 'student' in args:
			self.stdout.write( _(u'Number of students in database: %d') % Student.objects.count())

		if 'group' in args:
			self.stdout.write( _(u'Number of groups in database: %d') % Group.objects.count())

		if 'exam' in args:
			self.stdout.write( _(u'Number of exams in database: %d') % Exam.objects.count())


	

