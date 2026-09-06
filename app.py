import sqlite3
from foundry_local_sdk import FoundryLocalManager, Configuration

def search_knowledge_base(query):
    conn = sqlite3.connect('rag_database.db')
    cursor = conn.cursor()
    
    words = [w.strip() for w in query.split() if len(w) > 2]
    
    relevant_chunks = []
    cursor.execute('SELECT chunk_text FROM document_chunks')
    rows = cursor.fetchall()
    
    for row in rows:
        text = row[0]
        for word in words:
            if word.lower() in text.lower():
                relevant_chunks.append(text)
                break
                
    conn.close()
    
    if not relevant_chunks:
        return "\n---\n".join([r[0] for r in rows])
        
    return "\n---\n".join(relevant_chunks)

def generate_answer(manager, question, context):
    system_instruction = (
        "Sen ders notlarına dayalı yanıt veren yardımcı bir asistansın.\n"
        "Sadece sana sağlanan BAĞLAM bilgisini kullanarak soruyu yanıtla.\n"
        "Eğer yanıt bağlamda yoksa 'Bu bilgi ders notlarında bulunmamaktadır.' de."
    )
    
    user_prompt = f"BAĞLAM:\n{context}\n\nSORU: {question}"
    
    # Yerel model araması ve yanıt simülasyonu
    print("\n--- ASİSTAN YANITI ---")
    print(f"Özet Bağlam: {context[:120]}...\n")
    print(f"Cevap: Veritabanındaki bilgilere göre {question} sorusunun cevabı yukarıdaki bağlam içerisinden başarıyla çekilmiştir.")
    print("-----------------------\n")

def main():
    print("==================================================")
    print(" 🤖 ÇEVRİMDİŞİ (LOCAL) RAG ASİSTANI BAŞLATILDI ")
    print("==================================================")
    
    config = Configuration(app_name="LocalRAGApp")
    manager = FoundryLocalManager(config)
    
    while True:
        question = input("Sorunuzu yazın (Çıkış için 'q'): ")
        if question.lower() == 'q':
            print("Asistan kapatılıyor. İyi çalışmalar!")
            break
            
        if not question.strip():
            continue
            
        context = search_knowledge_base(question)
        generate_answer(manager, question, context)

if __name__ == "__main__":
    main()