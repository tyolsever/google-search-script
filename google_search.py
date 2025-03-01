import argparse
import urllib3
from googlesearch import search
import os

os.system('clear')

# Uyarıları devre dışı bırak
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def google_search(query, num_results=10, lang=None):
    urls = []
    try:
        # Eğer lang parametresi tanımlıysa, arama dilini belirle
        if lang:
            search_results = search(query, num_results=num_results, lang=lang, ssl_verify=False)
        else:
            search_results = search(query, num_results=num_results, ssl_verify=False)
        
        # Google'da arama yap ve sonuçları listeye ekle
        for url in search_results:
            urls.append(url)
            if len(urls) >= num_results:
                break
    except Exception as e:
        print(f"Arama sırasında bir hata oluştu: {e}")
    return urls

def main():
    parser = argparse.ArgumentParser(description="Google'da arama yap ve URL'leri listele.")
    parser.add_argument("-q", "--query", required=True, help="Arama sorgusu.")
    parser.add_argument("-n", "--num_results", type=int, default=10, help="Gösterilecek URL sayısı.")
    parser.add_argument("-l", "--lang", help="Arama dili (örneğin, 'tr' Türkçe için).")
    parser.add_argument("-o", "--output", help="Çıktı dosyası (opsiyonel).")
    args = parser.parse_args()
    
    # Google'da arama yap
    urls = google_search(args.query, args.num_results, args.lang)
    
    # Sonuçları ekrana yazdır
    for url in urls:
        print(url)
    
    # Eğer -o parametresi verilmişse, sonuçları dosyaya yaz
    if args.output:
        with open(args.output, "w") as file:
            for url in urls:
                file.write(url + "\n")
        print(f"Sonuçlar '{args.output}' dosyasına kaydedildi.")

if __name__ == "__main__":
    main()
