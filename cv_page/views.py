from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from cv_page.forms import CVForm
from cv_page.models import CV


def cv_url(request):
    return render(request, 'cv_page/cv.html')


def cv_detail(request):
    cv = get_object_or_404(CV)
    return render(request, 'cv_page/cv.html', {'cv': cv})


def cv_edit(request):
    cv = get_object_or_404(CV, pk=1)
    if request.method == "POST":
        form = CVForm(request.POST, instance=cv)
        if form.is_valid():
            cv = form.save(commit=False)
            cv.name = request.user
            cv.save()
            return redirect('cv_detail', pk=cv.pk)
    else:
        form = CVForm(instance=cv)
    return render(request, 'cv_page/cv_edit.html', {'form': form})


def cv_remove(request):
    cv = get_object_or_404(CV, pk=1)
    cv.delete()
    return redirect('cv_detail')
