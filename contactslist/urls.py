from django.urls import path, reverse_lazy
from . import views

app_name='contact'
urlpatterns = [
    path('', views.MainList.as_view(), name='all'),
    path('contact/<int:pk>', views.Detail.as_view(), name='contact_detail'),
    path('contact/create',
        views.Create.as_view(success_url=reverse_lazy('contact:all')), name='contact_create'),
    path('contact/<int:pk>/update',
        views.Upate.as_view(success_url=reverse_lazy('contact:all')), name='contact_update'),
    path('contact/<int:pk>/delete',
        views.Delete.as_view(success_url=reverse_lazy('contact:all')), name='contact_delete'),
    path('contact_picture/<int:pk>', views.stream_file, name='contact_picture'),
]