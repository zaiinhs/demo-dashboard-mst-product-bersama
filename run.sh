#!/bin/bash

# Run Streamlit dashboard
cd "$(dirname "$0")"
cd ..
source venv/bin/activate
streamlit run dashboard/dashboard.py
