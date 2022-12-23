from turtle import title
from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact,Post,Comment,upload
from django.contrib import messages 
from django.contrib.auth.models import User 
from django.contrib.auth  import authenticate,  login, logout
from django.contrib.auth.forms import UserCreationForm


# Creating  views functions here.
def home1(request): #,slug
     # slug=slug
    # post = Post.objects.get__object__or__404()
    # post = get_object_or_404(Post)
    # if request.method == 'POST':
    #         post = Post.objects.filter()
    #         post.likes += 1
    #         post2 = Post(likes = post.likes)
    #         post2.save()
    allPosts= Post.objects.all()
    allPosts= allPosts[::-1]
    comments= Comment.objects.filter()
    comments = comments[::-1]
    
    # comments = post.comments.filter(active=True)
    context={'allPosts': allPosts,'user':request.user,'comments': comments}#,'comments': comments, 'user': request.user}
    
    return render(request,'home/home.html',context)

def about(request):
    return render(request,'home/about.html')

#this is how user will get the chance to interact with website builder
def contactus(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['query']
        contact = Contact(name=name,email=email,phone=phone,content=content)
        contact.save()
    return render(request,'home/contactus.html')

#this will handle signup for user
def handlesignup(request):
    if request.method=="POST":
        # Get the signup parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        # check for wrong input
         
        if len(username)>30:
            messages.error(request, " Your user name must be under 30 characters")
            return redirect('handlelogin')

        # if not username.isalnum() or username in ['']:
        #     messages.error(request, " User name should only contain letters and numbers")
        #     return redirect('handlelogin')
        if (pass1!= pass2):
             messages.error(request, " Passwords do not match")
             return redirect('handlelogin')
        if User.objects.filter(username=username).exists():
            messages.error(f'Username "%s" is already in use.' % username)
            # (request, " User name should only contain letters and numbers")
            return redirect('handlelogin')
        # if not User.objects.filter(email__iexact='{{username}}@somaiya.edu', is_active=True):
        #     messages.error(request, "Invalid email!")
        #     return redirect("handlelogin")
        # if not email=='{{username}}@somaiya.edu':
        #     messages.error(request, "Invalid email!")
        #     return redirect("handlelogin")
        
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request, " Your JigyAasa Account has been successfully created")
        return redirect('handlelogin')

    else:
        return HttpResponse("404 - Not found")


#this will handle login for user
def handlelogin(request):
    if request.method=="POST":
        # Get the post parameters
        # username = self.cleaned_data['loginusername']
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']
        
        user=authenticate(username= loginusername, password= loginpassword)
        if not User.objects.filter(username__iexact=loginusername, is_active=True).exists():
            messages.error(request, "There is no such username exist!")
            return redirect("handlelogin")

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("home")
            
        
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("handlelogin")

    return render(request,"home/login.html")

#this will handle logout for user
def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('handlelogin')

#This will show the profile of user
def profile(request):
    if request.method == "POST":
        user = request.user
        profile_pic =  request.FILES['doc'] #request.POST['doc']
        profile_pic._name = f'{user}.jpg'
        profiles = upload(user=user,profile_pic=profile_pic)
        profiles.save()
    return render(request,'home/profile.html')

# for Posting questions in modal
def post1(request):
    if request.method=="POST":
        
        # Get the post parameters
        username=request.POST['name1']
        title = request.POST['title']
        question=request.POST['quest']
        print("yoo")
        if User.objects.filter(username=username).exists():
            # raise forms.ValidationError(u'Username "%s" is already in use.' % username)
            messages.success(request, " Your question is posted")
            post2 = Post(name=username,question=question,title=title)
            post2.save()
            
            return redirect('home')
        else:
            return redirect('home')
   
#for commenting on the question
def comment(request): 
    if request.method == "POST":
        comment=request.POST.get('comment')
        user=request.user
        postSno =request.POST.get('postSno')
        post= Post.objects.get(sno=postSno)
        
        comment1=Comment(comment2= comment, user=user, post=post)
        comment1.save()
        messages.success(request, "Your comment has been posted successfully")
        
    return redirect("home")
        

# technical page
def technical(request):
    allpostsTitle= Post.objects.filter(title='Technical')#title__icontains='title'
    allposts=  allpostsTitle
    allposts = allposts[::-1]
    comments= Comment.objects.filter()
    comments = comments[::-1]
    # comments = post.comments.filter(active=True)
    
    techpost={'allposts': allposts,'user':request.user,'comments': comments}
    return render(request,'home/technical.html',techpost)

# general page
def general(request):
    allpostsTitle= Post.objects.filter(title='General')#title__icontains='title'
    allposts=  allpostsTitle
    allposts = allposts[::-1]
    comments= Comment.objects.filter()
    comments = comments[::-1]
    # comments = post.comments.filter(active=True)
    
    Genpost={'allposts': allposts,'user':request.user,'comments': comments}
    return render(request,'home/general.html',Genpost)
    # return render(request,'home/general.html')

# Ask Experts page
def askexpert(request):
    # allpostsTitle= Post.objects.filter(title='General')#title__icontains='title'
    allposts = Post.objects.filter(title='Askexpert')

    allposts = allposts[::-1]
    # comments= Comment.objects.filter()
    comments = Comment.objects.all()

    comments = comments[::-1]
    # comments = post.comments.filter(active=True)
   
    techpost={'allposts': allposts,'user':request.user,'comments': comments}
    return render(request,'home/askexperts.html',techpost)



# for searching in All post
def Search(request):
    search=request.GET['search']
    if len(search)>78:
        allposts=Post.objects.none()
    else:
        allpostsTitle= Post.objects.filter(title__icontains=search)
        allpostsName= Post.objects.filter(name__icontains=search)
        allpostsQuestion =Post.objects.filter(question__icontains=search)
        allposts=  allpostsTitle.union(allpostsQuestion, allpostsName)
    if allposts.count()==0:
        messages.warning(request, "No search results found. Please try your query with more correct keywords.")
    allposts = allposts[::-1]
    comments= Comment.objects.filter()
    comments = comments[::-1]
    # comments = post.comments.filter(active=True)

    everypost={'allposts': allposts, 'query': search,'user':request.user,'comments': comments}
    return render(request, 'home/search.html', everypost)