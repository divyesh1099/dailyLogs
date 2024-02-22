from django.urls import path
from . import views
app_name = 'api'
urlpatterns = [
    path('', views.index, name='index'),
    path('logs/', views.LogEntryListCreate.as_view(), name='log-list-create'),
    path('logs/<int:pk>/', views.LogEntryDetailUpdateDelete.as_view(), name='log-detail-update-delete'),

]