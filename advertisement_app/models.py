from typing import Any
from django.db import models
from django.contrib import admin
from django.utils import timezone
from django.utils.html import format_html

# Create your models here.
class Advertisement(models.Model):
    title = models.CharField(max_length = 100, verbose_name = 'Название товара')
    description = models.TextField(verbose_name = 'Описание товара')
    price = models.DecimalField(verbose_name = 'Цена товара', max_digits = 8, decimal_places = 2)
    auction = models.BooleanField(verbose_name = 'Возможность торга', help_text = 'Возможность или невозможность торга')
    created_at = models.DateTimeField(verbose_name = 'Дата создания', auto_now_add = True) # - Заполняется при добавлении данных в ячейки
    updated_at = models.DateTimeField(verbose_name = 'Дата обновления',auto_now = True) # - Заполняется при любых изменениях данных в ячейке

    @admin.display(description = 'Дата создания')
    def created_date(self):
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="color:green; font-weight:bold">Сегодня в {}</span>', created_time
            )
        
        return self.created_at.strftime('%d.%m.%Y в %H:%M:%S')
    
    @admin.display(description = 'Дата обновления')
    def updated_date(self):
        if self.updated_at.date() == timezone.now().date():
            updated_time = self.updated_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="color:green; font-weight:bold">Сегодня в {}</span>', updated_time
            )
        
        return self.created_at.strftime('%d.%m.%Y в %H:%M:%S')
      
        
    def __str__(self):
        return f'Advertisement(id = {self.id}, title = {self.title}, description = {self.description}, price = {self.price}, auction = {self.auction}, created_at = {self.created_at}, updated_at = {self.updated_at})'

    class Meta:
        db_table = 'advertisement'

    