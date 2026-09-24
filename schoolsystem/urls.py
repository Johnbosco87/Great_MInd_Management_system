from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("admin/", admin.site.urls),

    # JWT login
    path(
        "api/login/",
        TokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),

    # Refresh expired access token
    path(
        "api/token/refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh",
    ),

    # Your existing Great Mind API
    path("api/", include("system.urls")),
]