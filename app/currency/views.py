from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views import generic

from currency.models import ContactUs, Rate, Source

from currency.forms import SourceForm, RateForm

from currency.model_choices import CurrencyType
# Create your views here.


class IndexView(generic.TemplateView):
    template_name = 'currency/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rate_count'] = Rate.objects.count()
        context['source_count'] = Source.objects.count()
        return context


class RateListView(LoginRequiredMixin, generic.ListView):
    queryset = Rate.objects.all()
    template_name = 'currency/rate_list.html'


class RateCreateView(LoginRequiredMixin, generic.CreateView):
    queryset = Rate.objects.all()
    template_name = 'currency/rate_create.html'
    form_class = RateForm
    success_url = reverse_lazy('currency:rate_list')
    initial = {'currency_type': CurrencyType.CURRENCY_TYPE_USD}


class RateUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    queryset = Rate.objects.all()
    template_name = 'currency/rate_update.html'
    form_class = RateForm
    success_url = reverse_lazy('currency:rate_list')

    def test_func(self):
        return self.request.user.is_superuser


class RateDetailsView(LoginRequiredMixin, generic.DetailView):
    queryset = Rate.objects.all()
    template_name = 'currency/rate_details.html'


class RateDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    queryset = Rate.objects.all()
    template_name = 'currency/rate_delete.html'
    success_url = reverse_lazy('currency:rate_list')

    def test_func(self):
        return self.request.user.is_superuser


class SourceListView(LoginRequiredMixin, generic.ListView):
    queryset = Source.objects.all()
    template_name = 'currency/source_list.html'


class SourceCreateView(LoginRequiredMixin, generic.CreateView):
    queryset = Rate.objects.all()
    template_name = 'currency/source_create.html'
    form_class = SourceForm
    success_url = reverse_lazy('currency:source_list')


class SourceDetailsView(LoginRequiredMixin, generic.DetailView):
    queryset = Source.objects.all()
    template_name = 'currency/source_details.html'


class SourceUpdateView(LoginRequiredMixin, generic.UpdateView):
    queryset = Source.objects.all()
    template_name = 'currency/source_update.html'
    form_class = SourceForm
    success_url = reverse_lazy('currency:source_list')


class SourceDeleteView(LoginRequiredMixin, generic.DeleteView):
    queryset = Source.objects.all()
    template_name = 'currency/source_delete.html'
    success_url = reverse_lazy('currency:source_list')


class ContactUsListView(LoginRequiredMixin, generic.ListView):
    queryset = ContactUs.objects.all()
    template_name = 'currency/contact_us.html'


class UserProfileView(LoginRequiredMixin, generic.UpdateView):
    queryset = get_user_model().objects.all()
    template_name = 'currency/my_profile.html'
    success_url = reverse_lazy('index')
    fields = (
        'first_name',
        'last_name',
    )

    def get_object(self, queryset=None):
        return self.request.user
