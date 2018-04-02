from django.views import View
from django.shortcuts import render
# Create your views here.
# from ypages.baseview import BaseView
from teldir.models import (Category, Contact)

SEARCHBY_ALPHA = 1
SEARCHBY_NUMERIC = 2
SEARCHBY_CATEGORY = 3


class HomePageView(View):  # CRUD
    def get(self, request, search=0, startwith=0):
        category_id = 0
        if search == SEARCHBY_ALPHA:  # filter homepage by a,b,c
            context = chr(startwith + 64)
            rows = Contact.objects.filter(is_deleted=False, name__istartswith=context).order_by("name")
        elif search == SEARCHBY_NUMERIC:  # filter homepage by 1905
            rows = Contact.objects.filter(is_deleted=False, name__regex=r'\d').order_by("name")
        elif search == SEARCHBY_CATEGORY:  # filter homepage by category ie schools
            if startwith > 0:
                category_id = startwith
                rows = Contact.objects.filter(is_deleted=False, category_id=startwith).order_by("name")
            else:
                rows = Contact.objects.filter(is_deleted=False).order_by("name")
        else:  # default for homepage
            # test = "Contact.objects.filter(title__regex=r'\d')"
            rows = Contact.objects.filter(is_deleted=False).order_by("name")
        context = {'rows': rows, 'categories': Category.objects.filter(is_deleted=False).order_by("category"),
                   'category_selected_id': category_id}

        return render(request, "home.html", context)

# class HomePageView(BaseView):
#     template_name = ("", "home.html", "", "")
#     model = Contact
#     key_field = "name"
