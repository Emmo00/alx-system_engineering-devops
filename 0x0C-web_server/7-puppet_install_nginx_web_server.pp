# configure nginx server
package { 'nginx':
  ensure => installed,
}

exec { 'add nginx index': 
     path    => '/usr/bin', 
     command => "echo 'Hello World!' | sudo tee /var/www/html/index.html ; ", 
}

# Define the Nginx configuration file
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "
    server {
      listen 80;
      server_name _;
      
      location /redirect_me {
        return 301 /;
      }
      
      # Include other Nginx configuration directives as needed
      
      # ...
    }
  ",
  notify  => Service['nginx'],
}
