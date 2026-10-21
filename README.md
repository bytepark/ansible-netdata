[![Build Status](https://travis-ci.org/bytepark/ansible-netdata.svg?branch=master)](https://travis-ci.org/bytepark/ansible-netdata)

ansible-netdata
=========

Ansible role to install and configure Netdata

Requirements
------------

Requires bash.

Role Variables
--------------
See `defaults/main.yml` for all available variables and there usage info.

### Silencing alarms

On every run the role resets all alarms (`cmd=RESET` on the health management API) and then
silences the alarms listed in `netdata_silenced_alarms`. The reset also cancels any silencer set
outside this role, for example a maintenance window that silences all notifications while the
playbook runs. Set `netdata_reset_alarms: no` to skip the reset.

Side effect: without the reset, an alarm removed from `netdata_silenced_alarms` stays silenced
until the silencers are reset, for example by a run with `netdata_reset_alarms: yes`.

Dependencies
------------

No dependencies.


Install from github
----------------
In your ansible project's root, run:
`ansible-galaxy install git+https://github.com/bytepark/ansible-netdata.git,master`

ℹ️ Add `--force` after the command to force update your local role with latest from github.

ℹ️ You can choose another branch by changing `master` to your desired branch.


Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: bytepark.netdata }


Troubleshooting
----------------

If netdata service cannot start, there might be a file/folder permission issue, fix it by running the following on the host (not on your ansible machine)

``` 
#Fixes netdata service start errors:
chown -R netdata:root /var/lib/netdata
chown -R netdata:root /etc/netdata
```

License
-------

MIT

Author Information
------------------

bytepark / 2019.

Contributors Information
------------------
[Amir Moradi](https://github.com/amirhmoradi)
