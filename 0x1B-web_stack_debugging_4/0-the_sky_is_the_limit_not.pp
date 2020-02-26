# changed ulimit value for max open files
exec { '/etc/default/nginx':
  command => "sed -i 's/15/2000/g' /etc/default/nginx",
  path    => '/bin/',
}

service { 'nginx':
  ensure    => running,
  subscribe => Exec['/etc/default/nginx'],
}
