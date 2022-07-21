from django.urls import path
from . import views
# from .views import home


# urlpatterns = [
#     path('/<str:category>', NewsHome.as_view(), name="News_home")]
urlpatterns=[
    # path("",views.home,name="home"),
path("",views.home1,name="home1"),
path("paginator/<str:filename>",views.paginator,name="paginator")
]