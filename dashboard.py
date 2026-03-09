import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.io as pio

# Set Plotly template
pio.templates.default = "plotly_white"

# Set page config
st.set_page_config(page_title="Dashboard Kategori Produk", page_icon="📦", layout="wide")

# --- Load Principal (cat_b) mapping from Google Sheet ---
PRINCIPAL_SHEET_URL = "https://docs.google.com/spreadsheets/d/1cYxsxIzPrKKbtbRSkQ1DWoj9Yi7a0ZwGncOwPEYgg4c/gviz/tq?tqx=out:csv&sheet=clean_principal"

@st.cache_data(ttl=3600)
def load_principal_mapping():
    try:
        df_principal = pd.read_csv(PRINCIPAL_SHEET_URL)
        CAT_B_MAP = dict(zip(df_principal["cat_b"], df_principal["description"]))
        return CAT_B_MAP
    except Exception as e:
        st.warning(f"Gagal memuat data principal: {e}")
        return {}

CAT_B_MAP = load_principal_mapping()

# --- Load Sub Category (subcat_c) mapping from Google Sheet ---
SUBCAT_SHEET_URL = "https://docs.google.com/spreadsheets/d/1COzeL-c4d3kU3w8hY0WqtzPVm5MBVG1h4aBJkRl-2R4/gviz/tq?tqx=out:csv&sheet=Sub%20category"

@st.cache_data(ttl=3600)
def load_subcat_mapping():
    try:
        df_subcat = pd.read_csv(SUBCAT_SHEET_URL)
        SUBCAT_C_MAP = dict(zip(df_subcat["subcat_c"], df_subcat["description"]))
        return SUBCAT_C_MAP
    except Exception as e:
        st.warning(f"Gagal memuat data sub category: {e}")
        return {}

SUBCAT_C_MAP = load_subcat_mapping()

# --- Mapping Category Codes to Descriptions ---
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

# Judul dashboard
st.title("📦 Dashboard Analisis Data Master Produk")

# URL Google Sheet - Sheet: Data Product Latest (11,988 records)
# Using gid=676398421 from spreadsheet https://docs.google.com/spreadsheets/d/1d0V4YLivf4O8pJZWGoO7ai_1ZnOMHPrJtSwItOUiuDo/edit?gid=676398421
gsheet_url = "https://docs.google.com/spreadsheets/d/1d0V4YLivf4O8pJZWGoO7ai_1ZnOMHPrJtSwItOUiuDo/gviz/tq?tqx=out:csv&gid=676398421"

# Import data with cache
@st.cache_data(ttl=3600)
def load_data():
    try:
        df = pd.read_csv(gsheet_url)
        df = df.dropna(axis=0, how="all")
        df = df.dropna(axis=1, how="all")
        return df
    except Exception as e:
        st.error(f"Gagal memuat data: {e}")
        return None

df = load_data()

