
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Proyecto, Contaduria, Usuarios
from django.db.models import Sum
import xlwt, datetime, os
from django.http import HttpResponse
from django.contrib.auth.models import User


#@login_required
def registrarBR(request):
    if request.method == 'POST':
        id_contaduria = request.POST.get('id_contaduria')
        numero_escritura = request.POST.get('numero_escritura')
        valor_beneficiencia = request.POST.get('valor_beneficiencia')
        valor_registro = request.POST.get('valor_registro')
        valor_deposito_cliente = request.POST.get('valor_deposito')
        nombre_proyecto = request.POST.get('nombre_proyecto')
    
        total = float(valor_beneficiencia or 0) + float(valor_registro or 0)
        
        if not numero_escritura:
            error_message = 'El campo Numero de escritura es obligatorio'
            contadurias = Contaduria.objects.all()
            return render(request, 'contabilidad/registrarBR.html', {'contadurias': contadurias, 'error_message': error_message})
        
        contadurias = Contaduria.objects.create(
            id_contaduria = id_contaduria,
            numero_escritura=numero_escritura,
            valor_beneficiencia=valor_beneficiencia,
            valor_registro=valor_registro,
            valor_deposito=valor_deposito_cliente,
            nombre_proyecto=nombre_proyecto,
            total=total
        )
        contadurias.save()
        return redirect('beneficiencia_registro')
    else:
        contadurias = Contaduria.objects.all()
        return render(request, 'contabilidad/registrarBR.html', {'contadurias': contadurias})
    
def index(request):
    if request.method == 'POST':
        username = request.POST.get('usuario')
        password = request.POST.get('contraseña')

        usuario_auth = authenticate(request, username=username, password=password)

        if usuario_auth is not None:
            login(request, usuario_auth)
            return redirect('beneficiencia_registro')
        else:
            messages.error(request, 'El usuario o la contraseña son incorrectos')
            return render(request, 'index.html', {'usuario': username})
    else:
        return render(request, 'index.html')

def error(request):
    return render(request, 'contabilidad/404.html')

def total(request):
    suma_total = Contaduria.objects.aggregate(
        total_beneficiencia=Sum('valor_beneficiencia'), 
        total_registro=Sum('valor_registro'),
    )

    total_asume = (suma_total['total_beneficiencia'] or 0) + \
                  (suma_total['total_registro'] or 0)
    
    contadurias = Contaduria.objects.all()
    return render(request, 'registrarBR.html', {'total_asume': total_asume, 'contadurias': contadurias})


def eliminarBR(request):
    if request.method == 'POST':
        numero_registro = request.POST.get('numero_registro')
        contaduria = Contaduria.objects.filter(id_contaduria=numero_registro).first()
        
        if contaduria:
            contaduria.delete()
            return redirect('Ebeneficiencia_registro')
        else:
            error_message = 'El registro no existe'
            contadurias = Contaduria.objects.all()
            return render(request, 'contabilidad/eliminar.html', {'contadurias': contadurias, 'error_message': error_message})
    else:
        contadurias = Contaduria.objects.all()
        return render(request, 'contabilidad/eliminarBR.html', {'contadurias': contadurias})

