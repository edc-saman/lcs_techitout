from django.shortcuts import render, redirect

from .forms import CreateNewUser


def signup(request):
    if request.method == "POST":
        form = CreateNewUser(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CreateNewUser()
    return render(request, "LCS/signup.html", {'form': form})
