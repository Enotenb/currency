from django.urls import reverse_lazy
from django.views import generic
from django.core.mail import send_mail
from django.conf import settings

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


class RateListView(generic.ListView):
    queryset = Rate.objects.all()
    template_name = 'currency/rate_list.html'


class RateCreateView(generic.CreateView):
    queryset = Rate.objects.all()
    template_name = 'currency/rate_create.html'
    form_class = RateForm
    success_url = reverse_lazy('currency:rate_list')
    initial = {'currency_type': CurrencyType.CURRENCY_TYPE_USD}


class RateUpdateView(generic.UpdateView):
    queryset = Rate.objects.all()
    template_name = 'currency/rate_update.html'
    form_class = RateForm
    success_url = reverse_lazy('currency:rate_list')


class RateDetailsView(generic.DetailView):
    queryset = Rate.objects.all()
    template_name = 'currency/rate_details.html'


class RateDeleteView(generic.DeleteView):
    queryset = Rate.objects.all()
    template_name = 'currency/rate_delete.html'
    success_url = reverse_lazy('currency:rate_list')


class SourceListView(generic.ListView):
    queryset = Source.objects.all()
    template_name = 'currency/source_list.html'


class SourceCreateView(generic.CreateView):
    queryset = Rate.objects.all()
    template_name = 'currency/source_create.html'
    form_class = SourceForm
    success_url = reverse_lazy('currency:source_list')


class SourceDetailsView(generic.DetailView):
    queryset = Source.objects.all()
    template_name = 'currency/source_details.html'


class SourceUpdateView(generic.UpdateView):
    queryset = Source.objects.all()
    template_name = 'currency/source_update.html'
    form_class = SourceForm
    success_url = reverse_lazy('currency:source_list')


class SourceDeleteView(generic.DeleteView):
    queryset = Source.objects.all()
    template_name = 'currency/source_delete.html'
    success_url = reverse_lazy('currency:source_list')


class ContactUsListView(generic.ListView):
    queryset = ContactUs.objects.all()
    template_name = 'currency/contact_us.html'


class ContactUsCreateView(generic.CreateView):
    model = ContactUs
    success_url = reverse_lazy('currency:rate_list')
    template_name = 'currency/contactus_create.html'
    fields = (
        'email_from',
        'subject',
        'message',
    )

    def form_valid(self, form):
        response = super().form_valid(form)

        subject = 'ContactUs From Currency Project'
        message = f'''
        Subject From Client: {self.object.subject}
        Email: {self.object.email_from}
        Wants to contact
        '''

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )

        return response
