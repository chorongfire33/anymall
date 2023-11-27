from django.shortcuts import render, redirect, get_object_or_404
from .models import CustomUser, Product  # 이렇게 변경합니다.

def home(request):
    user = CustomUser.objects.get()  # User 대신 CustomUser를 사용합니다.
    return render(request, "index.html")

def login_email(request):
    return render(request, "login_email.html")

def sign_in(request):
    return render(request, "sign_in.html")

def sign_up(request):
    return render(request, "sign_up.html")

def shop(request):

    product = Product.objects.all()

    context = {
        'products':product
    }
    print(context)
    return render(request, "shop.html", context)


def product(request):
    return render(request, "product.html")

# def mypage(request):
#     # if request.session.get("user_email"):
#     #     user_email = request.session["user_email"]

#     #     try:
#     #         user = User.objects.get(user_email=user_email)
#     #         return render(request, "mypage.html", user)
#     #     except User.DoesNotExist:
#     #         return redirect("home")

#     user = get_object_or_404(CustomUser, user_no=8)  # User 대신 CustomUser를 사용합니다.


#     context = {
#         "user_name" : user.user_name
#     }

#     return render(request, "mypage.html", context)
def mypage(request):
    if request.session.get("user_email"):
        user_email = request.session["user_email"]

    #     try:
    #         user = User.objects.get(user_email=user_email)
    #         return render(request, "mypage.html", user)
    #     except User.DoesNotExist:
    #         return redirect("home")

    user = get_object_or_404(User, user_no=8)


    context = {
        "user_name" : user.user_name
    }

    return render(request, "mypage.html", context)


def admin_set(request):
    return render(request, "admin_set.html")

from .models import *

def admin_category(request):
    if request.method == "POST":
        category_name = request.POST.get("category_name")
        category = Category(category_name=category_name)
        category.save()
        return redirect("admin_category")
    else:
        categories = Category.objects.all()
        return render(request, "admin_category.html", {"categories": categories})

def delete_category(request, category_id):
    if request.method == "POST":
        category = Category.objects.get(pk=category_id)
        category.delete()
        return redirect("admin_category")
    else:
        return render(request, "admin_category.html")