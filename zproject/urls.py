from django.contrib import admin
from django.urls import path, include


from rest_framework import routers
from api_payments.views import Rest_Payments, Rest_Payments_expired
from api_servicios.views import Rest_Services
from api_users.views import UserCreateView, UserListView

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



from django.urls import re_path
from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="API Payments",
        default_version='v1',
        description="Proyecto TODO API de Silabuz",
        terms_of_service="https://github.com/MDCIrony",
        contact=openapi.Contact(email="miguel.acastillodiaz@outlook.es"),
        license=openapi.License(name="BSD License"),
),
    public=True,
    permission_classes=[permissions.AllowAny],
)


router = routers.DefaultRouter()
router.register(r'services', Rest_Services, 'Services')
router.register(r'payments', Rest_Payments, 'Payments')
router.register(r'payments-expired', Rest_Payments_expired, 'Payments-expired')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api_users.urls')),
    path('users/all/', UserListView.as_view(), name='user-list'),
    path('users/', UserCreateView.as_view(), name='user-create'),
    
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path("token/", TokenObtainPairView.as_view(), name="get_token"),
    path("token/refresh/", TokenRefreshView.as_view(),  name="refresh_token"),

]

urlpatterns += router.urls
