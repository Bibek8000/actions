from django import forms 
from .models import Note
class NoteForm(forms.Form):
    title = forms.CharField(
        max_length=100,
        error_messages={'required':"title is required"}
    )
    description = forms.CharField(
        widget = forms.Textarea(),
        error_messages={'required':"Description is required"}
    )
    def clean_description(self):
        des = self.cleaned_data.get('description','')
        if len(des) < 10:
            raise forms.ValidationError(
            'Description must be at least 10 char long')
        return des

    def create(self,validated_data):
        return Note.objects.create(**validated_data)