### Etapa 1: Construcción de la aplicación Vue.js
FROM node:18-alpine AS build
WORKDIR /app
# Copiar los archivos de dependencias
COPY package*.json ./
# Instalar dependencias
RUN npm install
# Copiar el resto del código fuente
COPY . .
# Construir la aplicación para producción
RUN npm run build

### Etapa 2: Servir la aplicación con Nginx
FROM nginx:stable-alpine
# Copiar los archivos construidos al directorio de Nginx
COPY --from=build /app/dist /usr/share/nginx/html
COPY default.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
