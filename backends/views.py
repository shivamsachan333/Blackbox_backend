from http.client import NOT_FOUND
import json
import os
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Blog, Communitie, Contact, Course, HomeHeading, Lead, SocialMedias, Testimonial,Strategie, Webinar, WebinarRegisteration, courseRegisteration,  whatweoffer
from rest_framework import generics
from .serializers import BlogsSerializer, CommunitySerializer, CourseSerializer, HomeHeadingSerializer, SocialMediasSerializer, StrategieSerializer,TestimonialSerializer, WebinarRegisterationSerializer, WebinarSerializer, whatweofferSerializer


from rest_framework.generics import RetrieveAPIView
from django.views.decorators.http import require_POST

from datetime import datetime
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_GET
from django.http import JsonResponse
from .models import Blog
from django.core.serializers import serialize
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string







current_date = datetime.now().strftime('%d%m%Y')



class Home(generics.ListAPIView):
    queryset = HomeHeading.objects.all()
    serializer_class = HomeHeadingSerializer


class socialMedias(generics.ListAPIView):
    queryset = SocialMedias.objects.all()
    serializer_class = SocialMediasSerializer


class Testimonial(generics.ListAPIView):
    queryset =  Testimonial.objects.all()
    serializer_class = TestimonialSerializer




class Strategie(generics.ListAPIView):
    queryset =  Strategie.objects.all()
    serializer_class = StrategieSerializer



class WebinarRegisterations(generics.ListAPIView):
    queryset = WebinarRegisteration.objects.all()
    serializer_class = WebinarRegisterationSerializer






@csrf_exempt  # Use this decorator if CSRF protection is enabled
@require_POST
def webinar_registerations(request):
    if request.method == 'POST':
        print('Received POST request')
        print('Request data:', request.POST)
        data = json.loads(request.body)

        print('Received POST request')
        print('Request data:', data)
        try:
            full_name = data['full_name']
            email_address = data['email_address']
            phone_number = data['phone_number']
            country =data['country']
            Webinar_name = data['Webinar_name']
            years_of_trading_experience = data['years_of_trading_experience']
            author_name = data['author_name']
            
            param = Webinar_name.replace(' ', '_').lower() + "_"+str(current_date)
            if not full_name:
                raise ValueError('Full name is required')
            registration = WebinarRegisteration.objects.create(
                full_name=full_name,
                email_address=email_address,
                phone_number=phone_number,
                country=country,
                Webinar_name=Webinar_name,
                years_of_trading_experience=years_of_trading_experience,
                Webinar_author=author_name,
                parmas = param
            )
            registration.save()
            try:
                subject = "Join Black-Box Club! An Exclusive Traders' Community"
                # Load the HTML content of the email
                html_content = render_to_string('email_template.html', {'full_name': full_name})

                # Create an EmailMultiAlternatives object
                msg = EmailMultiAlternatives(subject, '', settings.EMAIL_HOST_USER, [email_address])

                # Attach the HTML content
                msg.attach_alternative(html_content, "text/html")

                # Send the email
                msg.send()
                print(f"Email send to the user {full_name}")
            except :
                print("The given mail id is not correct")
                pass
            if Communitie.objects.filter(phone_number=phone_number).exists():
                return JsonResponse({'message': 'Form data saved successfully'})
            else:
                saving_community = Communitie.objects.create(
                    full_name=full_name,
                    email_address =email_address,
                    phone_number=phone_number,
                    country=country,
                    years_of_trading_experience=years_of_trading_experience,
                )
                saving_community.save()
                return JsonResponse({'message': 'Form data saved successfully'})
            
            
        except Exception as e:
            print('An error occurred:', str(e))
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'message': 'Method Not Allowed'}, status=405)

class Communities(generics.ListAPIView):
    queryset = Communitie.objects.all()
    serializer_class = CommunitySerializer
