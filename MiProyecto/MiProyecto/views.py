from django.http import HttpResponse
import datetime
from django.template import Template, Context

# Request: Para realizar peticiones
# HttpResponse: Para enviar la respuesta usando el protocolo http.

#Esto es una vista. 
def bienvenida(request ): #Aqui pasamos un objeto de tipo request como argumento 
    return HttpResponse("Bienvenido o bienvenida a este curso de Django.")

def bienvenidaRojo(request ): #Aqui pasamos un objeto de tipo request como argumento 
    return HttpResponse("<p style='color: red'>Bienvenido o bienvenida a este curso de Django.</p>")

def categoriaEdad( request, edad):
    if edad >=18:
        if edad >= 60:
            categoria = "Tercera Edad"
        else:
            categoria = "Adultez"
    else:
        if edad <= 10:
            categoria = "Infancia"
        else:
            categoria = "Adolecencia"
    resultado = "<h1> Categoría de la edad: %s</h1>" %categoria
    return HttpResponse(resultado)

def obtenerMomentoActual(request):
    #respuesta = "<h1> Momento Actual: {0} </h1>" .format(datetime.datetime.now())
    respuesta = "<h1> Momento Actual: {0} </h1>" .format(datetime.datetime.now().strftime("%A %d/%m/%Y %H:%M:%S"))
    return HttpResponse(respuesta)

def contenidoHTML(request, nombre, edad):
    contenido = """
    <html>
    <body>
    <p> Nombre: %s / Edad: %s </p>
    </body>
    </html>
    """ %( nombre, edad )
    return HttpResponse(contenido)

def miPrimeraPlantilla(request):
    #abrimos el documento que contiene a la plantilla
    plantillaExterna = open( "C:/Users/jorge/OneDrive/Documentos/Python/Django/Proyectos Django/MiProyecto/MiProyecto/plantilla/miPrimeraPlantilla.html" )
    template = Template(plantillaExterna.read())
    plantillaExterna.close()
    #crear un contexto
    contexto = Context()
    #renderizar el documento
    documento = template.render(contexto)
    return HttpResponse(documento) 

def plantillaParametros(request):
    """
    Este es un comentario
    multi Linea
    """
    nombreyapellido = "Jorge Ambrosio"
    fechaActual = datetime.datetime.now()
    lenguajes = ["Python", "Ruby", "JavaScript" , "Java", "C#" , "Kotlin"]
    #abrimos el documento que contiene a la plantilla
    plantillaExterna = open( "C:/Users/jorge/OneDrive/Documentos/Python/Django/Proyectos Django/MiProyecto/MiProyecto/plantilla/plantillaParametrosHTML.html" )
    template = Template(plantillaExterna.read())
    plantillaExterna.close()
    #crear un contexto
    contexto = Context({"nombre":nombreyapellido , "fechaActual" : fechaActual , "lenguajes": lenguajes })
    #renderizar el documento
    documento = template.render(contexto)
    return HttpResponse(documento) 
