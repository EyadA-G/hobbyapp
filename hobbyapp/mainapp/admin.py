from django.contrib import admin

from mainapp.models import Users, Hobbies, Friend_Request
# Register your models here.
#Courses listed here
class UsersAdmin(admin.ModelAdmin):
    pass

admin.site.register(Users, UsersAdmin)
#Modules listed here
class HobbiesAdmin(admin.ModelAdmin):
    pass

admin.site.register(Hobbies, HobbiesAdmin)
#Users listed here
class FriendReqAdmin(admin.ModelAdmin):
    pass

admin.site.register(Friend_Request, FriendReqAdmin)
