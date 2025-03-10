from django.http import HttpResponse
from django.shortcuts import render

from burgers.models import Burger


def main(request):
    # return HttpResponse("안녕하세요. 장고 웹 프레임워크~~ Hello World")
    return render(request, "main.html")

def lunch_list(request):
    # return HttpResponse("lunch_list : 점심 메뉴입니다.")
    return render(request, "lunch_list.html")

def intro(request):
    return HttpResponse("반갑습니다. 이상용입니다.")

def burger_list(request):
    burgers = Burger.objects.all()
    print("햄버거 전체 목록: ", burgers)
    # 화면에 데이터 탑재하기.
    context = {
        "burgers": burgers
    }
    # 화면에 데이터 전달하기.
    return render(request, "burger_list.html", context)

def burger_search(request):
    print(request.GET)
    return render(request, "burger_search.html")



