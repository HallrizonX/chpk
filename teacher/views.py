from django.shortcuts import render
from django.shortcuts import get_object_or_404, get_list_or_404
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from office.models import Subject, Teacher, Files, Profile


class TeacherIndex(LoginRequiredMixin, View):
    """ Class for get html template of all subjects"""
    login_url = '/auth/login/'
    redirect_field_name = ''

    def get(self, request):
        if Profile.objects.get(user=request.user).access_profile == "":
            return render(request, 'office/not_access.html', {})

        teachers = get_list_or_404(Teacher.objects.order_by('profile__name'))

        return render(request, 'public_teacher/index.html', context={
            "teachers": teachers,
        })


class TeacherDetail(LoginRequiredMixin, View):
    """ Class for get detail subject"""
    login_url = '/auth/login/'
    redirect_field_name = ''

    def get(self, request, username):
        if Profile.objects.get(user=request.user).access_profile == "":
            return render(request, 'office/not_access.html', {})

        teacher = get_object_or_404(Teacher, profile__user__username=username)

        return render(request, 'public_teacher/detail.html', context={
            "subjects": teacher.subjects,
            "teacher": teacher,
            "files": teacher.files.all(),
        })
