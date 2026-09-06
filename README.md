 🤖 Çevrimdışı (Local) RAG Asistanı

Bu proje, Microsoft Foundry Local SDK ve SQLite veritabanı altyapısını kullanarak yerel ders notları üzerinde offline arama ve yanıt üretimi yapan bir RAG (Retrieval-Augmented Generation) sistemidir.

 🚀 Özellikler
- **Tamamen Çevrimdışı:** İnternet bağlantısı gerektirmeden yerel cihazda çalışır.
- **SQLite Veritabanı:** Dokümanlar parçalanarak (chunking) ilişkisel veritabanında saklanır.
- **Streamlit Web Arayüzü:** Kullanıcı dostu modern sohbet ekranı sunar.

 🛠️ Çalıştırma Adımları

1. Gerekli kütüphaneleri yükleyin:
   ```bash
   pip install foundry-local-sdk sqlite3 streamlit
