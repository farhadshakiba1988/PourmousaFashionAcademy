from django.shortcuts import render

from base.models import Course


def slide(request):
    ctx = {}
    ctx['course'] = Course.objects.all()
    return render(request, 'base/index.html', ctx)
