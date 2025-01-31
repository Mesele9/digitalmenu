from django.shortcuts import render
from .models import Category, MenuItem

import qrcode
from django.http import HttpResponse
from django.conf import settings
import os

def generate_qr_code(request):
    menu_url = request.build_absolute_uri('/')  # Full URL of the menu page
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(menu_url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    qr_code_path = os.path.join(settings.MEDIA_ROOT, 'menu_qr_code.png')
    img.save(qr_code_path)

    with open(qr_code_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type='image/png')
        response['Content-Disposition'] = 'inline; filename=menu_qr_code.png'
        return response

    
def qr_code_page(request):
    return render(request, 'menu/qr_code_page.html')


def menu_view(request):
    categories = Category.objects.all()
    menu_items = MenuItem.objects.all()
    context = {
        'categories': categories,
        'menu_items': menu_items,
    }
    return render(request, 'menu/menu.html', context)
