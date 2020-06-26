# Freshdesk: a helpdesk system
Freshdesk allows the export of activity information of all tickets.

## Execution
In the repo, I support a "freshdesk-auto-bash" which is a executable bash script. We can run it on Linux/Unix terminal.

**Example:**
```bash
bash ./freshdesk-auto-bash
```

## Testing
A simple and quick way is to check "ticket_activities", and "ticket_status" tables in SQLite database.

**Example:**
```bash
sqlite3 activities.db 

> select * from ticket_activities limit 10;
> select * from ticket_status limit 10;
```

## Libraries
**Python libs:**
+ argparse, pandas, json, sqlalchemy, json, datetime, time, string, random

## Reference
Data Engineer Challenge @ Anginic, Jun 2020