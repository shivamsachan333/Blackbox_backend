from django.contrib import admin
from django.urls import path, include
from django.views.static import serve as serve_static

from . import views

urlpatterns = [
    path('abcs',views.abcs,name='abcs'),
    path('courses/',views.CourseSerializers.as_view(),name='courses'),
    path('courses/<str:course_name>/', views.CourseDetailAPIView.as_view(), name='course-detail'),
     path('webinars/<str:webinar_name>/', views.WebinarDetailAPIView.as_view(), name='webinar-detail'),
    path('webinars/', views.WebinarListAPIView.as_view(), name='webinar-list'),
    path('home', views.Home.as_view(), name='Home'),
    path('socialMedias', views.socialMedias.as_view(), name='socialMedias'),
    path('whatweOffers',views.whatweOffers.as_view(),name='whatweOffers'),
    path('Testimonial', views.Testimonial.as_view(), name='Testimonial'),
    path('Strategie', views.Strategie.as_view(), name='Strategie'),
    
    path('Communities', views.Communities.as_view(), name='Communities'),
    path('webinar_registerations/', views.webinar_registerations, name='webinar_registerations'),
    path('course_registerations/', views.course_registerations, name='course_registerations'),
    path('ContactUs/', views.ContactUs, name='ContactUs'),
    
    path('whatweOffers/<str:Title>/', views.WhatweofferContentAPIView.as_view(), name='WhatweofferContentAPIView'),
    path('lead/', views.lead, name='lead'),
    path('Blogs/<str:Title>/', views.BlogsDetailAPIView.as_view(), name='blog-detail'),
    path('Blogs', views.Blogs.as_view(), name='Blogs'),
    path('^(?P<path>.*)$', serve_static),
]