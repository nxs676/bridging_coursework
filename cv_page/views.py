from django.shortcuts import render, get_object_or_404, redirect

from cv_page.forms import CVForm
from cv_page.models import CV


def cv_detail(request):
    cv = get_object_or_404(CV)
    return render(request, 'cv_page/cv.html', {'cv': cv})


def cv_edit(request, pk):
    cv = get_object_or_404(CV)
    if request.method == "POST":
        form = CVForm(request.POST, instance=cv)
        if form.is_valid():
            cv = form.save(commit=False)
            cv.save()
            return redirect('cv')
    else:
        form = CVForm(instance=cv)
    return render(request, 'cv_page/cv_edit.html', {'form': form})
