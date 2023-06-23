# create a file in /tmp
class filetest {
file { '/tmp/school':
  ensure  => present,
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
  content  => 'I love Puppet',
   }
}
