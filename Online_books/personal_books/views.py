from django.shortcuts import render, redirect

# Create your views here.
from django.conf import settings
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from .models import Books, UserProfile
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, View
from django.urls import reverse
from django.http import HttpResponse

global flag


def home(request):
    global flag
    flag = False
    obj = None
    print("request.home", request.POST)
    if request.method == "POST":
        if "read" in request.POST:
            obj = Books.objects.get(Title=request.POST["read"])
            flag = True
            nochange = True

            return render(request, "display_form.html", {"obj": obj, "flag": flag, "nochange": nochange})
        elif "update" in request.POST:
            flag = True
            obj = Books.objects.get(Title=request.POST["update"])
            return render(request, "display_form.html", {"obj": obj, "flag": flag}, )
        elif "delete" in request.POST:
            delete1(request.POST["delete"])
        elif "title" in request.POST:
            return add(request)

    obj = Books.objects.filter(user1=UserProfile.objects.get(user=request.user))

    return render(request, "index.html", {"obj": obj, "user": request.user})


def add(request):
    if request.method == "POST":
        flag1 = False
        rating = 1
        if "fav" in request.POST and request.POST["fav"] == 'on': flag1 = True
        if "rating" in request.POST and request.POST["rating"] != "":
            if 1 <= int(request.POST["rating"]) >= 5: rating = int(request.POST["rating"])
        if len(Books.objects.filter(Title=request.POST["title"])) == 0:

            try:
                b = Books.objects.create(user1=UserProfile.objects.get(user=request.user), Title=request.POST["title"],
                                         Author=request.POST["author"], Genre=request.POST["genre"]
                                         , Type=request.POST["type"], Rating=rating, Review=request.POST["review"],
                                         Favorite=flag1)

                b.save()
            except:
                print("finished")
        else:
            print("here")
            Books.objects.filter(Title=request.POST["title"]).update(Author=request.POST["author"],
                                                                     Genre=request.POST["genre"]
                                                                     , Type=request.POST["type"], Rating=rating,
                                                                     Review=request.POST["review"],
                                                                     Favorite=flag1)
        obj = Books.objects.filter(user1=UserProfile.objects.get(user=request.user))
        print("before redirect",obj)
        return redirect("/")

    return render(request, "display_form.html")



def delete1(title_name):
    Books.objects.filter(Title=title_name).delete()
    return
