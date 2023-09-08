# increased the max number of files opened by nginx

exec {'increase max number of files':
  command => "sudo sed -i 's/ULIMIT=\"-n 15\"/ULIMIT=\"-n 30000\"/g' /etc/default/nginx",
  path    => '/usr/local/bin/:/bin/',
}
