from django.db import models
from accounts.models import Account
import uuid
# Create your models here.
class BasicCv(models.Model):
    owner = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50)
    idno = models.CharField(max_length=50)
    dob = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    nation = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    religion = models.CharField(max_length=50)

    university = models.CharField(max_length=200, blank=True)
    university_year = models.CharField(max_length=50, blank=True)
    university_course = models.CharField(max_length=200, blank=True)

    highschool = models.CharField(max_length=200)
    highschool_year = models.CharField(max_length=50)
    highschool_cert = models.CharField(max_length=200)

    primary = models.CharField(max_length=200)
    primary_year = models.CharField(max_length=50)
    primary_cert = models.CharField(max_length=200)


    skill_one = models.CharField(max_length=50)
    skill_two = models.CharField(max_length=50)
    skill_three = models.CharField(max_length=50)

    hobby_one = models.CharField(max_length=50)
    hobby_two = models.CharField(max_length=50) 
    hobby_three = models.CharField(max_length=50)
    
    referee_name_one = models.CharField(max_length=50)
    referee_contact_one = models.CharField(max_length=20)
    referee_post_one = models.CharField(max_length=200)
    referee_company_one = models.CharField(max_length=200)
    
    referee_name_two = models.CharField(max_length=50)
    referee_contact_two = models.CharField(max_length=20)
    referee_post_two = models.CharField(max_length=200)
    referee_company_two = models.CharField(max_length=200)
    
    referee_name_three = models.CharField(max_length=50, blank=True)
    referee_contact_three = models.CharField(max_length=20, blank=True)
    referee_post_three = models.CharField(max_length=200, blank=True)
    referee_company_three = models.CharField(max_length=200, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name
    

class AdvancedBasic(models.Model):
    owner = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50)
    idno = models.CharField(max_length=50)
    dob = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    nation = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    religion = models.CharField(max_length=50)

    career = models.CharField(max_length=200, blank=True)

    university = models.CharField(max_length=200, blank=True)
    university_year = models.CharField(max_length=50, blank=True)
    university_course = models.CharField(max_length=200, blank=True)

    highschool = models.CharField(max_length=200)
    highschool_year = models.CharField(max_length=50)
    highschool_cert = models.CharField(max_length=200)

    primary = models.CharField(max_length=200)
    primary_year = models.CharField(max_length=50)
    primary_cert = models.CharField(max_length=200)

    work1 = models.CharField(max_length=200)
    work1_year = models.CharField(max_length=50)

    work2 = models.CharField(max_length=200, blank=True)
    work2_year = models.CharField(max_length=50, blank=True)

    work3 = models.CharField(max_length=200, blank=True)
    work3_year = models.CharField(max_length=50, blank=True)

    work4 = models.CharField(max_length=200, blank=True)
    work4_year = models.CharField(max_length=50, blank=True)

    skill_one = models.CharField(max_length=50)
    skill_two = models.CharField(max_length=50)
    skill_three = models.CharField(max_length=50)

    hobby_one = models.CharField(max_length=50)
    hobby_two = models.CharField(max_length=50) 
    hobby_three = models.CharField(max_length=50)
    
    referee_name_one = models.CharField(max_length=50)
    referee_contact_one = models.CharField(max_length=20)
    referee_post_one = models.CharField(max_length=200)
    referee_company_one = models.CharField(max_length=200)
    
    referee_name_two = models.CharField(max_length=50)
    referee_contact_two = models.CharField(max_length=20)
    referee_post_two = models.CharField(max_length=200)
    referee_company_two = models.CharField(max_length=200)
    
    referee_name_three = models.CharField(max_length=50, blank=True)
    referee_contact_three = models.CharField(max_length=20, blank=True)
    referee_post_three = models.CharField(max_length=200, blank=True)
    referee_company_three = models.CharField(max_length=200, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name