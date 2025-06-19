
from .views import *
from rest_framework import routers
urlpatterns = [

]

router = routers.SimpleRouter()
router.register('products', ProductViewSet, basename='products')
router.register('category', CategoryViewSet, basename='category')
router.register('country', CountryProivodstvaViewSet, basename='country')
router.register('brand', BrandViewSet, basename='brand')
router.register('bill', BillViewSet, basename='bill')
router.register('pos_order', Pos_orderViewSet, basename='pos_order')

urlpatterns += router.urls