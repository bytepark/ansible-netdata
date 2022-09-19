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
netdata_user
netdata_webfiles_owner
netdata_webfiles_group
netdata_bind_ip
netdata_registry_enabled
netdata_registry
netdata_registry_hostname
netdata_silenced_alarms
netdata_monitored_vhosts
netdata_ml
netdata_claim_token
netdata_claim_room
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
