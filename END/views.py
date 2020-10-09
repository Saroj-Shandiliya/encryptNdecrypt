from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse,HttpResponseRedirect
from django import forms
from django.core.mail import send_mail
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker
from . import urls
import os
import requests
import uuid 
import datetime
import random

#variables

lis=[
    ('1','User ID (Direct)'),
    ('2','User ID (via Key)'),
    ('3','Guest ID'),
    ('4','Random Guest')
]
txt=''
e=0
oka=2
om=1
m=1
lm=[]
d=''
name=''
q=[]
ran=''
timeec=''
usn=''
tim=0
enc=''
key=''
notif=''
de=''
noti=[]
o=0
mez=''
ok=0
f=1
w=[]
eml=''

#Engine created for SQLalchemy


engine=create_engine(os.getenv('HEROKU_POSTGRESQL_GREEN_URL'))
db=scoped_session(sessionmaker(bind=engine))

s="select * from sg1;"
pw=db.execute(s).fetchall()

appname='END'




#Forms
class sign1(forms.Form):
    Username=forms.CharField(label='Username',max_length=10,widget=forms.TextInput(attrs={
        'type':'text',
        'placeholder':'Username',
        'pattern':"[A-Za-z0-9!@#$%&*()_-]{2,20}",
        'title':'No spaces in between, Maximum length:10',
    }))
    Email=forms.EmailField(label='Email',max_length=300,widget=forms.EmailInput(attrs={
        'type':'email',
        'placeholder':'Email'
    }))
    Password=forms.CharField(label='Password',min_length=8,max_length=20,widget=forms.PasswordInput(attrs={
        'type':'password',
        'placeholder':'Password'
    }))

class user(forms.Form):                     #Username for Username
    Username=forms.CharField(label='Username',max_length=15,widget=forms.TextInput(attrs={
        'type':'text',
        'placeholder':'Username'
    }))

class pasm(forms.Form):                     # password
    Password=forms.CharField(label='Password',max_length=20,widget=forms.PasswordInput(attrs={
        'type':'password'
    }))

class forg(forms.Form):                     # email for the forgot password user
    Email=forms.CharField(label='Email',max_length=50,widget=forms.EmailInput(attrs={
        'type':'email',
        'placeholder':'Email'
    }))

class secu(forms.Form):                     # security key
    Key=forms.CharField(label='Security Key:',max_length=15,widget=forms.PasswordInput(attrs={
        'type':'password',
        'placeholder':'Key'
    }))

class Log(forms.Form):                      # login
    Email=forms.CharField(max_length=50,widget=forms.EmailInput(attrs={
        'type':'email',
        'placeholder':'Email',
        'name':''
    }))

class Feed(forms.Form):
    Feed=forms.CharField(max_length=150,widget=forms.TextInput(attrs={
        'type':'text',
        'placeholder':'Advice',
        'name':''
    }))

class Log1(forms.Form):
    Password=forms.CharField(max_length=20,widget=forms.PasswordInput(attrs={
        'type':'password',
        'placeholder':'Password',
        'name':''
    }))

class verif(forms.Form):
    verif=forms.CharField(label='Code',max_length=36,widget=forms.TextInput(attrs={
        'type':'text',
        'placeholder':'Code'
    }))

class ans(forms.Form):
    Answer=forms.CharField(label='Code',max_length=6,min_length=6,widget=forms.PasswordInput(attrs={
        'type':'password',
        'placeholder':'Code'
    }))

class Enc(forms.Form):                   # encrypt form
    Encrypt=forms.CharField(label ='Encrypt:',max_length=100,widget=forms.TextInput(attrs={
        'type':'text',
        'placeholder':'Message',
        'pattern':"[A-Za-z0-9!@#$%&*() _-]{1,100}",
        'title':'Use only A-Z,a-z,0-9,!@#$%&*()_-[]',
    }))
    Type=forms.ChoiceField(label='Method',required='True',choices = lis)
    
class gue(forms.Form):                  # guest id 
    Guest_ID=forms.CharField(label='Guest',max_length=50,widget=forms.TextInput(attrs={
        'type':'text',
        'placeholder':'Guest Id'
    }))

class gueu(forms.Form):                 #guest key
    Key =forms.CharField(label='Security',max_length=15,widget=forms.PasswordInput(attrs={
        'type':'password',
        'placeholder':'Key'
    }))

class rad(forms.Form):                  # random id message
    Encrypted_Message=forms.CharField(label='Encrypted Message',max_length=36,widget=forms.TextInput(attrs={
        'type':'text',
        'placeholder':'Key'
    }))

class ennc(forms.Form):                  # email and key of the decrypter for uus
    Email_Receiver =forms.EmailField(label='Receiver Email id',max_length=300,widget=forms.EmailInput(attrs={
        'type':'email',
        'placeholder':'Receiver Email Id'
    }))
    Key =forms.CharField(label='Security Key',max_length=15,widget=forms.PasswordInput(attrs={
        'type':'password',
        'placeholder':'Key'
    }))

class nam(forms.Form):                  # email of the decrypter for uud
    Email_Receiver =forms.EmailField(label='Receiver Email id',max_length=300,widget=forms.EmailInput(attrs={
        'type':'email',
        'placeholder':'Receiver Email Id'
    }))

# Create your views here.

def start(request):
    return render(request,'start.html')

def login(request):
    if "End" not in request.session:
        request.session['End']=[]
    if "fog" in request.session:
        del request.session['fog']
    if 'for' in request.session:
        del request.session['for']
    try:
        if request.method=='POST' and m==1:
            form=Log(request.POST)
            forme=Log1(request.POST)
            if form.is_valid() and forme.is_valid():
                name=form.cleaned_data['Email']
                pwd=forme.cleaned_data['Password']
                pwd=hash(pwd)
                name=name.lower()
                request.session['End']=[]
                ran=''
                r,ud,ran,ch=check(name,pwd)
                if ch==True:
                    if "End" in request.session:
                        del request.session['End']
                    if "for" in request.session:
                        del request.session['for']
                    request.session['for']=[]
                    request.session['for']+=[name]
                    return HttpResponseRedirect(reverse('verify'))
                request.session['End'] +=[ud]
                request.session['End'] +=[ran]
                if r==3:
                    eml=name
                    usn=''
                    q=request.session['End']
                    s="SELECT usn FROM sg1 WHERE uuidu='"+q[0]+"';"
                    pw=db.execute(s).fetchall()
                    pw=str(pw)
                    j=len(pw)-4
                    h=0
                    for h in range(j):
                        if h>2:
                            usn=usn+pw[h]
                    jo=len(usn)
                    sam=''
                    for io in range(jo):
                        if usn[io]==' ':
                            usn[io]
                        else:
                            sam=sam+usn[io]
                    return HttpResponseRedirect(reverse('Profiles',kwargs={'rname':sam}))
                elif r==1:
                    if "End" in request.session:
                        del request.session['End']
                    msg='User ID does not exist!!'
                    return render(request,'END/main.html',{
                        'form':Log(),
                        'form1':Log1(),
                        'msg':msg,
                    })
                elif r==2:
                    if "End" in request.session:
                        del request.session['End']
                    msg=':(   Invalid Password!!'
                    return render(request,'END/main.html',{
                            'form':Log(),
                            'form1':Log1(),
                            'msg':msg,
                    })
                else:
                    if "End" in request.session:
                        del request.session['End']
                    msg=':(   Invalid Input!!'
                    return render(request,'END/main.html',{
                        'form':Log(),
                        'form1':Log1(),
                        'msg':msg,
                    })
            elif form == '':
                if "End" in request.session:
                    del request.session['End']
                msg=':(   Invalid Input!!'
                return render(request,'END/main.html',{
                    'form':Log(),
                    'form1':Log1(),
                    'msg':msg,
                })
            else:
                if "End" in request.session:
                    del request.session['End']
                msg=''
                return render(request,'END/main.html',{
                    'form':Log(),
                    'form1':Log1(),
                    'msg':msg,
                })
        else:
            if "End" in request.session:
                del request.session['End']
            msg=''
            return render(request,'END/main.html',{
                'form':Log(),
                'form1':Log1(),
            })
    except:
        if "End" in request.session:
            del request.session['End']
        msg=''
        return render(request,'END/main.html',{
            'form':Log(),
            'form1':Log1(),
        })

