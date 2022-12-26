from django.shortcuts import render
from .models import Empleado, Departamento, Puesto
from django.http import HttpResponse


from AppCoder.forms import EmpleadoForm, DepartamentoForm, PuestoForm
# Create your views here.
def inicio(request):
    return render (request, "AppCoder/inicio.html")

def empleadoFormulario(request):
    if request.method=="POST":
        form= EmpleadoForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data #convierte de la info en modo formulario a un diccionario
            dni= informacion["dni"]
            nombre= informacion["nombre"]
            id_departamento= informacion["id_departamento"]
            id_puesto= informacion["id_puesto"]
            emple= Empleado(dni=dni, nombre=nombre, id_departamento=id_departamento, id_puesto=id_puesto)
            emple.save()
            return render(request, "AppCoder/inicio.html" ,{"mensaje": "Se registró el empleado"})
        else:
            return render(request, "AppCoder/empleadoFormulario.html" ,{"form": form, "mensaje": "Informacion no valida"})
        
    else:
        formulario=EmpleadoForm()
        return render (request, "AppCoder/empleadoFormulario.html", {"form": formulario})

def mostrarEmpleados(request):
    empleados=Empleado.objects.all()
    return render(request, "AppCoder/mostrarEmpleados.html", {"empleados":empleados})

def busquedaEmpleado(request):
    return render(request, "AppCoder/busquedaEmpleado.html")

def muestraBusquedaEmpleado(request):
    
    dni= request.GET["dni"]
    if dni!="":
        empleados= Empleado.objects.filter(dni=dni)
        return render(request, "AppCoder/muestraBusquedaEmpleado.html", {"empleados": empleados})
    else:
        return render(request, "AppCoder/busquedaEmpleado.html", {"mensaje": "Debe ingresar un DNI"})

def departamentosFormulario(request):
    if request.method=="POST":
        form= DepartamentoForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data #convierte de la info en modo formulario a un diccionario
            codigo= informacion["codigo"]
            nombre= informacion["nombre"]
            departamento= Departamento(codigo=codigo, nombre=nombre)
            departamento.save()
            return render(request, "AppCoder/inicio.html" ,{"mensaje": "Se guardó el departamento"})
        else:
            return render(request, "AppCoder/departamentosFormulario.html" ,{"form": form, "mensaje": "Informacion no valida"}) 
    else:
        formulario=DepartamentoForm()
        return render (request, "AppCoder/departamentosFormulario.html", {"form": formulario}) 

def puestosFormulario(request):
    if request.method=="POST":
        form= PuestoForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data #convierte de la info en modo formulario a un diccionario
            codigo= informacion["codigo"]
            nombre= informacion["nombre"]
            departamento= informacion["departamento"]
            puesto= Puesto(codigo=codigo, nombre=nombre,departamento=departamento)
            puesto.save()
            return render(request, "AppCoder/inicio.html" ,{"mensaje": "Puesto Guardado"})
        else:
            return render(request, "AppCoder/puestosFormulario.html" ,{"form": form, "mensaje": "Informacion no valida"}) 
    else:
        formulario=PuestoForm()
        return render (request, "AppCoder/puestosFormulario.html", {"form": formulario})                            

