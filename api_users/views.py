from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from rest_framework import status, viewsets
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken

from .models import User
from .permissions import IsAdmin
from .serializers import (CustomTokenObtainSerializer, EmailSerializer,
                          UserSerializer)


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated, IsAdmin)
    lookup_field = 'username'

    @action(
        detail=False,
        methods=('get', 'patch'),
        permission_classes=(IsAuthenticated,),
        url_path='me',
        url_name='action_me',
    )
    def action_me(self, request, *args, **kwargs):
        if request.method == 'GET':
            serializer = self.get_serializer(request.user)
            return Response(serializer.data)
        elif request.method == 'PATCH':
            serializer = self.get_serializer(
                request.user, data=request.data, partial=True
            )
            serializer.is_valid(raise_exception=True)
            serializer.save(role=request.user.role)
            return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(('POST',))
@permission_classes((AllowAny,))
def token_obtain(request):
    serializer = CustomTokenObtainSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    email = serializer.data['email']
    code = serializer.data['confirmation_code']
    user = get_object_or_404(User, email=email)

    if not default_token_generator.check_token(user, code):
        error_message = 'confirmation_code не соответствует email'
        return Response(
            {'confirmation_code': error_message},
            status=status.HTTP_400_BAD_REQUEST,
        )

    user.is_active = True
    user.save()
    access_token = str(AccessToken.for_user(user))
    return Response({'token': access_token}, status=status.HTTP_200_OK)


@api_view(('POST',))
@permission_classes((AllowAny,))
def pre_reg(request):
    email = request.data.get('email')
    serializer = EmailSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    user, created = User.objects.get_or_create(email=email)
    if created:
        user.is_active = False
        user.save()
    token = default_token_generator.make_token(user)
    send_mail(
        'Регистрационный код.',
        f'Ваш код: {token}.',
        settings.DEFAULT_FROM_EMAIL,
        [serializer.data['email']],
    )
    return Response({'email': email}, status=status.HTTP_200_OK)
