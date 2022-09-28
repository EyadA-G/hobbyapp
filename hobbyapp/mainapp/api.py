
import json
from django.http import JsonResponse
from django.http.response import HttpResponseBadRequest
from django.shortcuts import get_object_or_404, render
from mainapp.forms import UpdateForm
from mainapp.serializer import UserSerializer
from .models import Hobbies, Users
def user_api(request):
    queryset = Users.objects.all()
    serializer = UserSerializer(queryset, many=True, context={"request":request})
    return JsonResponse({
        'user':[ 
            serializer.data
            ]
    })
def hobby_api(request):
    return JsonResponse({
        'hobby':[
            hobby.to_dict()
            for hobby in Hobbies.objects.all()
        ]
    })
def add_hobby(request):
    if request.method == "POST":
        print('log')
        # we are doing loading from front ent  sending post request and information required to make class
        req = json.loads(request.body)
        DOC = Hobbies.objects.create(name=req["name"])

        return JsonResponse({
            "DOC": {
                'name': DOC.to_dict(),
                
            }
        })
    return HttpResponseBadRequest("Invalid method")

def edit_user(request):
    if request.method == "PUT":
        form = UpdateForm(instance=object, data=request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UpdateForm(instance=object)

    return render(request, 'login.html', {
        'object': object,
        'name': form,
    })