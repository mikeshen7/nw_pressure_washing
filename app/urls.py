from django.urls import path
from .views import HomePageView, ContactListView, ContactDetailView, ContactCreateView, ContactUpdateView, ContactDeleteView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('list/', ContactListView.as_view(), name='contact_list'),
    path('<int:pk>/', ContactDetailView.as_view(), name='contact_detail'),
    path('create/', ContactCreateView.as_view(), name='contact_create'),
    path('<int:pk>/update/', ContactUpdateView.as_view(), name='contact_update'),
    path('<int:pk>/delete/', ContactDeleteView.as_view(), name='contact_delete'),
]