from django.shortcuts import render

from images.models import Image


def home(request):
    images = Image.objects.filter(tags__name__in=["homepage"])[:9]

    return render(request, 'home.html', {'images': images})


def sleeves(request):
    images = Image.objects.filter(tags__name__in=["sleeve"])[:3]

    return render(request, 'sleeves.html', {'images': images})


def story(request):
    images = Image.objects.filter(tags__name__in=["story"])[:3]

    return render(request, 'story.html', {'images': images})