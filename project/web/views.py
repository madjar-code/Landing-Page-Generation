from django.shortcuts import render
from web.models import Web
from offer.models import Offer


def get_landing_page(request, id):
    web = Web.objects.get(id=id)
    template = web.template
    offers = web.offers.all()

    # print(f'\n\n\n{template.web}\n\n\n')

    context = {
        'head': web.html_code,
        'offers': offers,
        'template_styles': template.template_styles
    }

    return render(request, template.get_file_name(), context)


def get_test_page(request):
    return render(request, 'philippines.html')