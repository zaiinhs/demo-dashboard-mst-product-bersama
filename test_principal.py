"""
Test script to verify principal (cat_b) functionality
"""

import pandas as pd

# --- Mapping Category Codes to Descriptions ---
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

# Test CAT_B_MAP
print("=== CAT_B_MAP Test ===")
print(f"Total entries: {len(CAT_B_MAP)}")
print(f"First 5 entries: {list(CAT_B_MAP.items())[:5]}")

# Load data
gsheet_url = "https://docs.google.com/spreadsheets/d/1d0V4YLivf4O8pJZWGoO7ai_1ZnOMHPrJtSwItOUiuDo/gviz/tq?tqx=out:csv&sheet=[FINAL]%20Data%20Product%20Latest"
df = pd.read_csv(gsheet_url)

print("\n=== Data Test ===")
print(f"Total records: {len(df)}")
print(f"Unique cat_b values: {df['cat_b'].nunique()}")

# Check which principal codes are in the map
print("\n=== Principal Code Coverage ===")
df["cat_b_in_map"] = df["cat_b"].apply(lambda x: x in CAT_B_MAP)
covered = df[df["cat_b_in_map"]]["cat_b"].nunique()
uncovered = df[~df["cat_b_in_map"]]["cat_b"].nunique()

print(f"Covered principals: {covered} ({covered/df['cat_b'].nunique()*100:.1f}%)")
print(f"Uncovered principals: {uncovered} ({uncovered/df['cat_b'].nunique()*100:.1f}%)")

# Get top 20 principals by product count
print("\n=== Top 20 Principals (Unmapped) ===")
top20_unmapped = df["cat_b"].value_counts().head(20)
for code, count in top20_unmapped.items():
    print(f"{code}: {count} products")

# Get top 20 principals with descriptions
print("\n=== Top 20 Principals (Mapped) ===")
df["cat_b_desc"] = df["cat_b"].apply(lambda x: CAT_B_MAP.get(x, x))
top20_mapped = df["cat_b_desc"].value_counts().head(20)
for desc, count in top20_mapped.items():
    print(f"{desc}: {count} products")

# Check if any of the top 20 are not in the map
print("\n=== Unmapped Top 20 Principals ===")
unmapped_top20 = []
for code, count in top20_unmapped.items():
    if code not in CAT_B_MAP:
        unmapped_top20.append(code)

if unmapped_top20:
    print(f"Found {len(unmapped_top20)} unmapped principal codes in top 20:")
    for code in unmapped_top20:
        print(f"  - {code}")
else:
    print("All top 20 principal codes are mapped!")

# Sample product data with principal descriptions
print("\n=== Sample Product Data ===")
sample = df[["name", "cat_b", "cat_b_desc", "cat_a", "pcode"]].head(5)
print(sample.to_string())
