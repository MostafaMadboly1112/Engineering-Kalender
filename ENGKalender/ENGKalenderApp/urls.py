from django.urls import path
from .views import  Booking_list, BookingView

app_name = 'ENGKalenderApp'

urlpatterns = [
    path('booking_list/', Booking_list.as_view(), name= 'BookingList'),
    path('book/',BookingView.as_view(), name='BookingView' )
]