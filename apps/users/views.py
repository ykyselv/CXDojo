from django.db import IntegrityError
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .data_collector import data_collector
from .forms import DataCollectorForm
from .models import User


class MainPageView(generic.TemplateView):
    template_name = "main_page.html"


class Collect_data(generic.View):
    model = User
    template_name = "collect_data.html"
    success_url = reverse_lazy("main_page")
    initial = {"key": "value"}
    form_class = DataCollectorForm

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form_class(request.POST, initial=self.initial)

        if form.is_valid():
            path_to_csv = form.cleaned_data.get("csv_file_path")
            path_to_xml = form.cleaned_data.get("xml_file_path")
            try:
                data_collector(path_to_csv, path_to_xml)
            except FileNotFoundError:
                return render(request, "file_not_found.html")
            except IntegrityError:
                return render(request, "duplicates_error.html")
        return render(request, self.template_name, {"form": form})


class UserListView(generic.ListView):
    model = User
    template_name = 'userlist.html'

# Create your views here.
