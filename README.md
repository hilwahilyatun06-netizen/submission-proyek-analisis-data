# 📊 E-Commerce Public Dataset Dashboard

Dashboard ini dibuat menggunakan **Streamlit** untuk melakukan analisis dan visualisasi data pada **E-Commerce Public Dataset**.

## 🛠️ Teknologi yang Digunakan

* Python
* Streamlit
* Pandas
* Matplotlib

## 📁 Struktur Project

```text
submission-proyek-analisis-data/
│
├── E-Commerce Public Dataset.ipynb
├── README.md
├── customers_dataset.csv
├── dashboard.py
├── main_data.csv
└── requirements.txt
```

## ⚙️ Setup Virtual Environment

Pastikan **Python** sudah terinstall pada komputer.

Buka **Command Prompt** atau **Terminal**, kemudian masuk ke folder project:

```bash
cd nama-folder-project
```

Buat virtual environment dengan perintah:

```bash
python -m venv venv
```

Aktifkan virtual environment pada Windows:

```bash
venv\Scripts\activate
```

Jika berhasil, biasanya akan muncul tulisan `(venv)` pada bagian awal terminal.

## 📦 Install Library

Setelah virtual environment aktif, install seluruh library yang dibutuhkan menggunakan `requirements.txt`:

```bash
pip install -r requirements.txt
```

## ▶️ Menjalankan Dashboard

Pastikan file `dashboard.py` dan `main_data.csv` berada dalam folder project yang sama.

Jalankan dashboard dengan perintah:

```bash
streamlit run dashboard.py
```

Setelah berhasil dijalankan, Streamlit akan membuka dashboard pada browser. Jika tidak terbuka otomatis, akses:

```text
http://localhost:8501
```

## 📊 Fitur Dashboard

Dashboard menyediakan beberapa hasil analisis, yaitu:

* Total jumlah pesanan.
* Total jumlah produk.
* Total nilai penjualan.
* Perkembangan jumlah pesanan per bulan.
* Perkembangan total nilai penjualan per bulan.
* 10 kategori produk dengan jumlah pesanan tertinggi.
* 10 kategori produk dengan total nilai penjualan tertinggi.
* Tabel ringkasan kategori produk.
* Kesimpulan hasil analisis.

## 📌 Dataset

Dashboard menggunakan `main_data.csv` yang berisi data transaksi dan kategori produk.

Kolom yang digunakan dalam dashboard meliputi:

* `order_id`
* `order_purchase_timestamp`
* `product_id`
* `price`
* `product_category_name`
* `product_category_name_english`

## 👩‍💻 Author

**Hilwa Hilyatun Niswah**

Project Analisis Data — E-Commerce Public Dataset
