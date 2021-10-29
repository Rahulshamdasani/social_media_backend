from django.http import Http404
# from django.shortcuts import render, redirect
# from django.conf import settings
# from django.contrib.auth.models import User

# from .forms import ProfileForm


from .models import Profile
# from django.contrib.auth.models import User
# from accounts import models
# # Create your views here.

# def profile_detail_view(request, username, *args, **kwargs):
#     # get the profile for the passed username
#     qs = Profile.objects.filter(user__email = username)
#     if not qs.exists():
#         raise Http404
#     profile_obj = qs.first()
#         # is_following = profile_obj in user.following.all()
#     context = {
#         "username": username,
#         "profile": profile_obj
#     }
#     return render(request, "profiles/detail.html", context)



# # View to update profile form
# def profile_update_view(request, *args, **kwargs):
#     if not request.user.is_authenticated:
#         return redirect("/login?next=/profile/update")
#     my_profile = request.user.profile

#     form = ProfileForm(request.POST, instance = my_profile)

#     if form.is_valid():
#         profileObj = form.save(commit=False)
#         first_name = form.cleaned_data.get('first_name')
#         last_name = form.cleaned_data.get('last_name')
#         email_address = form.cleaned_data.get('email_address')
#         my_profile.first_name = first_name
#         my_profile.last_name = last_name
#         my_profile.email_address = email_address
#         my_profile.save()

#     context = {
#         "form":form,
#         "btn_label":"Save",
#         "title":"Update Profile",
#         'curr_prof':my_profile
#     }
#     return render(request, "profiles/form.html", context)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, status
from django.contrib.auth.models import User
from .serializer import ProfileSerializer

class UserProfileView(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    # authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.AllowAny,]

    def get(self, request, email, format=None):
        """
        Returns the wanted user by email id.
        """
        try:
            data = email
            print(f'{data=} ')
            wantedProfile = data
            print(f'{wantedProfile=}')
            
            if Profile.objects.filter(user__email=wantedProfile).exists():
                print("inside IF******")
                profile = Profile.objects.filter(user__email=wantedProfile).first()
                profilejson = ProfileSerializer(profile)
                print(profilejson)
                return Response(
                    {'profile': profilejson.data},
                    status=status.HTTP_200_OK
                )
            else:
                return Response(

                    {'error': 'user profile not found'},
                    status=status.HTTP_404_NOT_FOUND
                )
        except:
            return Response(

                {'error': 'data not found or loaded properly in request'},
                status=status.HTTP_400_BAD_REQUEST
            )

from django.contrib.auth import get_user_model # new
from rest_framework import generics 
# from .permissions import IsAuthorOrReadOnly
from .permissions import IsAuthorOrReadOnly
from .serializer import ProfileSerializer # new

class UpdateUserDetails(generics.UpdateAPIView):
        
    permission_classes = [IsAuthorOrReadOnly]
    serializer_class = ProfileSerializer

    def patch(self, request, email = None):
        print("Email passed is ",email)
        if not email:
            return Response(

                    {'error': 'Could not update'},
                    status=status.HTTP_404_NOT_FOUND
                )
        
        currProfile = Profile.objects.filter(user__email = email)
        if(not currProfile):
            return Response(

                    {'error': 'Prof not tonjsgnkjhnfsknklnNot found'},
                    status=status.HTTP_404_NOT_FOUND
                )
        currProfile = currProfile.first()
        print(currProfile)

        if currProfile:
            
            currProfile.first_name = request.data['first_name']
            currProfile.last_name = request.data['last_name']
            currProfile.display_name = request.data['display_name']
            currProfile.locations = request.data['locations']
            currProfile.bio = request.data['bio']
            currProfile.save()
            # if(currProfile.save()):
            return Response({'Success':'Saved'}, status=status.HTTP_200_OK)
            # else:
                # return Response({'Error':'Not saving'}, status=status.HTTP_304_NOT_MODIFIED)
