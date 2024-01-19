#!/usr/bin/pup
# installs puppet-lint when run

# File: site.pp

# Ensure Python is installed
package { 'python3':
  ensure => present,
}

# Ensure pip is installed
package { 'python3-pip':
  ensure => present,
}

# Install Flask using pip3
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => [Package['python3'], Package['python3-pip']],
}
