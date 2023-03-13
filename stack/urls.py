from django.urls import path
from stack import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path("register/",views.SignUpView.as_view(),name="register"),
    path("login",views.SignInView.as_view(),name="signin"),
    path("home",views.IndexView.as_view(),name="index"),
    path("questions/<int:id>/answers/add",views.AddAnswerView.as_view(),name="add-answer"),
    path("answers/<int:id>/upvote/add",views.UpvoteView.as_view(),name="upvote"),
    path("profile/add",views.UserProfileCreateView.as_view(),name="profile-add"),
    path("profile/details",views.ProfileDetailView.as_view(),name="profile-detail"),
    path("profile/<int:id>/change",views.ProfileUpdateView.as_view(),name="profile-edit"),
    path("questions/<int:pk>/remove",views.QuestionDeleteView.as_view(),name="question-delete"),
    path("answers/<int:id>/upvote/remove",views.UpVoteRemoveView.as_view(),name="upvote-remove"),
    path("signout",views.SignoutView.as_view(),name="signout")
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)