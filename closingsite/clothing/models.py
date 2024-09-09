from django.db import models


class ClothingModel(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    desc = models.TextField(verbose_name='Описание')
    price = models.IntegerField(verbose_name='Цена')
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика')

    class Meta:
        verbose_name = 'Одежда'
        ordering = ['title']


class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название рубрики')

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
