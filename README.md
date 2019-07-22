[![Build Status](https://travis-ci.org/bytepark/ansible-netdata.svg?branch=master)](https://travis-ci.org/bytepark/ansible-netdata)

ansible-netdata
=========

Ansible role to install and configure Netdata

Requirements
------------

Requires bash.

Role Variables
--------------
Variable defaults

```
netdata.user
netdata.webfiles_owner
netdata.webfiles_group
netdata.bind_ip
netdata.registry_enabled
netdata.registry
netdata.registry_hostname
netdata.silenced_alarms
```


Dependencies
------------

No dependencies.

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: bytepark.netdata }

License
-------

MIT

Author Information
------------------

bytepark / 2019.
