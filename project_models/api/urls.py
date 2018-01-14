from django.conf.urls import url
from .views import EmployeeListCreateAPIView, DepartmentListCreateAPIView


urlpatterns = [
    url(r'^employees/$', EmployeeListCreateAPIView.as_view(), name="employees_list"),
    url(r'^departments/$', DepartmentListCreateAPIView.as_view(), name="departments_list")

]

