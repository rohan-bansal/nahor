from django.shortcuts import get_object_or_404, redirect
from .models import URL


def root(request, url_hash):
    url = get_object_or_404(URL, url_hash=url_hash)
    url.clicked()

    return redirect(url.full_url)

