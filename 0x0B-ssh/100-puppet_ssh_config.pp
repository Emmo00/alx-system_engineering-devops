file { '~/.ssh':
    ensure => directory,
    owner  => 'ubuntu',
    group  => 'ubunty',
    mode   => '0700',
  }

  file { '~/.ssh/config':
    ensure  => present,
    owner   => 'ubuntu',
    group   => 'ubuntu',
    mode    => '0600',
    content => "Host *\n    IdentityFile ~/.ssh/school\n    PasswordAuthentication no\n",
  }
