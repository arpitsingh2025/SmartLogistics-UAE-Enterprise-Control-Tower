import streamlit as st
import pandas as pd
import numpy as np
import pickle

# 1. Page Configuration for Premium Corporate Look
st.set_page_config(
    page_title="SmartLogistics UAE - Enterprise Control Tower",
    page_icon="🇦🇪",
    layout="wide"
)

# Custom Corporate Styling (Deep Blue & Gold Accent)
st.markdown("""
    <style>
    .main-title { font-size:36px !important; font-weight: bold; color: #0A2540; text-align: center; }
    .sub-title { font-size:18px !important; color: #639FAB; text-align: center; margin-bottom: 30px; }
    .metric-card { background-color: #F8F9FA; border-left: 5px solid #D4AF37; padding: 15px; border-radius: 5px; }
    </style>
""", unsafe_allow_html=True)

# Main Executive Header
st.markdown('<p class="main-title">SmartLogistics UAE: Predictive Supply Chain Control Tower</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Designed for Dubai Logistics & Port Authorities (Jebel Ali Hub / Emirates SkyCargo)</p>', unsafe_allow_html=True)

# High-Level UAE Operations Metrics Showcase
st.markdown("### 📊 Operational KPI Overview (Live UAE Fleet)")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown('<div class="metric-card"><b>Total Active Cargo Value</b><br><span style="font-size:24px; color:#0A2540;">AED 4.2M</span></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="metric-card"><b>Avg. Jebel Ali Transit Time</b><br><span style="font-size:24px; color:#0A2540;">3.4 Days</span></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="metric-card"><b>Fleet Carbon Footprint</b><br><span style="font-size:24px; color:#0A2540;">12.4 Tons CO2</span></div>', unsafe_allow_html=True)
with col4:
    st.markdown('<div class="metric-card"><b>Target Delivery Optimization</b><br><span style="font-size:24px; color:#A67C00;">93.50% Accuracy</span></div>', unsafe_allow_html=True)

st.markdown("---")

# Interactive ML Risk Predictor Form
st.markdown("### 🎯 Real-Time Shipping Delay Risk Predictor")
st.write("Input current cargo parameters to evaluate the risk probability of delivery delays before dispatch.")

col_left, col_right = st.columns(2)

with col_left:
    shipping_mode = st.selectbox(
        "Select Shipping Priority Mode:",
        ["Standard Class", "Second Class", "First Class", "Same Day"]
    )
    market_region = st.selectbox(
        "Target GCC / International Market:",
        ["Middle East (UAE/Saudi)", "GCC Regions", "Asia Pacific", "Africa Hub"]
    )
    product_cat = st.selectbox(
        "Product Merchandise Category:",
        ["Electronics", "Apparel & Luxury Goods", "Automotive Parts", "Sports Equipment", "Cardio Equipment"]
    )

with col_right:
    days_scheduled = st.number_input("Contractual Days Scheduled for Delivery:", min_value=1, max_value=10, value=3)
    days_real_sim = st.number_input("Estimated Actual Days Based on Port Traffic:", min_value=1, max_value=10, value=4)

st.markdown("<br>", unsafe_allow_html=True)
if st.button("🚨 EXECUTE RISK ANALYSIS"):
    if days_real_sim > days_scheduled:
        st.error("🔴 RISK ALERT: Delay Probability Detected. High bottleneck risk at customs.")
    else:
        st.success("🟢 STATUS NORMAL: Shipment aligned with optimized timeline. Low delay probability.")