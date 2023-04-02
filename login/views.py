from django.shortcuts import render

# Create your views here.

def loginaction(request):
    global fn,em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",password="$$$lamjung$$$@@@",database="ims")
        cursor=m.cursor()
        d=request.POST
        for key, value in d.items():
            if key=="Full Name":
                fn=value
            if key=="email":
                em=value
            if key=="password":
                pwd=value
        
        c="insert into ims_admin values('{}','{}','{}')".format(fn,em,pwd)
        cursor.executer(c)
        m.commit()

    return render(request,'login_page.html')