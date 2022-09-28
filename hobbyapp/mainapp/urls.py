
from django.contrib import admin
from django.urls import path
# from hobbiesapp.settings import STATIC_URL
from django.conf import settings
from django.conf.urls.static import static
from mainapp.views import loginPage,logoutUser, view_all, filter_hobbies
from mainapp.api import  add_hobby, edit_user, hobby_api, user_api
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', loginPage, name='login'),
    path('logout/',logoutUser, name='logout'),
    path('hobbies/',filter_hobbies, name='hobbies'),
    path ('main/users.html',view_all, name='users'),
    
    path ('api/hobies/', hobby_api, name="hobby_api"),
    path ('api/courses/', user_api, name="user_api"),
    path ('api/addhobby', add_hobby, name="add_hobby"),
    path ('api/edituser/', edit_user, name="edit api"),
    # path ('api/courses/', hobbies_api, name="hobbies api"),
    # path ('api/course/<int:course_id>/', hobby_del_api, name="hobby_del api"),

] + static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
