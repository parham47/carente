from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,Http404,HttpResponseNotAllowed
from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth.mixins import LoginRequiredMixin , PermissionRequiredMixin
from django.views.generic import View,ListView,DetailView,FormView,UpdateView
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from .models import cars
from .forms import SendcarsForm


class carsIndex(ListView):
    model = cars
    context_object_name = 'cars'
    template_name = 'cars/index.html'
    paginate_by = 4

    def get_queryset(self):
        return cars.objects.order_by('saltolid')

    def get_context_data(self , **kwargs):
        context = super().get_context_data(**kwargs)
        context['modelcar'] = 'cars Model'
        return context


class SinglecarsView(DetailView):
    model = cars
    template_name = 'cars/single.html'

    def get_context_data(self , **kwargs):
        context = super().get_context_data(**kwargs)
        context['modelcar'] = self.object.modelcar
        return context


class SendcarsView(LoginRequiredMixin , PermissionRequiredMixin , FormView):
    template_name = 'cars/send.html'
    form_class = SendcarsForm
    permission_required = ('cars.add_cars',)
    success_url = reverse_lazy('cars:cars')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)



class EditcarsView(LoginRequiredMixin, PermissionRequiredMixin ,UpdateView):
    model = cars
    template_name = 'cars/edit.html'
    form_class = SendcarsForm
    permission_required = ('cars.change_cars',)
    success_url = reverse_lazy('cars:cars')


    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


        
def home(request):
    return render(request, 'home.html')
def formjadid(request):
    return render(request, 'formjadid.html')
