from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from assets.models import OwnedProperty, Structure, AddressModel, Locks


class PropertyListView(LoginRequiredMixin, ListView):
    model = OwnedProperty
    template_name = "assets/property_list.html"

    def get_queryset(self):
        qs = OwnedProperty.objects.filter(owner=self.request.user)
        return qs


class PropertyDetailView(LoginRequiredMixin, DetailView):
    model = OwnedProperty
    template_name = "assets/property_detail.html"

    def get_queryset(self):
        qs = OwnedProperty.objects.filter(owner=self.request.user)
        return qs


class PropertyCreateView(LoginRequiredMixin, CreateView):
    model = OwnedProperty
    template_name = "assets/property_create.html"
    fields = [
        "legal_name",
    ]

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy("assets:property_list")


class PropertyEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = OwnedProperty
    template_name = "assets/property_update.html"
    fields = ["legal_name"]

    def test_func(self):
        obj = self.get_object()
        return obj.owner == self.request.user


class PropertyDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = OwnedProperty
    template_name = "assets/property_delete.html"
    success_url = reverse_lazy("assets:property_list")

    def test_func(self):
        obj = self.get_object()
        return obj.owner == self.request.user


class StructureCreateView(LoginRequiredMixin, CreateView):
    model = Structure
    template_name = "assets/structure_create.html"
    fields = ["name", "description", "structure_type", "owned_property"]

    def get_queryset(self):
        return OwnedProperty.objects.filter(owner=self.request.user)


class StructureDetailView(LoginRequiredMixin, DetailView):
    model = Structure
    template_name = "assets/structure_detail.html"


class LocksCreateView(LoginRequiredMixin, CreateView):
    model = Locks
    template_name = "assets/locks_create.html"
    fields = [
        "description",
        "floor",
        "room",
        "lock_type",
        "manufacturer",
        "key_marking",
        "key_image",
        "structure",
    ]
    success_url = reverse_lazy("assets:property_list")
