import uuid
from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from core.models import CreationModificationDateBase


class OwnedProperty(CreationModificationDateBase):
    """Describe the property owned"""

    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    legal_name = models.CharField(_("Name"), max_length=128, blank=True, null=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return self.legal_name

    def get_absolute_url(self):
        return reverse("property_detail", kwargs={"pk": self.pk})


class Structure(CreationModificationDateBase):
    """Model to define improvement to property"""

    name = models.CharField(max_length=256, blank=True, null=True)
    description = models.TextField()
    structure_type = models.CharField(max_length=125, blank=True, null=True)
    owned_property = models.ForeignKey(
        OwnedProperty, on_delete=models.CASCADE, related_name="structures"
    )

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("assets:structure_detail", kwargs={"pk": self.pk})


class Locks(CreationModificationDateBase):
    """Lock and key information"""

    description = models.CharField(max_length=125, blank=True, null=True)
    floor = models.CharField(max_length=50, blank=True, null=True)
    room = models.CharField(max_length=125, blank=True, null=True)
    lock_type = models.CharField(max_length=256, blank=True, null=True)
    manufacturer = models.CharField(max_length=125, blank=True, null=True)
    key_marking = models.CharField(max_length=50)
    key_image = models.ImageField(upload_to=f"properties/keys/", blank=True, null=True)
    structure = models.ForeignKey(
        Structure, on_delete=models.CASCADE, related_name="locks"
    )

    def __str__(self) -> str:
        return self.room

    def get_absolute_url(self):
        return reverse("locks_detail", kwargs={"pk": self.pk})


class AddressModel(CreationModificationDateBase):
    "Address of OwnedProperty"

    name = models.CharField(_("Full name"), max_length=1024)
    address1 = models.CharField(_("Address line 1"), max_length=1024)
    address2 = models.CharField(
        _("Address line 2"), max_length=1024, blank=True, null=True
    )
    zip_code = models.CharField(_("ZIP"), max_length=12)
    city = models.CharField(_("City"), max_length=1024)
    owned_property = models.ForeignKey(OwnedProperty, on_delete=models.CASCADE)

    def __str__(self):
        return self.address1
