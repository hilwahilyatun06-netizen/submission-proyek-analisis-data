import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# =========================
# KONFIGURASI DASHBOARD
# =========================

st.set_page_config(
    page_title="E-Commerce Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 E-Commerce Public Dataset")
st.subheader("Dashboard Analisis Data Penjualan")


# =========================
# LOAD DATA
# =========================

main_data = pd.read_csv("main_data.csv")

# Mengubah kolom tanggal menjadi datetime
main_data["order_purchase_timestamp"] = pd.to_datetime(
    main_data["order_purchase_timestamp"],
    errors="coerce"
)


# =========================
# INFORMASI DATA
# =========================

st.header("📋 Informasi Data")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Pesanan",
        main_data["order_id"].nunique()
    )

with col2:
    st.metric(
        "Total Produk",
        main_data["product_id"].nunique()
    )

with col3:
    st.metric(
        "Total Penjualan",
        f"R$ {main_data['price'].sum():,.2f}"
    )


# =========================
# PERTANYAAN 1
# =========================

st.header("1. Perkembangan Pesanan dan Penjualan per Bulan")

sales_df = main_data.copy()

sales_df["month"] = (
    sales_df["order_purchase_timestamp"]
    .dt.to_period("M")
    .astype(str)
)

monthly_sales = sales_df.groupby("month").agg(
    total_orders=("order_id", "nunique"),
    total_sales=("price", "sum")
).reset_index()


# Grafik jumlah pesanan
st.subheader("Perkembangan Jumlah Pesanan")

fig1, ax1 = plt.subplots(figsize=(12, 5))

ax1.plot(
    monthly_sales["month"],
    monthly_sales["total_orders"],
    marker="o"
)

ax1.set_title("Perkembangan Jumlah Pesanan per Bulan")
ax1.set_xlabel("Bulan")
ax1.set_ylabel("Jumlah Pesanan")
ax1.tick_params(axis="x", rotation=45)

plt.tight_layout()

st.pyplot(fig1)


# Grafik total penjualan
st.subheader("Perkembangan Total Nilai Penjualan")

fig2, ax2 = plt.subplots(figsize=(12, 5))

ax2.plot(
    monthly_sales["month"],
    monthly_sales["total_sales"],
    marker="o"
)

ax2.set_title("Perkembangan Total Nilai Penjualan per Bulan")
ax2.set_xlabel("Bulan")
ax2.set_ylabel("Total Penjualan")
ax2.tick_params(axis="x", rotation=45)

plt.tight_layout()

st.pyplot(fig2)


# =========================
# PERTANYAAN 2
# =========================

st.header("2. Kategori Produk dengan Pesanan dan Penjualan Tertinggi")


category_summary = main_data.groupby(
    "product_category_name_english"
).agg(
    total_orders=("order_id", "nunique"),
    total_sales=("price", "sum")
).reset_index()

category_summary = category_summary.rename(
    columns={
        "product_category_name_english": "category"
    }
)

category_summary["category"] = category_summary[
    "category"
].fillna("unknown")


# =========================
# 10 KATEGORI DENGAN PESANAN TERTINGGI
# =========================

st.subheader("10 Kategori dengan Jumlah Pesanan Tertinggi")

top_orders = category_summary.sort_values(
    "total_orders",
    ascending=False
).head(10)

fig3, ax3 = plt.subplots(figsize=(12, 5))

ax3.bar(
    top_orders["category"],
    top_orders["total_orders"]
)

ax3.set_title(
    "10 Kategori dengan Jumlah Pesanan Tertinggi"
)
ax3.set_xlabel("Kategori Produk")
ax3.set_ylabel("Jumlah Pesanan")
ax3.tick_params(axis="x", rotation=45)

plt.tight_layout()

st.pyplot(fig3)


# =========================
# 10 KATEGORI DENGAN PENJUALAN TERTINGGI
# =========================

st.subheader("10 Kategori dengan Total Penjualan Tertinggi")

top_sales = category_summary.sort_values(
    "total_sales",
    ascending=False
).head(10)

fig4, ax4 = plt.subplots(figsize=(12, 5))

ax4.bar(
    top_sales["category"],
    top_sales["total_sales"]
)

ax4.set_title(
    "10 Kategori dengan Total Nilai Penjualan Tertinggi"
)
ax4.set_xlabel("Kategori Produk")
ax4.set_ylabel("Total Penjualan")
ax4.tick_params(axis="x", rotation=45)

plt.tight_layout()

st.pyplot(fig4)


# =========================
# TABEL DATA KATEGORI
# =========================

st.subheader("Ringkasan Kategori Produk")

st.dataframe(
    category_summary.sort_values(
        "total_sales",
        ascending=False
    ),
    use_container_width=True
)


# =========================
# KESIMPULAN
# =========================

st.header("📌 Kesimpulan")

highest_order_category = top_orders.iloc[0]["category"]
highest_sales_category = top_sales.iloc[0]["category"]

st.write(
    f"Kategori dengan jumlah pesanan tertinggi adalah "
    f"**{highest_order_category}**, sedangkan kategori "
    f"dengan total nilai penjualan tertinggi adalah "
    f"**{highest_sales_category}**."
)

st.write(
    "Hasil dashboard menunjukkan bahwa kategori dengan "
    "jumlah pesanan tertinggi tidak selalu memiliki total "
    "nilai penjualan tertinggi karena total penjualan juga "
    "dipengaruhi oleh harga produk."
)
