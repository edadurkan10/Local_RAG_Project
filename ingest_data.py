import sqlite3

def init_db():
    # SQLite veritabanına bağlan (yoksa otomatik oluşturur)
    conn = sqlite3.connect('rag_database.db')
    cursor = conn.cursor()
    
    # Parçalanmış metinleri tutacak tabloyu oluştur
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS document_chunks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            chunk_text TEXT
        )
    ''')
    conn.commit()
    conn.close()
    print("SQLite Veritabanı ve tablo hazırlandı.")

def ingest_document(file_path):
    conn = sqlite3.connect('rag_database.db')
    cursor = conn.cursor()
    
    # Önceki verileri temizleyelim (test için)
    cursor.execute('DELETE FROM document_chunks')
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Dokümanı çift satır sonuna (paragraflara) göre parçalayalım
    chunks = [chunk.strip() for chunk in content.split('\n\n') if chunk.strip()]
    
    for i, chunk in enumerate(chunks):
        cursor.execute('''
            INSERT INTO document_chunks (title, chunk_text)
            VALUES (?, ?)
        ''', (f"Parça {i+1}", chunk))
    
    conn.commit()
    conn.close()
    print(f"Toplam {len(chunks)} parça SQLite veritabanına başarıyla kaydedildi!")

if __name__ == "__main__":
    init_db()
    ingest_document('ders_notlari.txt')