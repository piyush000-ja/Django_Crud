from django.contrib import admin

from .models import Courses
from .models import Signup

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id','coursename','courseFee','courseDuration')


class signupAdmin(admin.ModelAdmin):
    list_display = ('id','firstname','lastname','email')




admin.site.register(Signup,signupAdmin)

admin.site.register(Courses,CourseAdmin)

