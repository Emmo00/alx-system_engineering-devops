# configure nginx server
package { 'nginx':
  ensure => installed,
}

exec { 'add nginx index': 
     path    => '/usr/bin', 
     command => "echo 'Hello World!' | sudo tee /var/www/html/index.html ; ", 
}

exec { 'configure redirect nginx': 
     path    => '/usr/bin', 
     command => "sudo sed -i \"s/^[^#].*server_name.*/server_name _;\nrewrite ^\/redirect_me \/ permanent;/\" /etc/nginx/sites-available/default ; sudo service nginx start;", 
}