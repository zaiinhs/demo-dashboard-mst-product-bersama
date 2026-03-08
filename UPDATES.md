# Perubahan pada Dashboard Analisis Kategori Produk

## ✅ Update 1: Perbaikan Diagram Top 20 Kategori (Principal/Perusahaan)

### Masalah Sebelumnya
Diagram "Top 20 Kategori dengan Jumlah Produk Terbanyak" menampilkan **kode principal (cat_b)** seperti PR0001, PR0002, dll., yang tidak mudah dipahami oleh pengguna.

### Perbaikan yang Dilakukan

1. **Pembuatan Mapping Principal (CAT_B_MAP)**:
   - Menambahkan dictionary CAT_B_MAP dengan 105 mapping dari kode principal ke nama perusahaan/principal
   - Contoh: PR0001 → "MAYORA INDAH", PR0002 → "PERFETTI VAN MELLE"

2. **Perubahan Filter**:
   - Ubah label filter dari "Kategori" menjadi "Principal / Perusahaan"
   - Menampilkan nama perusahaan saat memilih filter (format_func)
   - Contoh: Pilihan filter menunjukkan "MAYORA INDAH" bukan "PR0001"

3. **Perubahan Visualisasi**:
   - Diagram bar chart "Top 20 Kategori" diubah menjadi "Top 20 Principal dengan Jumlah Produk Terbanyak"
   - Menampilkan nama perusahaan/principal pada sumbu x
   - Contoh: "WINGS GROUP" (1298 produk), "UNILEVER INDONESIA" (521 produk)

4. **Perubahan Treemap**:
   - Hierarki kategori diubah menjadi: Kategori Utama > Principal > Sub-Kategori
   - Menampilkan nama principal (tidak lagi kode) pada treemap

5. **Perubahan Tabel Detail**:
   - Menambahkan kolom "cat_b_desc" pada tabel untuk menampilkan nama principal
   - Menghilangkan kolom "cat_b" yang hanya menampilkan kode

6. **Perubahan Metrik**:
   - Metrik "Kategori" diubah menjadi "Principal" untuk kesesuaian terminologi

### Coverage Mapping
- Total principal yang di-mapping: 105 (7.3% dari total 1373 unique cat_b)
- Semua **Top 20 principal dengan jumlah produk terbanyak** sudah di-mapping!
  - OTHERS (PR0256) - 1298 produk
  - WINGS GROUP (PR0396) - 786 produk
  - UNILEVER INDONESIA (PR0025) - 521 produk
  - MAYORA INDAH (PR0001) - 376 produk
  - INDOFOOD (PR0036) - 309 produk
  - dll.

### Hasil Akhir
Dashboard sekarang menampilkan **nama perusahaan/principal yang mudah dipahami** pada:
- Filter sidebar
- Diagram top 20 principal
- Treemap hierarki kategori
- Tabel detail produk
- Metrik utama

Pengguna dapat dengan jelas melihat distribusi produk per principal/perusahaan tanpa harus memahami kode-kode yang rumit.
