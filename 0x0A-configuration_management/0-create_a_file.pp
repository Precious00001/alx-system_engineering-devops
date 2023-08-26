# Creating A file in tmp folder named school

file { '/tmp/school':
  content =>'I love Puppet',
  owner   => 'www-data',
    mode    => '0744',
  group   => 'www-data',
}
