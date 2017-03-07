rom django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import FormActions
from crispy_forms.layout import Submit, Button
from ..util import paginate




class ExamCreateForm(ModelForm):
    class Meta:
        model = Exam
        fields = '__all__'

    def __init__(self,*args, **kwargs):
        super(ExamCreateForm,self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)

            # return HttpResponseRedirect(
            #     u'%s?status_message=5' %  reverse('exam'))


        # set form tag attributes
        self.helper.form_action = reverse('exam_add')
        # self.helper.form_action = u'%s?status_message=5' % reverse('exam_add')

        self.helper.form_method = 'POST'
        self.helper.form_class = 'col-sm-12 form-horizontal'

        # set form field properties
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-8 input-group'
        self.helper.attrs = {'novalidate': ''}

        # add buttons
        # self.helper.layout.fields.append(self)
        self.helper.layout.fields.append(FormActions(
            Submit('add_button', _(u'save'), css_class="btn btn-primary"),
            Submit('cancel_button', _(u'cancel'), css_class="btn btn-link"),
)) 