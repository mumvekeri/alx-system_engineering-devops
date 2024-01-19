#!/usr/bin/pup
# my_flask_module/manifests/init.pp

class my_flask_module {
  package { 'python3-pip':
    ensure => installed,
  }

  exec { 'install_flask':
    command => '/usr/bin/pip3 install flask==2.1.0',
    unless  => '/usr/bin/pip3 show flask | grep -q "Version: 2.1.0"',
    require => Package['python3-pip'],
  }
}

include my_flask_module

