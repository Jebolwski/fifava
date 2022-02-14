from dataclasses import field
from tkinter.ttk import Widget
from django import forms
from .models import *


class FormForm(forms.ModelForm):

    class Meta:
        model = Form
        fields="__all__"


    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        for fields in self.fields:
            self.fields[fields].widget.attrs.update({'class':'form-control col-4','rows':'3'})
