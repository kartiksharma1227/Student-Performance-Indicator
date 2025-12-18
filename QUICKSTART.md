# 🚀 Quick Start Guide

## Setup Instructions

### ✅ Already Completed

- ✅ Virtual environment created (`venv/`)
- ✅ All dependencies installed
- ✅ Package installed in editable mode
- ✅ Project is production-ready

## How to Run the Application

### Option 1: Using the Shell Script (Recommended)

```bash
./run_app.sh
```

### Option 2: Manual Activation

```bash
# Activate virtual environment
source venv/bin/activate

# Run the application
python app.py
```

### Option 3: Direct Command

```bash
venv/bin/python app.py
```

## Accessing the Application

Once the server starts, you'll see:

```
* Running on http://0.0.0.0:8000
```

Open your browser and navigate to:

- **Home Page**: http://localhost:8000
- **Prediction Page**: http://localhost:8000/predictdata

## Testing the Prediction

Sample input for testing:

- **Gender**: Female
- **Race/Ethnicity**: Group E
- **Parental Level of Education**: Master's Degree
- **Lunch Type**: Standard
- **Test Preparation Course**: Completed
- **Reading Score**: 85
- **Writing Score**: 88

Expected output: Math score around 80-90

## Stopping the Server

Press `CTRL + C` in the terminal

## Deactivating Virtual Environment

```bash
deactivate
```

## Reinstalling Dependencies (if needed)

```bash
source venv/bin/activate
pip install -r requirements.txt
pip install -e .
```

## Troubleshooting

### If you get "Port already in use" error:

```bash
# Find and kill the process using port 8000
lsof -ti:8000 | xargs kill -9
```

### If virtual environment doesn't activate:

```bash
# Recreate virtual environment
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install -e .
```

## Project Status

✅ **All bugs fixed!**

- ✅ HTML form field names corrected
- ✅ Reading/Writing score inputs fixed
- ✅ Bootstrap styling added
- ✅ Type hints corrected
- ✅ Code cleaned and optimized
- ✅ Professional UI/UX implemented
- ✅ Comprehensive README created

## For Development

### Running Tests (optional)

```bash
source venv/bin/activate
python src/components/data_ingestion.py
```

### Retraining the Model (optional)

```bash
source venv/bin/activate
python src/components/data_ingestion.py
```

This will:

1. Load data from `notebook/data/stud.csv`
2. Split into train/test sets
3. Train 8 different ML models
4. Select the best model
5. Save artifacts to `artifacts/` folder

---

**🎯 Ready for Resume!**

This project demonstrates:

- ✅ End-to-end ML pipeline
- ✅ Production-ready code
- ✅ Web deployment with Flask
- ✅ Professional UI/UX
- ✅ Best practices (logging, error handling, modular design)
