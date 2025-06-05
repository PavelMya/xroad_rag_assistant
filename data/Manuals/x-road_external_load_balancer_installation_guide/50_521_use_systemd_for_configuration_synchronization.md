#### 5.2.1 Use systemd for configuration synchronization

First, add `xroad-sync` as a `systemd` service.

Create a new file `/etc/systemd/system/xroad-sync.service`:

```
[Unit]
Description=X-Road Sync Task
After=network.target
Before=xroad-proxy.service
Before=xroad-signer.service
Before=xroad-confclient.service
Before=xroad-proxy-ui-api.service
[Service]
User=xroad
Group=xroad
Type=oneshot
Environment=XROAD_USER=xroad-slave
Environment=MASTER=<primary_host>

ExecStartPre=/usr/bin/test ! -f /var/tmp/xroad/sync-disabled

ExecStart=/usr/bin/rsync -e "ssh -o ConnectTimeout=5 " -aqz --timeout=10 --delete-delay --exclude db.properties --exclude "/conf.d/node.ini" --exclude "*.tmp" --exclude "/postgresql" --exclude "/globalconf" --exclude "/gpghome" --delay-updates --log-file=/var/log/xroad/slave-sync.log ${XROAD_USER}@${MASTER}:/etc/xroad/ /etc/xroad/
[Install]
WantedBy=multi-user.target
WantedBy=xroad-proxy.service
```
Where `<primary_host>` is the DNS name or IP address of the primary node.

The service will log `rsync` events to `/var/log/xroad/slave-sync.log`.

Then, add a timer for periodic updates.

Create a new file `/etc/systemd/system/xroad-sync.timer`:

```
[Unit]
Description=Sync X-Road configuration
[Timer]
OnBootSec=60
OnUnitActiveSec=60
[Install]
WantedBy=timers.target
```

RHEL only: Configure SELinux to allow `rsync` to be run as a `systemd` service

```bash
setsebool -P rsync_client 1
setsebool -P rsync_full_access 1
```
>**Note:** If the applications or services running on the system are customized, updating the SELinux policy to reflect the changes may be required, see [more information](https://access.redhat.com/articles/5494701).

Finally, enable the services:
```bash
systemctl enable xroad-sync.timer xroad-sync.service
systemctl start xroad-sync.timer
```

>**About the `rsync` options**
>
>* `--delay-updates` and `--delete-delay` make the sync more atomic by delaying modifications until data has been
>  downloaded. It is not fully atomic, however, since the files will be moved into place one by one. If the synchronization
>  is disrupted, no modifications will be made.
>* low connect timeout (5 seconds) and receive timeout (10 seconds) ensure that the synchronization won't hang if e.g.
>  a network connection fails.