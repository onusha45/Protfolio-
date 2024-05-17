from django.shortcuts import render
from django.http import HttpResponse 
from django.contrib import messages
from MyDetails.models import Contact

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        content = request.POST.get("content", "").strip()  # Make sure this matches the form field name
        number = request.POST.get("number", "").strip()
        
        # Debugging: Print received form data
        print(f"Received form data - Name: {name}, Email: {email}, Content: {content}, Number: {number}")
        
        if not name:
            messages.error(request, "Name is required.")
        elif not (1 < len(name) < 30):
            messages.error(request, "Length of name should be greater than 2 and less than 30 characters.")
        elif not email:
            messages.error(request, "Email is required.")
        elif not (1 < len(email) < 30):
            messages.error(request, "Invalid email. Try again.")
        elif not content:
            messages.error(request, "Content is required.")
        elif not (len(number) > 2 and len(number) < 13):
            messages.error(request, "Invalid number. Try again.")
        else:
            try:
                ins = Contact(name=name, email=email, content=content, number=number)
                ins.save()
                messages.success(request, "Thank you for contacting us. Your message has been saved.")
                print("Data has been saved to the database")
            except Exception as e:
                print(f"Error saving data: {e}")
                messages.error(request, "An error occurred while saving your message. Please try again.")
            return render(request, 'home.html')
    
    return render(request, 'home.html')
