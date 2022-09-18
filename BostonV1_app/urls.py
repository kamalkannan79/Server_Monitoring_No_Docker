from django.urls import path,include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('', views.index,name='index'),
    path('server_details/',views.server_details, name = 'server_details'),
    path('cpu_details/',views.cpu_details, name = 'cpu_details'),
    path('ram_details/',views.ram_details, name = 'ram_details'),
    path('disk_details/',views.disk_details, name = 'disk_details'),
    path('network_details/',views.network_details, name = 'network_details'),
    path('silk/', include('silk.urls', namespace='silk')),
    path('server_serial/',views.serverlist.as_view()),
    path('cpu_serial/',views.cpulist.as_view()),
    path('ram_serial/',views.ramlist.as_view()),
    path('disk_serial/',views.disklist.as_view()),
    path('user_analytics/',views.user_analytics, name = 'user_analytics'),
    #path('line/',views.cpu_graph,name = 'line'),
    #path('gpu_temp_graph/',views.gpu_temp_graph,name = 'gpu_temp_graph'),
    #path('cpu_temp_graph/',views.cpu_temp_graph,name = 'cpu_temp_graph'),
    #path('gpu_load/',views.gpu_load_graph,name = 'gpu_load'),
    #path('percent/',views.disk_graph,name = 'percent'),
    #path('memory_info/',views.memory_info,name = 'memory_info'),
]
