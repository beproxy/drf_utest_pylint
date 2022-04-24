server {
	listen 8080;
	client_max_body_size 0;
    server_name  _ default;

    proxy_pass_request_headers on;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header Host $http_host;
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_redirect off;

    location ~* /api/.*|admin(?:/(.*))? {
        proxy_pass              http://backend:8000;
    }

    location ^~ /staticfiles {
        alias /home/django/static;
        autoindex off;
    }
}