def check(name,pwd):
    ran=''
    s="SELECT uuidu FROM  sg1 WHERE "
    s +="eml='"+name+"';"
    pw=db.execute(s).fetchall()
    if pw == [] :
        ox=1
        q=''
        ran=''
        ch=False
        return ox,q,ran,ch
    else:
        q=cutter(pw)
        s="SELECT pwd FROM p1 WHERE "
        s +="uuidu='"+q+"';"
        pw=db.execute(s).fetchall()
        pas=cutter(pw)
        s="SELECT seal FROM  sg1 WHERE "
        s +="eml='"+name+"';"
        pw=db.execute(s).fetchall()
        seal=cutter(pw)
        if pwd==pas:
            s="SELECT verify FROM sg1 WHERE "
            s +="uuidu='"+q+"';"
            pw=db.execute(s).fetchall()
            pas=cutter(pw)
            if pas=='NT':
                ch=True
                if ch==True:
                    ox=''
                    q=''
                    ran=''
                    return ox,q,ran,ch
            if seal=='86':
                s="UPDATE sg1 SET seal='9089' WHERE eml='"+name+"';"
                db.execute(s)
                db.commit()
            ran=str(random.randint(1111111,9999999))
            s="UPDATE sg1 SET logc='"+ran+"' "
            s+="WHERE uuidu='"+q+"';"
            db.execute(s)
            db.commit()
            s="SELECT logn FROM sg1 WHERE "
            s +="uuidu='"+q+"';"
            pw=db.execute(s).fetchall()
            pw=str(pw)
            j=len(pw)-4
            no=''
            h=0
            for h in range(j):
                if h>2:
                    no=no+pw[h]
            num=int(no)+1
            s="UPDATE sg1 SET logn='"+str(num)+"' "
            s+="WHERE uuidu='"+q+"';"
            db.execute(s)
            db.commit()
            tim=str(datetime.datetime.now())
            tim=str(tim)
            s="UPDATE sg1 SET timee='"+tim+"' "
            s+="WHERE uuidu='"+q+"';"
            db.execute(s)
            db.commit()
            ox=3
            ch=''
            return ox,q,ran,ch
        else:
            ox=2
            ch=''
            return ox,q,ran,ch

def signup(request):
    try:
        if request.method=='POST':
            form=sign1(request.POST)
            if form.is_valid():
                us=form.cleaned_data['Username']
                eml=form.cleaned_data['Email']
                pwd=form.cleaned_data['Password']
                eml=eml.lower()
                s="SELECT verify FROM  SG1 WHERE "
                s +="eml='"+eml+"';"
                pw=db.execute(s).fetchall()
                lav=len(pw)
                if pw != []:
                    ed=cutter(pw)
                    if ed =='NT' or lav>1:
                        s="DELETE FROM  SG1 WHERE "
                        s +="eml='"+eml+"';"
                        pw=db.execute(s)
                        db.commit()
                    elif ed != 'NT':
                        msg='User Email already exist!! '
                        return render(request,'END/signup.html',{
                            'msg':msg,
                            'form':sign1(),
                        })
                emvf=str(random.randint(111111,999999))
                ud=str(uuid.uuid4())
                pwd=hash(pwd)
                no='0'
                tim=str(datetime.date.today())
                s="INSERT INTO sg1 (uuidu,usn,eml,seal,timec,logn,verify,vcode) "
                s+="VALUES ('"+ud+"','"+us+"','"+eml+"',9089,'"+tim+"','"+no+"','NT','"+emvf+"');"
                db.execute(s)
                db.commit()
                send_mail("Verification code [EnD].","Your EnD verification code |"+emvf+"|.","encryptndecrypt@gmail.com",[eml],    # This is a list
                    fail_silently = False     # Set this to False so that you will be noticed in any exception raised
                    )
                s="INSERT INTO p1 (uuidu,pwd) "
                s+="VALUES ('"+ud+"','"+pwd+"');"
                db.execute(s)
                db.commit()
                msg='User ID created!!'
                return HttpResponseRedirect(reverse('login'))
            else:
                msg='Invalid Input'
                return render(request,'END/signup.html',{
                    'form':sign1(),
                    'msg': msg,
                }) 
        else:
            return render(request,'END/signup.html',{
                'form':sign1(),
            })
    except:
        msg="Error occured!!"
        return render(request,'END/signup.html',{
            'form':sign1(),
            'msg':msg,
        })

def home(request,rname):
    q=request.session['End']
    s="SELECT logc FROM SG1 WHERE uuidu='"+q[0]+"';"
    pw=db.execute(s).fetchall()
    rn=cutter(pw)
    s="SELECT usn FROM SG1 WHERE uuidu='"+q[0]+"';"
    pw=db.execute(s).fetchall()
    usn=cutter(pw)
    try:
        io=0
        jo=len(usn)
        sam=''
        for io in range(jo):
            if usn[io]==' ':
                usn[io]
            else:
                sam=sam+usn[io]
        if rn==q[1] and sam==rname:
            if "Enc" in request.session:
                del request.session['Enc']
            noti=reverse1(q)
            fln,de,notif,eml=userfiles(q)
            s="SELECT emle,uuide FROM "+de+" WHERE acc='9089';"
            pw=db.execute(s).fetchall()                 #getting those messages which are not seen
            return render (request,'END/home.html',{
                'user':sam,
                'noti':noti,
                'dec':pw
            })
        else:
            s="UPDATE SG1 SET logc = 'no' WHERE uuidu='"+q[0]+"';"
            request.session['End']=[]
            ran=''
            q=[]
            usn=''
            return render(request,'END/error.html')
    except:
        if "Dnc" in request.session:
            del request.session['Dnc']
        if "Enc" in request.session:
            del request.session['Enc']
        if "End" in request.session:
            q=request.session['End']
            s=''
            s +="UPDATE sg1 SET Logc='no'"
            s +=" "
            s +="WHERE"
            s +=" "
            s +="uuidu='"+q[0]+"';"
            pw=db.execute(s)
            db.commit()
            ran='no'
            q=''
            de=''
            fln=''
            eml=''
            notif=''
            emle=''
            usn=''
            ran=''
            q=[]
            usn=''
            del request.session['End']
            return render(request,'END/error.html')

