# Dashboard Kategori Produk Bersama

Dashboard interaktif untuk analisis kategori produk dari data master produk Bersama. Dibangun dengan Streamlit dan Plotly.

## Fitur

- **Import Data Real-time**: Mengambil data produk dari Google Sheet (11,988 records)
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
  - **Distribusi Produk per Sub Category**: Bar chart top 20 sub category
- **Tabel Detail**: Menampilkan data produk dengan deskripsi kategori
- **Download Data**: Unduh data yang difilter sebagai CSV

## Prerequisites

- Python 3.7 atau lebih baru
- pip (package manager Python)

## Instalasi

1. Clone repository ini:
   ```bash
   git clone https://github.com/zaiinhs/demo-dashboard-mst-product-bersama.git
   cd demo-dashboard-mst-product-bersama
   ```

2. Buat virtual environment (opsional tapi disarankan):
   ```bash
   python -m venv venv
   ```

3. Activate virtual environment:
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`

4. Install dependensi:
   ```bash
   pip install -r requirements.txt
   ```

## Menjalankan Dashboard

### Cara 1: Menggunakan Script (Untuk Mac/Linux)
```bash
chmod +x run.sh
./run.sh
```

### Cara 2: Manual
```bash
# Activate virtual environment (jika menggunakan venv)
source venv/bin/activate

# Jalankan Streamlit
streamlit run dashboard.py
```

### Cara 3: Menggunakan Python Langsung
```bash
python -m streamlit run dashboard.py
```

Dashboard akan terbuka di browser default pada:
**http://localhost:8501**

## Struktur File

- `dashboard.py`: Kode utama dashboard Streamlit
- `requirements.txt`: Daftar dependensi Python
- `run.sh`: Script untuk menjalankan dashboard (Mac/Linux)
- `README.md`: Dokumentasi dashboard

## Sumber Data

1. **Data Produk**: Google Sheet dengan 11,988 records
   - Spreadsheet: `https://docs.google.com/spreadsheets/d/1d0V4YLivf4O8pJZWGoO7ai_1ZnOMHPrJtSwItOUiuDo`
   - Sheet: [FINAL] Data Product Latest (gid=676398421)

2. **Mapping Kategori**:
   - cat_a (Kategori Utama): Hardcoded dalam dashboard.py
   - cat_b (Principal): Ambil dari sheet clean_principal
   - subcat_c (Sub Category): Ambil dari sheet Sub category

## Deploy ke Streamlit Cloud

1. Push kode ke GitHub repository
2. Buka https://share.streamlit.io/
3. Klik "New app"
4. Pilih repository `zaiinhs/demo-dashboard-mst-product-bersama`
5. Konfigurasi:
   - Branch: main / master
   - File main: dashboard/dashboard.py
6. Klik "Deploy"

## Update Dashboard

Untuk memperbarui dashboard dengan data baru:
1. Pastikan Google Sheets sudah di-update
2. Dashboard akan secara otomatis mengambil data baru setiap 1 jam (cache TTL=3600 detik)
3. Atau klik tombol "Rerun" di pojok kanan atas dashboard
