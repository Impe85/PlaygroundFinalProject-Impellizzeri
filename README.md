# PlaygroundFinalProject-Impellizzeri

Blog de Arquería en Django
Este proyecto es un blog de arquería desarrollado con Django, el popular framework de desarrollo web en Python. A continuación se detallan los pasos y configuraciones principales para entender y trabajar con este proyecto.

Configuración del Entorno
Python y Django deben estar instalados.
Se recomienda usar un entorno virtual para la gestión de dependencias.

Estructura del Proyecto
Proyecto Django: blog_arqueria
Aplicación Django: arqueria
Modelos: El modelo principal es Post, que representa los artículos del blog.
Vistas y URLs: Se utilizan vistas genéricas de Django para las operaciones CRUD (Crear, Leer, Actualizar, Eliminar).
Plantillas: Las plantillas HTML se encuentran en arqueria/templates/arqueria.
Archivos Estáticos: Los archivos CSS y JavaScript personalizados están en la carpeta static.

Características Principales
CRUD para Posts: Los usuarios pueden crear, leer, actualizar y eliminar posts.
Plantillas con Bootstrap: Se utiliza Bootstrap para un diseño responsivo y moderno.
Barra de Navegación: Incluida en base.html para una navegación fácil entre las secciones del blog.
Estilos Personalizados: Posibilidad de añadir estilos personalizados en static/css/styles.css.

Configuración de base.html
Bootstrap: Integrado para el diseño responsivo y los componentes UI.
Estructura Base: Se incluyen secciones como <header>, <main>, y <footer>.

Archivos Estáticos
Se manejan a través de la carpeta static en la raíz del proyecto.
Configuración en settings.py para referenciar correctamente estos archivos.
