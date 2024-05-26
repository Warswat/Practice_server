from rest_framework.pagination import LimitOffsetPagination
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter

from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'description']
    pagination_class = LimitOffsetPagination
    # при необходимости добавьте параметры фильтрации


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    # при необходимости добавьте параметры фильтрации
    filter_backends = [SearchFilter]
    search_fields = ['=positions__product__id']
    pagination_class = LimitOffsetPagination

@api_view(['GET'])
def sample_view(request):
    return Response({'message': 'Всё работает!!! УРАА!!!!'})
