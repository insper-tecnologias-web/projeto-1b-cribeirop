import sqlite3
from dataclasses import dataclass

@dataclass
class Note:
    id: int = None
    title: str = None
    content: str = ''
           
class Database:
    def __init__(self, database):
        database = str(database)+'.db'
        self.conn = sqlite3.connect(database)
        self.note = self.conn.execute("CREATE TABLE IF NOT EXISTS note (id INTEGER PRIMARY KEY, title TEXT, content TEXT NOT NULL);")
    
    def add(self, note):
        self.conn.execute("INSERT INTO note (title, content) VALUES ('"+str(note.title)+"','"+note.content+"')")
        self.conn.commit()
    
    def get_all(self):
        cursor = self.conn.execute("SELECT * FROM note")
        result = [Note(id, title, content) for id, title, content in cursor]
        return result
    
    def update(self, entry):
        # print("UPDATE note SET title='"+str(entry.title)+"', content='"+entry.content+"' WHERE id="+str(entry.id))
        self.conn.execute("UPDATE note SET title='"+str(entry.title)+"', content='"+entry.content+"' WHERE id="+str(entry.id))
        self.conn.commit()

    def delete(self, note_id):
        self.conn.execute("DELETE FROM note WHERE id="+str(note_id))
        self.conn.commit()
