# Increases the open file limit for Nginx.                                               $
exec { 'increase-limit':                                                                 $
  onlyif   => 'test -e /etc/default/nginx',                                              $
  command  => 'sed -i "s/15/4096/" /etc/default/nginx; service nginx restart',           $
  provider => shell,                                                                     $
}
