from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import OwnedProperty


class PropertyTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.user = get_user_model().objects.create_user(
            email="test@email.com", password="secret"
        )
        cls.ownedproperty = OwnedProperty.objects.create(
            legal_name="123 5th Avenue", owner_id=cls.user.pk
        )

    def test_model_content(self):
        self.assertEqual(self.ownedproperty.legal_name, "123 5th Avenue")
