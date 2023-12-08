from django import forms
from .models import BasicCv, AdvancedBasic


class BasicCvForm(forms.ModelForm):
    class Meta:
        model = BasicCv
        fields = ('name', 'idno', 'dob', 'phone', 'email', 'gender', 'nation', 'status', 'language', 'religion', 'university', 'university_year','university_course','highschool','highschool_year','highschool_cert','primary','primary_year','primary_cert',
        'skill_one','skill_two','skill_three', 'hobby_one','hobby_two','hobby_three','referee_name_one','referee_contact_one','referee_post_one','referee_company_one','referee_name_two','referee_contact_two','referee_post_two','referee_company_two',
        'referee_name_three','referee_contact_three','referee_post_three','referee_company_three')
    def __init__(self, *args, **kwargs):
        super(BasicCvForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

class AdvancedBasicForm(forms.ModelForm):
    class Meta:
        model = AdvancedBasic
        fields = ('name', 'idno', 'dob', 'phone', 'email', 'gender', 'nation', 'status', 'language', 'religion', 'career', 'university', 'university_year','university_course','highschool','highschool_year','highschool_cert','primary','primary_year','primary_cert',
        'work1','work1_year','work2','work2_year','work3','work3_year','work4','work4_year','skill_one','skill_two','skill_three', 'hobby_one','hobby_two','hobby_three','referee_name_one','referee_contact_one','referee_post_one','referee_company_one','referee_name_two','referee_contact_two','referee_post_two','referee_company_two',
        'referee_name_three','referee_contact_three','referee_post_three','referee_company_three')
    def __init__(self, *args, **kwargs):
        super(AdvancedBasicForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'