from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth import authenticate,login
from django.views import generic
#it is used in django to get a text respinse in our webpage
# Create your views here.

def first(request):
    return HttpResponse('My First Django Page')

def second(request):
    return HttpResponse('My Sceond Django Page')

#render-->its a function that is used to connec your functions with templates to return are user interface layer

def third(request):
    return render(request,'third.html')

def des(request):
    return render(request,'wrk1.html')

def reg(request):
    if request.method=='POST':
        fname=request.POST.get('firstname')
        lname=request.POST.get('lastname')
        user=request.POST.get('uname')
        email=request.POST.get('email')
        ph=request.POST.get('phone')
        gen=request.POST.get('gender')
        add=request.POST.get('address')
        dob=request.POST.get('dob')
        psw=request.POST.get('psw')
        copsw=request.POST.get('cpsw')
        if psw==copsw:
            a=register(fname=fname,lname=lname,username=user,email=email,phone=ph,gender=gen,address=add,dob=dob,password=psw)
            a.save()
            return HttpResponse('registration success')
        else:
            return HttpResponse('password incorrect')
    return render(request,'reg.html')

# def login(request):
#     if request.method=='POST':
#         email=request.POST.get('email')
#         password=request.POST.get('psw')
#         a=register.objects.all() #[(id num,name,phn),(id num2,name2,phn2)]
#         for i in a:
#             if(i.email==email and i.password==password): #email-->models(register)==email-->view(login)
#                 return HttpResponse('Login Successfull')
#         else:
#             return HttpResponse('Login Failed')
#     return render(request,'login.html')
# def index(request):
#     return render(request,'index.html')
def fileupload(request):
    if request.method=='POST':
        fname=request.POST.get('fname')
        image=request.FILES['filename']
        desc=request.POST.get('desc')
        d=file_upload2(filename=fname,fileimage=image,des=desc)
        d.save()
        return HttpResponse('fileupload success')
    return render(request,'fileupload.html')

def emp_reg(request):
    if request.method=='POST':
        ename=request.POST.get('ename')
        email=request.POST.get('email')
        cmp=request.POST.get('cmp')
        des=request.POST.get('desc')
        phone=request.POST.get('mob')
        b=empreg(emp_name=ename,mail=email,cmpnm=cmp,des=des,phone=phone)
        b.save()
        return HttpResponse('Employee Registered')
    return render(request,'emp_reg.html')

def search_employee(request):
    if request.method=='POST':
        emp_name=request.POST.get('enm')
        phone=request.POST.get('phone')
        a=empreg.objects.all()
        for i in a:
            if(i.emp_name==emp_name and int(i.phone)==int(phone)):
                return HttpResponse('Employee Found')
        else:
            return HttpResponse('Employee Not Found')
    return render(request,'search_employee.html')

#product details--html file:
#product name,price, pro_cmpany,quantity,exp_date,description

#check:
#prod_name, prod_cmpny

def product_detail(request):
    if request.method=='POST':
        pro_name=request.POST.get('pname')
        price=request.POST.get('price')
        pro_cmpny=request.POST.get('cname')
        quan=request.POST.get('quan')
        expdt=request.POST.get('exp')
        descrp=request.POST.get('description')
        c=product(pro_name=pro_name,price=price,pro_cmpny=pro_cmpny,quan=quan,expdt=expdt,descrp=descrp)
        c.save()
        return HttpResponse('Product Added Successfully')
    return render(request,'product_detail.html')

def product_check(request):
    if request.method=='POST':
        pro_name=request.POST.get('pname')
        pro_cmpny=request.POST.get('cname')
        c=product.objects.all()
        for i in c:
            if(i.pro_name==pro_name and i.pro_cmpny==pro_cmpny):
                return HttpResponse('Product Found')
        else:
            return HttpResponse('product Not Found')
    return render(request,'product_check.html')

def fileupload3(request):
    if request.method=='POST':
        audio=request.POST.get('aname')
        audio1=request.FILES['af']
        vedio=request.POST.get('vname')
        vedio1=request.FILES['vf']
        pdf=request.POST.get('pdfname')
        pdf1=request.FILES['pdf']
        e=file_upload3(audioname=audio,audio=audio1,vedioname=vedio,vedio=vedio1, pdfname=pdf,pdf=pdf1)
        e.save()
        return HttpResponse('Files Upload Successfully')
    return render(request,'fileupload3.html')

def checkbox(request):
    if request.method=='POST':
        name=request.POST.get('fname')
        state=request.POST.get('state')
        tamil=request.POST.get('ch1')
        if tamil=='on':
            tamil=True
        else:
            tamil=False
        malayalam=request.POST.get('ch2')
        if malayalam=='on':
            malayalam=True
        else:
            malayalam=False
        english=request.POST.get('ch3')
        if english=='on':
            english=True
        else:
            english=False
        a=check_box(fullname=name,state=state,tamil=tamil,malayalam=malayalam,english=english)
        a.save()
        return HttpResponse('Datas Add Sucessfully')

    return render(request,'checkbox.html')


def display(request):
    a=register.objects.all()
    b = empreg.objects.all()

    return render(request,'display.html',{'data':a,'data1':b})

def imgdisplay(request):

    id=[]
    filename=[]
    image=[]
    des=[]
    image_path = []
    a = file_upload2.objects.all()
    for i in a:
        id1=i.id
        id.append(id1)
        name=i.filename
        filename.append(name)
        im=str(i.fileimage).split('/')[-1]
        image.append(im)
        description=i.des
        des.append(description)
        ip=i.fileimage
        image_path.append(i.fileimage.url)
    mylist=zip(id,filename,image,des,image_path)
    return render(request,'imgdisplay.html',{'data':mylist})





