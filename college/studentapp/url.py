from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^studentform',views.student),
    url(r'^save-student',views.save_student),
    url(r'^get_student_data/$','studentapp.views.get_student_detail',name='get_student_detail'),
    url(r'^update_student_data/$', 'studentapp.views.update_student_detail', name='update_student_detail'),
    url(r'^delete_data/$', 'studentapp.views.delete_student_detail', name='delete_student_detail'),
]
