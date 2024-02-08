from django.shortcuts import render
from django.http import HttpResponse
from .models import Course
from django.views.generic.edit import CreateView
from django.urls import reverse
# Create your views here.
def index(request):
    return HttpResponse('Hello, world.')

def courses(request):
    
    number_of_years = request.GET.get('number_of_years',3)


    course_list = Course.objects.filter(number_of_years__gte=number_of_years).order_by('-number_of_years')
    context = {
        'courses':course_list
    }
    return render(request,'myapp/courses.html',context)

class CourseCreateView(CreateView):
    model = Course
    fields = "__all__"

    def get_success_url(self):
        return reverse('course')