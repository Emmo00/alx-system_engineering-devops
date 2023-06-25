# config ssh on slave
exec { 'config ssh':
    path    => '/usr/bin/',
    command => "echo -e '#\tIdentityFile ~/.ssh/school' >> /etc/ssh/ssh_config; sed -i 's/#*PasswordAuthentication yes/# PasswordAuthentication no/' /etc/ssh/ssh_config",
}
