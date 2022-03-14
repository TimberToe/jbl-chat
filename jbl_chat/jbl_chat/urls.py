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
from cgitb import lookup
from django.contrib import admin
from django.urls import include, path
from rest_framework_nested import routers
from chat import views
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet, basename="user")
router.register(r"rooms", views.ChatRoomViewSet, basename="room")

chatroom_router = routers.NestedSimpleRouter(router, r"rooms", lookup="chatRoom")
chatroom_router.register(
    r"messages", views.ChatRoomMessageViewSet, basename="room-messages"
)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("api/", include(router.urls)),
    path("api/", include(chatroom_router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("admin/", admin.site.urls),
]
