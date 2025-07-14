当然可以！我已经将你提供的 `README.md` 补全并将 `Usage` 和 `License` 两个部分正确地加进去了 ✅

---

### ✅ 补全后的完整 `README.md` 内容如下：

````markdown
<p align="center">
  <img src="https://raw.githubusercontent.com/FANG-WEIJUN/python-calculator/main/calculator_badge.png" width="150" alt="Calculator Logo">
</p>

<h1 align="center">🧮 Python Calculator</h1>

<p align="center">
  <a href="https://github.com/FANG-WEIJUN/python-calculator"><img src="https://img.shields.io/badge/Language-Python3.7+-blue.svg"></a>
  <a href="https://github.com/FANG-WEIJUN/python-calculator/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-green.svg"></a>
  <img src="https://img.shields.io/badge/GUI-Tkinter-orange.svg">
  <img src="https://img.shields.io/badge/Patches-welcome-brightgreen.svg">
</p>

---

## ✨ Features
- ➕ Basic arithmetic operations
- 🖼️ Graphical interface using **Tkinter**
- 📦 Build executable easily with **PyInstaller**

---

## 📦 Requirements
- 🐍 Python 3.7 or higher
- 📦 [PyInstaller](https://www.pyinstaller.org/) (only required for building `.exe`)

---

## 🛠️ Installation

```bash
git clone https://github.com/FANG-WEIJUN/python-calculator.git
cd python-calculator
python -m venv venv

# Windows
.\venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
````

---

## 🚀 Usage

▶️ **Run the calculator:**

```bash
python calculator.py
```

📦 **Use the built executable (Windows only):**

```bash
.\dist\calculator.exe
```

> You can build it using:
>
> ```bash
> pyinstaller --onefile calculator.py
> ```

---

## 📄 License

This project is licensed under the **MIT License**.
See [`LICENSE`](https://github.com/FANG-WEIJUN/python-calculator/blob/main/LICENSE) for details.
