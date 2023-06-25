file { '~/.ssh':
    ensure => directory,
    owner  => 'slave',
    group  => 'slave',
    mode   => '0700',
  }

  file { '~/.ssh/school':
    ensure => present,
    owner  => 'slave',
    group  => 'slave',
    mode   => '0600',
    source => 'puppet:///modules/ssh_slave_config/school',
  }

  file { '/etc/ssh/ssh_config':
    ensure  => present,
    owner   => 'slave',
    group   => 'slave',
    mode    => '0600',
    content => "Host *\n    IdentityFile ~/.ssh/school\n    PasswordAuthentication no\n",
  }
