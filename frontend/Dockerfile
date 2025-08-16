# frontend/Dockerfile
FROM nginx:alpine

# Copiamos el index.html a la carpeta que Nginx usa por defecto
COPY index.html /usr/share/nginx/html/index.html

# Exponemos el puerto 80
EXPOSE 80

# Nginx ya viene con CMD que ejecuta en primer plano
