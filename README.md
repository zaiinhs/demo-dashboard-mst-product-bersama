# Dashboard Data Product Latest

Dashboard interaktif untuk analisis data produk menggunakan Streamlit.

## Fitur

- **Import Data**: Mengambil data dari Google Sheet secara real-time
- **Filter Data**: Filter berdasarkan tanggal, kategori produk, dan wilayah
- **Metrik Utama**: Menampilkan total penjualan, quantity, dan profit
- **Visualisasi**:
  - Bar chart: Penjualan per kategori produk
  - Line chart: Tren penjualan harian
  - Pie chart: Distribusi penjualan per wilayah
  - Heatmap: Korelasi antara variabel numerik
- **Download Data**: Unduh data yang difilter sebagai CSV
- **Tabel Detail**: Menampilkan data yang sudah difilter

## Instalasi

1. Pastikan Anda memiliki Python 3.7 atau lebih baru
2. Install dependensi:
   ```bash
   pip install streamlit pandas plotly seaborn matplotlib
   ```
3. Atau install dari requirements.txt:
   ```bash
   pip install -r requirements.txt
   ```

## Menjalankan Dashboard

1. Masuk ke folder dashboard:
   ```bash
   cd dashboard
   ```
2. Jalankan Streamlit:
   ```bash
   streamlit run dashboard.py
   ```
3. Dashboard akan terbuka di browser (biasanya http://localhost:8501)

## Struktur File

- `dashboard.py`: Kode utama dashboard Streamlit
- `README.md`: Dokumentasi dashboard

## Customisasi

Jika kolom di data Anda berbeda, ubah nama kolom di file `dashboard.py`. Misalnya:
- Ubah `Product Category` menjadi `Kategori Produk`
- Ubah `Sales` menjadi `Penjualan`
- Ubah `Region` menjadi `Wilayah`

## Deploy ke Streamlit Cloud

1. Push kode ke GitHub repository
2. Buka https://streamlit.io/cloud
3. Klik "Deploy an app"
4. Pilih repository Anda
5. Konfigurasi:
   - Branch: main
   - File main: dashboard/dashboard.py
6. Klik "Deploy"

## Sumber Data

Data diambil dari Google Sheet:
https://docs.google.com/spreadsheets/d/1d0V4YLivf4O8pJZWGoO7ai_1ZnOMHPrJtSwItOUiuDo/edit?usp=sharing
