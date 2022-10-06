from django.db import models

from django.core.validators import MinValueValidator
from django.urls import reverse
from django.contrib.auth.models import User


class Post(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
    )
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,
                               verbose_name='автор поста',
                               blank=True,
                               null=True,
                               on_delete=models.CASCADE)
    category = models.ForeignKey(to='Category',
                                 on_delete=models.CASCADE,
                                 related_name='posts',)

    def __str__(self):
        return f'{self.name.title()}: {self.description[:20]}'

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name.title()


class Comment(models.Model):
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             verbose_name='Пост',
                             related_name='comments',
                             blank=True,
                             null=True)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               verbose_name='Автор комментария',
                               blank=True,
                               null=True)
    content = models.TextField(verbose_name='Текст комментария')
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(verbose_name='Статус комментария', default=False)
