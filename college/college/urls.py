from django.conf.urls import include, url
from django.contrib import admin
from collegeapp import url as collegeurl
from studentapp import url as studenturl
from collegeapp import views
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^collegeapp/', include(collegeurl)),
    url(r'^studentapp/', include(studenturl)),
    url(r'^$', 'collegeapp.views.base'),
    url(r'^datatable/','collegeapp.views.datatable'),
    url(r'^get-student-detail/', 'studentapp.views.get_student_detail'),
    url(r'^update_student_data/', 'studentapp.views.update_student_detail'),
    url(r'^delete_data/', 'studentapp.views.delete_student_detail')
]
