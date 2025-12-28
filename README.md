# Aprendiendo Flask 🌶️

Este repositorio es mi espacio personal de práctica y documentación.

### 🎯 Objetivo
Mi meta es aprender a crear aplicaciones web con Python usando el framework **Flask**.

Iré subiendo aquí todo mi código, ejercicios y pruebas a medida que avance en mi aprendizaje, empezando desde cero.

## 📝 Notas de mi aprendizaje
>Requirements: Para poner los requerimientos automáticos usar *pip freeze > requeriments.txt*

>Renderizar: Llenar espacios blancos, por ejemplo un formulario en HTML que espera que el programa le dé el nombre del usuario.

>Debugging: ver los errores de forma detallada que ocurrió en nuestro programa. Esto solo se usa en el modo desarrollo, debido a que si algo tira error el debug tira exactamente las líneas de código donde se tiene dicho error.

>Request: Un navegador envia una solicitud a un servidor. Podemos saber distintos datos que vienen del cliente a nuestro servidor.

>Remote_addr: Nos sirve para saber de dónde es la IP del cliente. Nos sirve para saver de que país es y mostrarle la página en su idioma, por si intentá entrar a una cuenta 50 veces y le podemos bloquear su IP o por ejemplo si ya votó en una encuesta, no lo dejamos votar de neuvo.

>Response: Respuesta del servidor a la solicitud del navegador.

>Make_response: Nos permite redirigir hacia otra rutas pasando parametros y tambien nos permite crear cookies.

>Cookie: Como HTML no tiene memoria, entonces una cookie es un pequeño archivo de texto que el servidor le envía al navegador del cliente y guarda la info de este mismo para mostrarselo cada vez que vuelva.

>Render_template: Usamos esto para que el return haga el renderizado, le tenemos que pasar el archivo html como primer parametro y como segundo le pasamos el contexto, dicho contexto es la variable que está en el html y esa variable es igual al valor que esta almacenado en el archivo .py. Por eso se hace user_ip = user_ip. Pero la primera siempre debe llamarese como está en el template y la segunda como está en el .py

>Estructura de decisión en html: Se hace usando corchetes y porcentajes { % if % }, en el else se usa el href="{{url_for{'index} }}" y luego se cierra con un {% endif %}

>Ciclos: Para no ir declarando parametros dentro del render_template, se crea otro contexto diccionario para que contenga todos los parametros. luego para usarlo hay que descomprimirlo con un ** y así no tendremos que poner context.item, context.user_ip, etc.

>Herencia de Templates: Básicamente es poder crear un *template base* (archivo HTML) que pueda ser reutilizado en otros HTML sin tener que copiar el mismo código.

>Bloques: Jinja maneja bloques, por ende cuando heredemos necesitamos decir que cosas queremos del padre y que cosas del actual deseamos reemplazar o unir del actual HTML.

>Super: Permite llamar al atributo padre y heredar el contenido, no sobreescribirlo

>Macro: Es un HTML que contiene funciones que nos permite renderizar mini-templates para determinadas partes de nuestra interfaz

>Templates estátivos: Son HTML que siempre vamos a usar en todos los demas HTML, por eso es que son estáticos. Por ejemplo la barra de navegación.

>Archivos estáticos: Son archivos que siempre vamos a usar, por eso van en la carpeta static y adentro pondremos el CSS e imágenes dentro de sus respectivas carpetas.

>Manejo de errores: Para manejar errores de forma personalizada (como no encontrar la ruta) usamos *errorhandler(404)*

>Bootstrap: Es un framework frontend que nos permite crear interfaces. 

>Session: Nos permite guardar de forma encriptada los datos que se almacenan en las cookies. Para que esto sea posible tenemos que configurar un *secret key*. Ya que es necesario para descifrar los datos.Ahora vamos a guardar los datos en una sesión, no en una cookie; Esto nos permite que si alguien modifica la cookie, al recargar la página, vuelva al valor original almacenado.

>Entorno de Flask: Cuando corremos la app, estamos en un servidor de producción. Ahora queremos que el entorno cambie a desarrollo. Exportamos *FLASK_ENV=development* y verificamos con *echo $FLASK_ENV*

>Formularios: Usamos desde bootstrap/wtf.html el cual renderiza formularios.

>Validadores: En wtforms encontramos los validators, en este caso, DataRequired se encarga de que haya información cargada en los campos.

>Mensajes Flash: Son mensajes o alertas que son disparadas en el contenido HTML para que un usuario obtenga instrucciones para realizar un determinado proceso. La razón por la cual se usa la clase *alert alert-success alert-dismissible* es para que se cree un boton que quite el mensaje y no se quede renderizado en la pantalla. Dentro de los atributos del boton tendra un data-dismiss y clase close para cerrar. El *&times;* es una forma antigua de hacer un signo por (en este caso es la x de cierre). La ventana no se va a cerrar con ese signo, así que hay que importar los scripts en el base.html.

>Test: Nos permiten probar nuestra app antes de salir a producción. *Flask_testing* va  a ser la libreria para hacer los test. Lo que hacemos es analizar los objetos de respuesta (Ej: ver si el endpoint '/index' funciona correctamente). Para eso necesitamos importar unittest, crear un comando propio para usar en consola, definimos la función test, creamos una instancia de unittest, usamos la clase 'TestLoader', la cual necesita el atributo 'discover' y este atributo recibe como parametro la carpeta donde estaran los tests. Para poder hacer los tests, debemos correr el comando *config.bat development main.py*. Esto hace que windows lea el config.bat, agarra la palabra development y lo mete en donde se puse %1, luego agarra la palabra main.py y lo mete en donde se puso %2. Ejecuta los set y muestra el mensaje de confirmación. Para comprobar que funciona ejecutamos el comando *echo %FLASK_APP%* y debe mostrar *main.py*.

>Escribir los tests: Cuando corremos el *flask test* busca en la carpeta test todos los archivos que empiezan con dicha palabra. En el *test_app* vamos a escribir el algoritmo necesario para probar la aplicación web.

>AssertRedirect: Tuve que agregar el *_external=True* debido a que el test busca URLs absolutas, sin el external es relativa
---
*Repositorio de Danilo.*