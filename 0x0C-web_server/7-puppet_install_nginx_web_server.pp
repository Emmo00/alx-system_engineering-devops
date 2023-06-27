# configure nginx server
package { 'nginx':
  ensure => installed,
}
service { 'nginx':
  ensure => running,
  enable => true,
}
file { 'add permanent redirect':
  path   => '/etc/nginx/sites-available/default',
  line   => "server_name _;\nrewrite ^/redirect_me / permanent;",
  match  => '^server\s*{',
  ensure => present,
}
file { '/var/www/html/index.html':
  path    => '/var/www/html/index.html',
  ensure  => present,
  content => 'Hello World!',
}
