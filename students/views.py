from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Student

class StudentListView(ListView):
    model = Student
    template_name = 'students/student_list.html'

class StudentDetailView(DetailView):
    model = Student
    template_name = 'students/student_detail.html'

class StudentCreateView(CreateView):
    model = Student
    template_name = 'students/student_form.html'
    fields = ['name', 'course', 'year_level']

class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'students/student_form.html'
    fields = ['name', 'course', 'year_level']

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'students/student_confirm_delete.html'
    success_url = reverse_lazy('student-list')