def export_to_excel(request):
     
        header_style = xlwt.easyxf(
            'font: bold on; align: wrap on, vert centre, horiz center;'
            'borders: top_color black, bottom_color black, right_color black, left_color black,'
            'left thin, right thin, top thin, bottom thin;'
            'pattern: pattern solid, fore_color light_green;'
        )

        data_style = xlwt.easyxf(
            'align: wrap on, vert centre, horiz center;'
            'borders: top_color black, bottom_color black, right_color black, left_color black,'
            'left thin, right thin, top thin, bottom thin;'
        )
        
        texto = xlwt.easyxf(
            
            'pattern: pattern solid, fore_color white; font: color green;'
        )

        try: 
            response = HttpResponse(content_type='application/ms-excel')
            response['Content-Disposition'] = 'attachment; filename="contaduria.xls"'
            fecha = datetime.datetime.now().strftime("%d/%m/%Y")
            img = os.path.join(os.path.dirname(__file__), 'static/img/regis.bmp')
            img2 = os.path.join(os.path.dirname(__file__), 'static/img/FIRMA.bmp')
            

            workbook = xlwt.Workbook(encoding='utf-8')
            worksheet = workbook.add_sheet('contaduria')
            
            contadurias = Contaduria.objects.all()
            worksheet.insert_bitmap(img, 0, 0, scale_x=0.18, scale_y=0.17)
            worksheet.insert_bitmap(img2, 26, 2, scale_x=0.50, scale_y=0.55)
            
                
            worksheet.row(1).height_mismatch = True  
            worksheet.row(1).height = 500
            worksheet.row(2).height_mismatch = True  
            worksheet.row(2).height = 500 
            worksheet.row(3).height_mismatch = True  
            worksheet.row(3).height = 500
            worksheet.row(4).height_mismatch = True  
            worksheet.row(4).height = 500
            worksheet.row(5).height_mismatch = True  
            worksheet.row(5).height = 500
            
            worksheet.col(1).width = 4800
            worksheet.col(1).width = 4800
            worksheet.col(2).width = 4800
            worksheet.col(3).width = 4800
            worksheet.col(4).width = 4800
            worksheet.col(5).width = 4800
            
            worksheet.row(1).height = 5 * 1
            worksheet.write_merge(9, 9, 0, 7, 'CUENTA DE COBRO No:', xlwt.easyxf('font: bold on'))
            worksheet.write_merge(10, 10, 0, 7, 'CONSTRUCTORA BOLIVAR S.A. NIT. 860.513.493-1', xlwt.easyxf('font: bold on'))
            worksheet.write_merge(11, 11, 0, 7, 'DEBE A: NOTARIA QUINTA DE BOGOTÁ ANDRÉS HIBER ARÉVALO PACHECO', xlwt.easyxf('font: bold on'))
            worksheet.write_merge(12, 12, 0, 7, 'NIT. 91.230.903-3', xlwt.easyxf('font: bold on'))
            worksheet.write_merge(13, 13, 0, 7, 'Bogotá. D.C.', xlwt.easyxf('font: bold on'))
            worksheet.write_merge(14, 14, 0, 7, fecha, xlwt.easyxf('font: bold on'))
            worksheet.write_merge(16, 16, 0, 7, 'Por concepto del impuesto de beneficiencia y registro')
            for contaduria in contadurias:
                proyecto_texto = f'Proyecto: {Contaduria.nombre_proyecto}'
            worksheet.write_merge(17, 17, 0, 7, proyecto_texto)
            
            

            columns = ['ITEM', 'Numero de escritura', 'Beneficiencia', 'Registro', 'Deposito cliente', 'Total asume C. B']

            for col_num, column_title in enumerate(columns):
                worksheet.write(19, col_num, column_title, header_style) 

            contadurias = Contaduria.objects.all()
            total_asumee = sum(contaduria.total for contaduria in contadurias) 
            row_num = 20
            for contaduria in contadurias:
                
                beneficiencia = f'$ {contaduria.valor_beneficiencia:,}'
                registro = f'$ {contaduria.valor_registro:,}'
                deposito = f'$ {contaduria.valor_deposito:,}'
                total = f'$ {contaduria.total:,}'
                total_asumeee = f'$ {total_asumee:,}'
                
                worksheet.write(row_num, 0,contaduria.id_contaduria, data_style)
                worksheet.write(row_num, 1, contaduria.numero_escritura, data_style)
                worksheet.write(row_num, 2, beneficiencia, data_style)
                worksheet.write(row_num, 3, registro, data_style)
                worksheet.write(row_num, 4, deposito, data_style)
                worksheet.write(row_num, 5, total, data_style)
                row_num += 1
            
        
            worksheet.write_merge(row_num, row_num, 0, 4, 'TOTAL CUENTA DE COBRO:', header_style)
            worksheet.write(row_num, 5, total_asumeee, data_style)

            worksheet.write_merge(row_num + 7, row_num + 7, 2, 32, 'ANDRÉS HIBER ARÉVALO PACHECO', xlwt.easyxf('font: bold on'))
            worksheet.write_merge(row_num + 8, row_num + 8, 2, 33, 'NOTARIO QUINTO DEL CÍRCULO DE BOGOTÁ', xlwt.easyxf('font: bold on'))
            worksheet.write_merge(row_num + 9, row_num + 9, 2, 34, 'carrera 15 A No. 120 - 63')
            worksheet.write_merge(row_num + 10, row_num + 10, 2, 34, 'PBX 5550958 /59 / 60 /61 /62')
            worksheet.write_merge(row_num + 11, row_num + 11, 2, 35, 'E-mail: andres.arevalo@notaria5.com.co', texto)

            workbook.save(response)
            return render(request, 'contabilidad/404.html')
        except Exception as e: 
            
            return render(request, 'contabilidad/404.html', {'error_message': str(e)})
        
