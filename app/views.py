from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Contact
from django.urls import reverse_lazy

# from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
# from .serializer import RosterSerializer
# from .permissions import isOwnerOrReadOnly


class HomePageView(TemplateView):
    template_name = 'home.html' # points to html file


class ContactListView(ListView):
    template_name = 'contact_list.html'
    model = Contact
    context_object_name = 'contacts'


class ContactDetailView(DetailView):
    template_name = 'contact_detail.html'
    model = Contact


class ContactCreateView(CreateView):
    template_name = 'contact_create.html'
    model = Contact
    fields = ['description', 'last_name', 'first_name', 'email', 'address', 'phone']


class ContactUpdateView(UpdateView):
    template_name = 'contact_update.html'
    model = Contact
    fields = ['description', 'last_name', 'first_name', 'email', 'address', 'phone']


class ContactDeleteView(DeleteView):
    template_name = 'contact_delete.html'
    model = Contact
    success_url = reverse_lazy('contact_list')

