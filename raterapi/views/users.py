from rest_framework import viewsets, status, permissions, serializers
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

class UserViewSet(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]

    @action(detail=False, methods=['post'], url_path='register')
    def register_account(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            # Use email as username
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            user = User.objects.create_user(
                username=email,
                email=email,
                password=password
            )
            print(f"User created: {user.email}, password hash: {user.password}")
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'], url_path='login')
    def user_login(self, request):
        email = request.data.get('email').strip().lower()
        password = request.data.get('password')
        print(f'Login attempt: email={email}, password={password}')

        # Authenticate directly using username=email
        user = authenticate(username=email, password=password)
        print(f"Authenticate result: {user}")

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            print(f"Token found: {token.key}")
            return Response({
                'token': token.key, 
                'id': user.id,
                'email': user.email

               },   status=status.HTTP_200_OK)
        else:
            print("Invalid credentials")
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)