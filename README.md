# Aprendiendo Flask 🌶️

Este repositorio es mi espacio personal de práctica y documentación.

### 🎯 Objetivo
Mi meta es aprender a crear aplicaciones web con Python usando el framework **Flask**.

Iré subiendo aquí todo mi código, ejercicios y pruebas a medida que avance en mi aprendizaje, empezando desde cero.

## 📝 Notas de mi aprendizaje
>Renderizar: Llenar espacios blancos, por ejemplo un formulario en HTML que espera que el programa le dé el nombre del usuario.

>Debugging: ver los errores de forma detallada que ocurrió en nuestro programa. Esto solo se usa en el modo desarrollo, debido a que si algo tira error el debug tira exactamente las líneas de código donde se tiene dicho error.

>Request: Un navegador envia una solicitud a un servidor. Podemos saber distintos datos que vienen del cliente a nuestro servidor.

>Response: Respuesta del servidor a la solicitud del navegador
>Make_response: Nos permite redirigir hacia otra rutas pasando parametros y tambien nos permite crear cookies.

>Cookie: Como HTML no tiene memoria, entonces una cookie es un pequeño archivo de texto que el servidor le envía al navegador del cliente y guarda la info de este mismo para mostrarselo cada vez que vuelva.

>Render_template: Usamos esto para que el return haga el renderizado, le tenemos que pasar el archivo html como primer parametro y como segundo le pasamos el contexto, dicho contexto es la variable que está en el html y esa variable es igual al valor que esta almacenado en el archivo .py. Por eso se hace user_ip = user_ip. Pero la primera siempre debe llamarese como está en el template y la segunda como está en el .py

>Estructura de decisión en html: Se hace usando corchetes y porcentajes { % if % }, en el else se usa el href="{{url_for{'index} }}" y luego se cierra con un {% endif %}

>Ciclos: Para no ir declarando parametros dentro del render_template, se crea otro contexto diccionario para que contenga todos los parametros. luego para usarlo hay que descomprimirlo con un ** y así no tendremos que poner context.item, context.user_ip, etc.

>Herencia de Templates: Básicamente es poder crear un *template base* (archivo HTML) que pueda ser reutilizado en otros HTML sin tener que copiar el mismo código.

>Bloques: Jinja maneja bloques, por ende cuando heredemos necesitamos decir que cosas queremos del padre y que cosas del actual deseamos reemplazar o unir del actual HTML.

>Super: Permite llamar al atributo padre y heredar el contenido, no sobreescribirlo

>Macro: Es un HTML que contiene funciones que nos permite renderizar mini-templates para determinadas partes de nuestra interfaz
---
*Repositorio de Danilo.*