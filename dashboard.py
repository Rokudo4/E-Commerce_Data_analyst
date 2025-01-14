import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
rfm_df = pd.read_csv(https://raw.githubusercontent.com/Rokudo4/E-Commerce_Data_analyst/refs/heads/main/rfm_df.csv)
sales_product_data = pd.read_csv(https://raw.githubusercontent.com/Rokudo4/E-Commerce_Data_analyst/refs/heads/main/sales_product.csv)
customers_data = pd.read_csv(https://raw.githubusercontent.com/Rokudo4/E-Commerce_Data_analyst/refs/heads/main/customers_df.csv)


# Title and Description
st.title("E-Commerce Dashboard")
st.markdown("### Analisis Data E-Commerce")
st.markdown("Dashboard ini menjawab tiga pertanyaan bisnis utama:")
st.markdown("1. Kota tempat tinggal customer terbanyak.\n2. Kategori produk yang paling banyak terjual.\n3. Analisis RFM pada pelanggan.")

# Kota Tempat Tinggal Customer Terbanyak
st.header("1. Kota Tempat Tinggal Customer Terbanyak")
kota_counts = customers_data['customer_city'].value_counts().head(5)
fig, ax = plt.subplots()
kota_counts.plot(kind='bar', ax=ax, color='skyblue')
ax.set_title("Top 5 Kota dengan Jumlah Customer Terbanyak")
ax.set_xlabel("Kota")
ax.set_ylabel("Jumlah Customer")
st.pyplot(fig)

# Kategori Produk yang Paling Banyak Terjual
st.header("2. Kategori Produk yang Paling Banyak Terjual")
kategori_counts = sales_product_data['product_category_name'].value_counts().head(5)
fig, ax = plt.subplots()
kategori_counts.plot(kind='bar', ax=ax, color='orange')
ax.set_title("Top 5 Kategori Produk")
ax.set_xlabel("Kategori")
ax.set_ylabel("Jumlah Terjual")
st.pyplot(fig)

# Best Customers by Recency, Frequency, and Monetary
st.header("3. Analisis RFM pada Pelanggan")
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

# Top Recency (Lowest is Better)
top_recency = rfm_df.nsmallest(5, 'recency')
axs[0].bar(top_recency['customer_id'], top_recency['recency'], color='skyblue')
axs[0].set_title("By Recency (days)")
axs[0].set_xlabel("Customer ID")
axs[0].set_ylabel("Recency")
axs[0].tick_params(axis='x', rotation=45)

# Top Frequency (Highest is Better)
top_frequency = rfm_df.nlargest(5, 'frequency')
axs[1].bar(top_frequency['customer_id'], top_frequency['frequency'], color='orange')
axs[1].set_title("By Frequency")
axs[1].set_xlabel("Customer ID")
axs[1].set_ylabel("Frequency")
axs[1].tick_params(axis='x', rotation=45)

# Top Monetary (Highest is Better)
top_monetary = rfm_df.nlargest(5, 'monetary')
axs[2].bar(top_monetary['customer_id'], top_monetary['monetary'], color='green')
axs[2].set_title("By Monetary")
axs[2].set_xlabel("Customer ID")
axs[2].set_ylabel("Monetary")
axs[2].tick_params(axis='x', rotation=45)

# Display the plots
st.pyplot(fig)