def encrypt(request,rname):
    try:
        q=request.session['End']
        if "Dnc" not in request.session:
            request.session['Dnc']=[]
        w=request.session['Dnc']
        s="SELECT logc FROM SG1 WHERE uuidu='"+q[0]+"';"
        pw=db.execute(s).fetchall()
        rn=cutter(pw)
        s="SELECT usn FROM SG1 WHERE uuidu='"+q[0]+"';"
        pw=db.execute(s).fetchall()
        usn=cutter(pw)
        if rn==q[1] and rname==usn:
            if request.method=='POST':
                if w[0]==1:
                    form=Enc(request.POST)      # entered for the first time
                elif w[0]==2:
                    form=nam(request.POST)      # if entered for the second time after the enc 
                elif w[0]==3:
                    form=ennc(request.POST)
                elif w[0]==4:
                    form=secu(request.POST)
                if form.is_valid():
                    if w[0]==1:
                        tec=form.cleaned_data['Encrypt']
                        met=form.cleaned_data['Type']
                        mez=str(met)
                        request.session['Dnc']+=[mez]
                        request.session['Dnc']+=[tec]
                        r=True
                    elif w[0]==2:
                        r=True
                    elif w[0]==3:
                        r=True
                    elif w[0]==4:
                        r=True
                    else:
                        r=False
                    w=request.session['Dnc']
                    if r==True :
                        if w[1]=='1':
                            if w[0]==1:
                                noti=reverse1(q)
                                w[0]=2
                                request.session['Dnc']=w
                                return render(request,'END/Encrypt.html',{
                                'user':usn,
                                'form':Enc(),
                                'form1':nam(),
                                'noti':noti,
                                'om':w[0]
                                })
                            elif w[0]==2:
                                q=request.session['End']
                                enc, key, tim, timeec, txt=encrptxt(w[2])
                                mez=''
                                usd=form.cleaned_data['Email_Receiver']                  #getting the dec user email
                                s="SELECT dect FROM fn1 WHERE eml='"+usd+"';"
                                pw=db.execute(s).fetchall()                #getting file name of the decrypters dec file
                                k=cutter(pw)
                                s="SELECT seal FROM  SG1 WHERE "
                                s +="eml='"+usd+"';"
                                pw=db.execute(s).fetchall()
                                seal=cutter(pw)
                                if k==[] or seal=='86':
                                    msg='No such user with email exist!!'
                                    noti=reverse1(q)
                                    om=0
                                    del request.session['Dnc']
                                    t=1
                                    noti=reverse1(q)
                                    request.session['Dnc']=[]
                                    request.session['Dnc']+=[t]
                                    return render(request,'END/Encrypt.html',{
                                    'user':usn,
                                    'form':Enc(),
                                    'noti':noti,
                                    'om':t,
                                    'msg':msg
                                    })
                                ud=str(uuid.uuid1())
                                fln,de,notif,eml=userfiles(q)
                                s="INSERT INTO "+fln+" (uuide,timeec,mang,emld,acc) VALUES ('"+ud+"','"+timeec+"','uud1','"+usd+"','9089');"
                                db.execute(s)                           #inserting into user encfile 
                                db.commit()
                                s="INSERT INTO uud1 (uuidu,enct,enck,enctm,emld,acc) VALUES('"+ud+"','"+enc+"','"+key+"','"+tim+"','"+usd+"','9089');"
                                db.execute(s)                           #inserting in main enc file 
                                db.commit()
                                s="INSERT INTO "+k+" (uuide,mang,emle,acc) VALUES ('"+ud+"','uud1','"+eml+"','9089');"
                                db.execute(s)                               #inserting into the dec userd dec file
                                db.commit()
                                dc=''                               
                                for i in range(len(k)-4):
                                    dc=dc+k[i]
                                dc=dc+'nott'
                                s="INSERT INTO "+dc+"(msg,status) VALUES ('Message received from "+eml+".','9089');"
                                db.execute(s)                               #inserting into dec user nott file
                                db.commit()
                                timeec=''
                                tim=''
                                key=''
                                enc=''
                                msg='Message Sent :)'
                                usd=''
                                t=1
                                noti=reverse1(q)
                                del request.session['Dnc']
                                request.session['Dnc']=[]
                                request.session['Dnc']+=[t]
                                return render(request,'END/Encrypt.html',{
                                'user':usn,
                                'msg':msg,
                                'form':Enc(),
                                'noti':noti,
                                'om':t
                                })
                        elif w[1]=='2':
                            if w[0] == 1:
                                noti=reverse1(q)
                                w[0]=3
                                request.session['Dnc']=w
                                return render(request,'END/Encrypt.html',{
                                'user':usn,
                                'form':ennc(),
                                'noti':noti,
                                'om':w[0]
                                })
                            elif w[0]==3:
                                q=request.session['End']
                                w=request.session['Dnc']
                                enc, key, tim, timeec, txt=encrptxt(w[2])
                                mez=''
                                t=1
                                fln,de,notif,eml=userfiles(q)
                                usd=form.cleaned_data['Email_Receiver']                  #getting the dec user email
                                s="SELECT dect FROM fn1 WHERE eml='"+usd+"';"
                                pw=db.execute(s).fetchall()                #getting file name of the decrypters dec file
                                k=cutter(pw)
                                s="SELECT seal FROM  SG1 WHERE "
                                s +="eml='"+usd+"';"
                                pw=db.execute(s).fetchall()
                                seal=cutter(pw)
                                if k==[] or seal=='86':
                                    msg='No such user with email exist!!'
                                    noti=reverse1(q)
                                    om=0
                                    del request.session['Dnc']
                                    t=1
                                    noti=reverse1(q)
                                    request.session['Dnc']=[]
                                    request.session['Dnc']+=[t]
                                    return render(request,'END/Encrypt.html',{
                                    'user':usn,
                                    'form':Enc(),
                                    'noti':noti,
                                    'om':t,
                                    'msg':msg
                                    })
                                sa=form.cleaned_data['Key']                               #getting the security key
                                ud=str(uuid.uuid1())
                                s="INSERT INTO "+fln+" (uuide,timeec,mang,emld,acc) VALUES ('"+ud+"','"+timeec+"','uus1','"+usd+"','9089');"
                                db.execute(s)                            #inserting into users enc file
                                db.commit()
                                s="INSERT INTO uus1 (uuidu,enct,enck,enctm,emld,sa,acc) VALUES('"+ud+"','"+enc+"','"+key+"','"+tim+"','"+usd+"','"+sa+"','9089');"
                                db.execute(s)                           #inserting in main enc file 
                                db.commit()
                                s="INSERT INTO "+k+" (uuide,mang,emle,acc) VALUES ('"+ud+"','uus1','"+eml+"','9089');"
                                db.execute(s)                               #inserting into the dec userd dec file
                                db.commit()
                                dc=''                               
                                for i in range(len(k)-4):
                                    dc=dc+k[i]
                                dc=dc+'nott'
                                s="INSERT INTO "+dc+"(msg,status) VALUES ('Message received from "+eml+".','9089');"
                                db.execute(s)                               #inserting into dec user nott file
                                db.commit()
                                timeec=''
                                tim=''
                                key=''
                                enc=''
                                msg='Message Sent :)'
                                usd=''
                                del request.session['Dnc']
                                noti=reverse1(q)
                                request.session['Dnc']=[]
                                request.session['Dnc']+=[t]
                                return render(request,'END/Encrypt.html',{
                                'user':usn,
                                'msg':msg,
                                'form':Enc(),
                                'noti':noti,
                                'om':t
                                })
                        elif w[1]=='3':
                            if w[0]==1:
                                msg='Enter key:'
                                w[0]=4
                                request.session['Dnc']=w
                                noti=reverse1(q)
                                return render(request,'END/Encrypt.html',{
                                'user':usn,
                                'msg':msg,
                                'form1':secu(),
                                'noti':noti,
                                'om':w[0]
                                })
                            elif w[0]==4:
                                if form.is_valid():
                                    sa=form.cleaned_data['Key']
                                    q=request.session['End']
                                    w=request.session['Dnc']
                                    enc, key, tim, timeec, txt=encrptxt(w[2])
                                    t=1
                                    mez=''
                                    fln,de,notif,eml=userfiles(q)
                                    fn=str(random.randint(11111111,99999999))
                                    usd='Guest Id/'+fn+usn
                                    ud=str(uuid.uuid1())
                                    s="INSERT INTO "+fln+" (uuide,timeec,mang,emld,acc) VALUES ('"+ud+"','"+timeec+"','ud1','"+usd+"','9089');"
                                    db.execute(s)                            #inserting into users enc file
                                    db.commit()
                                    s="INSERT INTO ug1 (uuidu,enct,enck,enctm,gid,sa,wrn,encc,acc) VALUES ('"+ud+"','"+enc+"','"+key+"','"+tim+"','"+usd+"','"+sa+"','0','"+eml+"','9089');"
                                    db.execute(s)                           #inserting in main enc file
                                    db.commit()
                                    msg='Message Created!!'
                                    msg1=usd
                                    usd=''
                                    del request.session['Dnc']
                                    noti=reverse1(q)
                                    request.session['Dnc']=[]
                                    request.session['Dnc']+=[t]
                                    return render(request,'END/Encrypt.html',{
                                    'user':usn,
                                    'msg1':msg1,
                                    'form':Enc(),
                                    'noti':noti,
                                    'om':t
                                    })
                                else:
                                    t=1
                                    del request.session['Dnc']
                                    noti=reverse1(q)
                                    request.session['Dnc']=[]
                                    request.session['Dnc']+=[t]
                                    msg='Invalid Input!!'
                                    return render(request,'END/Encrypt.html',{
                                    'user':usn,
                                    'form':Enc(),
                                    'msg':msg,
                                    'noti':noti,
                                    'om':t
                                    })
                        elif w[1]=='4':
                            q=request.session['End']
                            fln,de,notif,eml=userfiles(q)
                            enc, key, tim, timeec, txt=encrptxt(w[2])
                            t=1
                            mez=''
                            usd='Random Guest'
                            ud=str(uuid.uuid1())
                            ti=str(datetime.date.today())
                            s="INSERT INTO "+fln+" (uuide,timeec,mang,emld,acc) VALUES ('"+ud+"','"+timeec+"','ur1','"+usd+"','9089');"
                            db.execute(s)                            #inserting into users enc file
                            db.commit()
                            s="INSERT INTO ur1 (uuidu,enct,enck,enctm,time,encc,acc) VALUES ('"+ud+"','"+enc+"','"+key+"','"+tim+"','"+ti+"','"+eml+"','9089');"
                            db.execute(s)                           #inserting in main enc file
                            db.commit()
                            msg='Message Created!!'
                            msg1='ID: '+ud
                            usd=''
                            del request.session['Dnc']
                            request.session['Dnc']=[]
                            request.session['Dnc']+=[t]
                            noti=reverse1(q)
                            return render(request,'END/Encrypt.html',{
                            'user':usn,
                            'msg1':msg1,
                            'form':Enc(),
                            'noti':noti,
                            'om':t
                            })
                        elif w[1]=='':
                            t=1
                            msg='Error'
                            del request.session['Dnc']
                            noti=reverse1(q)
                            return render(request,'END/Encrypt.html',{
                            'user':usn,
                            'msg':msg,
                            'form':Enc(),
                            'noti':noti,
                            'om':t
                            })
                        else:
                            om=1
                            del request.session['Dnc']
                            noti=reverse1(q)
                            msg='Message Not Created'
                            return render(request,'END/Encrypt.html',{
                            'user':usn,
                            'form':Enc(),
                            'msg':msg,
                            'noti':noti,
                            'om':om
                            })
                    elif r==False:
                        del request.session['Dnc']
                        om=1
                        msg='Message Not Created'
                        noti=reverse1(q)
                        return render(request,'END/Encrypt.html',{
                        'user':usn,
                        'form':Enc(),
                        'msg':msg,
                        'noti':noti,
                        'om':om
                        })
            else:
                t=1
                noti=reverse1(q)
                if "Dnc" in request.session:
                    del request.session["Dnc"]
                request.session['Dnc']=[]
                request.session['Dnc']+=[t]
                return render(request,'END/Encrypt.html',{
                'user':usn,
                'form':Enc(),
                'noti':noti,
                'om':t
                })
        else:
            s="UPDATE SG1 SET logc = 'no' WHERE uuidu='"+q[0]+"';"
            del request.session['End']
            del request.session['Dnc']
            ran=''
            q=[]
            usn=''
            return render(request,'END/error.html')
    except:
        if "Dnc" in request.session:
            del request.session['Dnc']
        if "Enc" in request.session:
            del request.session['Enc']
        if "End" in request.session:
            q=request.session['End']
            s=''
            s +="UPDATE sg1 SET Logc='no'"
            s +=" "
            s +="WHERE"
            s +=" "
            s +="uuidu='"+q[0]+"';"
            pw=db.execute(s)
            db.commit()
            ran='no'
            q=''
            de=''
            fln=''
            eml=''
            notif=''
            emle=''
            usn=''
            ran=''
            q=[]
            usn=''
            del request.session['End']
            return render(request,'END/error.html')

