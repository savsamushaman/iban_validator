from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from core.serializers import IBANSerializer, UserSerializer
from core.models import IBAN

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    model = get_user_model()
    queryset = model.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class IBANViewset(viewsets.ModelViewSet):

    model = IBAN
    queryset = model.objects.all()
    serializer_class = IBANSerializer

    def create(self, request, *args, **kwargs):

        serializer = IBANSerializer(data=request.data)
        
        response = {}

        if serializer.is_valid():
            commit = request.data.get('commit')
            commit = True if commit is None else commit

            # makes more sense to turn committing off, then turn comitting on
            if commit != False:
                serializer.save()
            
            response['iban'] = serializer.data['iban']
            response['is_valid'] = serializer.data['is_valid']
            response['errors'] = []

            return Response(response, status=status.HTTP_200_OK)
        
        response['iban'] = serializer.data['iban']
        response['is_valid'] = False
        response['errors'] = serializer.errors['iban']

        return Response(response, status=status.HTTP_400_BAD_REQUEST)


