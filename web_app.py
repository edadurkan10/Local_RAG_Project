import streamlit as st
import sqlite3

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

# Sayfa Tasarımı
st.set_page_config(page_title="Yerel RAG Asistanı", page_icon="🤖")
st.title("🤖 Çevrimdışı (Local) RAG Asistanı")
st.caption("Microsoft Foundry Local ve SQLite Tabanlı Yerel Soru-Cevap Sistemi")

# Sohbet Geçmişi Başlatma
if "messages" not in st.session_state:
    st.session_state.messages = []

# Eski mesajları ekrana basma
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Kullanıcıdan Girdi Alma
if prompt := st.chat_input("Ders notlarınızla ilgili bir soru sorun..."):
    # Kullanıcı mesajını göster ve hafızaya ekle
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Veritabanından bağlamı bul
    context = search_knowledge_base(prompt)
    
    # Yanıt Oluşturma
    response = f"**Veritabanından Bulunan Bağlam:**\n\n>{context}\n\n**Asistan Yanıtı:** Sorduğunuz '{prompt}' sorusunun cevabı yukarıdaki ders notu bağlamı içerisinde yer almaktadır."

    # Asistan yanıtını göster ve hafızaya ekle
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
