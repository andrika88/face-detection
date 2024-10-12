# Face Detection Project

This is a simple **Face Detection** project using Python and OpenCV. The program captures video from the webcam, detects faces using the Haar Cascade classifier, and draws rectangles around the detected faces in real-time.

## Prerequisites

Sebelum memulai, pastikan Anda telah menginstal Python 3.x di sistem Anda.

## Installation

### 1. Clone the Repository

Clone repository ini ke mesin lokal Anda:
```bash
git clone https://github.com/username/repository-name.git
cd repository-name
```
### 2. Create a Virtual Environment

Buat virtual environment dengan menggunakan venv:

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

Aktifkan virtual environment yang baru saja Anda buat:

- Windows:

```powershell
venv\Scripts\activate
```

- MacOS/Linux: 
```bash
source venv/bin/activate
```

Setelah diaktifkan, Anda akan melihat nama virtual environment di prompt terminal Anda.

### 4. Install OpenCV

Instal OpenCV menggunakan pip:

```bash
pip install opencv-python
```

### 5. Download Haar Cascade XML File

Unduh file haarcascade_frontalface_alt2.xml dari OpenCV GitHub:https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_alt2.xml dan simpan di direktori proyek Anda


# Project Files

haarcascade_frontalface_alt2.xml: Pre-trained Haar Cascade model used for face detection.
main.py: Main Python script for capturing video and detecting faces.

# How to Run
- Pastikan Anda berada di direktori proyek dan virtual environment aktif.

- Jalankan skrip Python:

```bash
python main.py
```
- Sebuah jendela akan terbuka, menampilkan umpan webcam dengan persegi panjang di sekitar wajah yang terdeteksi.

- Tekan q untuk menutup jendela dan menghentikan program.