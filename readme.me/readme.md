Optimizador de Portafolio

Autora: Daniela Cecilia Coello Pabon
El Optimizador de Portafolio es una aplicación web diseñada para seleccionar proyectos según su peso y ganancia máxima. Utiliza una arquitectura moderna con un backend en FastAPI, un frontend en HTML/JavaScript y despliegue en contenedores con Docker y Docker Compose.

Tabla de Contenidos

Estructura del Proyecto
Características
Requisitos
Configuración y Ejecución
Uso
Comandos Útiles
Notas
Licencia


Estructura del Proyecto
C:\Coello_Daniela_Examen_Final_Arquitectura
│
├─ backend/                  # Código y Dockerfile del backend
│  ├─ Dockerfile            # Configuración de Docker para el backend
│  └─ app/                 # Archivos de la aplicación FastAPI
│
├─ frontend/                 # Código y Dockerfile del frontend
│  ├─ Dockerfile            # Configuración de Docker para el frontend
│  └─ index.html           # Frontend en HTML y JavaScript
│
└─ docker-compose.yml       # Configuración de Docker Compose


Características

Optimización de Proyectos: Selecciona proyectos para maximizar la ganancia dentro de una capacidad de peso dada.
Backend en FastAPI: API eficiente para cálculos de optimización.
Frontend Interactivo: Interfaz amigable para agregar proyectos y visualizar resultados.
Despliegue con Docker: Configuración sencilla con Docker y Docker Compose.
Compatibilidad sin CORS: Comunicación fluida entre frontend y backend en la red de Docker.


Requisitos

Docker Desktop instalado y en ejecución.
Docker Compose (incluido en Docker Desktop).
Navegador web moderno (Chrome, Firefox, Edge, etc.).


Configuración y Ejecución
1️⃣ Construir las imágenes Docker
Desde la carpeta raíz del proyecto, ejecuta:
docker-compose build

Esto generará las imágenes para los servicios backend y frontend.
2️⃣ Levantar los contenedores
Ejecuta los contenedores en segundo plano con:
docker-compose up -d


Backend: Disponible en http://localhost:8000
Frontend: Disponible en http://localhost:8080

3️⃣ Verificar contenedores en ejecución
Comprueba que los contenedores estén activos:
docker ps

Salida esperada:
CONTAINER ID   IMAGE                                     STATUS         PORTS
...backend     coello_daniela_examen_final_arquitectura-backend   Up      0.0.0.0:8000->8000/tcp
...frontend    coello_daniela_examen_final_arquitectura-frontend  Up      0.0.0.0:8080->80/tcp


Uso

Abre tu navegador en http://localhost:8080.
Agrega proyectos especificando Nombre, Peso y Ganancia.
Define la Capacidad máxima del portafolio.
Haz clic en Calcular para obtener los proyectos seleccionados.
Visualiza la tabla de resultados con la Ganancia total y el Peso total.


Comandos Útiles

Ver logs del backend:

docker-compose logs backend


Ver logs del frontend:

docker-compose logs frontend


Detener los contenedores:

docker-compose down


Limpiar contenedores y volúmenes:

docker-compose down -v


Notas

El frontend se comunica con el backend mediante la URL http://backend:8000/optimizar dentro de la red de Docker.
Nginx sirve el frontend directamente desde /usr/share/nginx/html/index.html.
La lógica completa para agregar proyectos, calcular optimización y mostrar resultados está implementada en index.html.
No hay problemas de CORS gracias a la red interna de Docker.


Licencia
Este proyecto está licenciado bajo los términos de la Licencia MIT. Consulta el archivo LICENSE para más detalles.