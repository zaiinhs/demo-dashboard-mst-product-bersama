"""
Test if Plotly Express is causing the deprecated warning.
"""

import pandas as pd
import plotly.express as px
import streamlit as st

# Load data
gsheet_url = "https://docs.google.com/spreadsheets/d/1d0V4YLivf4O8pJZWGoO7ai_1ZnOMHPrJtSwItOUiuDo/gviz/tq?tqx=out:csv&sheet=[FINAL]%20Data%20Product%20Latest"
df = pd.read_csv(gsheet_url)

print("=== Plotly Express Version ===")
import plotly
print(f"Plotly version: {plotly.__version__}")
print(f"Plotly Express version: {px.__version__}")

print("\n=== Testing Plotly Express Figure Creation ===")

# Test bar chart creation without any parameters
print("\n1. Creating basic bar chart:")
try:
    fig1 = px.bar(df.groupby("cat_a").size().reset_index(), 
                 x="cat_a", y=0)
    print("✅ Success - No warnings")
except Exception as e:
    print(f"❌ Error: {e}")

# Test bar chart with title
print("\n2. Creating bar chart with title:")
try:
    fig2 = px.bar(df.groupby("cat_a").size().reset_index(), 
                 x="cat_a", y=0,
                 title="Product by Category")
    print("✅ Success - No warnings")
except Exception as e:
    print(f"❌ Error: {e}")

# Test bar chart with all parameters
print("\n3. Creating bar chart with all parameters:")
try:
    fig3 = px.bar(df.groupby("cat_a").size().reset_index(), 
                 x="cat_a", y=0,
                 title="Product by Category",
                 color="cat_a",
                 text_auto=True)
    fig3.update_layout(xaxis_title="Category", yaxis_title="Count")
    fig3.update_xaxes(tickangle=45)
    print("✅ Success - No warnings")
except Exception as e:
    print(f"❌ Error: {e}")

# Test treemap
print("\n4. Creating treemap:")
try:
    fig4 = px.treemap(df.groupby(["cat_a", "cat_b"]).size().reset_index(),
                     path=["cat_a", "cat_b"],
                     values=0)
    print("✅ Success - No warnings")
except Exception as e:
    print(f"❌ Error: {e}")

print("\n=== All Plotly Express tests completed ===")
