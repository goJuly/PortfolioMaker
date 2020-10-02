import logging

from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from .forms import InquiryForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Portfolio


logger = logging.getLogger(__name__)


class IndexView(generic.TemplateView):
    template_name = "index.html"


class InquiryView(generic.FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm
    success_url = reverse_lazy('portfolio:inquiry')

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, 'メッセージを送信しました')
        logger.info('Inquiry send by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)


class PortfolioListView(LoginRequiredMixin, generic.ListView):
    model = Portfolio
    template_name = 'portfolio_list.html'

    def get_queryset(self):
        portfolios = Portfolio.objects.filter(user=self.request.user).order_by('-created_at')
        return portfolios
