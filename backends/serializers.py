from rest_framework import serializers
from .models import FAQ, Blog, Communitie, Contact, Course, What_you_learn,  HomeHeading, Lead, List, ProgramDetail,SocialMedias, Testimonial,Strategie, ThisClassFor, Webinar, WebinarRegisteration, courseRegisteration,  whatweoffer

class HomeHeadingSerializer(serializers.ModelSerializer):
    class Meta :
        model = HomeHeading
        fields = '__all__'

class SocialMediasSerializer(serializers.ModelSerializer):
    class Meta :
        model = SocialMedias
        fields = '__all__'

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta :
        model = Testimonial
        fields = '__all__'



class StrategieSerializer(serializers.ModelSerializer):
    class Meta :
        model = Strategie
        fields = '__all__'



   
class WebinarRegisterationSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebinarRegisteration
        fields = '__all__'


class CommunitySerializer(serializers.ModelSerializer):
    class Mets:
        model = Communitie
        fields = '__all__'
        


class BlogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

class whatweofferSerializer(serializers.ModelSerializer):
    class Meta:
        model = whatweoffer
        fields = '__all__'
class ContactSerializer(serializers.ModelSerializer):
    class Meta :
        model = Contact
        fields = '__all__'

class leadsSerialier(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'



class ProgramDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramDetail
        fields = '__all__'

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'
class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields =  '__all__'

class CourseSerializer(serializers.ModelSerializer):
    program_details = ProgramDetailSerializer(many=True, read_only=True)
    faqs = FAQSerializer(many=True, read_only=True)
    lists = ListSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields =  '__all__'







class WhatYouLearnSerializer(serializers.ModelSerializer):
    class Meta:
        model = What_you_learn
        fields = '__all__'

class ThisClassForSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThisClassFor
        fields = '__all__'
class WebinarSerializer(serializers.ModelSerializer):
    what_you_learn = WhatYouLearnSerializer(many=True, read_only=True, source='What_you_learn')

    this_class_for = ThisClassForSerializer(many=True, read_only=True)
    class Meta:
        model = Webinar
        fields = '__all__'




class courseRegisterationSerializer(serializers.ModelSerializer):
    class Meta:
        model = courseRegisteration
        fields = '__all__'