from django import forms

class OrderForm(forms.Form):
    name = forms.CharField(max_length=100)
    milk = forms.ChoiceField(choices=[('Full Cream', "Full Cream"), ('Soy', 'Soy'), ('No Milk', "No Milk")], widget=forms.RadioSelect)
    temperature = forms.ChoiceField(choices=(('Regular', 'Regular'), ('Warm', 'Warm'), ('Extra Hot', 'Extra Hot')), widget=forms.RadioSelect)