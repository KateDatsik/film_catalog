from django.db import models
from django.contrib.auth.models import User


class Genre(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название жанра')

    def __str__(self):
        return self.name


class Movie(models.Model):
    title_ru = models.CharField(max_length=200, verbose_name='Название на русском')
    title_orig = models.CharField(max_length=200, verbose_name='Оригинальное название')
    movie_rating = models.FloatField(null=True, blank=True, verbose_name='Рейтинг фильма')
    genres = models.ManyToManyField(Genre, verbose_name='Жанры')
    year = models.PositiveIntegerField(null=True, blank=True, verbose_name='Год выпуска')
    description = models.TextField(max_length=1024, null=True, verbose_name='Описание')
    poster = models.FileField(upload_to='movies/posters/', null=True, blank=True, verbose_name='Постер')
    published = models.BooleanField(default=False, verbose_name='Публикация')

    def __str__(self):
        return f"{self.title_ru} ({self.year})" if self.year else self.title_ru


class Comment(models.Model):
    film = models.ForeignKey(Movie, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'Comment by {self.user} on {self.film}'


class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
