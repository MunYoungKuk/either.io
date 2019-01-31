from django.shortcuts import render,redirect
from .models import Question, Answer
# Create your views here.
def index(request):
    questions = Question.objects.all()
    return render(request,"either/index.html",{"questions":questions})
    
def new(request):
    return render(request,"either/new.html")

def create(request):
    title = request.POST.get("title")
    A = request.POST.get("A")
    B = request.POST.get("B")
    
    Question.objects.create(title=title,A=A,B=B)
    
    return redirect("/either/")

def read(request,id):
    question = Question.objects.get(pk=id)
    count_A = question.answer_set.filter(pick=0).count()
    count_B = question.answer_set.filter(pick=1).count()
    sum_AB = count_A + count_B
    if sum_AB == 0:
        A_per = 0
        B_per = 0
    else:
        A_per = count_A / sum_AB * 100
        B_per = count_B / sum_AB * 100
    
    return render(request,"either/read.html",{"question":question, "A_per":A_per,"B_per":B_per})
    
def random(request):
    question = Question.objects.order_by('?')[0]
    count_A = question.answer_set.filter(pick=0).count()
    count_B = question.answer_set.filter(pick=1).count()
    sum_AB = count_A + count_B
    if sum_AB == 0:
        A_per = 0
        B_per = 0
    else:
        A_per = count_A / sum_AB * 100
        B_per = count_B / sum_AB * 100
    
    return render(request,"either/read.html",{"question":question, "A_per":A_per,"B_per":B_per})
def comment_create(request,id):
    question = Question.objects.get(pk=id)
    pick = int(request.POST.get("pick"))
    comment = request.POST.get("comment")
    
    Answer.objects.create(question=question,pick=pick,comment=comment)
    
    return redirect(f"/either/{id}/")