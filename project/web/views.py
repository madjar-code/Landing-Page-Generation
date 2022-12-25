from django.shortcuts import render
from web.models import Web


def get_landing_page(request, id):
    web = Web.objects.get(id=id)
    context = {
        'html_code': web.template.html_code,
    }
    print(web.template.html_code)

    return render(request, 'common.html', context)