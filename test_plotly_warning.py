"""
Test script to identify where the Plotly configuration warning is coming from.
"""

import pandas as pd
import plotly.express as px
import streamlit as st

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

CAT_B_MAP = {
    "PP0708": "MAYORA_PROMO",
    "PP0711": "INDOBOGA SEMESTA RASA",
    "PP0713": "UNICHARM PROMO 1",
    "PP0714": "UNICHARM PROMO 2",
    "PP0715": "UNICHARM PROMO 3",
    "PR0001": "MAYORA INDAH",
    "PR0002": "PERFETTI VAN MELLE",
    "PR0004": "FOOD STATION",
    "PR0005": "GROUP APRIL",
    "PR0006": "STANDARDPEN INDUSTRIES",
    "PR0007": "JOYKO",
    "PR0008": "BUTTERFLY",
    "PR0009": "NACHI TAPE INDUSTRY",
    "PR0010": "FABER-CASTELL AG",
    "PR0011": "SNOWMAN INDONESIA",
    "PR0012": "KENKO SINAR INDONESIA",
    "PR0013": "ARTLINE SHACIHATA JAPAN",
    "PR0162": "COMBIPHAR",
    "PR0016": "GARUDA FOOD",
    "PR0017": "NUTRICIA SEJAHTERA INDONESIA",
    "PR0018": "KALBE MONIRAGA",
    "PR0019": "NESTLE INDONESIA",
    "PR0020": "FRISIAN FLAG INDONESIA",
    "PR0021": "NUTRICLUB",
    "PR0022": "SARIHUSADA",
    "PR0023": "UNICHARM",
    "PR0024": "ANUGRAH SETIA LESTARI/ UNILEVER",
    "PR0025": "UNILEVER INDONESIA",
    "PR0026": "ULTRAJAYA MILK/UNILEVER",
    "PR0027": "ADABI CONSUMER INDUSTRIES",
    "PR0326": "DANONE",
    "PR0029": "OTSUKA",
    "PR0030": "SINAR SOSRO",
    "PR0031": "SARI MURNI",
    "PR0032": "NISSIN FOODS INDONESIA",
    "PR0033": "FORISA NUSAPERSADA",
    "PR0034": "KRAFT INDONESIA",
    "PR0035": "CHEMINDO LOKA",
    "PR0036": "INDOFOOD",
    "PR0037": "REFINA",
    "PR0038": "UNICHEM CANDI BOROBUDUR",
    "PR0028": "ENESIS",
    "PR0040": "PASEO INDONESIA",
    "PR0041": "JOENOES IKAMULYA",
    "PR0042": "SINDE BUDI SENTOSA",
    "PR0043": "HEINZ ABC",
    "PR0045": "DJARUM",
    "PR0046": "NOJORONO",
    "PR0047": "GUDANG GARAM",
    "PR0048": "INDOCAFE",
    "PR0050": "AQUA GOLDEN MISSISSIPPI",
    "PR0051": "KAO",
    "PR0089": "KALBE FARMA",
    "PR0053": "KALDU SARI NABATI",
    "PR0055": "SCOTCH-BRITE",
    "PR0056": "UNITAMA SARI MAS",
    "PR0057": "KHONG GUAN INDONESIA",
    "PR0058": "DELTOMED LABORATORIES",
    "PR0059": "SIDOMUNCUL",
    "PR0060": "DUE KELINCI",
    "PR0061": "PROCTER & GAMBLE",
    "PR0062": "SOFTEX INDONESIA",
    "PR0063": "KARA SANTAN PERTAMA",
    "PR0064": "MULTIMAS NABATI ASAHAN",
    "PR0065": "MOTASA INDONESIA",
    "PR0066": "DUNIA BINTANG WALET",
    "PR0067": "PUNDI KENCANA",
    "PR0068": "KINO",
    "PR0069": "MANDOM INDONESIA",
    "PR0070": "BINA KARYA PRIMA",
    "PR0071": "ULTRA SAKTI",
    "PR0072": "ICHI TAN INDONESIA",
    "PR0073": "BENFOOD DINAMIKA SENTOSA",
    "PR0074": "YUPI INDO JELLY GUM",
    "PR0075": "JAVA PRIMA ABADI",
    "PR0382": "KT&G",
    "PR0077": "GOO.N INDONESIA",
    "PR0078": "TIGA PILAR SEJAHTERA FOOD",
    "PR0079": "SWALLOW",
    "PR0080": "LEVIOS TIRTA ALAMI",
    "PR0081": "COCA-COLA",
    "PR0082": "AJINOMOTO GROUP",
    "PR0083": "SIANTAR TOP",
    "PR0084": "GODREJ INDONESIA",
    "PR0076": "ORANG TUA",
    "PR0086": "ABC PRESIDENT",
    "PR0087": "FUMAKILLA",
    "PR0088": "GLAXO SMITH KLINE",
    "PR0352": "PERKEBUNAN NUSANTARA",
    "PR0090": "YEO HIAP SENG",
    "PR0091": "EAGLE INDO PHARMA",
    "PR0092": "LASALLEFOOD INDONESIA",
    "PR0093": "LUCKY STRIKE",
    "PR0094": "SUKANDA DJAYA",
    "PR0095": "MARIMAS",
    "PR0096": "S. C. JOHNSON & SON",
    "PR0097": "NUTRIFOOD",
    "PR0098": "NIRAMAS UTAMA",
    "PR0099": "GENKI",
    "PR0100": "WILMAR",
    "PR0256": "OTHERS",
    "PR0396": "WINGS GROUP",
    "PR0115": "PHILIP MORRIS INDONESIA",
    "PR0405": "KAPAL API GROUP",
    "PR0330": "SINARMAS"
}