def decrypt(request,rname):
    try:
        q=request.session['End']
        if "Enc" not in request.session:
            request.session['Enc']=[]
        w=request.session['Enc']
        s="SELECT logc FROM SG1 WHERE uuidu='"+q[0]+"';"
        pw=db.execute(s).fetchall()
        rn=cutter(pw)
        s="SELECT usn FROM SG1 WHERE uuidu='"+q[0]+"';"
        pw=db.execute(s).fetchall()
        usn=cutter(pw)
        if rn==q[1] and rname==usn:
            try:
                if request.method=='POST':
                    w=request.session['Enc']
                    fln,de,notif,eml=userfiles(q)
                    if w[0] == 0 :
                        sec=request.POST.get('dec')
                        w+=[sec]
                        s="SELECT mang FROM "+de+" WHERE uuide='"+w[1]+"';"
                        pw=db.execute(s).fetchall()
                        mag=cutter(pw)
                        w+=[mag]
                    elif w[0]==[1]:
                        form=secu(request.POST)
                    if not w[1] == False or form.is_valid():
                        if w[2]=='uud1':
                            decto,emle=decryptxt(w[1],w[2],de,eml)
                            o=2
                            w[0]=[o]
                            kl=o
                            noti=reverse1(q)
                            s="SELECT emle,uuide FROM "+de+" WHERE acc='9089';"
                            pw=db.execute(s).fetchall()                 #getting those messages which are not seen
                            sec=''
                            del request.session['Enc']
                            return render(request,'END/decfnl.html',{
                                'dec':pw,
                                'noti':noti,
                                'user':usn,
                                'i':emle,
                                'j':decto,
                                'o':kl
                            })
                        elif w[2]=='uus1':
                            if w[0] == 0:
                                o=1
                                w[0]=[o]
                                request.session['Enc']=w
                                kl=o
                                noti=reverse1(q)
                                s="SELECT emle,uuide FROM "+de+" WHERE acc='9089';"
                                pw=db.execute(s).fetchall()                 #getting those messages which are not seen
                                return render(request,'END/decfnl.html',{
                                    'dec':pw,
                                    'noti':noti,
                                    'user':usn,
                                    'form1':secu(),
                                    'o':kl
                                })
                            elif w[0] == [1]:
                                o=0
                                w[0]=[o]
                                if form.is_valid():
                                    ke=form.cleaned_data['Key']
                                    s="SELECT sa FROM uus1 WHERE uuidu='"+w[1]+"';"
                                    pw=db.execute(s).fetchall()         #getting keys
                                    sa=cutter(pw)
                                    bol= sa==ke                     #comparing security answers/keys
                                    if bol:
                                        kl=2
                                        fln,de,notif,eml=userfiles(q)
                                        decto,emle=decryptxt(w[1],w[2],de,eml)
                                        noti=reverse1(q)
                                        s="SELECT emle,uuide FROM "+de+" WHERE acc='9089';"
                                        pw=db.execute(s).fetchall()                 #getting those messages which are not seen
                                        mag=''
                                        del request.session['Enc']
                                        return render(request,'END/decfnl.html',{
                                            'dec':pw,
                                            'noti':noti,
                                            'user':usn,
                                            'i':emle,
                                            'j':decto,
                                            'o':kl
                                        })
                                    else:
                                        o=0
                                        w[0]=[o]
                                        kl=3
                                        msg='Invalid key!'
                                        noti=reverse1(q)
                                        s="SELECT emle,uuide FROM "+de+" WHERE acc='9089';"
                                        pw=db.execute(s).fetchall()                 #getting those messages which are not seen
                                        del request.session['Enc']
                                        return render(request,'END/decfnl.html',{
                                            'dec':pw,
                                            'noti':noti,
                                            'user':usn,
                                            'msg':msg,
                                            'o':kl
                                        })
                                else:
                                    o=0
                                    w[0]=[o]
                                    kl=3
                                    msg='Invalid Input!'
                                    noti=reverse1(q)
                                    s="SELECT emle,uuide FROM "+de+" WHERE acc='9089';"
                                    pw=db.execute(s).fetchall()                 #getting those messages which are not seen
                                    del request.session['Enc']
                                    return render(request,'END/decfnl.html',{
                                        'dec':pw,
                                        'noti':noti,
                                        'user':usn,
                                        'msg':msg,
                                        'o':kl
                                    })
                        else:
                            noti=reverse1(q)
                            s="SELECT emle,uuide FROM "+de+" WHERE acc='9089';"
                            pw=db.execute(s).fetchall()                 #getting those messages which are not seen
                            o=0
                            w[0]=[o]
                            w=[]
                            request.session['Enc']=w
                            del request.session['Enc']
                            return render(request,'END/decfnl.html',{
                                'dec':pw,
                                'noti':noti,
                                'user':usn,
                                'o':o
                            })
                    else:
                        noti=reverse1(q)
                        o=0
                        w[0]=[o]
                        w=[]
                        request.session['Enc']=w
                        del request.session['Enc']
                        s="SELECT emle,uuide FROM "+de+" WHERE acc='9089';"
                        pw=db.execute(s).fetchall()                 #getting those messages which are not seen
                        return render(request,'END/decfnl.html',{
                            'dec':pw,
                            'noti':noti,
                            'user':usn,
                            'o':o
                        })
                else:
                    del request.session['Enc']
                    fln,de,notif,eml=userfiles(q)
                    noti=reverse1(q)
                    s="SELECT emle,uuide FROM "+de+" WHERE acc='9089';"
                    pw=db.execute(s).fetchall()                 #getting those messages which are not seen
                    o=0
                    w=[o]
                    request.session['Enc']=[]
                    request.session['Enc']=w
                    return render(request,'END/decfnl.html',{
                        'dec':pw,
                        'noti':noti,
                        'user':usn,
                        'o':o
                    })
            except:
                s="UPDATE SG1 SET logc = 'no' WHERE uuidu='"+q[0]+"';"
                del request.session['End']
                del request.session['Enc']
                ran=''
                q=[]
                w=[]
                usn=''
                return render(request,'END/error.html')
        else:
            s="UPDATE SG1 SET logc = 'no' WHERE uuidu='"+q[0]+"';"
            del request.session['End']
            del request.session['Enc']
            ran=''
            q=[]
            w=[]
            usn=''
            return render(request,'END/error.html')
    except:
        if "Dnc" in request.session:
            del request.session['Dnc']
        if "Enc" in request.session:
            del request.session['Enc']
        if "End" in request.session:
            q=request.session['End']
            s=''
            s +="UPDATE sg1 SET Logc='no'"
            s +=" "
            s +="WHERE"
            s +=" "
            s +="uuidu='"+q[0]+"';"
            pw=db.execute(s)
            db.commit()
            ran='no'
            q=''
            de=''
            fln=''
            eml=''
            notif=''
            emle=''
            usn=''
            ran=''
            q=[]
            usn=''
            del request.session['End']
            return render(request,'END/error.html')

def manage(request,rname):
    try:
        q=request.session['End']
        s="SELECT logc FROM SG1 WHERE uuidu='"+q[0]+"';"
        pw=db.execute(s).fetchall()
        rn=cutter(pw)
        s="SELECT usn FROM SG1 WHERE uuidu='"+q[0]+"';"
        pw=db.execute(s).fetchall()
        usn=cutter(pw)
        if rn==q[1] or rname==usn:
            fln,de,notif,eml=userfiles(q)
            s="SELECT emld,timeec FROM "+fln+";"
            pw=db.execute(s).fetchall()
            noti=reverse1(q)
            return render(request,'END/mng.html',{
                'noti':noti,
                'user':usn,
                'dec':pw,
            })
        else:
            s="UPDATE SG1 SET logc = 'no' WHERE uuidu='"+q[0]+"';"
            del request.session['End']
            ran=''
            q=[]
            usn=''
            return render(request,'END/error.html')
    except:
        if "Dnc" in request.session:
            del request.session['Dnc']
        if "Enc" in request.session:
            del request.session['Enc']
        if "End" in request.session:
            q=request.session['End']
            s=''
            s +="UPDATE sg1 SET Logc='no'"
            s +=" "
            s +="WHERE"
            s +=" "
            s +="uuidu='"+q[0]+"';"
            pw=db.execute(s)
            db.commit()
            ran='no'
            q=''
            de=''
            fln=''
            eml=''
            notif=''
            emle=''
            usn=''
            ran=''
            q=[]
            usn=''
            del request.session['End']
            return render(request,'END/error.html')
        else:
            ran='no'
            q=''
            de=''
            fln=''
            eml=''
            notif=''
            emle=''
            usn=''
            ran=''
            q=[]
            usn=''
            return render(request,'END/logout.html')

