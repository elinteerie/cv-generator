from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from .models import Profile
import os
from htmltopdf import HTMLURLToPDF


# Create your views here.


def accept(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        summary = request.POST.get('summary', '')
        degree = request.POST.get('degree', '')
        school = request.POST.get('school', '')
        university = request.POST.get('university', '')
        previous_work = request.POST.get('previous_work', '')
        skill = request.POST.get('skill', '')
        profile = Profile(name=name, email=email, phone=phone, summary=summary, degree=degree, school=school,
                          university=university, previous_work=previous_work, skill=skill).save()

    return render(request, 'pdf/accept.html')


def resume(request, id):
    user_profile = Profile.objects.get(pk=id)
    filename = 'filename.pdf'

  # HTML FIle to be converted to PDF - inside your Django directory
    template = get_template('pdf/resume.html')

    context = {'user_profile': user_profile}

  # Render the HTML
    html = template.render(context)

    return response
