# 📊 E-Commerce Public Dataset Dashboard

Dashboard ini dibuat menggunakan **Streamlit** untuk melakukan analisis dan visualisasi data pada **E-Commerce Public Dataset**.

## 🛠️ Teknologi yang Digunakan

* Python
* Streamlit
* Pandas
* Matplotlib

## ⚙️ Setup Virtual Environment

Pastikan Python sudah terinstall pada komputer.

Buka **Command Prompt** atau **Terminal**, kemudian masuk ke folder project:

```bash
cd nama-folder-project
```

Buat virtual environment:

```bash
python -m venv venv
```

Aktifkan virtual environment pada Windows:

```bash
venv\Scripts\activate
```

Jika berhasil, biasanya akan muncul `(venv)` pada bagian awal terminal.

## 📦 Install Library

Setelah virtual environment aktif, install library yang dibutuhkan dengan menjalankan perintah:

```bash
pip install streamlit pandas matplotlib
```

## ▶️ Menjalankan Dashboard

Pastikan file `dashboard.py` berada di dalam folder project.

Jalankan dashboard dengan perintah:

```bash
streamlit run dashboard.py
```

Setelah berhasil dijalankan, dashboard dapat dibuka melalui browser pada alamat:

```text
http://localhost:8501
```

## 📁 Dataset

Dashboard menggunakan beberapa file dataset berikut:

* `orders_dataset.csv`
* `order_items_dataset.csv`
* `products_dataset.csv`
* `product_category_name_translation.csv`

Pastikan file dataset tersedia pada folder yang sesuai dengan path yang digunakan pada `dashboard.py`.

## 📌 Fitur Dashboard

Dashboard menampilkan:

* Perkembangan jumlah pesanan per bulan.
* Perkembangan total nilai penjualan per bulan.
* 10 kategori produk dengan jumlah pesanan tertinggi.
* 10 kategori produk dengan total nilai penjualan tertinggi.
* Kesimpulan hasil analisis.

## 👩‍💻 Author

**Hilwa Hilyatun Niswah**

Project Analisis Data — E-Commerce Public Dataset
