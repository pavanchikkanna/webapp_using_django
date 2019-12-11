from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import farmer,sell,buy
import datetime
# Create your views here.
def home(request):
    return render(request,'index.html')

#authenctication handlers
def auth(request):
    return render(request,'auth.html')

def signin(request):
    r_email=str(request.GET['email'])
    r_passwrd=str(request.GET['password'])
    f_obj=farmer.objects.filter(email=r_email)
    if len(f_obj)==1 and f_obj[0].email==r_email and f_obj[0].password==r_passwrd:
        data='ok'
        request.session['user']=r_email
    else:
        data="notok"
    return JsonResponse({'data':data})

def signup(request):
    r_email=request.GET['email']
    r_name=request.GET['name']
    r_passwrd=request.GET['password']
    f_obj=farmer.objects.filter(email=r_email)
    if len(f_obj)==0:
        f_obj=farmer(email=r_email,name=r_name,password=r_passwrd)
        f_obj.save()
        data="ok"
    else:
        data="notok"
    return JsonResponse({'data':data})
def logout(request):
    try:
        del request.session['user']
    except:
        pass
    return redirect('/auth/')



def profile(request):
    try:
        user=request.session['user']
        print(request.session['user'])
        return render(request,'profile.html',{'obj':farmer.objects.filter(email=user)[0]})
    except:
        return redirect('/auth/')

def profileupdate(request):
    try:
        user=request.session['user']
        f_obj=farmer.objects.get(email=user)
        f_obj.name=request.GET['name']
        f_obj.street=request.GET['street']
        f_obj.city=request.GET['city']
        f_obj.district=request.GET['district']
        f_obj.phone=request.GET['phone']
        try:
            f_obj.save()
            data="ok"
        except:
            data="notok"
        return JsonResponse({'data':data})
    except:
        return redirect('/auth/')



def sell_form(request):
    try:
        user=request.session['user']
        return render(request,'sell.html')
    except:
        return redirect('/auth/')

def upload(request):
    f_obj=farmer.objects.get(email=request.session['user'])
    sell_obj=sell(p_name=request.GET['name'],description=request.GET['discription'],
    f_id=f_obj,quantity=request.GET['quantity'],
    p_type=request.GET['type'],price=request.GET['price'])
    try:
        sell_obj.save()
        data="ok"
    except:
        data='notok'
    return JsonResponse({'data':data})


def sale(request):
    try:
        user=request.session['user']
        x=buy.objects.values_list('p_id',flat=True)
        print(x)
        d=dict()
        for i in x:
            if i not in d:
                d[i]=True
            else:
                continue
        p_obj=[]
        for i in sell.objects.all():
            if i.p_id not in d:
                p_obj.append(i)
            
        return render(request,'buy.html',{'products':p_obj})
    except:
        return redirect('/auth/')

def want(request):
    try:
        user=request.session['user']
        f_obj=farmer.objects.get(email=user)
        p_obj=sell.objects.get(p_id=request.GET['id'])
        b_obj=buy(f_id=f_obj,p_id=p_obj,date=datetime.date.today())
        b_obj.save()
        return JsonResponse({'data':'ok'})
    except:
        return JsonResponse({'data':'notok'})
