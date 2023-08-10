# correct require statement

exec {'correct import extension':
	command => "sudo sed -i 's/.phpp/.php/g' /var/www/html/wp-settings.php",
	path    => '/usr/local/bin/:/bin/',
 	return  => [0,1],
}
