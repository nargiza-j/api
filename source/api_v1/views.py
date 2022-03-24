import json
from http import HTTPStatus

from django.http import HttpResponse, JsonResponse, HttpResponseNotAllowed
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import ensure_csrf_cookie


@ensure_csrf_cookie
def get_csrf_token(request):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed(["GET"])


def add_view(request, *args, **kwargs):
    if request.body:
        response_data = json.loads(request.body)
        try:
            num1 = int(response_data["A"])
            num2 = int(response_data["B"])
            answer = num1+num2
            response_data = {
                "answer": answer
            }
        except Exception as e:
            response_data = {
                "error": str(e)
            }
            return JsonResponse(response_data, status=HTTPStatus.BAD_REQUEST)
    return JsonResponse(response_data)


def substract_view(request, *args, **kwargs):
    if request.body:
        response_data = json.loads(request.body)
        try:
            num1 = int(response_data["A"])
            num2 = int(response_data["B"])
            answer = num1-num2
            response_data = {
                "answer": answer
            }
        except Exception as e:
            response_data = {
                "error": str(e)
            }
            return JsonResponse(response_data, status=HTTPStatus.BAD_REQUEST)
    return JsonResponse(response_data)


def multiply_view(request, *args, **kwargs):
    if request.body:
        response_data = json.loads(request.body)
        try:
            num1 = int(response_data["A"])
            num2 = int(response_data["B"])
            answer = num1*num2
            response_data = {
                "answer": answer
            }
        except Exception as e:
            response_data = {
                "error": str(e)
            }
            return JsonResponse(response_data, status=HTTPStatus.BAD_REQUEST)
    return JsonResponse(response_data)


def divide_view(request, *args, **kwargs):
    if request.body:
        response_data = json.loads(request.body)
        try:
            num1 = int(response_data["A"])
            num2 = int(response_data["B"])
            answer = num1/num2
            response_data = {
                "answer": answer
            }
        except Exception as e:
            response_data = {
                "error": str(e)
            }
            return JsonResponse(response_data, status=HTTPStatus.BAD_REQUEST)
    return JsonResponse(response_data)



