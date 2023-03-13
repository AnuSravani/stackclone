from stack.models import Questions,Answers
def activities(request):
    if request.user.is_authenticated:
        cnt=Questions.objects.filter(User=request.user).count()
        ant=Answers.objects.filter(user=request.user).count()
        return {"qcnt":cnt,"acnt":ant}
    else:
        return {"qcount":0}

