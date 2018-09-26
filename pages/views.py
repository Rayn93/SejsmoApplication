from django.shortcuts import render, redirect

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect


from stations.models import Station
from localQuakes.models import LocalQuake

from globalQuakes.models import GlobalQuake

# Create your views here.
from django.views.generic import ListView

from .forms import ContactForm




class HomeView(ListView):
    template_name = "pages/home.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     last_quakes = LocalQuake.objects.all().order_by('-id')[:5]
    #     last_earthquakes = GlobalQuake.objects.all().order_by('-id')[:5]
    #     context['group'] = zip(last_quakes, last_earthquakes)
    #     return context

    queryset = LocalQuake.objects.all().order_by('-id')[:20]
    context_object_name = 'last_quakes'

    # queryset2 = GlobalQuake.objects.all().order_by('-id')[:5]
    # context_object_name2 = 'last_earthquakes'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['last_earthquakes'] = GlobalQuake.objects.all().order_by('-id')[:10]
        return context


class AboutView(ListView):
    template_name = "pages/about.html"
    model = Station


def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "pages/contact.html", {'form': form})


def successView(request):
    return HttpResponse('Success! Thank you for your message.')
