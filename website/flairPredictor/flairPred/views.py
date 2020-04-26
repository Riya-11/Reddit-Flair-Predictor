from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import urlForm
from . import utils
import praw
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import RedditPost
from .serializers import RedditPostSerializer
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

reddit = praw.Reddit(client_id='#', client_secret='#',
                     user_agent='#')


@api_view(['GET', 'POST'])
def post_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        posts = RedditPost.objects.all()
        serializer = RedditPostSerializer(posts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RedditPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            result = utils.predictutil(serializer.data['upload_file'])
            if not result:
                return Response({}, status=status.HTTP_201_CREATED)
            return Response(result, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def get_url(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = urlForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            post_url = form.cleaned_data['post_url']
            result = utils.predictFlair(post_url)
            submission = reddit.submission(url=post_url)
            title = str(submission.title)
            body = str(submission.selftext)
            flair = str(result[0])
            # return redirect('/result')
            return render(request, 'result.html', {'title': title, 'body': body, 'flair': flair})

    else:
        form = urlForm()
        # return HttpResponse('Please work for gods sake')
        return render(request, 'index.html', {'result': None, 'form': form})