def about(request,rname):
    try:
        q=request.session['End']
        s="SELECT logc FROM SG1 WHERE uuidu='"+q[0]+"';"
        pw=db.execute(s).fetchall()
        rn=cutter(pw)
        s="SELECT usn FROM SG1 WHERE uuidu='"+q[0]+"';"
        pw=db.execute(s).fetchall()
        usn=cutter(pw)
        if rn==q[1] and rname==usn:
            return render(request,'END/aboutfinal.html',{
                'user':usn,
            })
        else:
            s="UPDATE SG1 SET logc = 'no' WHERE uuidu='"+q[0]+"';"
            del request.session['End']
            ran=''
            q=[]
            usn=''
            return render(request,'END/error.html')
    except:
        if "Dnc" in request.session:
            del request.session['Dnc']
        if "Enc" in request.session:
            del request.session['Enc']
        if "End" in request.session:
            q=request.session['End']
            s=''
            s +="UPDATE sg1 SET Logc='no'"
            s +=" "
            s +="WHERE"
            s +=" "
            s +="uuidu='"+q[0]+"';"
            pw=db.execute(s)
            db.commit()
            ran='no'
            q=''
            de=''
            fln=''
            eml=''
            notif=''
            emle=''
            usn=''
            ran=''
            q=[]
            usn=''
            del request.session['End']
            return render(request,'END/error.html')
        else:
            ran='no'
            q=''
            de=''
            fln=''
            eml=''
            notif=''
            emle=''
            usn=''
            ran=''
            q=[]
            usn=''
            return render(request,'END/logout.html')

def notification(request,rname):
    try:
        q=request.session['End']
        if "Dnc" not in request.session:
            request.session['Dnc']=[]
        w=request.session['Dnc']
        s="SELECT logc FROM SG1 WHERE uuidu='"+q[0]+"';"
        pw=db.execute(s).fetchall()
        rn=cutter(pw)
        s="SELECT usn FROM SG1 WHERE uuidu='"+q[0]+"';"
        pw=db.execute(s).fetchall()
        usn=cutter(pw)
        if rn==q[1] and rname==usn:
            noti=reverse1(q)
            return render(request,'END/notif.html',{
                'user':usn,
                'noti':noti,
            })
        else:
            s="UPDATE SG1 SET logc = 'no' WHERE uuidu='"+q[0]+"';"
            del request.session['End']
            if "Dnc" in request.session:
                del request.session['Dnc']
            if "Enc" in request.session:
                del request.session['Enc']
            ran=''
            q=[]
            usn=''
            return render(request,'END/error.html')
    except:
        if "Dnc" in request.session:
            del request.session['Dnc']
        if "Enc" in request.session:
            del request.session['Enc']
        if "End" in request.session:
            q=request.session['End']
            s=''
            s +="UPDATE sg1 SET Logc='no'"
            s +=" "
            s +="WHERE"
            s +=" "
            s +="uuidu='"+q[0]+"';"
            pw=db.execute(s)
            db.commit()
            ran='no'
            q=''
            de=''
            fln=''
            eml=''
            notif=''
            emle=''
            usn=''
            ran=''
            q=[]
            usn=''
            del request.session['End']
            return render(request,'END/error.html')
        else:
            ran='no'
            q=''
            de=''
            fln=''
            eml=''
            notif=''
            emle=''
            usn=''
            ran=''
            q=[]
            usn=''
            return render(request,'END/logout.html')

def verify(request):
    try:
        q=request.session['for']
        if request.method=="POST":
            form=verif(request.POST)
            if form.is_valid():
                ver=form.cleaned_data['verif']
                s="SELECT vcode FROM SG1 WHERE eml='"+q[0]+"';"
                pw=db.execute(s).fetchall()
                pw=emlcutter(pw)
                if ver==pw:
                    r=1
                    msg=':) Email Verified!'
                    s="UPDATE SG1 SET verify='ED' WHERE eml='"+q[0]+"';"
                    db.execute(s)
                    db.commit()
                    s="SELECT uuidu FROM SG1 WHERE eml='"+q[0]+"';"
                    pw=db.execute(s).fetchall()
                    ud=cutter(pw)
                    s="SELECT usn FROM SG1 WHERE uuidu='"+ud+"';"
                    pw=db.execute(s).fetchall()
                    us=cutter(pw)
                    io=0
                    jo=len(us)
                    sam=''
                    for io in range(jo):
                        if us[io]==' ':
                            us[io]
                        else:
                            sam=sam+us[io]
                    fn=''
                    fn=str(random.randint(11111,99999))                  #file name decleration
                    s="INSERT INTO FN1 (uuidu,eml,enc,nott,dect) "         #entering file name to the fn1 file 
                    s+="VALUES ('"+ud+"','"+q[0]+"','"+'End'+sam+fn+'enct'+"','"+'End'+sam+fn+'nott'+"','"+'End'+sam+fn+'dect'+"');"
                    db.execute(s)
                    db.commit()
                    s="CREATE TABLE "+'End'+sam+fn+'enct'+"( "
                    s+="uuide varchar not null unique,"
                    s+="timeec varchar not null,"
                    s+="mang varchar not null ,"
                    s+="timedc varchar,"
                    s+="emld varchar,"
                    s+="acc varchar);"
                    db.execute(s)
                    db.commit()
                    s="CREATE TABLE "+'End'+sam+fn+'nott'+"( "
                    s+="id serial primary key,"
                    s+="msg varchar not null,"
                    s+="status varchar);"
                    db.execute(s)
                    db.commit()
                    s="CREATE TABLE "+'End'+sam+fn+'dect'+"( "
                    s+="uuide varchar not null unique,"
                    s+="timedc varchar ,"
                    s+="mang varchar not null ,"
                    s+="emle varchar not null,"
                    s+="acc varchar);"
                    db.execute(s)
                    db.commit()
                    if 'for' in request.session:
                        del request.session['for']
                    return render(request,"END/email.html",{
                        'msg':msg,
                        'om':r
                    })
                else:
                    r=1
                    msg=':) Email Not Verified!'
                    if 'for' in request.session:
                        del request.session['for']
                    return render(request,"END/email.html",{
                        'msg':msg,
                        'om':r
                    })
        else:
            r=0
            return render(request,"END/email.html",{
                'form':verif(),
                'om':r
            })
    except:
        if "End" in request.session:
            del request.session['End']
        msg='Error!!'
        return render(request,'END/error.html')

def logout(request):
    if "Dnc" in request.session:
        del request.session['Dnc']
    if "Enc" in request.session:
        del request.session['Enc']
    if "End" in request.session:
        q=request.session['End']
        s=''
        s +="UPDATE sg1 SET Logc='no'"
        s +=" "
        s +="WHERE"
        s +=" "
        s +="uuidu='"+q[0]+"';"
        pw=db.execute(s)
        db.commit()
        ran='no'
        q=''
        de=''
        fln=''
        eml=''
        notif=''
        emle=''
        usn=''
        ran=''
        q=[]
        usn=''
        del request.session['End']
        return render(request,'END/logout.html')
    else:
        ran='no'
        q=''
        de=''
        fln=''
        eml=''
        notif=''
        emle=''
        usn=''
        ran=''
        q=[]
        usn=''
        return render(request,'END/logout.html')

def feed(request):
    return render(request,'END/aboutlogin.html')

def feedu(request,rname):
    try:
        q=request.session['End']
        if "Dnc" not in request.session:
            request.session['Dnc']=[]
        w=request.session['Dnc']
        s="SELECT logc FROM SG1 WHERE uuidu='"+q[0]+"';"
        pw=db.execute(s).fetchall()
        rn=cutter(pw)
        s="SELECT usn FROM SG1 WHERE uuidu='"+q[0]+"';"
        pw=db.execute(s).fetchall()
        usn=cutter(pw)
        if rn==q[1] and rname==usn:
            if request.method=="POST":
                form=Feed(request.POST)
                if form.is_valid():
                    feed=form.cleaned_data['Feed']
                    s="SELECT eml FROM SG1 WHERE uuidu='"+q[0]+"';"
                    pw=db.execute(s).fetchall()
                    eml=cutter(pw)
                    uuidu=q[0]
                    s="INSERT INTO feed (uuidu,email,feedback) VALUEs ('"+uuidu+"','"+eml+"','"+feed+"');"
                    db.execute(s)
                    db.commit()
                    o=1
                    msg='Thank you for your valuable feedback :)'
                    return render(request,"END/feedback.html",{
                        'form':Feed(),
                        'msg1':msg,
                        'o':o,
                        'user':usn
                    })
                else:
                    o=0
                    msg='Invalid Input!!'
                    return render(request,"END/feedback.html",{
                        'form':Feed(),
                        'msg':msg,
                        'o':o,
                        'user':usn
                    })
            else:
                o=0
                return render(request,"END/feedback.html",{
                    'form':Feed(),
                    'o':o,
                    'user':usn
                })
        else:
            s="UPDATE SG1 SET logc = 'no' WHERE uuidu='"+q[0]+"';"
            del request.session['End']
            if "Dnc" in request.session:
                del request.session['Dnc']
            if "Enc" in request.session:
                del request.session['Enc']
            ran=''
            q=[]
            usn=''
            return render(request,'END/error.html')
    except:
        s="UPDATE SG1 SET logc = 'no' WHERE uuidu='"+q[0]+"';"
        del request.session['End']
        if "Dnc" in request.session:
            del request.session['Dnc']
        if "Enc" in request.session:
            del request.session['Enc']
        ran=''
        q=[]
        usn=''
        return render(request,'END/error.html')

