from foundry_local_sdk import FoundryLocalManager, Configuration

def main():
    print("Foundry Local başlatılıyor...")
    config = Configuration(app_name="LocalRAGApp")
    manager = FoundryLocalManager(config)
    
    print("Katalog nesnesi kontrol ediliyor...")
    catalog = manager.catalog
    print("Bağlantı başarılı! SDK tam olarak hazır.")

if __name__ == "__main__":
    main()