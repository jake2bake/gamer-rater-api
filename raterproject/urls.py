from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from raterapi.views import UserViewSet, GameView, CategoryView, GameCategoryView, ReviewView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'games', GameView, 'game')
router.register(r'categories', CategoryView, 'category')
router.register(r'gamecategories', GameCategoryView, 'gamecategory')
router.register(r'reviews', ReviewView, 'review')
urlpatterns = [
    path('', include(router.urls)),
    path('login', UserViewSet.as_view({'post': 'user_login'}), name='login'),
    path('register', UserViewSet.as_view({'post': 'register_account'}), name='register'),
]

