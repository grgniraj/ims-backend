from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.shortcuts import render
from inventory.models import Admin

# Create your views here.

def signaction(request):
    if request.method == "POST":
        password = request.POST['password']
        try:
            validate_password(password)
        except ValidationError as e:
            # The password entered by the user is invalid
            # Handle the error here
            error_message = "Invalid password. Your password must contain at least 8 characters and should contain at least one uppercase letter, one lowercase letter, one digit, and one special character."
            context = {'error_message': error_message}
            return render(request, 'signup_page.html', context)
        else:
            context={}
            # The password entered by the user is valid
            # Process the data here
                    # Get the form data from the request
            full_name = request.POST['fullname']
            email = request.POST['email']
            
            cpassword = request.POST['cpassword']
            if cpassword.__eq__(password):
            # Create a new ImsAdmin instance with the form data
                admin = Admin(name=full_name, email=email, password=password)

            # Save the new instance to the database
                status = admin.save()
                return render(request, 'signup_page.html', context)
            else:
                error_message = "Password Mismatch!!"
                context = {'error_message': error_message}
                return render(request, 'signup_page.html', context)
    else:
        context={}
        return render(request,'signup_page.html',context)

def homeaction(request):
    return render(request,'Home.html')