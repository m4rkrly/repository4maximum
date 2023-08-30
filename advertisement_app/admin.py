from django.contrib import admin
from .models import Advertisement

# Register your models here.


class AdminAdvertisement(admin.ModelAdmin):
    list_display = ['id', 'user', 'title', 'description', 'price', 'auction', 'created_date', 'updated_date', 'show_image']
    list_filter = ['auction', 'created_at']
    actions = ['auction_false', 'auction_true']

    fieldsets = (
        ('Основная информация'
         ,
         {
             'fields':('user', 'title', 'description', 'price', 'image')
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