def guest(request):
    try:
        if request.method == 'POST':
            form=gue(request.POST)
            form1=gueu(request.POST)
            if form.is_valid() and form1.is_valid():
                idg=form.cleaned_data['Guest_ID']
                ke=form1.cleaned_data['Key']
                s="SELECT sa FROM ug1 WHERE gid='"+idg+"';"
                pw=db.execute(s).fetchall()
                s="SELECT acc FROM ug1 WHERE gid='"+idg+"';"
                wp=db.execute(s).fetchall()
                wp=cutter(wp)
                io=emlcutter(wp)
                if pw==[]:
                    msg='Guest id not found!!'
                    return render(request,'END/guest.html',{
                        'msg':msg,
                        'form':gue(),
                        'form1':gueu()
                    })
                elif wp=='9862' or io=='9862':
                    msg='Guest id expired!!'
                    return render(request,'END/guest.html',{
                        'msg':msg,
                        'form':gue(),
                        'form1':gueu()
                    })
                else:
                    key=cutter(pw)
                    if ke==key:
                        mag='ug1'
                        s="SELECT uuidu FROM ug1 WHERE gid='"+idg+"' AND sa='"+ke+"';"
                        pw=db.execute(s).fetchall()         #getting the uuide of the enc
                        uid=cutter(pw)
                        de=''
                        eml=''
                        dec,emle=rgdecryptxt(uid,mag,de,eml)
                        s="SELECT encc FROM ug1 WHERE gid='"+idg+"' AND sa='"+ke+"';"
                        pw=db.execute(s).fetchall()     #getting the email of the creator
                        eml=cutter(pw)
                        s="UPDATE "+mag+" SET acc='9862' WHERE uuidu='"+uid+"';"
                        db.execute(s)                   #updating acc status in the ug1 file
                        db.commit()
                        s="SELECT enc FROM fn1 WHERE eml='"+eml+"';"
                        pw=db.execute(s).fetchall()
                        em=cutter(pw)                  #getting the name of enc file of the creator
                        s="UPDATE "+em+" SET acc='9862' WHERE uuide='"+uid+"';"
                        db.execute(s)                   #updating the creators enc file
                        db.commit()
                        no=''
                        for i in range(len(em)-4):
                            no=no+em[i]
                        no=no+'nott'
                        s="INSERT INTO "+no+" (msg,status) VALUES ('Message decrypted by "+idg+".','9089');"
                        db.execute(s)                           #updating the creators notification
                        db.commit()
                        ok=1
                        msg1='Message:'+dec
                        return render(request,'END/guest.html',{
                            'msg':msg1,
                            'form':gue(),
                            'form1':gueu(),
                            'ok':ok
                        })
                    elif ke != key:
                        s="SELECT wrn FROM ug1 WHERE gid='"+idg+"';"
                        pw=db.execute(s).fetchall()         #getting the wrn of the enc
                        wrn=cutter(pw)
                        if wrn=='3':
                            s="SELECT uuideu FROM ug1 WHERE gid='"+idg+"';"
                            pw=db.execute(s).fetchall()         #getting the uuide of the enc
                            uid=cutter(pw)
                            s="UPDATE ug1 SET acc='9862' WHERE uuidu='"+uid+"';"
                            db.execute(s)                   #updating acc status in the ug1 file
                            s="SELECT encc FROM ug1 WHERE gid='"+idg+"';"
                            pw=db.execute(s).fetchall()     #getting the email of the creator
                            eml=cutter(pw)
                            s="SELECT enc FROM fn1 WHERE eml='"+eml+"';"
                            pw=db.execute(s).fetchall()
                            eml=cutter(pw)                  #getting the name of enc file of the creator
                            s="UPDATE "+eml+" SET acc='9862' WHERE uuide='"+uid+"';"
                            db.execute(s)                   #updating the creators enc file
                            for i in range(len(en)-4):
                                no=no+en[i]
                            no=no+'nott'
                            s="INSERT INTO "+no+" (msg,status) VALUES ('"+idg+" has been blocked.','9089');"
                            db.execute(s)                           #updating the creators notification
                            msg='Guest Id has been Blocked!!'
                            ok=0
                            return render(request,'END/guest.html',{
                                'msg':msg,
                                'form':gue(),
                                'ok':ok,
                                'form1':gueu()
                            })
                        else:
                            ok=0
                            wr=int(wrn)
                            wr=wr+1
                            wrn=str(wrn)
                            s="UPDATE ug1 SET wrn='"+wrn+"' WHERE gid='"+idg+"';"
                            db.execute(s)
                            msg='Invalid Key!!'
                            return render(request,'END/guest.html',{
                                'msg':msg,
                                'form':gue(),
                                'ok':ok,
                                'form1':gueu()
                            })
            else:
                ok=0
                msg='Invalid Input!!'
                return render(request,'END/guest.html',{
                    'msg':msg,
                    'form':gue(),
                    'form1':gueu()
                })
        else:
            ok=2
            return render(request,'END/guest.html',{
                'form':gue(),
                'form1':gueu(),
                'ok':ok
            })
    except:
        if "End" in request.session:
            del request.session['End']
        msg='Error!!'
        return render(request,'END/error.html')

def randomguest(request):
    try:
        if request.method=='POST':
            form=rad(request.POST)
            if form.is_valid():
                man=form.cleaned_data['Encrypted_Message']
                s="Select acc FROM ur1 WHERE uuidu='"+man+"';"
                pw=db.execute(s).fetchall()
                if pw == []:
                    msg=':(   Invalid Input!!'
                    oka=2
                    return render(request,'END/random.html',{
                        'msg':msg,
                        'form':rad(),
                        'oka':oka
                    })
                elif pw == [('9862',)]:
                    msg=':(   Message Expired!!'
                    oka=2
                    return render(request,'END/random.html',{
                        'msg':msg,
                        'form':rad(),
                        'oka':oka
                    })
                else:
                    s="Select time FROM ur1 WHERE uuidu='"+man+"';"
                    pw=db.execute(s).fetchall()
                    tim=cutter(pw)
                    td=str(datetime.date.today())
                    if td>tim:
                        s="Select encc FROM ur1 WHERE uuidu='"+man+"';"
                        pw=db.execute(s).fetchall()
                        eml=cutter(pw)
                        s="UPDATE ur1 SET acc='9862' WHERE uuidu='"+man+"';"
                        db.execute(s)                   #updating acc status in the ug1 file
                        db.commit()
                        s="UPDATE "+eml+" SET acc='9862' WHERE uuide='"+man+"';"
                        db.execute(s)                   #updating the creators enc file
                        db.commit()
                        msg=':(   Message Expired!!'
                        oka=2
                        return render(request,'END/random.html',{
                            'msg':msg,
                            'form':rad(),
                            'oka':oka
                        })
                    elif td==tim:
                        s="Select enct FROM ur1 WHERE uuidu='"+man+"';"
                        pw=db.execute(s).fetchall()
                        enct=cutter(pw)
                        mag='ur1'
                        de=''
                        eml=''
                        dec,emle=rgdecryptxt(man,mag,de,eml)
                        s="SELECT encc FROM ur1 WHERE uuidu='"+man+"';"
                        pw=db.execute(s).fetchall()     #getting the email of the creator
                        eml=cutter(pw)
                        s="SELECT enc FROM fn1 WHERE eml='"+eml+"';"
                        pw=db.execute(s).fetchall()         #getting the enc file name of the creator
                        eml=cutter(pw)
                        oka=1
                        return render(request,'END/random.html',{
                            'msg1':dec,
                            'form':rad(),
                            'oka':oka
                        })
                
            else:
                oka=2
                msg=':(   Invalid Input!'
                return render(request,'END/random.html',{
                    'msg':msg,
                    'form':rad(),
                    'oka':oka
                })
        else:
            oka=2
            return render(request,'END/random.html',{
                'form':rad(),
                'oka':oka
            })
    except:
        if "End" in request.session:
            del request.session['End']
        msg='Error!!'
        return render(request,'END/error.html')

