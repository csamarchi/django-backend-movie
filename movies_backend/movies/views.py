from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from django.views import View
from .models import Movie
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json

class Movies(View):
    @method_decorator(crf_exempt)
    def dispatch(self, request, *args, **kwargs):
        print(self, request, args, kwargs, ' this is stuff')
        return super(Movies, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        if(request.user.is_authenticated):

            user = User.objects.get(id=request.user.id)

            movie_list = list(user.movies.all().values())

            return JsonResponse({
                'Content-Type': 'application/json',
                'status': 200,
                'data': movie_list
            }, safe=False)
        else:
            return JsonResponse({
                'Content-Type': 'application/json',
                'status': 200,
                'message': 'Must be logged in to see the data'
                }, safe=False)

    def post(self, request):
        # reading the requests body, (think body-parser) but its not middleware
        data = request.body.decode('utf8')
        # parsing the json (think bodyParser.json()) in express, but its not middleware!
        data = json.loads(data)
        try:
            new_movie = Movie(title=data["title"], description=data["description"])
            new_movie.save()
            return JsonResponse({"created": data}, safe=False)
        except:
            return JsonResponse({"error": "not a valid data"}, safe=False)
