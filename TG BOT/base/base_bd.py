import sqlite3 as sq


def start_base():
    global base, cur
    base = sq.connect("barber.pd")
    cur = base.cursor()
    if base:
        print("Data connect")
    base.execute("CREATE TABLE IF NOT EXISTS Services(name TEXT PRIMARY KEY, description TEXT, price TEXT)")
    base.commit()

async def sql_add_command(state):
    async with state.proxy() as date:
        cur.execute("INSERT INTO Services VALUES (?, ?, ?)", tuple(date.values()))
        base.commit()
        print("save_Services")

async def sql_read(call):
    for ret in cur.execute("SELECT * FROM Services").fetchall():
        await call.message.bot.send_message(call.message.chat.id, f"name of the service : {ret[0]}\ndescription {ret[1]}\nprice {ret[2]}")

