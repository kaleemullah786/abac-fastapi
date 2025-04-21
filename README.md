# Project Setup

Follow these steps to set up and run the project:

---

## 1. Create a Virtual Environment

```bash
python -m venv .venv
```
## 2. Activate the Virtual Environment
### On Windows PowerShell:
```bash
.venv\Scripts\activate.ps1
```
### On Windows CMD:
```bash
.venv\Scripts\activate.bat
```
### On macOS/Linux:
```bash
source .venv/bin/activate
```
## 3. Install Dependencies
```bash
pip install -r requirements.txt
```
## 4. Navigate to the App Directory
```bash
cd app
```
## 5. Run the FastAPI Application
```bash
fastapi dev main.py
```
