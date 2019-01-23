from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .forms import RestaurantCreateForm, RestaurantLocationCreateForm
from .models import RestaurantLocation
# Create your views here. It handles request. than go to urls. put
# this view into the url

@login_required(login_url = '/login/')
def restaurant_createview(request):
    form = RestaurantLocationCreateForm(request.POST or None)
    errors = None
    if form.is_valid():
        if request.user.is_authenticated():
            instance = form.save(commit = False)
            instance.owner = request.user    
            instance.save()
            return HttpResponseRedirect("/restaurants/")
        else:
            return HttpResponseRedirect("/login/")
    if form.errors:
        print(form.errors)
        errors = form.errors
    template_name = 'restaurants/form.html'
    context = {"form" : form, "errors":errors}
    return render(request, template_name, context)

    
def restaurant_listview(request):
    template_name = 'restaurants/restaurantslocation_list.html'
    queryset = RestaurantLocation.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, template_name, context) 


# class RestaurantListView(ListView):
#     queryset = RestaurantLocation.objects.all()
#     template_name = 'restaurants/restaurantslocation_list.html'


# class SearchRestaurantListView(ListView):
#     template_name = 'restaurants/restaurantslocation_list.html'

#     def get_queryset(self):
#             print(self.kwargs)
#             slug = self.kwargs.get("slug")
#             if slug:
#                 queryset = RestaurantLocation.objects.filter(category__iexact='veg')
#             else:
#                 queryset = RestaurantLocation.objects.none()
#             return queryset

class RestaurantListView(ListView):
    def get_queryset(self):
        slug = self.kwargs.get("slug")
        if slug:
            queryset = RestaurantLocation.objects.filter(
                Q(category__iexact=slug) |
                Q(category__iexact=slug)
            )
        else:
            queryset = RestaurantLocation.objects.all()
        return queryset


class RestaurantDetailView(DetailView):

    queryset = RestaurantLocation.objects.all()

    def get_context_data(self, *args, **kwargs):
        print(self.kwargs)
        context = super(RestaurantDetailView, self).get_context_data(*args,**kwargs)
        print(context)
        return context

    # def get_object(self, *args, **kwargs):
    #     rest_id = self.kwargs.get('rest_id')
    #     obj = get_object_or_404(RestaurantLocation,id = rest_id)
    #     return obj

# class RestaurantListview(ListView):
#     queryset = RestaurantLocation.objects.filter(category__iexact = 'veg/non-veg')


class RestaurantCreateView(LoginRequiredMixin, CreateView):
    form_class = RestaurantLocationCreateForm
    login_url = "/login/"
    template_name = 'form.html'
    success_url = "/restaurants/"

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user    
        # instance.save()
        return super(RestaurantCreateView, self).form_valid(form)


    def get_context_data(self, *args, **kwargs):
        context = super(RestaurantCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Add Restaurant'
        return context

    # def password_reset(request, is_admin_site=False):
    #     template_name='registration/password_reset_form.html',
    #     email_template_name='registration/password_reset_email.html',
    #     password_reset_form=PasswordResetForm, 
    #     token_generator=default_token_generator,
    #     post_reset_redirect=None)
