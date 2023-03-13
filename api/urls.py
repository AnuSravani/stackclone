from django.urls import path
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
router=DefaultRouter()
router.register("accounts/users",views.UsersView,basename="users")
router.register("user/profile",views.ProfileView,basename="profile")
router.register("questions",views.QuestionsView,basename="questions")
router.register("answers",views.AnswersView,basename="answers")
urlpatterns=[
    # path("token/",ObtainAuthToken.as_view())
    path("token/",TokenObtainPairView.as_view()),
    path("token/refresh/",TokenRefreshView.as_view())
]+router.urls