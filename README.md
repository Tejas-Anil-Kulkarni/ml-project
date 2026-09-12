# 🎓 Student Performance Prediction

A Machine Learning web application that predicts a student's **Mathematics Score** based on demographic information, parental education, lunch type, test preparation, reading score, and writing score.

The project uses a complete machine learning pipeline including **data ingestion, data transformation, model training, model evaluation, and prediction through a Flask web application**.

---

## 🚀 Features

* 📊 Predicts student Mathematics performance
* 🤖 Machine Learning based prediction
* 🔄 Complete ML training pipeline
* 🧹 Automated data preprocessing
* 📈 Multiple regression models evaluated
* 🔍 Hyperparameter tuning using GridSearchCV
* 🌐 Flask-based web application
* 🎨 Responsive and modern user interface
* ⚠️ Custom exception handling
* 📝 Logging system for debugging and monitoring
* 💾 Trained model and preprocessor saved using Pickle

---

## 🛠️ Technologies Used

### Programming Language

* Python

### Machine Learning

* Scikit-learn
* Pandas
* NumPy

### Web Development

* Flask
* HTML
* CSS
* Jinja2

### Tools

* Anaconda
* Git & GitHub
* VS Code

---

## 📁 Project Structure

```text
project2/
│
├── artifacts/
│   ├── model.pkl
│   └── preprocessor.pkl
│
├── logs/
│
├── notebooks/
│
├── src/
│   ├── components/
│   │   ├── data_ingetion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   │
│   ├── pipeline/
│   │   └── predict/
│   │       └── _pipeline.py
│   │
│   ├── exception.py
│   ├── logger.py
│   └── utils.py
│
├── templates/
│   ├── index.html
│   └── home.html
│
├── static/
│   └── css/
│       └── style.css
│
├── app.py
├── requirements.txt
├── setup.py
└── README.md
```

---

## 🧠 Machine Learning Workflow

The project follows a standard end-to-end ML workflow:

```text
Dataset
   ↓
Data Ingestion
   ↓
Train / Test Split
   ↓
Data Transformation
   ↓
Feature Engineering
   ↓
Model Training
   ↓
Model Evaluation
   ↓
Hyperparameter Tuning
   ↓
Best Model Selection
   ↓
Save Model + Preprocessor
   ↓
Flask Application
   ↓
User Input
   ↓
Prediction
```

---

## 📊 Input Features

The application takes the following inputs:

| Feature                     | Description                                    |
| --------------------------- | ---------------------------------------------- |
| Gender                      | Student's gender                               |
| Race / Ethnicity            | Student's ethnic group                         |
| Parental Level of Education | Parent's highest education level               |
| Lunch                       | Standard or free/reduced lunch                 |
| Test Preparation            | Whether the student completed test preparation |
| Reading Score               | Previous reading score                         |
| Writing Score               | Previous writing score                         |

### Output

The model predicts:

**Mathematics Score**

The predicted score is displayed on the web application.

---

## 🤖 Machine Learning Models

The project evaluates different regression algorithms and uses hyperparameter tuning to select a suitable model.

Some of the models used/evaluated include:

* Linear Regression
* Decision Tree Regressor
* Random Forest Regressor
* Gradient Boosting Regressor
* AdaBoost Regressor
* K-Nearest Neighbors Regressor
* XGBoost Regressor
* CatBoost Regressor

The final model is selected based on its performance on the validation/test data.

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
```

Move into the project directory:

```bash
cd project2
```

---

### 2. Create a virtual environment

Using Conda:

```bash
conda create -n venv python=3.10 -y
```

Activate it:

```bash
conda activate venv
```

You can also use a Python virtual environment if preferred.

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

Start the Flask application:

```bash
python app.py
```

You should see something similar to:

```text
* Running on http://127.0.0.1:5000
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## 🌐 Application Pages

### Home Page

The landing page introduces the Student Performance Prediction application.

### Prediction Page

Users can enter student information and previous reading/writing scores.

The trained machine learning model then predicts the student's Mathematics Score.

---

## 📦 Artifacts

The trained machine learning components are stored in the `artifacts` directory.

```text
artifacts/
├── model.pkl
└── preprocessor.pkl
```

### `model.pkl`

Contains the trained machine learning model.

### `preprocessor.pkl`

Contains the preprocessing pipeline used to transform input data before prediction.

> These files must be available when running the prediction application unless the project is configured to generate them automatically.

---

## 📝 Logging

The project includes a logging system for tracking application events and errors.

Logs are stored inside:

```text
logs/
```

Example log information includes:

* Timestamp
* File name
* Line number
* Log level
* Error messages

---

## ⚠️ Custom Exception Handling

A custom exception class is implemented to provide more useful error messages.

Instead of displaying only:

```text
FileNotFoundError
```

the application can provide information such as:

```text
Error occurred in python script name [...]
in line [...]
error message [...]
```

This makes debugging the ML pipeline easier.

---

## 🔮 Future Improvements

Some possible improvements for this project:

* Add user authentication
* Add prediction history
* Add database support
* Improve model accuracy
* Add data visualization
* Deploy the application online
* Add REST API endpoints
* Add Docker support
* Add automated testing
* Add CI/CD using GitHub Actions
* Improve UI/UX
* Add model performance comparison charts

---

## 📌 Known Considerations

The prediction quality depends on the dataset and trained model.

The predicted Mathematics Score should be treated as a **machine learning estimate**, not an exact representation of a student's future performance.

---

## 👨‍💻 Author

**Tejas**

AIML Engineering Student

This project was developed as part of learning and implementing an **end-to-end Machine Learning project with Flask**.

---

## ⭐ If You Like This Project

If you found this project useful or interesting, consider giving the repository a ⭐ on GitHub.

```text
Machine Learning → Flask → Prediction → Deployment
```

