import mariadb
import random
import signal
from threading import Event

def update_value(temp, rhs):
    try:
        conn = mariadb.connect(
            user='root',
            password='root',
            host='mariadb',
            port=3306,
            database='example_db'
        )
    except mariadb.Error as e:
        print(f"Error connecting to db: {e}")
        return

    cur = conn.cursor()
    cur.execute(f'INSERT INTO example_table (ts_id, temperature, rhs) VALUES(NOW(), {temp}, {rhs})')
    print(f'{cur.rowcount} rows inserted')
    conn.commit()

exit = Event()

def quit(signo, _frame):
    print(f'Interrupted by {signo}, shutting down')
    exit.set()

for sig in ('TERM', 'HUP', 'INT'):
    signal.signal(getattr(signal, 'SIG'+sig), quit)

temp = 22.5
rhs = 60

while not exit.is_set():
    temp += (random.random() - 0.5) * 0.1
    rhs += (random.random() - 0.5) * 0.5
    print(f'Got ({temp}, {rhs}), updating db')
    update_value(temp, rhs)
    exit.wait(5)
