from django import forms

from teldir.models import (Category, Contact)


class CreateCategory_Form(forms.ModelForm):
    category = forms.CharField(required=True, max_length=15, help_text='eg schools, hospital', label="Category",
                               widget=forms.TextInput(
                                attrs={'class': 'form-control', 'placeholder': 'enter category name'}))

    class Meta:
        model = Category
        fields = ['category']


class CreateContact_Form(forms.ModelForm):
    name = forms.CharField(required=True, max_length=50, help_text="Enter full name of person or office [50 chars]",
                           label="Full Name", widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(required=False, max_length=50, help_text="Enter full contact address [50 chars]",
                              label="Address", widget=forms.TextInput(attrs={'class': 'form-control'}))
    category_id = forms.ModelChoiceField(required=False, help_text="Select appropriate category from dropdown",
                                      queryset=Category.objects.filter(is_deleted=False).order_by("category"),
                                      label='Category', empty_label='Select appropriate category',
                                      widget=forms.Select(attrs={'class': 'form-control'}))
    landline_no = forms.CharField(required=False, max_length=30, label="Landline No",
                                  help_text="Enter full landline with area code [30 chars]",
                                  widget=forms.TextInput(attrs={'class': 'form-control'}))
    mobile_no = forms.CharField(required=False, max_length=30, label="Mobile No",
                                help_text="Enter mobile numbers [30 chars]",
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=False, max_length=50, label="Email", help_text="Enter email address",
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Contact
        fields = ['name', 'address', 'category_id', 'landline_no', 'mobile_no', 'email']
