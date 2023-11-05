from django import forms

from myapp.models import Todo


class TodosForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ("name",)
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"})
        }
