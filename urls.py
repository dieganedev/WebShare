from django.conf.urls import url


urlpatterns = [
    ...
    url(r'^api-auth/', include('rest_framework.urls'))
]