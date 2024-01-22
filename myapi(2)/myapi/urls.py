from django.contrib import admin
from django.urls import include, re_path
from rest_framework import permissions
from django.contrib import admin
from django.urls import path,include

from django.conf.urls.static import static
from rest_framework_swagger.views import get_swagger_view
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.conf import settings

schema_view = get_schema_view(
    openapi.Info(
        title="Harshal API",
        default_version='v1',
        description="Welcome to the world of Jaseci",
        terms_of_service="https://www.jaseci.org",
        contact=openapi.Contact(email="jason@jaseci.org"),
        license=openapi.License(name="Awesome IP"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    re_path(r'^doc(?P<format>\.json|\.yaml+)$',schema_view.without_ui(cache_timeout=0), name='schema-json'),  #<-- Here
    re_path('doc/', schema_view.with_ui('swagger', cache_timeout=0),name='schema-swagger-ui'),  #<-- Here
    re_path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),name='schema-redoc'),  #<-- Here
    re_path('admin/', admin.site.urls),
    re_path('', include('myapiapp.urls')),
]