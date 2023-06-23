# killmenow
exec { 'killmenow':
    command => 'pkill -f "killmenow"',
    path    => '/usr/local/bin/:/bin/',
  }