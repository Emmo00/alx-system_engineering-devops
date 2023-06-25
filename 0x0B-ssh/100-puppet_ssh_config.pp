file { '~/.ssh':
    ensure => directory,
    owner  => 'ubuntu',
    group  => 'ubunty',
    mode   => '0700',
  }

  file { '~/.ssh/school':
    ensure => present,
    owner  => 'ubuntu',
    group  => 'ubuntu',
    mode   => '0600',
  }

  file { '/etc/ssh/ssh_config':
    ensure  => present,
    owner   => 'ubuntu',
    group   => 'ubuntu',
    mode    => '0600',
    content => "Host *\n    IdentityFile ~/.ssh/school\n    PasswordAuthentication no\n",
  }
