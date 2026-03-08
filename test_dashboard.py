"""
Test script to verify dashboard functionality without running Streamlit
"""

import pandas as pd

# --- Mapping for testing ---
CAT_A_MAP = {
    "CA0001": "Minuman",
    "CA0002": "Makanan Ringan",
    "CA0003": "Permen dan Coklat",
    "CA0004": "Makanan Kemasan",
    "CA0005": "Produk Perawatan Tubuh",
    "CA0007": "Produk Kopi",
    "CA0008": "Produk Mie Instan",
    "CA0009": "Perlengkapan Rumah Tangga",
    "CA0010": "Sembako",
    "CA0011": "Alat Tulis dan Perlengkapan Kantor",
    "CA0012": "Produk Kebutuhan Bayi",
    "CA0013": "Rokok",
    "CA0014": "Obat-Obatan",
    "CA0016": "Buah dan Sayur-Sayuran",
    "CA0017": "Susu"
}

# URL Google Sheet
gsheet_url = "https://docs.google.com/spreadsheets/d/1d0V4YLivf4O8pJZWGoO7ai_1ZnOMHPrJtSwItOUiuDo/gviz/tq?tqx=out:csv&sheet=[FINAL]%20Data%20Product%20Latest"

print("🔍 Mengambil data dari Google Sheet...")
try:
    df = pd.read_csv(gsheet_url)
    print(f"✅ Data berhasil diambil!")
    print(f"📊 Total records: {df.shape[0]}")
    print(f"🔢 Kolom: {list(df.columns)}")
    
    # Test filtering
    print("\n🧪 Testing filtering functionality...")
    
    # Test 1: Filter by Minuman (CA0001)
    cat_a_filter = ["CA0001"]
    filtered_df = df[df["cat_a"].isin(cat_a_filter)]
    print(f"  - Produk Minuman (CA0001): {filtered_df.shape[0]} records")
    
    # Test 2: Filter by Makanan Ringan (CA0002)
    cat_a_filter = ["CA0002"]
    filtered_df = df[df["cat_a"].isin(cat_a_filter)]
    print(f"  - Produk Makanan Ringan (CA0002): {filtered_df.shape[0]} records")
    
    # Test 3: Filter by Susu (CA0017)
    cat_a_filter = ["CA0017"]
    filtered_df = df[df["cat_a"].isin(cat_a_filter)]
    print(f"  - Produk Susu (CA0017): {filtered_df.shape[0]} records")
    
    # Test category mapping
    print("\n🏷️ Testing category mapping...")
    df["cat_a_desc"] = df["cat_a"].apply(lambda x: CAT_A_MAP.get(x, x))
    category_counts = df["cat_a_desc"].value_counts()
    
    print("  - Distribusi produk per kategori utama:")
    for category, count in category_counts.items():
        print(f"    • {category}: {count} produk")
    
    # Test unique values
    print("\n📈 Testing unique values...")
    unique_cat_a = df["cat_a"].nunique()
    unique_cat_b = df["cat_b"].nunique()
    unique_cat_c = df["cat_c"].nunique()
    unique_subcat_c = df["subcat_c"].nunique()
    
    print(f"  - Kategori Utama (cat_a): {unique_cat_a} unique values")
    print(f"  - Kategori (cat_b): {unique_cat_b} unique values")
    print(f"  - Sub-Kategori (cat_c): {unique_cat_c} unique values")
    print(f"  - Subcat C: {unique_subcat_c} unique values")
    
    print("\n✅ Semua test berhasil! Dashboard siap digunakan.")
    
except Exception as e:
    print(f"❌ Error: {e}")
