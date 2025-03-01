# Google Search Script

Bu Python betiği, Google'da belirli bir sorgu için arama yaparak sonuçları listeler ve isteğe bağlı olarak bir dosyaya kaydeder. Betik, komut satırı argümanları ile esnek bir şekilde kullanılabilir.

## Özellikler

- Google'da belirli bir sorgu için arama yapar.
- Sonuçları ekrana yazdırır veya bir dosyaya kaydeder.
- Arama dilini belirleme seçeneği sunar (`lang` parametresi).
- SSL sertifikası doğrulama uyarılarını devre dışı bırakır.

## Kurulum

### Gereksinimler

- Python 3.6 veya üzeri
- `urllib3` ve `googlesearch-python` kütüphaneleri

### Adım Adım Kurulum

1. **Projeyi GitHub'dan İndirin:**

   ```bash
   git clone https://github.com/tyolsever/google-search-script.git
   cd google-search-script

Gerekli Kütüphaneleri Yükleyin:

```bash
pip install -r requirements.txt
```

Alternatif olarak, kütüphaneleri manuel olarak yükleyebilirsiniz:

```bash
pip install urllib3 googlesearch-python
```

Betiği Çalıştırın:

```bash
python google_search.py -q "inurl:.php?id=" -n 10 -l tr -o results.txt
```
## Kullanım

Betik, komut satırı argümanları ile kullanılır. Aşağıda kullanılabilir argümanların bir listesi bulunmaktadır:

| Argüman                 | Açıklama                                                                |
|-------------------------|-------------------------------------------------------------------------|
| `-q`, `--query`         | Zorunlu: Arama sorgusu (örneğin, `inurl:.php?id=`).                     |
| `-n`, `--num_results`   | Opsiyonel: Gösterilecek sonuç sayısı (varsayılan: 10).                  |
| `-l`, `--lang`          | Opsiyonel: Arama dili (örneğin, `tr` Türkçe için).                      |
| `-o`, `--output`        | Opsiyonel: Sonuçların kaydedileceği dosya adı.                          |

### Örnek Kullanımlar

- **Sadece Ekrana Yazdırma:**

  ```bash
  python script.py -q "inurl:.php?id=" -n 5

Dosyaya Kaydetme:

```bash
python google_search.py -q "inurl:.php?id=" -n 5 -l tr -o results.txt
```

Varsayılan Sonuç Sayısı ile Arama:

```bash
python google_search.py -q "inurl:.php?id="
```

Lisans
Bu proje MIT Lisansı altında lisanslanmıştır. Daha fazla bilgi için LICENSE dosyasını inceleyebilirsiniz.