# Load data
gsheet_url = "https://docs.google.com/spreadsheets/d/1d0V4YLivf4O8pJZWGoO7ai_1ZnOMHPrJtSwItOUiuDo/gviz/tq?tqx=out:csv&sheet=[FINAL]%20Data%20Product%20Latest"
df = pd.read_csv(gsheet_url)
df["cat_a_desc"] = df["cat_a"].apply(lambda x: CAT_A_MAP.get(x, x))
df["cat_b_desc"] = df["cat_b"].apply(lambda x: CAT_B_MAP.get(x, x))

print("=== Testing Plotly Express ===")

# Test 1: Bar chart without any arguments
print("\n1. Testing bar chart without arguments:")
try:
    cat_a_dist = df["cat_a_desc"].value_counts().reset_index()
    cat_a_dist.columns = ["cat_a_desc", "count"]
    fig1 = px.bar(cat_a_dist, x="cat_a_desc", y="count")
    print("✅ Bar chart created successfully")
except Exception as e:
    print(f"❌ Error: {e}")

# Test 2: Bar chart with title and labels
print("\n2. Testing bar chart with title and labels:")
try:
    cat_b_dist = df["cat_b_desc"].value_counts().head(5).reset_index()
    cat_b_dist.columns = ["cat_b_desc", "count"]
    fig2 = px.bar(cat_b_dist, 
                 x="cat_b_desc", 
                 y="count",
                 title="Test Chart",
                 color="cat_b_desc",
                 text_auto=True)
    fig2.update_layout(xaxis_title="X Axis", yaxis_title="Y Axis")
    print("✅ Bar chart with title created successfully")
except Exception as e:
    print(f"❌ Error: {e}")

# Test 3: Treemap
print("\n3. Testing treemap:")
try:
    category_hierarchy = df.groupby(["cat_a_desc", "cat_b_desc"])["pcode"].count().reset_index()
    category_hierarchy.columns = ["cat_a_desc", "cat_b_desc", "count"]
    fig3 = px.treemap(category_hierarchy,
                     path=["cat_a_desc", "cat_b_desc"],
                     values="count")
    print("✅ Treemap created successfully")
except Exception as e:
    print(f"❌ Error: {e}")

# Test 4: Streamlit plotly chart
print("\n4. Testing Streamlit plotly chart:")
try:
    from io import StringIO
    import sys
    
    # Capture stdout
    captured_output = StringIO()
    sys.stdout = captured_output
    
    # Try to create and display a simple plot
    temp_fig = px.bar(cat_b_dist, x="cat_b_desc", y="count")
    st.plotly_chart(temp_fig, config={"responsive": True})
    
    sys.stdout = sys.__stdout__
    output = captured_output.getvalue()
    
    if "deprecated" in output.lower() or "warning" in output.lower():
        print("⚠️ Warning detected in output:")
        print(output.strip())
    else:
        print("✅ No warnings detected")
        
except Exception as e:
    print(f"❌ Error: {e}")
    sys.stdout = sys.__stdout__

print("\n=== All tests completed ===")
