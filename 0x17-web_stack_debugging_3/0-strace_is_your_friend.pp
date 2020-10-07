# fixes Apache error 500 by fixing typo in wordpress
exec { 'fix typo':
  onlyif   => 'test -e /var/www/html/wp-settings.php',
  provider => shell,
  path     => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  command  => "sed -i 's/phpp/php/' /var/www/html/wp-settings.php",
}
