# drf version
from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from api.user.serializers import RegisterSGCCSerializer
from api.user.models import JoinSGCC


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1


class RegisterSGCCView(ListCreateAPIView):
    serializer_class = RegisterSGCCSerializer
    pagination_class = StandardResultsSetPagination
    ordering = ['-id']

    def get_queryset(self):
        join_sgcc_queryset = JoinSGCC.objects.all()
        queryset = []
        for join_sgcc in join_sgcc_queryset:
            queryset.append(join_sgcc.__dict__)
            queryset[len(queryset)-1].update(join_sgcc.user.__dict__)
        return queryset


class RegisterSGCCListView(ListAPIView):
    serializer_class = RegisterSGCCSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsSetPagination
    ordering = ['-id']

    def get_queryset(self):
        join_sgcc_queryset = JoinSGCC.objects.all()
        queryset = []
        for join_sgcc in join_sgcc_queryset:
            queryset.append(join_sgcc.__dict__)
            queryset[len(queryset)-1].update(join_sgcc.user.__dict__)
        return queryset



