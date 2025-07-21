# 📱 QR Code Generator (Offline)

A lightweight Django web app to generate and download QR codes from any text or URL — **no database, no file saving, and no internet required once hosted locally**.

> ✅ Works in browser and on phone  
> ✅ No database used  
> ✅ Downloadable QR code  
> ✅ Works offline (with local hosting)

---

## 🚀 Features

- ✅ Generate a QR code from any text or URL  
- ✅ Display the QR code on the page  
- ✅ Click to **download the QR code image** (as PNG)  
- ❌ No database (no `models.py`, no `db.sqlite3`)  
- ✅ No file is saved — image is handled in-memory and encoded as base64

---

## 🛠 Built With

- **Python 3.x**
- **Django**
- **qrcode**
- **Pillow**
- **HTML/CSS**
- (Optional) Ready to be upgraded to a Progressive Web App (PWA)

---

## 📄 How It Works

When the user submits a text or link:
- A QR code is generated in memory using the `qrcode` and `Pillow` libraries.
- It is converted to a base64 image.
- The image is embedded in the HTML and can be previewed or downloaded instantly.

---

## 📂 Project Structure

```

qr-code-scanner-offline/
├── manage.py
├── qr\_code\_project/
│   ├── settings.py
│   └── urls.py
├── websites/
│   ├── views.py
│   ├── forms.py
│   ├── templates/
│   │   └── websites/
│   │       └── home.html
├── requirements.txt
├── .gitignore
└── README.md

````

---

## ⚙️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/qr-code-scanner-offline.git
cd qr-code-scanner-offline
````

### 2. Set Up Virtual Environment

```bash
python -m venv myenv
myenv\Scripts\activate   # On Windows
# OR
source myenv/bin/activate  # On Linux/macOS
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the App

```bash
python manage.py runserver
```

Visit: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 🧾 Example Usage

1. Type a link or message (e.g., `https://nust.edu.pk`)
2. Click **"Generate QR Code"**
3. View the generated QR code immediately
4. Click **"Download QR Code"** to save it as a PNG file

---

## 📦 requirements.txt

```
Django>=4.2
qrcode
Pillow
```

---

## 🧾 .gitignore

```
__pycache__/
*.pyc
db.sqlite3
myenv/
.env
```

---

## ✅ To-Do (Optional Enhancements)

* [ ] Add **PWA support** to make the web app work completely offline
* [ ] Add QR **scanning** functionality using JavaScript
* [ ] Allow customization of QR code (size, colors)

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

**Made with ❤️ using Django and Python**
