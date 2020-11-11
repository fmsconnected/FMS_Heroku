login(request, user)

AllLogin.objects.create(user=request.user)
