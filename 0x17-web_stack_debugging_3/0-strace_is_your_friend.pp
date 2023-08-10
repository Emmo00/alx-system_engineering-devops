# correct require statement

exec {'correct import extension':
	command => "sudo sed -i 's/class-wp-locale.phpp/class-wp-locale.php/g' /var/www/html/wp-settings.php",
	path    => '/usr/local/bin/:/bin/',
}
