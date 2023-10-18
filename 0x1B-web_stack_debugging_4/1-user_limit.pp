# This Puppet code defines two `exec` resources that modify the file
# `/etc/security/limits.conf` to increase the hard and soft file limits for
# the "holberton" user. The "exec" resource is used to execute shell commands.

# Increase the hard file limit for the "holberton" user to 50000.
exec { 'increase-hard-file-limit-for-holberton-user':
  command => 'sed -i "/holberton hard/s/4/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

# Increase the soft file limit for the "holberton" user to 50000.
exec { 'increase-soft-file-limit-for-holberton-user':
  command => 'sed -i "/holberton soft/s/5/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
