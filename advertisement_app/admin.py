from django.contrib import admin
from .models import Advertisement

# Register your models here.


class AdminAdvertisement(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'auction', 'created_date', 'updated_date']
    list_filter = ['auction', 'created_at']
    actions = ['auction_false', 'auction_true']

    fieldsets = (
        ('Основная информация'
         ,
         {
             'fields':('title', 'description', 'price')
         }  
         
        ),
        (
            'Дополнительно'
            ,
            {
                'fields':('auction',),
                'classes':['collapse']
            }
        )
    )

    @admin.action(description = 'Убрать возможность торга')
    def auction_false(self, rq, queryset):
        queryset.update(auction = False)

    @admin.action(description = 'Добавить возможность торга')
    def auction_true(self, rq, queryset):
        queryset.update(auction = True)


admin.site.register(Advertisement, AdminAdvertisement)
