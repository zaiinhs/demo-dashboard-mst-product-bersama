"""
Test if text_auto parameter in Plotly Express is causing the deprecated warning.
"""

import pandas as pd
import plotly.express as px

# Load data
gsheet_url = "https://docs.google.com/spreadsheets/d/1d0V4YLivf4O8pJZWGoO7ai_1ZnOMHPrJtSwItOUiuDo/gviz/tq?tqx=out:csv&sheet=[FINAL]%20Data%20Product%20Latest"
df = pd.read_csv(gsheet_url)

print("=== Testing Plotly Express Parameters ===")

# Test without text_auto
print("\n1. Without text_auto=True:")
try:
    fig1 = px.bar(df.groupby("cat_a").size().reset_index(),
                 x="cat_a", y=0,
                 title="Product by Category")
    print("✅ Success - No warnings")
except Exception as e:
    print(f"❌ Error: {e}")

# Test with text_auto=True
print("\n2. With text_auto=True:")
try:
    import sys
    import io
    
    # Capture output
    old_stderr = sys.stderr
    sys.stderr = io.StringIO()
    
    fig2 = px.bar(df.groupby("cat_a").size().reset_index(),
                 x="cat_a", y=0,
                 title="Product by Category",
                 text_auto=True)
    
    # Check if there were any warnings
    err = sys.stderr.getvalue()
    if "deprecated" in err.lower() or "warning" in err.lower():
        print("⚠️ Warning detected:")
        print(err.strip())
    else:
        print("✅ Success - No warnings")
        
    sys.stderr = old_stderr
except Exception as e:
    print(f"❌ Error: {e}")
    sys.stderr = old_stderr

# Test with color parameter
print("\n3. With color parameter:")
try:
    import sys
    import io
    
    old_stderr = sys.stderr
    sys.stderr = io.StringIO()
    
    fig3 = px.bar(df.groupby("cat_a").size().reset_index(),
                 x="cat_a", y=0,
                 title="Product by Category",
                 color="cat_a")
    
    err = sys.stderr.getvalue()
    if "deprecated" in err.lower() or "warning" in err.lower():
        print("⚠️ Warning detected:")
        print(err.strip())
    else:
        print("✅ Success - No warnings")
        
    sys.stderr = old_stderr
except Exception as e:
    print(f"❌ Error: {e}")
    sys.stderr = old_stderr

# Test with color and text_auto
print("\n4. With color and text_auto:")
try:
    import sys
    import io
    
    old_stderr = sys.stderr
    sys.stderr = io.StringIO()
    
    fig4 = px.bar(df.groupby("cat_a").size().reset_index(),
                 x="cat_a", y=0,
                 title="Product by Category",
                 color="cat_a",
                 text_auto=True)
    
    err = sys.stderr.getvalue()
    if "deprecated" in err.lower() or "warning" in err.lower():
        print("⚠️ Warning detected:")
        print(err.strip())
    else:
        print("✅ Success - No warnings")
        
    sys.stderr = old_stderr
except Exception as e:
    print(f"❌ Error: {e}")
    sys.stderr = old_stderr

print("\n=== All parameter tests completed ===")
