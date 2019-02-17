from django.shortcuts import render
from django.shortcuts import get_object_or_404, get_list_or_404
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from office.models import Subject, Teacher, Files


class TeacherIndex(LoginRequiredMixin, View):
    """ Class for get html template of all subjects"""
    login_url = '/auth/login/'
    redirect_field_name = ''

    def get(self, request):
        teachers = get_list_or_404(Teacher.objects.order_by('profile__name'))
        for teacher in teachers:
            print(teacher.get_absolute_url())
            print(teacher.subjects.all())
        return render(request, 'public_teacher/index.html', context={
            "teachers": teachers,
        })


class TeacherDetail(LoginRequiredMixin, View):
    """ Class for get detail subject"""
    login_url = '/auth/login/'
    redirect_field_name = ''

    def get(self, request, username):

        teacher = get_object_or_404(Teacher, profile__user__username=username)

        return render(request, 'public_teacher/detail.html', context={
            "subjects": teacher.subjects,
            "teacher": teacher,
            "files": teacher.files.all(),
        })
