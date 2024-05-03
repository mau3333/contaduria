from django.db import models

class Proyecto(models.Model):
    id_proyecto = models.AutoField(primary_key=True)
    nombre_proyecto = models.CharField(max_length=50)
    
    class Meta:
        db_table = "proyecto"
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        
class Contaduria(models.Model):
    id_contaduria = models.IntegerField(primary_key=True)
    numero_escritura = models.IntegerField()
    nombre_proyecto = models.CharField(max_length=50)
    valor_beneficiencia = models.IntegerField()
    valor_registro = models.IntegerField()
    valor_deposito = models.IntegerField()
    total = models.IntegerField()

    class Meta:
        db_table = "contaduria"
        verbose_name = "contaduria"
        verbose_name_plural = "contadurias"

class Usuarios(models.Model):
    id_login = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=20)
    contraseña = models.CharField(max_length=20)
    
    class Meta:
        db_table = "usuario"
        verbose_name = "usuario"
        verbose_name_plural = "usuarios"

class Proyecto_bene(models.Model):
    id_proyecto = models.AutoField(primary_key=True)
    nombre_proyecto = models.CharField(max_length=50)
    
    class Meta:
        db_table = "proyecto_bene"
        verbose_name = "proyecto_bene"
        verbose_name_plural = "proyectos_bene"
        
class Contaduria_bene(models.Model):
    id_contaduria = models.IntegerField(primary_key=True)
    numero_escritura = models.IntegerField()
    nombre_proyecto = models.CharField(max_length=50)
    valor_beneficiencia = models.IntegerField()
    valor_deposito = models.IntegerField()
    total = models.IntegerField()

    class Meta:
        db_table = "contaduria_bene"
        verbose_name = "contaduria_bene"
        verbose_name_plural = "contadurias_bene"

class Proyecto_regi(models.Model):
    id_proyecto = models.AutoField(primary_key=True)
    nombre_proyecto = models.CharField(max_length=50)
    
    class Meta:
        db_table = "proyecto_regi"
        verbose_name = "proyecto_regi"
        verbose_name_plural = "proyectos_regi"
        
class Contaduria_regi(models.Model):
    id_contaduria = models.IntegerField(primary_key=True)
    numero_escritura = models.IntegerField()
    nombre_proyecto = models.CharField(max_length=50)
    valor_registro = models.IntegerField()
    valor_deposito = models.IntegerField()
    total = models.IntegerField()

    class Meta:
        db_table = "contaduria_regi"
        verbose_name = "contaduria_regi"
        verbose_name_plural = "contadurias_regi"