"""VegetableFactory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

import account
import statistics
import control
from django.conf.urls import url
from django.contrib import admin
from account import views
from statistics import views
from control import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('^$', account.views.indexPage),
    url(r'^account/', account.views.adminPage),
    url(r'^signin/', account.views.signInPage),
    url(r'^signup/', account.views.signUpPage),
    url(r'^control/', account.views.controlPage),
    url(r'^historyData/', account.views.historyDataPage),
    url(r'^controlAPIView/', account.views.controlAPIView.as_view()),
    url(r'^ControlStateAPIView/',control.views.ControlStateAPIView.as_view()),
    url(r'^LineChartAPIView/', statistics.views.LineChartAPIView.as_view()),
    url(r'^SittingHistoryAPIView/', statistics.views.SittingHistoryAPIView.as_view()),
    url(r'^DataHistoryAPIView/', statistics.views.DataHistoryAPIView.as_view()),

    # url(r'^ajaxAPIView/', views.ajaxAPIView.as_view()),
]
