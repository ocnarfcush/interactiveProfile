from django.shortcuts import HttpResponse, render


def home1(request):
    message = f"Hello {request.user.username}"
    return render(request, "home.html", {})