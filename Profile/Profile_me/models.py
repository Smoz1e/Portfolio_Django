from django.db import models

class AboutMe(models.Model):
    name = models.CharField(max_length=100)
    programming_level = models.CharField(max_length=100)
    story = models.TextField(blank=True, null=True)  # Поле для вашей истории или биографии
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)  # Поле для аватарки

    def __str__(self):
        return self.name


class ProgrammingLanguage(models.Model):
    name = models.CharField(max_length=100)
    experience_years = models.IntegerField()
    logo = models.ImageField(upload_to='language_logos/', default='path/to/default_logo.png')  # Поле для изображения логотипа языка

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='projects/')
    site_link = models.URLField(blank=True)
    file_link = models.URLField(blank=True)
    description = models.TextField()

    def __str__(self):
        return self.title

class WordsForEmployer(models.Model):
    content = models.TextField()

    def __str__(self):
        return self.content[:50]  # Ограничим вывод для __str__ до 50 символов, например

# Create your models here.
