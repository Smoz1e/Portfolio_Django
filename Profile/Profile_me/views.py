from django.shortcuts import render
from .models import *

def index(request):
    # Получаем данные для отображения из базы данных
    about_me_list = AboutMe.objects.all()
    programming_languages = ProgrammingLanguage.objects.all()
    projects = Project.objects.all()
    words_for_employer = WordsForEmployer.objects.all()
    certificates = Certificate.objects.all()
    
    # Передаем данные в шаблон index.html
    return render(request, 'index.html', {
        'about_me_list': about_me_list,
        'programming_languages': programming_languages,
        'projects': projects,
        'words_for_employer': words_for_employer,
        'certificates': certificates,
    })
