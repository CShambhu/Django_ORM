from django.contrib import admin
from MyAPP.models import Restaurant, Rating, Sale

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name','website','date_opened','latitude','longitude','restaurant_type')


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('user','restaurant','rating')

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ('restaurant','income','datetime')













