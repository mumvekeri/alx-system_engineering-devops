#!/usr/bin/pup
# installs puppet-lint when run

package { 'puppet-lint':
    ensure   => '2.1.1',
    provider => 'gem',
}
