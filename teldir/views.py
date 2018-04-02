from django.shortcuts import render

# Create your views here.

from ypages.baseview import BaseView
from teldir.models import (Category, Contact)
from teldir.forms import (CreateCategory_Form, CreateContact_Form)

#// template_name = model = form_class = key_field = title = success_url =  None
class CategoryView(BaseView):  # CRUD Action
    template_name = ("base_form.html", "list_category.html", "base_form.html", "base_confirm_delete_rec.html")
    model = Category
    form_class = CreateCategory_Form
    key_field = "category"
    title = "Category"
    success_url = 'teldir:category_index'
    grid_breakpoint_formcontrol = "col-xl-3 col-lg-4 col-md-6 col-sm-6 col-xs-6"
    context_menu = "mnuCategory"

class ContactView(BaseView):  # CRUD Action
    template_name = ("base_form.html", "list_contact.html", "base_form.html", "base_confirm_delete_rec.html")
    model = Contact
    form_class = CreateContact_Form
    key_field = "name"
    title = "Contact"
    success_url = 'teldir:contact_index'
    grid_breakpoint_formcontrol = "col-xl-3 col-lg-3 col-md-4 col-sm-6 col-xs-6"
    context_menu = "mnuContact"