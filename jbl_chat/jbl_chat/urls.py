"""jbl_chat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path
from rest_framework import routers
from chat import views

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"rooms", views.ChatRoomViewSet, basename="room")
router.register(r"groups", views.GroupViewSet)
router.register(r"members", views.ChatRoomMemberViewSet)
router.register(r"messages", views.ChatRoomMessageViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path(
        "api/", include(router.urls)
    ),  # endpoint always points to the latest version of the API
    path("api/v0/", include(router.urls)),  # Able to use different versions of the API
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