class Blogs(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogsSerializer

class whatweOffers(generics.ListAPIView):
    queryset = whatweoffer.objects.all()
    serializer_class=whatweofferSerializer




class CourseSerializers(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
class CourseDetailAPIView(generics.RetrieveAPIView):
    serializer_class = CourseSerializer
    lookup_field = 'course_name'  # Specify the lookup field

    def get_queryset(self):
        course_name = self.kwargs['course_name']
        return Course.objects.filter(course_name=course_name)







class BlogsDetailAPIView(generics.RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogsSerializer
    lookup_field = 'Title'

    




class WhatweofferContentAPIView(RetrieveAPIView):
    queryset = whatweoffer.objects.all()
    serializer_class = whatweofferSerializer
    lookup_field = 'Title'




    
# leads from ekta ma'am 
@csrf_exempt  # Use this decorator if CSRF protection is enabled
@require_POST
def lead(request):
    if request.method == 'POST':
        print('Received POST request')
        print('Request data:', request.POST)
        data = json.loads(request.body)

        print('Received POST request')
        print('Request data:', data)
        try:
            first_name = data['first_name']
            Last_name = data['last_name']
            email_address = data['email_address']
            phone_number = data['whatsapp_number']
            country =data['outside_india']
            years_of_trading_experience = data['years_of_trading_experience']
            param = (first_name + Last_name + "_"+str(current_date)).lower()

            if not first_name:
                raise ValueError('Full name is required')
            registration = Lead.objects.create(
                first_name=first_name,
                last_name = Last_name,
                email=email_address,
                whatsapp_number=phone_number,
                outside_india=country,
                years_of_trading_experience=years_of_trading_experience,
                parmas = param
            )
            registration.save()
            if Communitie.objects.filter(phone_number=phone_number).exists():
                return JsonResponse({'message': 'Form data saved successfully'})
            else:
                saving_community = Communitie.objects.create(
                    full_name=(first_name + Last_name),
                    email_address =email_address,
                    phone_number=phone_number,
                    country=country,
                    years_of_trading_experience=years_of_trading_experience,
                )
                saving_community.save()
                return JsonResponse({'message': 'Form data saved successfully'})
            
            
        except Exception as e:
            print('An error occurred:', str(e))
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'message': 'Method Not Allowed'}, status=405)








@csrf_exempt  # Use this decorator if CSRF protection is enabled
@require_POST
def ContactUs(request):
    if request.method == 'POST':
        print('Received POST request')
        print('Request data:', request.POST)
        data = json.loads(request.body)

        print('Received POST request')
        print('Request data:', data)
        try:
            name = data['name']
            email_address = data['email_address']
            phone_number = data['phone_number']
            country =data['country']
            message = data['message']
            years_of_trading_experience = data['years_of_trading_experience']
            param = (name + "_"+str(current_date)).lower()

            if not name:
                raise ValueError('Full name is required')
            Contactus = Contact.objects.create(
                name=name,
                email=email_address,
                phone_number=phone_number,
                country=country,
                message= message,
                years_of_trading_experience=years_of_trading_experience,
                parmas = param
            )
            Contactus.save()
            if Communitie.objects.filter(phone_number=phone_number).exists():
                return JsonResponse({'message': 'Form data saved successfully'})
            else:
                saving_community = Communitie.objects.create(
                    full_name=name,
                    email_address =email_address,
                    phone_number=phone_number,
                    country=country,
                    years_of_trading_experience=years_of_trading_experience,
                )
                saving_community.save()
                return JsonResponse({'message': 'Form data saved successfully'})
            
            
        except Exception as e:
            print('An error occurred:', str(e))
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'message': 'Method Not Allowed'}, status=405)




class WebinarListAPIView(generics.ListAPIView):
    queryset = Webinar.objects.all()
    serializer_class = WebinarSerializer


class WebinarDetailAPIView(generics.RetrieveAPIView):
    queryset = Webinar.objects.all()
    serializer_class = WebinarSerializer
    lookup_field = 'webinar_name'

    def get_object(self):
        queryset = self.get_queryset()
        queryset = self.filter_queryset(queryset)

        # Get the webinar_name from the URL path parameter
        webinar_name = self.kwargs['webinar_name']

        # Retrieve the webinar object by webinar_name
        obj = queryset.filter(webinar_name__iexact=webinar_name).first()

        # Check if the webinar object exists, raise NotFound if not found
        if not obj:
            raise NOT_FOUND(f"Webinar with name '{webinar_name}' not found.")

        return obj
    



@csrf_exempt  # Use this decorator if CSRF protection is enabled
@require_POST
def course_registerations(request):
    if request.method == 'POST':
        print('Received POST request')
        data = json.loads(request.body)
      

        print('Received POST request')
        print('Request data:', data)
        try:
            full_name = data['full_name']
            email_address = data['email_address']
            phone_number = data['phone_number']
            city =data['city']
            course_name = data['course_name']
            years_of_trading_experience = data['years_of_trading_experience']
            author_name = data['author_name']
            payment_link =data['payment_link']
            
            
            param = course_name.replace(' ', '_').lower() + "_"+str(current_date)
            if not full_name:
                raise ValueError('Full name is required')
            
            for i,j in data.items():
                print("    ")
                print(i, j)
            registration = courseRegisteration.objects.create(
                full_name=full_name,
                email_address=email_address,
                phone_number=phone_number,
                city=city,
                course_name=course_name,
                years_of_trading_experience=years_of_trading_experience,
                course_author=author_name,
                parmas = param
            )
            registration.save()
            try:
                subject = "Join Black-Box Club! An Exclusive Traders' Community"
                # Load the HTML content of the email
                html_content = render_to_string('course_regeisteration.html', {'full_name': full_name, 'payment_link':payment_link})

                # Create an EmailMultiAlternatives object
                msg = EmailMultiAlternatives(subject, '', settings.EMAIL_HOST_USER, [email_address])

                # Attach the HTML content
                msg.attach_alternative(html_content, "text/html")

                # Send the email
                msg.send()
                print(f"Email send to the user {full_name}")
            except :
                print("The given mail id is not correct")
                pass
            if Communitie.objects.filter(phone_number=phone_number).exists():
                return JsonResponse({'message': 'Form data saved successfully'})
            else:
                saving_community = Communitie.objects.create(
                    full_name=full_name,
                    email_address =email_address,
                    phone_number=phone_number,
                    country=city,
                    years_of_trading_experience=years_of_trading_experience,
                )
                saving_community.save()
                return JsonResponse({'message': 'Form data saved successfully'})
            
            
        except Exception as e:
            print('An error occurred:', str(e))
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'message': 'Method Not Allowed'}, status=405)

def abcs(request):
    return render(request, 'email_template.html', {'full_name': 'Pawan kumar'})