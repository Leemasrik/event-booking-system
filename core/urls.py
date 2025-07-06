from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # HTML Views
    path('events/', views.event_list, name='event_list'),
    path('events/<int:event_id>/', views.event_detail, name='event_detail'),
    path('bookings/', views.booking_list, name='booking_list'),
    path('bookings/success/<int:booking_id>/', views.booking_success, name='booking_success'),
    path('scan/', views.scan_attendance, name='scan_attendance'),
    path('scan-qr/', views.scan_qr_camera, name='scan_qr'),
    path('pay/<int:event_id>/', views.fake_payment, name='fake_payment'),
    path('success/<int:booking_id>/', views.booking_success, name='booking_success'), 
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
       path('signup/', views.signup_view, name='signup'),
     path('events/create/', views.create_event, name='create_event'),






    # JSON APIs
    path('api/events/', views.api_event_list, name='api_event_list'),
    path('api/events/<int:event_id>/', views.api_event_detail, name='api_event_detail'),
    path('api/book/<int:event_id>/', views.book_ticket, name='book_ticket'), 
    path('api/qr/<int:booking_id>/', views.download_qr_code),           # Download QR
    path('api/attend/<str:ticket_id>/', views.mark_attendance),   
    path('api/payment-webhook/', views.payment_webhook, name='payment_webhook'),
    path('api/attend/submit/', views.attendance_form),


 
]
