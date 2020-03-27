from django.urls import path
from .views import (
    blog_post_detail_view,

)

urlpatterns = [

    path('<str:slug>/', blog_post_detail_view),

]