def addisplay(request):
    id=[]
    aname=[]
    audio=[]
    vname=[]
    vedio=[]
    pdfname=[]
    pdf=[]
    a=file_upload3.objects.all()
    for i in a:
        id1=i.id
        id.append(id1)
        af=i.audioname
        aname.append(af)
        aud=str(i.audio).split('/')[-1]
        audio.append(aud)
        vdname=i.vedioname
        vname.append(vdname)
        vd=str(i.vedio).split('/')[-1]
        vedio.append(vd)
        p=i.pdfname
        pdfname.append(p)
        pd=str(i.pdf).split('/')[-1]
        pdf.append(pd)
    mylst=zip(id,aname,audio,vname,vedio,pdfname,pdf)
    return render(request,'addisplay.html',{'data':mylst})

def update_data(request,id):
    a=register.objects.get(id=id)
    if request.method=='POST':
        a.fname=request.POST.get('firstname')
        a.lname=request.POST.get('lastname')
        a.username=request.POST.get('uname')
        a.email=request.POST.get('email')
        a.phone=request.POST.get('phone')
        # a.gender=request.POST.get('gender')
        if str(request.POST.get('gender'))=='female' or str(request.POST.get('gender'))=='male':
            a.gender=request.POST.get('gender')
        else:
            a.save()
        a.address=request.POST.get('address')
        # a.dob=request.POST.get('dob')
        if len(str(request.POST.get('dob')))>0:
            a.dob=request.POST.get('dob')
        else:
            a.save()
        a.save()

        return redirect(display)

    return render(request,'editprofile.html',{'data':a})


def emp_update(request,id):
    a=empreg.objects.get(id=id)
    if request.method=='POST':
        a.emp_name=request.POST.get('ename')
        a.mail=request.POST.get('email')
        a.cmpnm=request.POST.get('cmp')
        a.des=request.POST.get('desc')
        a.phone=request.POST.get('mob')
        a.save()
        return redirect(display)
    return render(request,'empupdate.html',{'data1':a})


def img_update(request,id):
    a=file_upload2.objects.get(id=id)
    image=str(a.fileimage).split('/')[-1]
    if request.method=='POST':
        a.filename=request.POST.get('fname')
        if len(str(request.FILES['filename']))>0:
            a.fileimage=request.FILES['filename']
        else:
            a.save()
        a.des=request.POST.get('desc')
        a.save()
        return redirect(imgdisplay)
    return render(request,'imgupdate.html',{'data':a,'img':image})


def avp_update(request,id):
    a=file_upload3.objects.get(id=id)
    audio=str(a.audio).split('/')[-1]
    vedio=str(a.vedio).split('/')[-1]
    pdf=str(a.pdf).split('/')[-1]
    if request.method=='POST':
        a.audioname=request.POST.get('aname')
        if request.FILES.get('af')==None:
            a.save()
        else:
            a.audio=request.FILES.get('af')
            a.save()

        a.vedioname=request.POST.get('vname')
        if request.FILES.get('vf')==None:
            a.save()
        else:
            a.vedio=request.FILES.get('vf')
            a.save()

        a.pdfname=request.POST.get('pdfname')
        if request.FILES.get('pdf')=='POST':
            a.save()
        else:
            a.pdf=request.FILES.get('pdf')
            a.save()
        a.save()
        return redirect(addisplay)
    return render(request,'avpupdate.html',{'data':a,'audio':audio,'vedio':vedio,'pdf':pdf})


def delete_reg(request,id):
    a=register.objects.get(id=id)
    a.delete()
    return redirect(display)

def delete_employee(request,id):
    a=empreg.objects.get(id=id)
    a.delete()
    return redirect(display)

def del_image(request,id):
    a=file_upload2.objects.get(id=id)
    a.delete()
    return redirect(imgdisplay)

def del_avp(request,id):
    a=file_upload3.objects.get(id=id)
    a.delete()
    return redirect(addisplay)


def userregistration(request):
    if request.method=='POST':
        a=userreg(request.POST) #form store to a variable
        if a.is_valid(): #check the validitity of the form
            un = request.POST.get('username')
            f_name = request.POST.get('first_name')
            l_name = request.POST.get('last_name')
            em = request.POST.get('email')
            psd=request.POST.get('password')
            # psd = a.cleaned_data['password']
            b=User.objects.create_user(username=un,first_name=f_name,last_name=l_name,email=em,password=psd)
            b.save()
            return HttpResponse('authenticated user added')
        else:
            return HttpResponse('user not added')
    else:
        form=userreg()
        return render(request,'userregister.html',{'form1':form})


def userregis(requset):
    if requset.method=='POST':
        a=userform(requset.POST)
        if a.is_valid():
            us=a.cleaned_data['username']
            fn=a.cleaned_data['first_name']
            ln=a.cleaned_data['last_name']
            em=a.cleaned_data['email']
            ps=a.cleaned_data['password']
            cps=a.cleaned_data['conf']
            if ps==cps:
                user=User(username=us,first_name=fn,last_name=ln,email=em)
                user.set_password(ps)
                user.save()
                return HttpResponse('register')
            else:
                return HttpResponse("password does't match")
        else:
            return HttpResponse("faield")
    else:
        form=userform()
        return render(requset,'userregis.html',{'form':form})



def custom_login(request):
    if request.method=='POST':
        form =userlogin(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)


            if user is not None:
                login(request,user)
                return HttpResponse('logged in successfully')
            else:
                return HttpResponse('Invalid username or password')
        else:
            return HttpResponse('Invalid username or password')
    else:
        form=userlogin()
    return render(request,'login1.html')


#contaxt: is dictonar in django which is used it pass your datas from backend to frontend



