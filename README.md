# Instagram Crack

[![Python](https://img.shields.io/badge/python-3.12%2B-blue)](https://www.python.org/)
![Author Badge](https://img.shields.io/badge/Author-S.fajar15-blue?style=flat-square&logo=github)
![Python Badge](https://img.shields.io/badge/Written%20In-Python-yellow?style=flat-square&logo=python)
![Open Source Badge](https://img.shields.io/badge/Open%20Source-No-red?style=flat-square&logo=open-source-initiative)

## 📘 Deskripsi
Tools ini merupakan **InstagramCrack** berbasis Python yang digunakan untuk mengelola dan melakukan analisis terhadap akun Instagram.
Secara umum, tools ini berfungsi untuk Mengambil (dump) data pengguna dari berbagai sumber (followers, following, komentar, likes, atau hasil pencarian nama). Melakukan proses login via cookie Instagram. Melakukan validasi akun secara otomatis (cek hidup/mati, checkpoint, atau berhasil login). Menyimpan hasil dump dan hasil login ke dalam folder hasil. Melakukan multi-thread cracking menggunakan metode API Instagram dan Threads.

## 🚀 Fitur Utama
- 🔐 **Login via Cookie Instagram**
- 👥 **Dump Followers / Following**
- 💬 **Dump Username dari Komentar**
- ❤️ **Dump Username dari Likes**
- 🔎 **Dump Berdasarkan Nama**
- 🗂️ **Crack Akun dari File Dump**
- 📊 **Cek Hasil Crack (OK/CP)**

## 📋 Prasyarat

- Python 3.7+
- Module dependencies (lihat requirements.txt)
- Lisensi valid
- Cookie Instagram yang aktif

## 🚀 Instalasi
```bash
pkg update -y && pkg upgrade -y
pkg install clang python-pip libffi openssl libsodium binutils build-essential rust -y
apt install python-cryptography -y
SODIUM_INSTALL=system pip install pynacl
git clone --depth 1 https://github.com/s-fajar15/InstagramC.git
cd "InstagramC"
pip install -r requirements.txt
python run.py
```
