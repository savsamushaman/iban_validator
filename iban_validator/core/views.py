from django.contrib.auth import get_user_model

from rest_framework import status, viewsets, generics
from rest_framework.response import Response

from core.serializers import UserSerializer, GetIBANSerializer, PostIBANSerializer
from core.models import IBAN
from core.mixins import SerializerByMethodMixin

class User(viewsets.ModelViewSet):
    """
    API endpoint that allows viewing of the users.
    """
    model = get_user_model()
    queryset = model.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class IBAN(SerializerByMethodMixin, viewsets.ModelViewSet):

    queryset = IBAN.objects.all()
    
    serializer_map = {
        'GET': GetIBANSerializer,
        'POST': PostIBANSerializer,
    }

    def create(self, request, *args, **kwargs):

        serializer = PostIBANSerializer(data=request.data)
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


