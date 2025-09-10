````markdown
# 🧹 Missing Data Cleaner

An interactive **Streamlit app** to detect and clean missing values in your dataset.  
It provides:  
- 📂 **CSV Upload** from sidebar  
- 🔍 **Missing Values Summary (Table + Chart)**  
- ⚖️ **Fill Missing Values with Mean / Median / Mode (numeric)**  
- 📝 **Fill Categorical Columns with Mode**  
- 👀 **Preview Cleaned Dataset**  
- 💾 **Download Cleaned CSV File**  

---

## 📂 Required CSV Format

Your file **must have structured columns** (any schema is supported, but missing values will be cleaned).  
Example:  

| Name   | Age | Salary  | Department   |  
|--------|-----|---------|--------------|  
| Ravi   | 28  | NaN     | Sales        |  
| Meena  | NaN | 45000   | Engineering  |  
| Kumar  | 30  | 50000   | NaN          |  
| Anita  | 27  | 52000   | Engineering  |  
| Suresh | NaN | NaN     | NaN          |  

- **Supports both numeric & categorical columns**  
- Missing values will be handled according to your chosen strategy  

---


````markdown
## ⚙️ Setup & Run Instructions

### 1️⃣ Clone or Download Project
```bash
git clone <your-repo-link>
cd <project-folder>
````

---

### 2️⃣ Install Python and pip

* Download the latest stable Python 3 installer from [python.org](https://www.python.org/downloads/windows/).
* Run the installer and **check "Add python.exe to PATH"**.
* Make sure **pip** is selected during installation.
* Verify installation:

```bash
python --version
pip --version
```

---

### 3️⃣ Create Virtual Environment

Inside your project folder, run:

```bash
python -m venv .venv
```

This will create a folder `.venv` containing the isolated Python environment.

---

### 4️⃣ Activate Virtual Environment

* **Command Prompt / PowerShell:**

```bash
.venv\Scripts\activate
```

* **Git Bash:**

```bash
source .venv/Scripts/activate
```

You’ll know it’s active when you see `(.venv)` at the start of your terminal line.

---

### 5️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 6️⃣ Run Streamlit App

```bash
streamlit run app.py
```

✅ Open the provided **localhost URL** in your browser to start using the app.


---

## 📸 Screenshots

### 🔹 Upload Dataset & Preview

![Upload Dataset](7f0490e8-5421-4a12-b592-c327f918f4b1.png)

### 🔹 Missing Values Summary & Chart

![Missing Values](3ad85e26-435b-49d1-bef2-186a7ccae6d8.png)

### 🔹 Cleaned Dataset Preview & Download Option

![Cleaned Dataset](36eb8c21-1230-459f-9486-1def7acb353e.png)

---
