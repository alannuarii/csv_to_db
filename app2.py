import pandas as pd
from sqlalchemy import create_engine

# Langkah 1: Baca file CSV menggunakan pandas
file_path = 'data\setting_parameter.csv'  # Ganti dengan lokasi file CSV Anda
df = pd.read_csv(file_path)

# Langkah 2: Konversi kolom 'tanggal' dari format 'DD/MM/YYYY' menjadi 'YYYY-MM-DD'
df['tanggal'] = pd.to_datetime(df['tanggal'], format='%d/%m/%Y').dt.strftime('%Y-%m-%d')

# Langkah 3: Buat koneksi ke database
# Ganti 'username', 'password', 'host', 'dbname' sesuai dengan detail database Anda
engine = create_engine('mysql+pymysql://root:root@localhost/bssopt')

# Langkah 4: Upload data ke tabel 'setting_parameter'
df.to_sql('setting_parameter', con=engine, if_exists='replace', index=False)

# Opsional: Cetak pesan sukses
print("Data berhasil diupload ke tabel 'setting_parameter'")
