# 🎓 Student Performance Predictor

An end-to-end Machine Learning web application that predicts student math scores based on various demographic and educational factors. Built with Flask, scikit-learn, and advanced ML algorithms.

## 📊 Project Overview

This project demonstrates a complete ML pipeline from data analysis to production deployment, predicting student performance using:

- **Dataset**: 1000 student records from Kaggle
- **Target**: Math score prediction (0-100)
- **Features**: Gender, ethnicity, parental education, lunch type, test preparation, reading & writing scores
- **Models**: 8 algorithms with hyperparameter tuning
- **Deployment**: Flask web application

## 🚀 Live Demo

![Student Performance Predictor](https://img.shields.io/badge/Status-Production%20Ready-success)

### Features

- ✅ Real-time math score predictions
- ✅ User-friendly web interface with Bootstrap styling
- ✅ Input validation and error handling
- ✅ Professional ML pipeline architecture
- ✅ Comprehensive logging and exception handling

## 🛠️ Technologies Used

### Machine Learning & Data Science

- **Python 3.11**
- **scikit-learn** - ML algorithms and preprocessing
- **pandas** - Data manipulation
- **numpy** - Numerical computations
- **XGBoost** - Gradient boosting
- **CatBoost** - Categorical feature handling
- **seaborn & matplotlib** - Data visualization

### Web Framework

- **Flask** - Web application framework
- **Bootstrap 5** - Responsive UI design
- **HTML/CSS** - Frontend

### Utilities

- **dill** - Model serialization
- **logging** - Application monitoring

## 📁 Project Structure

```
ML-Project-1/
├── src/
│   ├── components/
│   │   ├── data_ingestion.py       # Data loading & splitting
│   │   ├── data_transformation.py  # Feature engineering & preprocessing
│   │   └── model_trainer.py        # Model training & selection
│   ├── pipeline/
│   │   └── predict_pipeline.py     # Prediction pipeline
│   ├── exception.py                # Custom exception handling
│   ├── logger.py                   # Logging configuration
│   └── utils.py                    # Helper functions
├── artifacts/
│   ├── model.pkl                   # Trained model
│   ├── preprocessor.pkl            # Data preprocessor
│   └── *.csv                       # Dataset splits
├── notebook/
│   ├── 1. EDA STUDENT PERFORMANCE.ipynb
│   └── 2. MODEL TRAINING.ipynb
├── templates/
│   ├── index.html                  # Landing page
│   └── home.html                   # Prediction form
├── app.py                          # Flask application
├── requirements.txt                # Dependencies
├── setup.py                        # Package setup
└── README.md

```

## 🔧 Installation

### Prerequisites

- Python 3.8+
- pip package manager

### Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/kartiksharma1227/ML-Project-1.git
cd ML-Project-1
```

2. **Create virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Install the package**

```bash
pip install -e .
```

## 🎯 Usage

### Running the Web Application

```bash
python app.py
```

The application will start on `http://localhost:8000`

### Making Predictions

1. Navigate to `http://localhost:8000`
2. Click "Get Started"
3. Fill in the student information:
   - Gender
   - Race/Ethnicity
   - Parental education level
   - Lunch type
   - Test preparation course status
   - Reading score (0-100)
   - Writing score (0-100)
4. Click "Predict Math Score"
5. View the predicted math score

### Training the Model (Optional)

To retrain the model with your own data:

```bash
python src/components/data_ingestion.py
```

## 📊 Model Performance

### Models Trained

1. Linear Regression
2. Decision Tree Regressor
3. Random Forest Regressor
4. Gradient Boosting Regressor
5. XGBoost Regressor
6. K-Neighbors Regressor
7. AdaBoost Regressor
8. CatBoost Regressor

### Best Model Selection

- **Method**: GridSearchCV with 3-fold cross-validation
- **Metric**: R² Score
- **Threshold**: R² > 0.6

### Key Insights from EDA

- **Gender Impact**: Female students tend to perform better overall
- **Lunch Type**: Standard lunch correlates with higher scores
- **Parental Education**: Higher education levels lead to better student performance
- **Test Preparation**: Course completion improves scores across all subjects
- **Ethnicity**: Group E students score highest, Group A lowest

## 🔍 ML Pipeline Details

### Data Preprocessing

1. **Numerical Features**: Reading score, Writing score

   - Imputation: Median strategy
   - Scaling: StandardScaler

2. **Categorical Features**: Gender, Ethnicity, Parental education, Lunch, Test prep
   - Imputation: Most frequent strategy
   - Encoding: One-Hot Encoding
   - Scaling: StandardScaler (sparse-aware)

### Feature Engineering

- Train-test split: 80-20
- Random state: 42 (reproducibility)
- Target variable: Math score

## 📈 Results & Visualization

The project includes comprehensive EDA with:

- Distribution analysis
- Correlation heatmaps
- Violin plots for score distributions
- Box plots for outlier detection
- Categorical feature impact analysis

## 🎨 Web Interface Features

- **Responsive Design**: Mobile-friendly Bootstrap 5 UI
- **Form Validation**: Client-side input validation
- **Beautiful UI**: Gradient backgrounds and smooth transitions
- **Real-time Predictions**: Instant results display
- **Error Handling**: User-friendly error messages

## 📝 API Endpoints

| Endpoint       | Method | Description               |
| -------------- | ------ | ------------------------- |
| `/`            | GET    | Landing page              |
| `/predictdata` | GET    | Prediction form           |
| `/predictdata` | POST   | Submit prediction request |

## 🔐 Production Considerations

- ✅ Modular code architecture
- ✅ Comprehensive error handling
- ✅ Logging system for debugging
- ✅ Input validation
- ✅ Model versioning through artifacts
- ✅ Scalable design patterns

## 📦 Dependencies

See `requirements.txt` for full list:

- pandas
- numpy
- seaborn
- matplotlib
- scikit-learn
- catboost
- xgboost
- Flask
- dill

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the MIT License.

## 👤 Author

**Kartik Sharma**

- GitHub: [@kartiksharma1227](https://github.com/kartiksharma1227)
- Email: kartiksharma1227@gmail.com

## 🙏 Acknowledgments

- Dataset source: [Kaggle - Students Performance in Exams](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams)
- Inspired by real-world ML deployment practices

## 📸 Screenshots

### Landing Page

Professional landing page with project overview and features.

### Prediction Interface

User-friendly form with dropdown selections and numerical inputs.

### Results Display

Clean results presentation with predicted math score.

---

⭐ Star this repository if you find it helpful!

**Built with ❤️ using Flask & Machine Learning**
