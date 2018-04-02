from django.contrib import messages
from django.shortcuts import (render, redirect)
from django.views import View
from django.shortcuts import get_object_or_404
from datetime import datetime

CRUD_CREATE = 0
CRUD_READ = 1
CRUD_UPDATE = 2
CRUD_DELETE = 3

CHOICES_CRUD = [
    (CRUD_CREATE, 'Create'),
    (CRUD_READ, 'Read'),
    (CRUD_UPDATE, 'Update'),
    (CRUD_DELETE, 'Delete')
]


class BaseView(View):  # CRUD
    """
    ------- usage ---------------
    CRUD_Base views for ypages project.
    template_name = ("form_base.html", "vehicle_list.html", "form_base.html", "confirm_rec_delete_base.html")
    success_url = ("vehicle_list.html", "", "vehicle_list.html", "vehicle_list.html")
    html_form = current_record = set when calling post/get method
    model = Vehile
    form_class = CreateVehicle_Form from forms.py
    context =
    key_field =
    title =
    grid_cols = ((3, 3, 4, 6, 12),(3, 3, 4, 6, 12),(3, 3, 4, 6, 12),(3, 3, 4, 6, 12))
    back2main_url = reverse('car:car_index')
    list_url = reverse('car:vehicle', kwargs={'pk': 0, 'crud': CRUD_READ})
    """
    template_name = model = form_class = grid_breakpoint_formcontrol = key_field = title = success_url = context_menu = None
    crud_context = {'create': CRUD_CREATE, 'read': CRUD_READ, 'update': CRUD_UPDATE, 'delete': CRUD_UPDATE}

    def get_queryset(self):
        return self.model.objects.all().filter(is_deleted=False).order_by(self.key_field)

    def get_kwargs(self, crud=CRUD_READ, pk=0):
        return {'crud': crud, 'pk': pk}

    def get_context(self, crud=CRUD_READ, pk=0, form=None):
        context = rows = html_form = None

        if crud == CRUD_READ:
            rows = self.get_queryset()
        else:

            if pk > 0:
                current_record = get_object_or_404(self.model, pk=pk)

            if crud == CRUD_DELETE:
                rows = current_record
            else:  # if create/update
                if form:
                    html_form = form
                else:
                    html_form = self.form_class()
                    if crud == CRUD_UPDATE:  html_form = self.form_class(instance=current_record)
                rows = html_form

        context = {'title': self.title, 'crud': CHOICES_CRUD[crud], 'rows': rows, 'grid_breakpoint_formcontrol' : self.grid_breakpoint_formcontrol, "context_menu" : self.context_menu}
        return {**context, **self.crud_context}

    def get(self, request, crud=1, pk=0):
        messages.success(request, 'Loading...')
        return render(request, self.template_name[crud], self.get_context(crud, pk))

    # default CRUD = 1 READ
    def post(self, request, crud=1, pk=0):
        context = current_record = html_form = None
        post_result = "Record {}d successfully...".format(CHOICES_CRUD[crud][1])
        if pk > 0: current_record = get_object_or_404(self.model, pk=pk)
        if crud == CRUD_DELETE:
            setattr(current_record, self.key_field, str(datetime.now()))
            current_record.is_deleted = True
            current_record.save()
        else:
            if crud == CRUD_CREATE:
                current_record = self.model.objects.all().filter(is_deleted=True).first()
                if current_record:
                    html_form = self.form_class(request.POST, instance=current_record)
                else:
                    html_form = self.form_class(request.POST)
            else:
                html_form = self.form_class(request.POST, instance=current_record)
            if html_form.is_valid():
                current_record = html_form.save(commit=False)
                current_record.is_deleted = False
                current_record.save()
                if 'ContinueSave' in request.POST:
                    messages.success(request, post_result)
                    return render(request, self.template_name[CRUD_CREATE], self.get_context(CRUD_CREATE,0))
            else:
                messages.success(request, 'Fill all required fields...')
                return render(request, self.template_name[crud], self.get_context(crud, pk, html_form))
        messages.success(request, post_result)
        return redirect(self.success_url, 1, 0)
