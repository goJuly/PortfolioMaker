from django.urls import path

from . import views


app_name = 'portfolio'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('inquiry/', views.InquiryView.as_view(), name="inquiry"),
    path('portfolio_list/', views.PortfolioListView.as_view(), name="portfolio_list"),
    path('portfolio_create/', views.PortfolioCreateView.as_view(), name="portfolio_create"),
]
