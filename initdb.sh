sudo /etc/init.d/mysql start
mysql -uroot -e "CREATE USER 'root'@'localhost'"
mysql -uroot -e "SET PASSWORD FOR 'root'@'localhost' = PASSWORD('pass111')"
mysql -uroot -e "CREATE DATABASE djbase"
mysql -uroot -e "GRANT ALL ON mybase.* TO 'root'@'localhost'"
