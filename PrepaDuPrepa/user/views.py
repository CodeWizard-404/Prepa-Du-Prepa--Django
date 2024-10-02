from http.client import HTTPResponse
from django.shortcuts import render, get_object_or_404
from user.models import CustomUser, course, subject, content
from django.http import HttpResponse

# Create your views here.


def course_index(request):
    courses = course.objects.all() 
    return render(request, 'course/course.html', {'courses': courses})

def course_show(request, course_id):
    course_obj = course.objects.get(courseId=course_id)
    return render(request, 'course/show.html', {'course': course_obj})

def download_pdf(request, content_id):
    c = get_object_or_404(content, pk=content_id)
    pdf_data = c.document.read()
    
    response = HttpResponse(pdf_data, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{c.document.name}"'
    return response

def index(request):
    professors = CustomUser.objects.filter(roles='ROLE_TEACHER')
    courses = course.objects.all()  
    return render(request, 'home/index.html', {'professors': professors, 'courses': courses})

def profile(request):
    return render(request, 'authentication/profile.html')

def registration(request):
    return render(request, 'authentication/register.html')

def login(request):
    return render(request, 'authentication/login.html')

def support(request):
    courses = course.objects.all()  
    return render(request, 'support/support.html', {'courses': courses})

def section(request):
    return render(request, 'course/course.html')

def newcourse(request):
    return render(request, 'course/new.html')

def show(request):
    return render(request, 'course/show.html')