from django import forms

class PostForm(forms.Form):
    identity = forms.CharField()
    # Style body text field as textarea
    text = forms.CharField(widget=forms.Textarea())
    # Make identity field autofocus
    identity.widget.attrs.update({'autofocus': 'autofocus'})

