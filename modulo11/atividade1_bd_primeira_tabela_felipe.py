import sqlite3

conn = sqlite3.connect('atividade_info_cliente.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        email TEXT NOT NULL
    )
''')

cursor.execute('''
    INSERT INTO clientes (nome, email) VALUES 
    ('Felipe Mendes', 'felipe.mendes@mail.com'),
    ('Samuel Sousa', 'samuel.sousa@mail.com')
''')

conn.commit()

conn.close()
