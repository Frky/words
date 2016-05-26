
from random import random, randint

from django import forms

from website.models import Word

class WordForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = ['word']
        widgets = {
                        'word': forms.TextInput(attrs={'placeholder': "new word"}),
            }
        labels = {
                        'word': "",
                }

    def save(self):
        word = Word(
                word=self.cleaned_data.get('word'),
                top=randint(0, 100), 
                left=randint(0, 100),
                zindex=randint(1, 1000),
                size=randint(1, 50) / 15.
            )
        word.save()
        return word