def forgot(request):
    try:
        if "fog" not in request.session:
            request.session["fog"]=[]
        w=request.session["fog"]
        if request.method == 'POST':
            if w[0]==1:
                form=forg(request.POST)
            elif w[0]==2:
                form=ans(request.POST)
            elif w[0]==3:
                form=pasm(request.POST)
            else:
                msg=':( Try Again!!'
                uid=''
                del request.session["fog"]
                request.session["fog"]=[]
                f=1
                request.session["fog"]+=[f]
                return render(request,'END/forgot.html',{
                    'form':forg(),
                    'f':f,
                    'msg':msg
                })
            if form.is_valid():
                if w[0]==1:
                    eml=form.cleaned_data['Email']
                    s="SELECT uuidu FROM  SG1 WHERE "
                    s +="eml='"+eml+"';"
                    pw=db.execute(s).fetchall()
                    if pw == []:
                        f=1
                        msg='No Such User exist!!'
                        return render(request,'END/forgot.html',{
                            'form':forg(),
                            'f':f
                        })
                    uid=cutter(pw)
                    w+=[uid]
                    emvf=str(random.randint(111111,999999))
                    s="UPDATE sg1 SET vcode = "+emvf+" WHERE "
                    s +="uuidu='"+uid+"';"
                    pw=db.execute(s)
                    db.commit()
                    send_mail("Reset Password [EnD].","Your EnD verification code |"+emvf+"|.","encryptndecrypt@gmail.com",[eml],    # This is a list
                        fail_silently = False     # Set this to False so that you will be noticed in any exception raised
                        )
                    f=2
                    w[0]=f
                    request.session["fog"]=w
                    return render(request,'END/forgot.html',{
                        'f':f,
                        'sa':ans()
                    })
                elif w[0]==2:
                    sae=form.cleaned_data['Answer']
                    uid=str(w[1])
                    s="SELECT vcode FROM  sg1 WHERE "
                    s +="uuidu='"+uid+"';"
                    pw=db.execute(s).fetchall()
                    sa=cutter(pw)
                    if sae==sa:
                        f=3
                        w[0]=f
                        uid=''
                        w[1]=[uid]
                        request.session["fog"]=w
                        msg='User Verified Enter New Password'
                        return render(request,'END/forgot.html',{
                            'f':f,
                            'sa':pasm(),
                            'msg':msg
                        })
                    else:
                        msg='Invalid Code!!'
                        uid=''
                        del request.session["fog"]
                        request.session["fog"]=[]
                        f=1
                        request.session["fog"]+=[f]
                        return render(request,'END/forgot.html',{
                            'form':forg(),
                            'f':f,
                            'msg':msg
                        })
                elif w[0]==3:
                    pas=form.cleaned_data['Password']
                    pas=hash(pas)
                    uid=str(w[1])
                    s="UPDATE p1 SET pwd='"+pas+"' WHERE uuidu='"+uid+"';"
                    db.execute(s)
                    db.commit()
                    msg='Password Changed!!'
                    f=1
                    uid=''
                    del request.session["fog"]
                    request.session["fog"]=[]
                    f=1
                    request.session["fog"]+=[f]
                    f=12
                    return render(request,'END/forgot.html',{
                        'msg':msg,
                        'f':f
                    })
                else:
                    msg=':( Try Again!!'
                    uid=''
                    del request.session["fog"]
                    request.session["fog"]=[]
                    f=1
                    request.session["fog"]+=[f]
                    return render(request,'END/forgot.html',{
                        'form':forg(),
                        'f':f,
                        'msg':msg
                    })
            else:
                msg=':( Try Again!!'
                uid=''
                del request.session["fog"]
                request.session["fog"]=[]
                f=1
                request.session["fog"]+=[f]
                return render(request,'END/forgot.html',{
                    'form':forg(),
                    'f':f,
                    'msg':msg
                })
        else:
            if "fog" in request.session:
                del request.session["fog"]
            request.session["fog"]=[]
            f=1
            request.session["fog"]+=[f]
            uid=''
            return render(request,'END/forgot.html',{
                'form':forg(),
                'f':f
            })
    except:
        if "End" in request.session:
            del request.session['End']
        if "fog" in request.session:
            del request.session['fog']
        msg='Error!!'
        return render(request,'END/error.html')

def username(request,rname):
    try:
        q=request.session['End']
        s="SELECT logc FROM SG1 WHERE uuidu='"+q[0]+"';"
        pw=db.execute(s).fetchall()
        rn=cutter(pw)
        s="SELECT usn FROM SG1 WHERE uuidu='"+q[0]+"';"
        pw=db.execute(s).fetchall()
        usn=cutter(pw)
        if rn==q[1] and rname==usn:
            if request.method=="POST":
                s="UPDATE SG1 SET seal='9862' WHERE uuidu='"+q[0]+"';"
                db.execute(s)
                db.commit()
                if "Dnc" in request.session:
                    del request.session['Dnc']
                if "Enc" in request.session:
                    del request.session['Enc']
                if "End" in request.session:
                    q=request.session['End']
                    s=''
                    s +="UPDATE sg1 SET Logc='no'"
                    s +=" "
                    s +="WHERE"
                    s +=" "
                    s +="uuidu='"+q[0]+"';"
                    pw=db.execute(s)
                    db.commit()
                    ran='no'
                    q=''
                    de=''
                    fln=''
                    eml=''
                    notif=''
                    emle=''
                    usn=''
                    ran=''
                    q=[]
                    usn=''
                    del request.session['End']
                    return render(request,'END/deactivate.html')
            else:
                s="SELECT logn FROM SG1 WHERE uuidu='"+q[0]+"';"
                pw=db.execute(s).fetchall()
                log=cutter(pw)
                s="SELECT eml FROM SG1 WHERE uuidu='"+q[0]+"';"
                pw=db.execute(s).fetchall()
                eml=cutter(pw)
                return render(request,'END/Settings.html',{
                    'user':usn,
                    'log':log,
                    'eml':eml
                })
        else:
            s="UPDATE SG1 SET logc = 'no' WHERE uuidu='"+q[0]+"';"
            del request.session['End']
            ran=''
            q=[]
            usn=''
            return render(request,'END/error.html')
    except:
        if "Dnc" in request.session:
            del request.session['Dnc']
        if "Enc" in request.session:
            del request.session['Enc']
        if "End" in request.session:
            q=request.session['End']
            s=''
            s +="UPDATE sg1 SET Logc='no'"
            s +=" "
            s +="WHERE"
            s +=" "
            s +="uuidu='"+q[0]+"';"
            pw=db.execute(s)
            db.commit()
            ran='no'
            q=''
            de=''
            fln=''
            eml=''
            notif=''
            emle=''
            usn=''
            ran=''
            q=[]
            usn=''
            del request.session['End']
            return render(request,'END/error.html')
        else:
            ran='no'
            q=''
            de=''
            fln=''
            eml=''
            notif=''
            emle=''
            usn=''
            ran=''
            q=[]
            usn=''
            return render(request,'END/logout.html')

def hash(nam):                          #hash of any text 
    pd=str(uuid.uuid5(uuid.NAMESPACE_X500,nam))
    return pd

def encrptxt(text):                     #encrypt text
    e=0
    y=0
    z=len(text)
    n=''
    g=0
    t=0
    enc=''
    a=''
    txt=''
    timeec=str(datetime.date.today())
    tik=str(datetime.datetime.now())
    s=tik
    for i in range(len(s)):
	    if i>13 and i<19:
		    if i!=16:
			    n=n+s[i]
    for i in range(2):
        t=t*60
        s=n[i+g]+n[i+1+g]
        g=g+1
        t=int(s)+t
    tim=str(t)                   #time for key 
    a=''
    key=''
    for i in text:
        sm=0
        k=0
        inc=1
        d=ord(i)
        e=t/127
        g,h=divmod(e,1)
        g=int(round(g))
        g=g*127
        t=(t-g)+y
        if (d%2)==0:
            d=d+t
            if d>=127:
                while d>=127:
                    d=d-127
                    k=k+1
                while d<40:
                    d=d+40
                    sm=sm+1
                key=key+'a'+str(k)+str(sm)
                a=chr(d)
                enc=enc+a
            elif d<127:
                while d<40:
                        d=d+40
                        sm=sm+1
                k=1
                key=key+'b'+str(k)+str(sm)
                a=chr(d)
                enc=enc+a
        elif (d%2)!=0:
            d=d-t
            if d<0:
                while d<0:
                    d=d+127
                    k=k+1
                while d<40:
                    d=d+40
                    sm=sm+1
                key=key+'c'+str(k)+str(sm)
                a=chr(d)
                enc=enc+a
            elif d>0:
                while d<40:
                    d=d+40
                    sm=sm+1
                k=1
                key=key+'d'+str(k)+str(sm)
                a=chr(d)
                enc=enc+a
        y=y+1
    mn=len(enc)
    if z==mn:
        txt='True'
        return enc,key,tim,timeec,txt
    else:
        txt='False'
        return enc,key,tim,timeec,txt

