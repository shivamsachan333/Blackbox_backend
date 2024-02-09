from django.contrib import admin
from django.http import HttpResponse
import csv

from django.contrib.admin import AdminSite
from django.utils import timezone
# Register your models here.
from django.contrib import admin
from .forms import ProgramDetailForm

from .models import FAQ, Blog, Communitie, Contact, Course,  What_you_learn,  HomeHeading, Lead, List, ProgramDetail, SocialMedias, Strategie, Testimonial, ThisClassFor, Webinar, WebinarRegisteration, courseRegisteration, whatweoffer
admin.site.register(HomeHeading)
admin.site.register(SocialMedias)
admin.site.register(Testimonial)
admin.site.register(Strategie)

class WebinarRegisterationAdmin(admin.ModelAdmin):

    search_fields = ('full_name', 'email_address', 'Webinar_name', 'date_of_registeration','parmas')

    actions = ['export_to_csv']

    def export_to_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="webinar_registerations_{timezone.now().strftime("%Y%m%d%H%M%S")}.csv"'

        writer = csv.writer(response)
        writer.writerow(['Full Name', 'Email Address', 'Phone Number', 'Webinar Name', 'Date of Registration'])

        for obj in queryset:
            writer.writerow([obj.full_name, obj.email_address, obj.phone_number, obj.Webinar_name, obj.date_of_registeration])

        return response

    export_to_csv.short_description = "Export selected records to CSV"

admin.site.register(WebinarRegisteration, WebinarRegisterationAdmin)

class CommunitieAdmin(admin.ModelAdmin):
    actions = ['export_as_csv']
    search_fields = ['full_name', 'email_address', 'phone_number', 'country']

    def export_as_csv(modeladmin, request, queryset):
        meta = modeladmin.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename={meta}.csv'

        writer = csv.writer(response)
        writer.writerow(field_names)

        for obj in queryset:
            writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export selected objects as CSV file"

admin.site.register(Communitie, CommunitieAdmin)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    class Media:
        js = ('tineyinject.js',)




@admin.register(whatweoffer)
class whatweofferAdmin(admin.ModelAdmin):
    class Media:
        js = ('tineyinject1.js',)





class LeadsAdmin(admin.ModelAdmin):
    search_fields = ['first_name', 'last_name', 'outside_india', 'whatsapp_number', 'email', 'years_of_trading_experience', 'date_of_joined', 'parmas']
    
    actions = ["export_as_csv"]

    def export_as_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="leads_export.csv"'

        writer = csv.writer(response)
        writer.writerow(['First Name', 'Last Name', 'Outside India', 'WhatsApp Number', 'Email', 'Years of Trading Experience', 'Date of Joined', 'Parmas'])

        for obj in queryset:
            writer.writerow([obj.first_name, obj.last_name, obj.outside_india, obj.whatsapp_number, obj.email, obj.years_of_trading_experience, obj.date_of_joined, obj.parmas])

        return response

    export_as_csv.short_description = "Export selected leads to CSV"

admin.site.register(Lead, LeadsAdmin)


class ContactAdmin(admin.ModelAdmin):
    search_fields = ['name', 'country', 'email', 'phone_number', 'years_of_trading_experience', 'parmas']

admin.site.register(Contact, ContactAdmin)

# Create a custom admin site



class ProgramDetailInline(admin.StackedInline):
    model = ProgramDetail
    form = ProgramDetailForm
    extra = 1


class FAQInline(admin.StackedInline):
    model = FAQ
    extra = 1

class ListInline(admin.StackedInline):
    model = List
    extra = 1

class CourseAdmin(admin.ModelAdmin):
    inlines = [ListInline,ProgramDetailInline, FAQInline ]

admin.site.register(Course, CourseAdmin)



class What_you_learnInline(admin.StackedInline):
    model = What_you_learn
    extra = 1

class ThisClassForInline(admin.StackedInline):
    model = ThisClassFor
    extra = 1

class WebinarAdmin(admin.ModelAdmin):
    inlines = [What_you_learnInline, ThisClassForInline]

admin.site.register(Webinar, WebinarAdmin)




class CourseRegistrationAdmin(admin.ModelAdmin):
    search_fields = ['course_name', 'course_time', 'course_author', 'full_name', 'email_address', 'phone_number', 'city', 'years_of_trading_experience', 'date_of_registeration', 'parmas']
    
    def export_to_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="course_registrations.csv"'
        
        writer = csv.writer(response)
        writer.writerow(['Course Name', 'Course Time', 'Course Author', 'Full Name', 'Email Address', 'Phone Number', 'City', 'Years of Trading Experience', 'Date of Registration', 'Params'])
        
        for obj in queryset:
            writer.writerow([obj.course_name, obj.course_time, obj.course_author, obj.full_name, obj.email_address, obj.phone_number, obj.city, obj.years_of_trading_experience, obj.date_of_registeration, obj.parmas])
        
        return response
    
    export_to_csv.short_description = "Export to CSV"
    
    actions = ['export_to_csv']

admin.site.register(courseRegisteration, CourseRegistrationAdmin)