if df is not None:
    st.sidebar.header("🔍 Filter Data")
    
    # Filter Kategori Utama (cat_a) - with descriptions
    if "cat_a" in df.columns:
        unique_cat_a = sorted(df["cat_a"].dropna().unique())
        cat_a_options = st.sidebar.multiselect(
            "Kategori Utama",
            options=unique_cat_a,
            default=unique_cat_a,
            format_func=lambda x: CAT_A_MAP.get(x, x)
        )
    
    # Filter Principal (cat_b) - filtered by cat_a
    if "cat_b" in df.columns:
        filtered_cat_b = df[df["cat_a"].isin(cat_a_options)]["cat_b"].dropna().unique()
        cat_b_options = st.sidebar.multiselect(
            "Principal / Perusahaan",
            options=sorted(filtered_cat_b),
            default=sorted(filtered_cat_b),
            format_func=lambda x: CAT_B_MAP.get(x, x)
        )
    
    # Filter Sub-Kategori (cat_c) - filtered by cat_a & cat_b
    if "cat_c" in df.columns:
        filtered_cat_c = df[
            (df["cat_a"].isin(cat_a_options)) & 
            (df["cat_b"].isin(cat_b_options))
        ]["cat_c"].dropna().unique()
        cat_c_options = st.sidebar.multiselect(
            "Sub-Kategori",
            options=sorted(filtered_cat_c),
            default=sorted(filtered_cat_c)
        )
    
    # Filter Subcat C (subcat_c) - filtered by all categories
    if "subcat_c" in df.columns:
        filtered_subcat_c = df[
            (df["cat_a"].isin(cat_a_options)) & 
            (df["cat_b"].isin(cat_b_options)) & 
            (df["cat_c"].isin(cat_c_options))
        ]["subcat_c"].dropna().unique()
        subcat_c_options = st.sidebar.multiselect(
            "Subcat C",
            options=sorted(filtered_subcat_c),
            default=sorted(filtered_subcat_c)
        )

    # Apply filters to data
    filtered_df = df.copy()
    if "cat_a" in df.columns:
        filtered_df = filtered_df[filtered_df["cat_a"].isin(cat_a_options)]
    if "cat_b" in df.columns:
        filtered_df = filtered_df[filtered_df["cat_b"].isin(cat_b_options)]
    if "cat_c" in df.columns:
        filtered_df = filtered_df[filtered_df["cat_c"].isin(cat_c_options)]
    if "subcat_c" in df.columns:
        filtered_df = filtered_df[filtered_df["subcat_c"].isin(subcat_c_options)]

    # --- Add description columns for visualization ---
    filtered_df["cat_a_desc"] = filtered_df["cat_a"].apply(lambda x: CAT_A_MAP.get(x, x))
    filtered_df["cat_b_desc"] = filtered_df["cat_b"].apply(lambda x: CAT_B_MAP.get(x, x))
    filtered_df["subcat_c_desc"] = filtered_df["subcat_c"].apply(lambda x: SUBCAT_C_MAP.get(x, x) if pd.notna(x) else x)

    # --- Metrik Utama ---
    st.subheader("📊 Metrik Utama")
    col1, col2, col3, col4 = st.columns(4)
    
    total_products = filtered_df["pcode"].count()
    col1.metric("Total Data Produk", total_products)
    
    total_cat_a = filtered_df["cat_a"].nunique()
    col2.metric("Kategori Utama", total_cat_a)
    
    total_cat_b = filtered_df["cat_b"].nunique()
    col3.metric("Principal", total_cat_b)
    
    total_subcat_c = filtered_df["subcat_c"].nunique()
    col4.metric("Sub-Kategori", total_subcat_c)

    # --- Distribusi Produk per Kategori Utama ---
    st.subheader("📈 Distribusi Produk per Kategori Utama")
    cat_a_dist = filtered_df["cat_a_desc"].value_counts().reset_index()
    cat_a_dist.columns = ["cat_a_desc", "Jumlah Produk"]
    fig1 = px.bar(cat_a_dist, x="cat_a_desc", y="Jumlah Produk",
                  title="Jumlah Produk per Kategori Utama",
                  text="Jumlah Produk")
    fig1.update_traces(marker_color="#1f77b4", textposition="outside")
    fig1.update_layout(
        xaxis_title="Kategori Utama",
        yaxis_title="Jumlah Produk",
        bargap=0.2,
        height=600,
        showlegend=False
    )
    st.plotly_chart(fig1, use_container_width=True)

    # --- Distribusi Produk per Principal (Top 20 Cat B) ---
    st.subheader("📉 Top 20 Principal dengan Jumlah Produk Terbanyak")
    cat_b_dist = filtered_df["cat_b_desc"].value_counts().reset_index().head(20)
    cat_b_dist.columns = ["cat_b_desc", "Jumlah Produk"]
    fig2 = px.bar(cat_b_dist, x="cat_b_desc", y="Jumlah Produk",
                  title="Top 20 Principal / Perusahaan",
                  text="Jumlah Produk")
    fig2.update_traces(marker_color="#2ca02c", textposition="outside")
    fig2.update_layout(
        xaxis_title="Principal / Perusahaan",
        yaxis_title="Jumlah Produk",
        xaxis_tickangle=45,
        bargap=0.2,
        height=600,
        showlegend=False
    )
    st.plotly_chart(fig2, use_container_width=True)

    # --- Hierarki Kategori (Treemap) ---
    st.subheader("🌳 Hierarki Kategori Produk")
    category_hierarchy = filtered_df.groupby(["cat_a_desc", "cat_b_desc", "cat_c"])["pcode"].count().reset_index()
    category_hierarchy.columns = ["cat_a_desc", "cat_b_desc", "cat_c", "Jumlah Produk"]
    fig3 = px.treemap(category_hierarchy,
                     path=["cat_a_desc", "cat_b_desc", "cat_c"],
                     values="Jumlah Produk",
                     title="Hierarki Kategori (Kategori Utama > Principal > Sub-Kategori)",
                     color_continuous_scale="Blues")
    fig3.update_layout(height=550)
    st.plotly_chart(fig3, use_container_width=True)

    # --- Distribusi Produk per Subcat C ---
    st.subheader("🏷️ Distribusi Produk per Sub Category")
    if not filtered_df["subcat_c"].isnull().all():
        subcat_c_dist = filtered_df["subcat_c"].value_counts().reset_index().head(20)
        subcat_c_dist.columns = ["subcat_c", "Jumlah Produk"]
        subcat_c_dist["description"] = subcat_c_dist["subcat_c"].map(SUBCAT_C_MAP).fillna(subcat_c_dist["subcat_c"])
        fig4 = px.bar(subcat_c_dist, x="description", y="Jumlah Produk",
                      title="Top 20 Sub Category dengan Jumlah Produk Terbanyak",
                      text="Jumlah Produk")
        fig4.update_traces(marker_color="#ff7f0e", textposition="outside")
        fig4.update_layout(
            xaxis_title="Sub Category",
            yaxis_title="Jumlah Produk",
            xaxis_tickangle=45,
            bargap=0.2,
            height=600,
            showlegend=False
        )
        st.plotly_chart(fig4, use_container_width=True)

    # --- Tabel Detail Data Produk ---
    st.subheader("📋 Detail Data Produk")
    display_columns = ["name", "cat_a_desc", "cat_b_desc", "cat_c", "subcat_c_desc", "pcode", "barcode"]
    available_columns = [col for col in display_columns if col in filtered_df.columns]
    st.dataframe(filtered_df[available_columns], use_container_width=True)

    # --- Download Data ---
    st.subheader("💾 Download Data")
    download_df = filtered_df.copy()
    download_columns = ["name", "cat_a", "cat_b", "cat_c", "subcat_c", "pcode", "barcode"]
    available_download_columns = [col for col in download_columns if col in download_df.columns]
    csv = download_df[available_download_columns].to_csv(index=False).encode("utf-8")
    st.download_button(
        label="Unduh Data (CSV)",
        data=csv,
        file_name="data_kategori_produk.csv",
        mime="text/csv"
    )

    # --- Footer ---
    st.markdown("---")
    st.markdown("""
        **Catatan:** Data diambil dari Google Sheet [FINAL] Data Product Latest dengan total 11988 records.
        Dashboard ini menampilkan analisis kategori produk dengan fitur filter dan visualisasi interaktif.
    """)