def decryptxt(dect,mag,de,eml):
    div=''       #divisional block 
    loop=0       #no of times to loop
    num=0        #no of times to increase time
    a=0          #ascii no of each character
    enc=''       #character representation of ascii
    dec=''       #decrypted text
    y=0          #second increment
    fn=''
    emle=''
    s="SELECT enct FROM "+mag+" WHERE uuidu='"+dect+"';"
    pw=db.execute(s).fetchall()
    enct=cutter(pw)
    s="SELECT enck FROM "+mag+" WHERE uuidu='"+dect+"';"
    pw=db.execute(s).fetchall()
    enck=cutter(pw)
    s="SELECT enctm FROM "+mag+" WHERE uuidu='"+dect+"';"
    pw=db.execute(s).fetchall()
    enctme=cutter(pw)
    enctm=int(enctme)
    orm=1
    global eve
    eve=0
    for i in enct:
        s=i
        if len(s)>1:
            h=len(s)-1
            a=int(s[h])
        else:
            a=ord(i)
        if a==92:
            eve=eve+1
            if orm==1 and eve>=2:
                orm=2
                eve=0
        if orm==1:
            div=enck[loop]
            loop=loop+1
            num=int(enck[loop])
            loop=loop+1
            sm=int(enck[loop])
            loop=loop+1
            if div=='a' or div=='A':
                for j in range(num):
                    a=a+127
                for ji in range(sm):
                    a=a-40
                e=enctm/127
                g,h=divmod(e,1)
                g=int(round(g))
                g=g*127
                enctm=(enctm-g)+y
                a=a-enctm
                enc=chr(a)
                dec=dec+enc
            elif div=='b' or div=='B':
                for ji in range(sm):
                    a=a-40
                e=enctm/127
                g,h=divmod(e,1)
                g=int(round(g))
                g=g*127
                enctm=(enctm-g)+y
                a=a-enctm
                enc=chr(a)
                dec=dec+enc
            elif div=='c' or div=='C':
                for j in range(num):
                    a=a-127
                for ji in range(sm):
                    a=a-40
                e=enctm/127
                g,h=divmod(e,1)
                g=int(round(g))
                g=g*127
                enctm=(enctm-g)+y
                a=a+enctm
                enc=chr(a)
                dec=dec+enc
            elif div=='d' or div=='D':
                for ji in range(sm):
                    a=a-40
                e=enctm/127
                g,h=divmod(e,1)
                g=int(round(g))
                g=g*127
                enctm=(enctm-g)+y
                a=a+enctm
                enc=chr(a)
                dec=dec+enc
            y=y+1
        elif orm==2:
            orm=1
    if mag=='uud1' or mag=='uus1':
        tm=str(datetime.datetime.now())
        s="UPDATE "+mag+" SET acc='9862' WHERE uuidu='"+dect+"';"
        db.execute(s)                   #updating the main file for status changes
        db.commit()
        s="UPDATE "+de+" SET acc='9862', timedc='"+tm+"' WHERE uuide='"+dect+"';"
        db.execute(s)                   #updating the user dec file for status changes
        db.commit()
        s="SELECT emle FROM "+de+" WHERE uuide='"+dect+"';"
        pw=db.execute(s).fetchall()         #getting the creators email id for status change
        emle=cutter(pw)
        s="SELECT enc FROM fn1 WHERE eml='"+emle+"';"
        pw=db.execute(s).fetchall()             
        en=cutter(pw)
        s="UPDATE "+en+" SET timedc='"+tm+"',acc='9862' WHERE uuide='"+dect+"';"
        db.execute(s)                       #updating the enc file of the creator
        db.commit()
        no=''                               
        for i in range(len(en)-4):
            no=no+en[i]
        no=no+'nott'
        s="INSERT INTO "+no+" (msg,status) VALUES ('Message decrypted by "+eml+".','9089');"
        db.execute(s)                           #updating the creators notification
        db.commit()
    if emle=='':
        emle=''
    return dec,emle

def cutter(pw):                         #cuts messages recieved via SQL
    pw=str(pw)
    j=len(pw)-4
    k=''
    h=0
    for h in range(j):
        if h>2:
            k=k+pw[h]
    return k

def emlcutter(pw):                         #cuts messages recieved via SQL
    pw=str(pw)
    j=len(pw)-3
    k=''
    h=0
    for h in range(j):
        if h>1:
            k=k+pw[h]
    return k

def reverse1(q):                      #reverse the messages
    x=0
    lm=[]
    pi=0
    s=''
    h=0
    s="SELECT nott FROM fn1 where uuidu='"+q[0]+"';"
    pw=db.execute(s).fetchall()
    notif=cutter(pw)
    s="SELECT msg FROM "+notif+" WHERE status='9089';"
    pw=db.execute(s).fetchall()
    p=len(pw)
    if p==0:
        return lm
    elif p>10:
        h=p-10
        p=p-h
    for i in range(p):
        if h==0:
            j=p-(i+1)
        elif h>0:
            j=h+(p-(i+1))
        s=pw[j]
        m=str(s)
        kl=len(m)-4
        k=''
        io=0
        for io in range(kl):
            if io>1:
                k=k+m[io]
        lm.append(k)
    notif=''
    s=''
    h=0
    io=0
    kl=0
    m=''
    k=''
    pw=''
    return lm

def userfiles(q):
    s="SELECT enc FROM fn1 where uuidu='"+q[0]+"';"
    pw=db.execute(s).fetchall()
    fln=cutter(pw)
    de=''
    notif=''
    for i in range(len(fln)-4):
        de=de+fln[i]
    de=de+'dect'
    for i in range(len(fln)-4):
        notif=notif+fln[i]
    notif=notif+'nott'
    s="SELECT eml FROM fn1 where uuidu='"+q[0]+"';"
    pw=db.execute(s).fetchall()
    eml=cutter(pw)
    return fln,de,notif,eml

def rgdecryptxt(dect,mag,de,eml):
    div=''       #divisional block 
    loop=0       #no of times to loop
    num=0        #no of times to increase time
    a=0          #ascii no of each character
    enc=''       #character representation of ascii
    dec=''       #decrypted text
    y=0          #second increment
    fn=''
    emle=''
    s="SELECT enct FROM "+mag+" WHERE uuidu='"+dect+"';"
    pw=db.execute(s).fetchall()
    enct=cutter(pw)
    s="SELECT enck FROM "+mag+" WHERE uuidu='"+dect+"';"
    pw=db.execute(s).fetchall()
    enck=cutter(pw)
    s="SELECT enctm FROM "+mag+" WHERE uuidu='"+dect+"';"
    pw=db.execute(s).fetchall()
    enctme=emlcutter(pw)
    enctm=int(enctme)
    orm=1
    global eve
    eve=0
    for i in enct:
        s=i
        if len(s)>1:
            h=len(s)-1
            a=int(s[h])
        else:
            a=ord(i)
        if a==92:
            eve=eve+1
            if orm==1 and eve>=2:
                orm=2
                eve=0
        if orm==1:
            div=enck[loop]
            loop=loop+1
            num=int(enck[loop])
            loop=loop+1
            sm=int(enck[loop])
            loop=loop+1
            if div=='a' or div=='A':
                for j in range(num):
                    a=a+127
                for ji in range(sm):
                    a=a-40
                e=enctm/127
                g,h=divmod(e,1)
                g=int(round(g))
                g=g*127
                enctm=(enctm-g)+y
                a=a-enctm
                enc=chr(a)
                dec=dec+enc
            elif div=='b' or div=='B':
                for ji in range(sm):
                    a=a-40
                e=enctm/127
                g,h=divmod(e,1)
                g=int(round(g))
                g=g*127
                enctm=(enctm-g)+y
                a=a-enctm
                enc=chr(a)
                dec=dec+enc
            elif div=='c' or div=='C':
                for j in range(num):
                    a=a-127
                for ji in range(sm):
                    a=a-40
                e=enctm/127
                g,h=divmod(e,1)
                g=int(round(g))
                g=g*127
                enctm=(enctm-g)+y
                a=a+enctm
                enc=chr(a)
                dec=dec+enc
            elif div=='d' or div=='D':
                for ji in range(sm):
                    a=a-40
                e=enctm/127
                g,h=divmod(e,1)
                g=int(round(g))
                g=g*127
                enctm=(enctm-g)+y
                a=a+enctm
                enc=chr(a)
                dec=dec+enc
            y=y+1
        elif orm==2:
            orm=1
    if mag=='uud1' or mag=='uus1':
        tm=str(datetime.datetime.now())
        s="UPDATE "+mag+" SET acc='9862' WHERE uuidu='"+dect+"';"
        db.execute(s)                   #updating the main file for status changes
        db.commit()
        s="UPDATE "+de+" SET acc='9862', timedc='"+tm+"' WHERE uuide='"+dect+"';"
        db.execute(s)                   #updating the user dec file for status changes
        db.commit()
        s="SELECT emle FROM "+de+" WHERE uuide='"+dect+"';"
        pw=db.execute(s).fetchall()         #getting the creators email id for status change
        emle=cutter(pw)
        s="SELECT enc FROM fn1 WHERE eml='"+emle+"';"
        pw=db.execute(s).fetchall()             
        en=cutter(pw)
        s="UPDATE "+en+" SET timedc='"+tm+"',acc='9862' WHERE uuide='"+dect+"';"
        db.execute(s)                       #updating the enc file of the creator
        db.commit()
        no=''                               
        for i in range(len(en)-4):
            no=no+en[i]
        no=no+'nott'
        s="INSERT INTO "+no+" (msg,status) VALUES ('Message decrypted by "+eml+".','9089');"
        db.execute(s)                           #updating the creators notification
        db.commit()
    if emle=='':
        emle=''
    return dec,emle
