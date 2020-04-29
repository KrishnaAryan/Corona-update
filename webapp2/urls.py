"""login_form URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Arunachal_Pradesh/',views.Arunachal_Pradesh,name='Arunachal_Pradesh'),
    path('Bihar/',views.Bihar,name='Bihar'),
    path('Gujarat/',views.Gujarat,name='Gujarat'),
    path('Andhra/',views.Andhra,name='Andhra'),
    path('Chhattishgarh/',views.Chhattishgarh,name='Chhattishgarh'),
    path('Haryana/',views.Haryana,name='Haryana'),
    path('Assam/',views.Assam,name='Assam'),
    path('Goa/',views.Goa,name='GoaGoa'),
    path('Himachal_Pradesh/',views.Himachal_Pradesh,name='Himachal_Pradesh'),
    path('Jammu_and_Kashmir/',views.Jammu_and_Kashmir,name='Jammu_and_Kashmir'),
    path('Kerla/',views.Kerla,name='Kerla'),
    path('Meghalaya/',views.Meghalaya,name='Meghalaya'),
    path('Jharkhand/',views.Jharkhand,name='Jharkhand'),
    path('Madhya_Pradesh/',views.Madhya_Pradesh,name='Madhya_Pradesh'),
    path('Mizoram/',views.Mizoram,name='Mizoram'),
    path('Karnattaka/',views.Karnattaka,name='Karnattaka'),
    path('Manipur/',views.Manipur,name='Manipur'),
    path('Nagaland/',views.Nagaland,name='Nagaland'),
    path('Odisha/',views.Odisha,name='Odisha'),
    path('Sikkim/',views.Sikkim,name='Sikkim'),
    path('Tripura/',views.Tripura,name='Tripura'),
    path('Punjab/',views.Punjab,name='Punjab'),
    path('Tamil_Nadu/',views.Tamil_Nadu,name='Tamil_Nadu'),
    path('Uttar_Pradesh/',views.Uttar_Pradesh,name='Uttar_Pradesh'),
    path('Rajasthan/',views.Rajasthan,name='Rajasthan'),
    path('Telangana/',views.Telangana,name='Telangana'),
    path('Uttarakhand/',views.Uttarakhand,name='Uttarakhand'),
path('West_Bengal/',views.West_Bengal,name='West_Bengal'),
]
