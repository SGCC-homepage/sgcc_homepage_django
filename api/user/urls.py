from django.urls import path

from api.user.views import RegisterSGCCView, RegisterSGCCListView

urlpatterns = [
    path('register/sgcc/', RegisterSGCCView.as_view()),
    path('register/sgcc/list/', RegisterSGCCListView.as_view()),
]