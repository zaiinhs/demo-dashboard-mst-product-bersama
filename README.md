# Dashboard Kategori Produk Bersama

Dashboard interaktif untuk analisis kategori produk dari data master produk Bersama. Dibangun dengan Streamlit dan Plotly.

## Fitur

- **Import Data Real-time**: Mengambil data produk dari Google Sheet [FINAL] Data Product Latest
- **Filter Interaktif**: Filter berdasarkan:
  - Kategori Utama (Minuman, Makanan Ringan, Susu, dll.)
  - Principal / Perusahaan (Mayora, Indofood, Nestle, dll.)
  - Sub-Kategori (Air Mineral, Biscuit, Bubble Gum, dll.)
- **Metrik Utama**:
  - Total Data Produk
  - Jumlah Kategori Utama
  - Jumlah Principal
  - Jumlah Sub-Kategori
- **Visualisasi Data**:
  - **Distribusi Produk per Kategori Utama**: Bar chart dengan label deskriptif
  - **Distribusi Produk per Principal**: Bar chart untuk principal terpilih kategori
  - **Hierarki Kategori**: Treemap interaktif (Kategori Utama → Principal → Sub-Kategori)
  - **Distribusi Produk per Subcat C**: Bar chart top 20 sub category
- **Tabel Detail**: Menampilkan data produk dengan deskripsi kategori
- **Download Data**: Unduh data yang difilter sebagai CSV

## Instalasi

1. Pastikan Anda memiliki Python 3.7 atau lebih baru
2. Install dependensi dari requirements.txt:
   ```bash
   pip install -r requirements.txt
   ```

## Menjalankan Dashboard

### Cara 1: Menggunakan Script (Mudah)
```bash
cd /Users/zain/Codes/Delman/Bersama/product-standardization/dashboard
chmod +x run.sh
./run.sh
```

### Cara 2: Manual
```bash
cd /Users/zain/Codes/Delman/Bersama/product-standardization
source venv/bin/activate
pip install -r requirements.txt
streamlit run dashboard/dashboard.py
```

Dashboard akan terbuka di browser default pada:
**http://localhost:8501**

## Struktur File

- `dashboard.py`: Kode utama dashboard Streamlit
- `requirements.txt`: Daftar dependensi Python
- `run.sh`: Script untuk menjalankan dashboard dengan mudah
- `README.md`: Dokumentasi dashboard

## Sumber Data

1. **Data Produk**: Google Sheet Data Product Latest (11,988 records)
   - URL: `https://docs.google.com/spreadsheets/d/1d0V4YLivf4O8pJZWGoO7ai_1ZnOMHPrJtSwItOUiuDo`
2. **Mapping Kategori**:
   - cat_a (Kategori Utama): Hardcoded dalam dashboard.py
   - cat_b (Principal): Ambil dari sheet clean_principal di `https://docs.google.com/spreadsheets/d/1cYxsxIzPrKKbtbRSkQ1DWoj9Yi7a0ZwGncOwPEYgg4c`
   - subcat_c (Sub Category): Ambil dari sheet Sub category di `https://docs.google.com/spreadsheets/d/1COzeL-c4d3kU3w8hY0WqtzPVm5MBVG1h4aBJkRl-2R4`

## Deploy ke Streamlit Cloud

1. Push kode ke GitHub repository
2. Buka https://streamlit.io/cloud
3. Klik "Deploy an app"
4. Pilih repository `zaiinhs/demo-dashboard-mst-product-bersama`
5. Konfigurasi:
   - Branch: main
   - File main: dashboard/dashboard.py
6. Klik "Deploy"

## Update Dashboard

Untuk memperbarui dashboard dengan data baru:
1. Pastikan Google Sheets sudah di-update
2. Dashboard akan secara otomatis mengambil data baru setiap 1 jam (cache TTL=3600 detik)
3. Atau tekan tombol "Rerun" di kanan atas dashboard
