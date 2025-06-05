### 5.6 Data quality issues in the database

The following error message may come up during the Central Server upgrade.

`Data quality issues in the XXXXX database. ...`

Before upgrading the packages from the current version to the target version, incorrect data in the postgreSQL database needs to be fixed.

For example, if the error message says:

```bash
root@test-cs:~# apt upgrade xroad-centralserver
...
Preparing to unpack .../xroad-center_7.4.0-1.ubuntu22.04_all.deb ...

ERROR: Data quality issues in the centerui_production database. There are duplicate data in the table SYSTEM_PARAMETERS columns pair (KEY, HA_NODE_NAME):.........................................................] 
----------------------------------------------------------------------------------------------------------------------------------------------
id|key|value|created_at|updated_at|ha_node_name|count
12|instanceIdentifier|cs|2021-03-10 07:37:26.59307|2021-03-10 07:37:26.59307|node_0|2
1|instanceIdentifier|CS|2021-03-10 07:37:26.59307|2021-03-10 07:37:26.59307|node_0|2
(2 rows)
----------------------------------------------------------------------------------------------------------------------------------------------
...
Please fix incorrect data before continuing.
```

To fix incorrect data, login to the postreSQL database server. By default, the database is named `centerui_production`, database user and schema both are named `centerui`.

```bash
psql -h <database host> -U <database user> -d <database>
```  

and run script that shows all duplicate data in the SYSTEM_PARAMETERS table.

```sql
select * from (select *, count(*) over (partition by key, ha_node_name order by key, ha_node_name) as count
      from system_parameters) as s
where s.count > 1;
```

If script return data, then delete thus system parameters rows what system parameter value is not used or just delete one duplicate row if the values is same.

```sql
delete from system_parameters where id = 12;
```

The interrupted installation can be finished using:

```bash
sudo apt --fix-broken install
```