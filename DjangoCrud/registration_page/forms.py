from django import forms
from registration_page.models import EmpModel


class EmpModelForm(forms.ModelForm):
    class Meta:
        model = EmpModel
        fields = "__all__"  # for getting all properties from EmpModel
        # fields=("ename","email")    # for getting specified properties from EmpModel
