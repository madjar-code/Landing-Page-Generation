from django.shortcuts import render
from web.models import Web
from offer.models import Offer


def get_landing_page(request, id):
    web = Web.objects.get(id=id)
    template = web.template
    offers = web.offers.all()
    print(template.template_styles)

    context = {
        'head': web.html_code,
        'offers': offers,
        'template_styles': template.template_styles
    }

    return render(request, template.get_file_name(), context)