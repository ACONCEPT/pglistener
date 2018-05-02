from postgreslib.postgres_cursor import get_cursor, get_cursor
from postgreslib.queries import watch_table, execute_query,execute_cursor
from postgreslib.create_tables import create_tables

with open("watch.sql","r") as f:
    watch = f.read()

conn = get_cursor(return_connection = True)[0]
execute_cursor(watch)
create_tables()

watch_table("parts")
while True:
	conn.poll()
	while conn.notifies:
		notify = conn.notifies.pop(0)
		print( "Got NOTIFY:", notify.pid, notify.channel, notify.payload)
