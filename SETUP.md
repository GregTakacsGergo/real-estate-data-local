# **Project Setup Guide**

## **Prerequisites to run this project**

Before you begin, ensure you have the following software installed on your system:

- **VS Code** (recommended) https://code.visualstudio.com/
- **Python** (version 3.12.6) https://www.python.org/downloads/release/python-3116/
- **Git** https://git-scm.com/downloads
- **MySQL**(version 8.) https://dev.mysql.com/downloads/installer/

### **Step 1: Clone the Repository**

1. Open up Vs Code and Clone the repository to your local machine

```cmd
git clone https://github.com/GregTakacsGergo/real-estate-data-local.git
```

### **Step 2: Create a virtual environment**

```bash
python3.12 -m venv .yourvenv
.yourvenv\Scripts\activate
```
put *.yourvenv* in the .gitignore !

### **Step 3: Install dependencies**

```bash
pip install -r requirements.txt
```

### **Step 4: Set up MySQL connection**

1. Open your downloaded MySQL Workbench
2. Turn on the server if not turned on automatically (usually 127.0.0.1 and port: 3306)
3. Ceate new schema
4. Configure db_config.py with your connection params
5. Create your config.py file ```DB_PASSWORD = "YOUR_pswd_123"```

### **Step 5: Set a SCRAPING_TARGET**

You should ask Greg for the url target, and save it as a variable in your config.py file:

```python 
SCRAPING_TARGET = "a url that leads to a site for which the apartment_data_fetcher.py is customized"
```

