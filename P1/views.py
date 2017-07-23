from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest
from django.views.decorators.csrf import csrf_protect

from P1.models import Post, Comment, Post_Word
from django.contrib.auth.models import Permission, User
from django.contrib.auth import authenticate, login
from django.template import loader
import datetime


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


def index(request):
    return HttpResponse('HHi')


def detail(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

    # def detail(request, question_id):
    #     try:
    #     except Question.DoesNotExist:
    #         raise Http404("Question does not exist")
    #     return render(request, 'polls/detail.html', {'question': question})


def auth_register(request):
    # post
    if request.method == 'POST':
        try:
            student_number = request.POST['student_number']
            password = request.POST['password']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            user = User.objects.create_user(student_number, password=password)
            user.last_name = last_name
            user.first_name = first_name
            user.email = email
            user.save()
        except:
            raise Http404("problem1!")
        return HttpResponse('successful sign up')


def auth_login(request):
    # post
    if request.method == 'POST':
        try:
            student_number = request.POST.get('student_number')
            password = request.POST['password']
            user = authenticate(request, username=student_number, password=password)
            if user is not None:
                login(request, user)
                return HttpResponse('successful login')
            else:
                return HttpResponse('unsuccessful login')
                # No backend authenticated the credentials
        except:
            raise Http404("problem in sending data")
    pass


def blog_posts(request):
    # get
    if not request.user.is_authenticated:
        return HttpResponse('not auth')
        # return render(request, 'polls/test.html', 'login plz')
    if request.method == 'GET':
        count = '1'
        offset = '0'
        try:
            if 'count' in request.GET:
                count = request.GET['count']
            if 'offset' in request.GET:
                offset = request.GET['offset']
            d = Post.objects.filter(std_id=request.user.id).all()  # [int(offset), int(offset) + int(count)]
            return HttpResponse(d[int(offset):int(offset) + int(count)])
        except:
            raise Http404('Problem!')

    pass


def blog_post(request):
    # get
    global text, title, summary
    text = "f_text"
    title = "f_title"
    summary = "f_summary"
    if request.method == 'GET':
        try:
            if 'id' in request.GET:
                post_id = request.GET['id']
                p = Post.objects.get(id=post_id)
                if p is None:
                    return render(request, 'polls/index.html')
                return HttpResponse(p.text)
                # return render(request, 'polls/test.html', p)
        except:
            raise Http404('problem')
    elif request.method == 'POST' and request.user.is_authenticated:
        try:
            if 'title' in request.POST:
                title = request.POST['title']
            if 'summary' in request.POST:
                summary = request.POST['summary']
            if 'text' in request.POST:
                text = request.POST['text']
            std_id = request.user
            post = Post(title=str(title), summary=str(summary), text=str(text), std_id=std_id)
            post.save()
        except:
            raise Http404('problemIC')
    return HttpResponse('success')


def blog_comments(request):
    if request.method == 'GET':
        count = '1'
        offset = '0'
        try:
            if 'post_id' in request.GET:
                post_id = request.GET['post_id']
                if 'count' in request.GET:
                    count = request.GET['count']
                if 'offset' in request.GET:
                    offset = request.GET['offset']
                c = Comment.objects.filter(post_id=post_id).all()
                return HttpResponse(c[int(offset): int(offset) + int(count)])
            else:
                return HttpResponse('post not found')
        except:
            raise Http404('Problem!')
    # get
    # post_id
    # count (اختیاری)
    # offset (اختیاری)

    pass


def blog_comment(request):
    # post
    if request.method == 'POST':
        try:
            if 'post_id' in request.POST and 'text' in request.POST:
                post_id = request.POST['post_id']
                text = request.POST['text']
                post = Post.objects.get(id=post_id)
                user = User.objects.get(id=request.user.id)
                com = Comment(post_id=post, text=text, std_id=user)
                com.save()
                return HttpResponse('success')
            else:
                return render(request, 'polls/test.html', 'problem in sending data')
        except:
            raise Http404('Problem')
    # post_id
    # text
    pass

    # Create your views here.


def search_blog(request):
    pos_l = dict()
    if request.method == 'POST':
        try:
            if 'search' in request.POST:
                l = str(request.POST['search']).split(" ")
                for l1 in l:
                    p = Post_Word.objects.filter(word=l1).all()
                    for p1 in p:
                        v = pos_l.get(p1.post.id)
                        if v is None:
                            pos_l.update(({p1.post.id: 1}))
                        else:
                            pos_l[p1.post.id] = v + 1
                f_l = sorted(pos_l.items(), key=lambda x: x[1])
                return HttpResponse(f_l[0:10])
            else:
                return Http404("1")
        except:
            return Http404("2")
