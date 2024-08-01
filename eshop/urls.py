"""
URL configuration for eshop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf import settings  # 1
from django.conf.urls.static import static  # 2
from core.views import *
from costumerapp.views import costumer_view
from news.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', homepage),
    path('', Homepage.get),
    path('search/', search),
    path('users/', users_list),
    # path('user/<int:id>/', user_cabinet, name='user-cabinet'), 
    path('user/<int:pk>/', UserCabinet.as_view(), name='user-cabinet'), 
    path('registration/', registration, name='registration'), 
    path('signin/', signin, name='signin'), 
    path('signout/', signout, name='signout'), 
    # path('product/<int:id>/', product_detail, name='product-detail'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    # path('product-create/', product_create, name='product-create'),
    path('product-create/', ProductCreateView.as_view(), name='product-create'),
    path('costumers/', costumer_view),
    path('news/', news_list, name='news-list'),
    # /new-detail/8/
    path('new-detail/<int:id>/', new_detail, name='new-detail'),
    path('new-create/', new_create, name='new-create'),
    path('profile-create/', profile_create, name='profile-create'),
    path('profile-update/<int:id>/', profile_update, name='profile-update'),
]   + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  # 3


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
