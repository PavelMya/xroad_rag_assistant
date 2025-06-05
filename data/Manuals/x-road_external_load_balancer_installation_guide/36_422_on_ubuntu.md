#### 4.2.2 on Ubuntu

```bash
sudo -u postgres pg_createcluster -p 5433 16 serverconf
```
In the above command, `16` is the *postgresql major version*. Use `pg_lsclusters` to find out what version(s) are available.