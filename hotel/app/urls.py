from django.urls import path
from .views import *
from django.conf.urls import handler404
from . import views


app_name='app'
urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('error404/', error404, name='error404'),
    path('checkout/<int:id>', checkout, name='checkout'),
    path('verify-phone/<int:reserve_id>', verify_phone, name="verify_phone"),
    path('coming-soon/', coming_soon, name='coming_soon'),
    path('contact/', contact, name='contact'),
    path('frequently-questions/', frequently_questions, name='frequently-questions'),
    path('privacy-policy/', privacy_policy, name='privacy_policy'),
    path('room/', room, name='room'),
    path('room-details/<int:id>', room_details, name='room_details'),
    path('services-1/', services_1, name='services_1'),
    path('team/', team, name='team'),
    path('bill/', bill, name='bill'),
    path('restaurant/<int:id>', restaurant, name='restaurant'),
    path('terms-condition/', terms_condition, name='terms_condition'),
    path('show-comment/', show_comment, name='show_comment'),

]
handler404 = 'app.views.error404'
