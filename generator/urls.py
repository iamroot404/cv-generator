from django.urls import path
from . import views

urlpatterns = [
    path('cv_list/', views.cv_list, name="cv_list"),
    path('basic/', views.basicCv, name="basic"),
    path('resume/<str:pk>/', views.resume, name="resume"),
    path('basic_preview/<str:pk>/', views.basic_preview, name="basic_preview"),
    path('download_list/', views.download_list, name="download_list"),
    path('delete_cv/<str:pk>/', views.delete_cv, name="delete_cv"),
    path('editBasic/<str:pk>/', views.editBasic, name="editBasic"),

    path('AdvancedBasic/', views.AdvancedBasicCV, name="AdvancedBasic"),
    path('AdvBresume/<str:pk>/', views.advBr, name="AdvBresume"),
    path('advbasic_preview/<str:pk>/', views.advbasic_preview, name="advbasic_preview"),
    path('advDownload_list/', views.advDownload_list, name="advDownload_list"),
    path('advdelete_cv/<str:pk>/', views.advdelete_cv, name="advdelete_cv"),
    path('editAdvBasic/<str:pk>/', views.editAdvBasic, name="editAdvBasic"),
]