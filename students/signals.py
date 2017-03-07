import logging
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models.student import Student
from .models.group import Group
from .models.exam import Exam


####student
@receiver(post_save, sender=Student)
def log_student_updated_added_event(sender, **kwargs):
	logger = logging.getLogger(__name__)
	student = kwargs['instance']
	if kwargs['created']:
		logger.info("Student added: %s %s (ID: %d)", student.first_name, 
			student.last_name, student.id)
	else:
		logger.info("Student updated: %s %s (ID: %d)", student.first_name, 
			student.last_name, student.id)

@receiver(post_delete, sender=Student)
def log_student_deleted_event(sender, **kwargs):
	logger = logging.getLogger(__name__)
	student = kwargs['instance']
	logger.info("Student deleted: %s %s (ID: %d)", student.first_name,
       student.last_name, student.id)


#####groups
@receiver(post_save, sender=Group)
def log_group_updated_added_event(sender, **kwargs):
	logger = logging.getLogger(__name__)
	group = kwargs['instance']
	if kwargs['created']:
		logger.info("Group added: %s (ID: %d)", group.title, group.id)
	else:
		logger.info("Group updated: %s (ID: %d)", group.title, group.id)

@receiver(post_delete, sender=Group)
def log_group_deleted_event(sender, **kwargs):
	logger = logging.getLogger(__name__)
	group = kwargs['instance']
	logger.info("Group deleted: %s (ID: %d)", group.title, group.id)


	#####exams
@receiver(post_save, sender=Exam)
def log_exam_updated_added_event(sender, **kwargs):
	logger = logging.getLogger(__name__)
	exam = kwargs['instance']
	if kwargs['created']:
		logger.info("Exam added: %s (ID: %d)", exam.title, exam.id)
	else:
		logger.info("Exam updated: %s (ID: %d)", exam.title, exam.id)

@receiver(post_delete, sender=Exam)
def log_exam_deleted_event(sender, **kwargs):
	logger = logging.getLogger(__name__)
	exam = kwargs['instance']
	logger.info("Exam deleted: %s (ID: %d)", exam.title, exam.id)
