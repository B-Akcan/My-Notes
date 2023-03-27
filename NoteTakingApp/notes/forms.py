from django import forms

class NewNote(forms.Form):
    title = forms.CharField(label="Title", max_length=100)
    content = forms.CharField(widget=forms.Textarea(attrs={"rows":13, "style":"resize:none;"}))
    marked = forms.BooleanField(required=False)