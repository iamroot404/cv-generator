from multiprocessing import context
from django.shortcuts import render, redirect, get_object_or_404
from . forms import BasicCvForm, AdvancedBasicForm
from .models import BasicCv, AdvancedBasic
from django.template import loader
from django.http import HttpResponse
import pdfkit
import datetime
from django.contrib.auth.decorators import login_required
from products.models import Product

# Create your views here.
@login_required(login_url= 'login')
def cv_list(request):
    temps = Product.objects.all()
    context = {
        'temps': temps,
    } 
    return render(request, 'generator/cv_list.html', context)

@login_required(login_url= 'login') 
def basicCv(request):
    current_user = request.user 
    if request.method =="POST":

        user = current_user
        name = request.POST.get("name", "")
        idno = request.POST.get("idno", "")
        dob = request.POST.get("dob", "")
        mobile = request.POST.get("mobile", "")
        email = request.POST.get("email", "")
        gender = request.POST.get("gender", "")
        nation = request.POST.get("nation", "")
        status = request.POST.get("status", "")
        language = request.POST.get("language", "")
        religion = request.POST.get("religion", "")
        university = request.POST.get("unvname", "")
        year = request.POST.get("unvstudy", "")
        course = request.POST.get("unvcourse", "")
        highschool = request.POST.get("highname", "")
        highyear = request.POST.get("highyear", "")
        highcert = request.POST.get("highcert", "")
        primary = request.POST.get("priname", "")
        priyear = request.POST.get("priyear", "")
        pricert = request.POST.get("pricert", "")
        skill_one = request.POST.get("skill1", "")
        skill_two = request.POST.get("skill2", "")
        skill_three = request.POST.get("skill3", "")
        hobby_one = request.POST.get("hob1", "")
        hobby_two = request.POST.get("hob2", "")
        hobby_three = request.POST.get("hob3", "")
        ref_post_one = request.POST.get("refpost", "")
        ref_company_one = request.POST.get("refcompany", "")
        ref_name_one = request.POST.get("refname", "")
        ref_cont_one = request.POST.get("refcont", "")
        ref_post_two = request.POST.get("refpost2", "")
        ref_company_two = request.POST.get("refcompany2", "")
        ref_name_two = request.POST.get("refname2", "")
        ref_cont_two = request.POST.get("refcont2", "")
        ref_post_three = request.POST.get("refpost3", "")
        ref_company_three = request.POST.get("refcompany3", "")
        ref_name_three = request.POST.get("refname3", "")
        ref_cont_three = request.POST.get("refcont3", "")
        
        
        basic = BasicCv(name=name, idno=idno, dob=dob, phone=mobile, email=email, gender=gender, nation=nation, status=status,
        language=language, religion=religion, university=university, university_year=year, university_course=course, highschool=highschool,
        highschool_year=highyear, highschool_cert=highcert, primary=primary, primary_year=priyear, primary_cert=pricert, skill_one=skill_one, 
        skill_two=skill_two, skill_three=skill_three, hobby_one=hobby_one, hobby_two=hobby_two, hobby_three=hobby_three, referee_post_one=ref_post_one, 
        referee_company_one=ref_company_one, referee_name_one=ref_name_one, referee_contact_one=ref_cont_one, referee_post_two=ref_post_two, 
        referee_company_two=ref_company_two, referee_name_two=ref_name_two, referee_contact_two=ref_cont_two,referee_post_three=ref_post_three, 
        referee_company_three=ref_company_three, referee_name_three=ref_name_three, referee_contact_three=ref_cont_three)
        

        basic.owner = current_user
        basic.save()
        return redirect('download_list')
    return render(request, 'generator/basic_cv.html')

@login_required(login_url= 'login')
def editBasic(request, pk):
    userdetails = get_object_or_404(BasicCv, owner=request.user, id=pk)
    if request.method == 'POST':
         basic_form = BasicCvForm(request.POST, instance=userdetails)
         if basic_form.is_valid():
            basic_form.save()
            return redirect('basic_preview', pk=pk)

    else:
        basic_form = BasicCvForm(instance=userdetails)

    context = {
        'basic_form': basic_form,
        'userdetails': userdetails,
        }

    return render(request, 'generator/editBasic.html', context)

@login_required(login_url= 'login')
def editAdvBasic(request, pk):
    userdetails = get_object_or_404(AdvancedBasic, owner=request.user, id=pk)
    if request.method == 'POST':
         basic_form = AdvancedBasicForm(request.POST, instance=userdetails)
         if basic_form.is_valid():
            basic_form.save()
            return redirect('advbasic_preview', pk=pk)

    else:
        basic_form = AdvancedBasicForm(instance=userdetails)

    context = {
        'basic_form': basic_form,
        'userdetails': userdetails,
        }

    return render(request, 'generator/editAdvBasic.html', context)

