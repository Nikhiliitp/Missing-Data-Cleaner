# 🧹 Missing Data Cleaner

An interactive **Streamlit application** for detecting and cleaning missing values in CSV datasets.

## ✨ Features

- 📂 **CSV File Upload** - Easy file upload through sidebar interface
- 🔍 **Missing Data Analysis** - Comprehensive summary with tables and visualizations
- ⚖️ **Smart Data Imputation** - Fill missing numeric values with mean, median, or mode
- 📝 **Categorical Data Handling** - Fill missing categorical values with mode
- 👀 **Data Preview** - View your cleaned dataset before download
- 💾 **Export Functionality** - Download cleaned data as CSV

## 📋 Requirements

- Python 3.7+
- Required packages listed in `requirements.txt`

## 📊 Supported Data Format

The application accepts CSV files with any column structure. Both numeric and categorical columns are supported.

**Example dataset:**

| Name   | Age | Salary | Department  |
|--------|-----|--------|-------------|
| Ravi   | 28  | NaN    | Sales       |
| Meena  | NaN | 45000  | Engineering |
| Kumar  | 30  | 50000  | NaN         |
| Anita  | 27  | 52000  | Engineering |
| Suresh | NaN | NaN    | NaN         |

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
cd missing-data-cleaner
```

### 2. Verify Python Installation

Ensure you have Python 3.7+ installed:

```bash
python --version
pip --version
```

If Python is not installed, download it from [python.org](https://www.python.org/downloads/).

### 3. Create Virtual Environment

```bash
python -m venv venv
```

### 4. Activate Virtual Environment

**Windows:**
```bash
# Command Prompt
venv\Scripts\activate

# PowerShell
venv\Scripts\Activate.ps1

# Git Bash
source venv/Scripts/activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

You should see `(venv)` in your terminal prompt when the environment is active.

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Application

```bash
streamlit run app.py
```

The application will automatically open in your default web browser.

## 📝 Usage

1. **Upload CSV File** - Use the sidebar file uploader
2. **Analyze Missing Data** - Review the missing data summary and visualizations
3. **Choose Cleaning Strategy** - Select appropriate imputation methods for different column types
4. **Preview Results** - Examine the cleaned dataset
5. **Download** - Export your cleaned data as a CSV file

## 🛠️ Dependencies

Create a `requirements.txt` file with the following packages:

```
streamlit
pandas
matplotlib
```

## 📁 Project Structure

```
missing-data-cleaner/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
└── venv/                 # Virtual environment (created after setup)
```

## 🔧 Troubleshooting

**Common Issues:**

- **Port already in use:** Run `streamlit run app.py --server.port 8502` to use a different port
- **Module not found:** Ensure your virtual environment is activated and dependencies are installed
- **File upload errors:** Check that your CSV file is properly formatted and not corrupted

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

**Happy Data Cleaning! 🎉**
