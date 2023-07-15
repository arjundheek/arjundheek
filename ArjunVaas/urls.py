"""ArjunVaas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "ArjunVaas"

urlpatterns = [
    path("", views.index, name="index"),
    path("", include("Accounts.urls")),
    path("home", views.home, name="home"),
    path("products/<int:category>", views.products, name="products"),
    path("products/json/<int:category>", views.ProductJson, name="products"),
    path("product/<int:id>", views.product, name="product"),
    path("slider2", views.slider2, name="slider2"),
    path("user-info", views.user_info, name="user-info"),
    path("user-profile", views.user_profile, name="user-profile"),
    path("update-user-profile", views.update_user_profile, name="update-user-profile"),
    path("user-profile-edit", views.user_profile_edit, name="user-profile-edit"),
    path("category/<int:brand>", views.category, name="category"),
    path("brands", views.brands, name="brands"),
    path("admin/", admin.site.urls),
    path("renew-profile", views.renew_profile, name="renew-profile"),
    path("edit-profile", views.edit_profile, name="edit-profile"),
    path("delete-profile", views.delete_profile, name="delete-profile"),
    path("create-new-profile", views.create_new_profile, name="create-new-profile"),
    path("select-profile", views.select_profile, name="select-profile"),
    path("select-photo", views.select_photo, name="select-photo"),
    path("save-tryon", views.save_tryon, name="save-tryon"),
    path("tryons", views.tryons, name="tryons"),
    path("delete-tryon", views.delete_tryon, name="delete-tryon"),
    path("add-image", views.add_image, name="add-image"),
    path("oauth/", views.google_auth, name="google_auth"),
    path("oauth/callback/", views.google_auth_callback, name="google_auth_callback"),
    path("get_email/", views.get_email, name="get_email"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