@login_required(login_url= 'login')
def AdvancedBasicCV(request):
    current_user = request.user 
    if request.method =="POST":

        user = current_user
        name = request.POST.get("name", "")
        idno = request.POST.get("idno", "")
        dob = request.POST.get("dob", "")
        mobile = request.POST.get("mobile", "")
        email = request.POST.get("email", "")
        gender = request.POST.get("gender", "")
        nation = request.POST.get("nation", "")
        status = request.POST.get("status", "")
        language = request.POST.get("language", "")
        religion = request.POST.get("religion", "")
        career = request.POST.get("career", "")
        university = request.POST.get("unvname", "")
        year = request.POST.get("unvstudy", "")
        course = request.POST.get("unvcourse", "")
        highschool = request.POST.get("highname", "")
        highyear = request.POST.get("highyear", "")
        highcert = request.POST.get("highcert", "")
        primary = request.POST.get("priname", "")
        priyear = request.POST.get("priyear", "")
        pricert = request.POST.get("pricert", "")
        work1 = request.POST.get("work1", "")
        work1_year = request.POST.get("work1_year", "")
        work2 = request.POST.get("work2", "")
        work2_year = request.POST.get("work2_year", "")
        work3 = request.POST.get("work3", "")
        work3_year = request.POST.get("work3_year", "")
        work4 = request.POST.get("work4", "")
        work4_year = request.POST.get("work3_year", "")
        skill_one = request.POST.get("skill1", "")
        skill_two = request.POST.get("skill2", "")
        skill_three = request.POST.get("skill3", "")
        hobby_one = request.POST.get("hob1", "")
        hobby_two = request.POST.get("hob2", "")
        hobby_three = request.POST.get("hob3", "")
        ref_post_one = request.POST.get("refpost", "")
        ref_company_one = request.POST.get("refcompany", "")
        ref_name_one = request.POST.get("refname", "")
        ref_cont_one = request.POST.get("refcont", "")
        ref_post_two = request.POST.get("refpost2", "")
        ref_company_two = request.POST.get("refcompany2", "")
        ref_name_two = request.POST.get("refname2", "")
        ref_cont_two = request.POST.get("refcont2", "")
        ref_post_three = request.POST.get("refpost3", "")
        ref_company_three = request.POST.get("refcompany3", "")
        ref_name_three = request.POST.get("refname3", "")
        ref_cont_three = request.POST.get("refcont3", "")
        
        
        AdvBasic = AdvancedBasic(name=name, idno=idno, dob=dob, phone=mobile, email=email, gender=gender, nation=nation, status=status,
        language=language, religion=religion, career=career, university=university, university_year=year, university_course=course, highschool=highschool,
        highschool_year=highyear, highschool_cert=highcert, primary=primary, primary_year=priyear, primary_cert=pricert, work1=work1, work1_year=work1_year, work2=work2, work2_year=work2_year, work3=work3, work3_year=work3_year, work4=work4, work4_year=work4_year, skill_one=skill_one, 
        skill_two=skill_two, skill_three=skill_three, hobby_one=hobby_one, hobby_two=hobby_two, hobby_three=hobby_three, referee_post_one=ref_post_one, 
        referee_company_one=ref_company_one, referee_name_one=ref_name_one, referee_contact_one=ref_cont_one, referee_post_two=ref_post_two, 
        referee_company_two=ref_company_two, referee_name_two=ref_name_two, referee_contact_two=ref_cont_two,referee_post_three=ref_post_three, 
        referee_company_three=ref_company_three, referee_name_three=ref_name_three, referee_contact_three=ref_cont_three)
        

        AdvBasic.owner = current_user
        AdvBasic.save()
        return redirect('advDownload_list')
    return render(request, 'generator/AdvBasic.html')


@login_required(login_url= 'login')
def resume(request, pk):
    current_user = request.user
    user_details = BasicCv.objects.get(id=pk, owner=current_user)
    template = loader.get_template('generator/resume.html')
    html = template.render({'user_details':user_details})
    options = {
        'page-size':'letter',
        'encoding':"UTF-8",
    }
    pdf = pdfkit.from_string(html,False,options)
    response = HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition'] = 'attachment'
    filename = 'resume.pdf'
    return response

@login_required(login_url= 'login')
def advBr(request, pk):
    current_user = request.user
    user_details = AdvancedBasic.objects.get(id=pk, owner=current_user)
    template = loader.get_template('generator/advbresume.html')
    html = template.render({'user_details':user_details})
    options = {
        'page-size':'letter',
        'encoding':"UTF-8",
    }
    pdf = pdfkit.from_string(html,False,options)
    response = HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition'] = 'attachment'
    filename = 'resume.pdf'
    return response

@login_required(login_url = 'login')
def download_list(request):
    current_user = request.user 
    basic = BasicCv.objects.filter(owner=current_user)
    advBasic = AdvancedBasic.objects.filter(owner=current_user)
    context = {
        'basic': basic,
        'advBasic': advBasic,
    }
    return render(request, 'generator/download_list.html', context)

@login_required(login_url = 'login')
def advDownload_list(request):
    current_user = request.user 
    basic = AdvancedBasic.objects.filter(owner=current_user)
    return render(request, 'generator/advdownload_list.html', {'basic':basic})

@login_required(login_url= 'login')
def basic_preview(request, pk):
    current_user = request.user 
    user_details = BasicCv.objects.get(id=pk, owner=current_user)
    context = {
        'user_details': user_details
    }

    return render(request, 'generator/basic_preview.html', context)

@login_required(login_url= 'login')
def advbasic_preview(request, pk):
    current_user = request.user 
    user_details = AdvancedBasic.objects.get(id=pk, owner=current_user)
    context = {
        'user_details': user_details
    }

    return render(request, 'generator/advbasic_preview.html', context)

@login_required(login_url = 'login')
def delete_cv(request, pk):
    current_user = request.user 
    item = BasicCv.objects.get(id=pk, owner=current_user)
    context = {'item': item}
    item.delete()
    return redirect('download_list')

@login_required(login_url = 'login')
def advdelete_cv(request, pk):
    current_user = request.user 
    item = AdvancedBasic.objects.get(id=pk, owner=current_user)
    context = {'item': item}
    item.delete()
    return redirect('advDownload_list')

    