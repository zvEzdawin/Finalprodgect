import sqlite3


conn = sqlite3.connect("Jokes.db")
cursor = conn.cursor()


cursor.execute("""
    CREATE TABLE IF NOT EXISTS Jokes (
        id INTEGER PRIMARY KEY,
        joke TEXT
    );
""")


jokes_data = [
    "Заходит программист в лифт, а ему надо на 12—й этаж. Нажимает 1, потом 2 и начинает лихорадочно искать кнопку Enter.",
    "Жил—был программист и было у него два сына — Антон и Неантон.",
    "Если бы программисты были врачами, им бы говорили «У меня болит нога», а они отвечали «Ну не знаю, у меня такая же нога, а ничего не болит».",
    "Программисты на работе общаются двумя фразами: «непонятно» и «вроде работает».",
    "Программист жене: — СD молча и не DVD меня до белого каления!"
]

cursor.executemany("INSERT INTO Jokes (joke) VALUES (?)", [(joke,) for joke in jokes_data])


conn.commit()
conn.close()