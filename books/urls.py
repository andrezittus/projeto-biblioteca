from django.urls import path
from books import views

app_name = 'books'

urlpatterns = [
    path('search/', views.search, name='search'),
    path('', views.index, name='index'),

    #book crud
    path('book/<int:book_id>/', views.book, name='book'),
    path('book/create/', views.create, name='create'),
    path('book/<int:book_id>/upgrade', views.update, name='update'),
    path('book/<int:book_id>/delete', views.delete, name='delete'),

    #user 
    path('user/create/', views.register, name='register'),
    path('user/login/', views.login_view, name='login'),
    path('user/logout/', views.logout_view, name='logout'),
    path('user/update/', views.user_update, name='user_update'),

    
]
