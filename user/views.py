from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User
from .serializers import RegistrationSerializer


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer


# from rest_framework.authtoken.models import Token

    # # user register olduktan sonra login yapıp token create etme!
    # def create(self, request, *args, **kwargs):
    #     response = super().create(request, *args, **kwargs)
    #     token = Token.objects.create(user_id = response.data['id'])
    #     response.data['token'] = token.key
    #     return response



# logout-1

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def logout(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response({"message": 'User Logout: Token Deleted'})


# logout-2
'''
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
# from django.contrib.auth import logout
from rest_framework import status

class LogoutView(APIView):
    
    def post(self, request, *args, **kwargs):
        return self.logout(request)
    
    def logout(self, request):
        try:
            request.user.auth_token.delete()
        except (AttributeError, ObjectDoesNotExist):
            pass
        
        response = Response({"detail": ("Successfully logged out.")},
                            status=status.HTTP_200_OK)
        return response
'''

