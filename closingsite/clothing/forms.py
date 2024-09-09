from django.forms import ModelForm
from .models import ClothingModel


class ClothingForm(ModelForm):
    class Meta:
        model = ClothingModel
        fields = ('title', 'desc', 'price', 'rubric')