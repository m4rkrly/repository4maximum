from typing import Any
from django.db import models

# Create your models here.
class Advertisement(models.Model):
    title = models.CharField(max_length = 100, verbose_name = 'Название товара')
    description = models.TextField(verbose_name = 'Описание товара')
    price = models.DecimalField(verbose_name = 'Цена товара', max_digits = 8, decimal_places = 2)
    auction = models.BooleanField(verbose_name = 'Возможность торга', help_text = 'Возможность или невозможность торга')
    created_at = models.DateTimeField(auto_now_add = True) # - Заполняется при добавлении данных в ячейки
    updated_at = models.DateTimeField(auto_now = True) # - Заполняется при любых изменениях данных в ячейке

    def __str__(self):
        return f'Advertisement(id = {self.id}, title = {self.title}, description = {self.description}, price = {self.price}, auction = {self.auction}, created_at = {self.created_at}, updated_at = {self.updated_at})'

    class Meta:
        db_table = 'advertisement'

    