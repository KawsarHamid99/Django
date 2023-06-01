1. Login:
    AuthenticationForm(request=request,data=request.POST)
    user=authenticate(username=uname,password=pass)
    if user is not None:
        login(request,user)


2. Registration:
    UserCreationForm(request.POST)

3. Profile/edit profile:
    UserChangeForm(request.POST,instance=request.user) <--- to update / post request 
    UserChangeForm(instance=request.user)<------get request


4. set/change password:
    POST:
    PasswordChangeForm(user=request.user,data=request.POST)
    SetPasswordForm(user=request.user,data=request.POST)

    GET:
    PasswordChangeForm(user=request.user)
    SetPasswordForm(user=request.user)