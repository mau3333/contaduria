from django.contrib import admin
from django.urls import path
from conta import views, viewsB, viewsR
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"), 
    path('beneficiencia_registro/', views.registrarBR, name="beneficiencia_registro"),
    path('registro/', viewsR.registrarR, name="registro"),
    path('beneficiencia/', viewsB.registrarB, name="beneficiencia"),
    #path('actualizar/', views.actualizar, name="actualizar"),
    path('Ebeneficiencia_registro/', views.eliminarBR, name="Ebeneficiencia_registro"), 
    path('Ebeneficiencia/', viewsB.eliminarB, name="Ebeneficiencia"), 
    path('Eregistro/', viewsR.eliminarR, name="Eregistro"), 
    path('export_to_excel/', views.export_to_excel, name='export_to_excel'),
    path('accounts/login/', views.error, name='login'),
    path('exportar_excel/', viewsB.export_to_excel_bene, name='exportar_excel'),
    path('exportar_excel_regi/', viewsR.exportar_excel_regi, name='exportar_excel_regi'),
    
    
]
