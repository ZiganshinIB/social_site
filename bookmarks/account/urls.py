from django.urls import path, include

from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # path('login/', views.user_login, name='login'),


    # Вход
    path('login/', auth_views.LoginView.as_view(), name='login'),
    # Выход
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Сменить пароль
    path('password_change/',
         auth_views.PasswordChangeView.as_view(),
         name='password_change'),
    # Успешно изменил пароль
    path('password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(),
         name='password_change_done'),

    # Сбрось пароля
    path('password_reset/',
         auth_views.PasswordResetView.as_view(),
         name='password_reset'),
    # Ссылка отправлена
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    # Ссылка подверждения для сброса пароля UID
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    # Успешно сбросил пароль
    path('reset/complete/',
         auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),

    # Расширение url для всех случии со входом в систему
    # path('', include('django.contrib.auth.urls')),

    # Регистрация
    path('register/', views.register, name='register'),
    # Первая страница пользователя
    path('', views.dashboard, name='dashboard'),
    # Изменение профиля
    path('edit/', views.edit, name='edit'),
]
