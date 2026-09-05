import os

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="E-Commerce Dashboard",
    layout="wide"
)

st.title("📊 E-Commerce Public Dataset")
st.subheader("Dashboard Analisis Data Penjualan")

# =========================
# LOAD DATA
# =========================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "main_data.csv")

main_df = pd.read_csv(DATA_PATH)
main_df["order_purchase_timestamp"] = pd.to_datetime(
    main_df["order_purchase_timestamp"]
)
main_df["category"] = main_df["product_category_name_english"].fillna("unknown")

# =========================
# SIDEBAR - FITUR INTERAKTIF
# =========================

st.sidebar.header("🔍 Filter Data")

min_date = main_df["order_purchase_timestamp"].min().date()
max_date = main_df["order_purchase_timestamp"].max().date()

start_date, end_date = st.sidebar.date_input(
    label="Rentang Tanggal Pesanan",
    value=[min_date, max_date],
    min_value=min_date,
    max_value=max_date
)

category_options = sorted(main_df["category"].unique().tolist())
selected_categories = st.sidebar.multiselect(
    label="Kategori Produk",
    options=category_options,
    default=category_options
)

# Menerapkan filter interaktif ke seluruh data yang ditampilkan pada dashboard
filtered_df = main_df[
    (main_df["order_purchase_timestamp"].dt.date >= start_date)
    & (main_df["order_purchase_timestamp"].dt.date <= end_date)
    & (main_df["category"].isin(selected_categories))
]

if filtered_df.empty:
    st.warning(
        "Tidak ada data pada rentang tanggal/kategori yang dipilih. "
        "Silakan ubah filter di sidebar."
    )
    st.stop()

# =========================
# RINGKASAN METRIK
# =========================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Pesanan", f"{filtered_df['order_id'].nunique():,}")

with col2:
    st.metric("Total Produk Terjual", f"{filtered_df['product_id'].nunique():,}")

with col3:
    st.metric("Total Nilai Penjualan", f"BRL {filtered_df['price'].sum():,.2f}")

st.divider()

# =========================
# PERTANYAAN 1: Perkembangan Pesanan & Penjualan per Bulan
# =========================

st.header("1. Perkembangan Pesanan dan Penjualan per Bulan")

trend_df = filtered_df.copy()
trend_df["month"] = trend_df["order_purchase_timestamp"].dt.to_period("M").astype(str)

monthly_sales = trend_df.groupby("month").agg(
    total_orders=("order_id", "nunique"),
    total_sales=("price", "sum")
).reset_index()

col_a, col_b = st.columns(2)

with col_a:
    fig1, ax1 = plt.subplots(figsize=(8, 5))
    ax1.plot(
        monthly_sales["month"],
        monthly_sales["total_orders"],
        marker="o"
    )
    ax1.set_title("Perkembangan Jumlah Pesanan per Bulan")
    ax1.set_xlabel("Bulan")
    ax1.set_ylabel("Jumlah Pesanan")
    ax1.tick_params(axis="x", rotation=45)
    st.pyplot(fig1)

with col_b:
    fig2, ax2 = plt.subplots(figsize=(8, 5))
    ax2.plot(
        monthly_sales["month"],
        monthly_sales["total_sales"],
        marker="o",
        color="orange"
    )
    ax2.set_title("Perkembangan Total Nilai Penjualan per Bulan")
    ax2.set_xlabel("Bulan")
    ax2.set_ylabel("Total Penjualan")
    ax2.tick_params(axis="x", rotation=45)
    st.pyplot(fig2)

# =========================
# PERTANYAAN 2: Kategori Produk Terbaik
# =========================

st.header("2. Kategori Produk dengan Pesanan dan Penjualan Tertinggi")

category_summary = filtered_df.groupby("category").agg(
    total_orders=("order_id", "nunique"),
    total_sales=("price", "sum")
).reset_index()

top_orders = category_summary.sort_values(
    "total_orders", ascending=False
).head(10)

top_sales = category_summary.sort_values(
    "total_sales", ascending=False
).head(10)

col_c, col_d = st.columns(2)

with col_c:
    fig3, ax3 = plt.subplots(figsize=(8, 5))
    ax3.bar(top_orders["category"], top_orders["total_orders"])
    ax3.set_title("10 Kategori dengan Jumlah Pesanan Tertinggi")
    ax3.set_xlabel("Kategori Produk")
    ax3.set_ylabel("Jumlah Pesanan")
    ax3.tick_params(axis="x", rotation=45)
    plt.setp(ax3.get_xticklabels(), ha="right")
    st.pyplot(fig3)

with col_d:
    fig4, ax4 = plt.subplots(figsize=(8, 5))
    ax4.bar(top_sales["category"], top_sales["total_sales"], color="orange")
    ax4.set_title("10 Kategori dengan Total Nilai Penjualan Tertinggi")
    ax4.set_xlabel("Kategori Produk")
    ax4.set_ylabel("Total Penjualan")
    ax4.tick_params(axis="x", rotation=45)
    plt.setp(ax4.get_xticklabels(), ha="right")
    st.pyplot(fig4)

st.subheader("Tabel Ringkasan Kategori Produk")
st.dataframe(
    category_summary.sort_values("total_sales", ascending=False),
    use_container_width=True
)

# =========================
# KESIMPULAN
# =========================

st.header("Kesimpulan")

best_month_orders = monthly_sales.sort_values(
    "total_orders", ascending=False
).iloc[0]
best_month_sales = monthly_sales.sort_values(
    "total_sales", ascending=False
).iloc[0]

st.write(
    f"Berdasarkan data pada rentang dan kategori yang dipilih, jumlah pesanan "
    f"tertinggi terjadi pada bulan **{best_month_orders['month']}** dengan "
    f"**{int(best_month_orders['total_orders']):,} pesanan**, sedangkan total "
    f"nilai penjualan tertinggi terjadi pada bulan "
    f"**{best_month_sales['month']}** sebesar "
    f"**BRL {best_month_sales['total_sales']:,.2f}**."
)

st.write(
    "Kategori dengan jumlah pesanan tertinggi adalah "
    f"**{top_orders.iloc[0]['category']}**, sedangkan kategori "
    "dengan total nilai penjualan tertinggi adalah "
    f"**{top_sales.iloc[0]['category']}**."
)
