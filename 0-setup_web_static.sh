#!/usr/bin/env bash
# sets up server for deploying webstatic
apt-get install nginx -y
mv /etc/nginx/nginx.conf /etc/nginx/nginx.conf.backup
mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html> " > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test /data/web_static/current
chown -R ubuntu:ubuntu /data/
echo "
events { }

http {
	server {
    		listen 80;

    	location / {
        	root /var/www/html;
		add_header X-Served-By $HOSTNAME;
    	}

        location /hbnb_static {
            alias /data/web_static/current/;
        }

    	location /redirect_me {
    		return 301 https://www.youtube.com/watch?v=6KFOcDmcoBg;
	    }
    	error_page 404 /custom_404.html;
    	location = /custom_404.html {
        	root /var/www/html;
		internal;
    	}
	}
}" > /etc/nginx/nginx.conf

service nginx restart
