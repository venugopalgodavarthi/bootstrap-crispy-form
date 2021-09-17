from django import forms
from myapp.models import registermodel
from django.utils.translation import gettext_lazy
class registerform(forms.ModelForm):
    class Meta():
        model = registermodel
        #fields = ['username','password','email','phone']
        fields= '__all__'
        #fields = ['username','password']
        #exclude = ['password']
        widgets ={'username':forms.TextInput,'password':forms.PasswordInput,'email':forms.TextInput}
        help_texts={'username':gettext_lazy('plz enter the username'),'password':gettext_lazy('plz enter the password')}
        labels={'username':gettext_lazy('USERNAME'),'password':gettext_lazy('PASSWORD')}
        
    def clean_username(self):
            res= self.cleaned_data['username']
            print(res)
            if len(res)>5:
                raise forms.ValidationError("plz enter the below 5 characters")
                print(res)
            return res
        