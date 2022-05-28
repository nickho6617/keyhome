from django.urls import path

from assets.views import (
    PropertyDetailView,
    PropertyListView,
    PropertyCreateView,
    PropertyEditView,
    PropertyDeleteView,
    StructureCreateView,
    StructureDetailView,
    LocksCreateView,
)

app_name = "assets"

urlpatterns = [
    path("property/new/", PropertyCreateView.as_view(), name="property_new"),
    path("property/<int:pk>", PropertyDetailView.as_view(), name="property_detail"),
    path("property/<int:pk>/edit/", PropertyEditView.as_view(), name="property_update"),
    path(
        "property/<int:pk>/delete/",
        PropertyDeleteView.as_view(),
        name="property_delete",
    ),
    path(
        "property/structure/new/", StructureCreateView.as_view(), name="structure_new"
    ),
    path(
        "property/structure/<int:pk>",
        StructureDetailView.as_view(),
        name="structure_detail",
    ),
    path("property/structure/locks/new/", LocksCreateView.as_view(), name="locks_new"),
    path("", PropertyListView.as_view(), name="property_list"),
]
