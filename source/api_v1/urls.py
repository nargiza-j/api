from django.urls import path


from api_v1.views import add_view, get_csrf_token, substract_view, multiply_view, divide_view

urlpatterns = [
    path('get-csrf-token/', get_csrf_token),
    path('add/', add_view, name="add"),
    path('substract/', substract_view, name="substract"),
    path('multiply/', multiply_view, name="multiply"),
    path('divide/', divide_view, name="divide"),
]