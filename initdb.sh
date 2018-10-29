sudo /etc/init.d/mysql start
mysql -uroot -e "CREATE DATABASE djbase;"

sudo python /home/box/web/ask/manage.py syncdb
