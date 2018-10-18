sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf

sudo rm -rf /etc/nginx/sites-enabled/default

sudo /etc/init.d/nginx restart

sudo ln -s /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
sudo ln -sf /home/box/web/etc/gunicorn-django.conf /etc/gunicorn.d/test-django

sudo /etc/init.d/gunicorn restart
