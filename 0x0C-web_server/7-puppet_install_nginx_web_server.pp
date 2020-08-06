# Install and configure Nginx on a web server with Puppet

package { 'nginx':
    ensure => installed,
    name   => 'nginx',
}

file { 'index.html':
    path    => '/var/www/html/index.html',
    content => 'Holberton School',
}

file_line { 'title':
    ensure   => present,
    path     => '/etc/nginx/sites-available/default;',
    after    => 'server_name _;',
    line     => 'rewrite ^/redirect_me https://www.holbertonschool.co permanent;',
    multiple => true,

}

service { 'nginx':
    ensure  => running,
    require => Package['nginx'],
}