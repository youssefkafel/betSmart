from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='dashboard'),
    path('create-bankroll', views.create_bankroll, name='create_bankroll'),
    path('create-bet', views.create_bet, name='create_bet'),
    path('update-bankroll', views.update_bet, name='update_bankroll'),
    path('update-bet', views.update_bet, name='update_bet'),
    path('bankroll/<int:id>', views.index_bankroll, name='index_bankroll'),

]