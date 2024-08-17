FROM nginx:latest

COPY docker/web/default.conf /etc/nginx/conf.d/default.conf
COPY staticfiles/ /var/www/static

EXPOSE 80:80
