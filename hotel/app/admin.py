from django.contrib import admin
from jalali_date import datetime2jalali, date2jalali
from jalali_date.admin import ModelAdminJalaliMixin, StackedInlineJalaliMixin, TabularInlineJalaliMixin
from .models import *



class FoodAdmin(admin.ModelAdmin):
    list_display =('name','status','foodType' , 'price')
    list_filter =(['name'])
    search_fields = ('name','status','foodType' , 'price')

class OptionAdmin(admin.ModelAdmin):
    list_display =('name','status' )
    list_filter =(['name'])
    search_fields = ('name','status' )

class RoomAdmin(admin.ModelAdmin):
    list_display =('name','price','number','suggested','capacity')
    list_filter =(['name'])
    search_fields = ('name','price','suggested','capacity' , 'number')

class ReserveAdmin(admin.ModelAdmin):
    list_display =('start_date','finish_date','name' , 'family','phone')
    list_filter =(['phone'])
    search_fields = ('start_date','finish_date','name' , 'family','phone')

class ContactAdmin(admin.ModelAdmin):
    list_display =('name','email','phone','subject')
    list_filter =(['name'])
    search_fields = ('name','email','phone' , 'subject')

class FoodReserveAdmin(admin.ModelAdmin):
    list_display =('food','reserve','num_food')
    list_filter =(['reserve'])

admin.site.register(Food , FoodAdmin)
admin.site.register(Option , OptionAdmin)
admin.site.register(Room , RoomAdmin)
admin.site.register(Reserve , ReserveAdmin)
admin.site.register(Contact , ContactAdmin)
admin.site.register(FoodReserve , FoodReserveAdmin)
