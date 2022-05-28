from django import forms
from .models import OwnedProperty, Locks, Structure


class PropertyForm(forms.ModelForm):
    model = OwnedProperty


class LocksForm(forms.ModelForm):
    model = Locks


class StructureForm(forms.ModelForm):
    model = Structure
