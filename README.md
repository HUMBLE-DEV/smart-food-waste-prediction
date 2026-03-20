# Smart Food Waste Prediction System

## 📌 Overview
Food waste is a major issue in large food service environments. This project uses **Machine Learning** to predict the number of meals required for a given day, based on historical consumption data and contextual factors (weather, festivals, expected customers). The trained model is deployed in a **Flask web application** with a professional UI.

---

## 📂 Project Structure
```
project_folder/
│── app.py                # Flask backend
│── model.pkl             # Saved ML model
│── dataset.csv           # Historical dataset
│── notebook/
│    └── model_training.ipynb  # ML pipeline notebook
│── templates/
│    └── index.html       # Web interface
│── static/
│    └── style.css        # Styling (blue + black theme)
│── README.md             # Project documentation
```

---

## ⚙️ Features
- End‑to‑end ML pipeline (data preprocessing, EDA, feature engineering, training, evaluation).
- Regression models (Random Forest, Gradient Boosting, XGBoost).
- Flask web app with:
  - Input form for contextual parameters.
  - Real‑time prediction of meals to prepare.
  - Professional UI (blue + black theme, compact layout).
- Error handling for empty/invalid inputs.
- Modular design for future expansion (dashboard, analytics).

---

## 📊 Dataset
Attributes:
- **Day_of_Week** (Monday–Sunday)  
- **Festival** (1 = Festival, 0 = Normal)  
- **Weather** (Sunny, Cloudy, Rainy, Stormy)  
- **Expected_Customers** (numeric)  
- **Previous_Day_Consumption** (numeric)  
- **Previous_Week_Same_Day** (numeric)  
- **Meals_Consumed** (target variable)

---

## 🚀 Installation & Usage
1. Clone the repository:
   ```bash
   git clone <repo_url>
   cd project_folder
   ```
   pip install -r requirements.txt


2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Train the model (optional, if you want to retrain):
   - Open `notebook/model_training.ipynb`
   - Run all cells
   - Save model as `model.pkl`

4. Run Flask app:
   ```bash
   python app.py
   ```

5. Open browser at:
   ```
   http://127.0.0.1:5000/
   ```

---

## 🧪 Example Input
- Day: Friday  
- Weather: Sunny  
- Festival: No  
- Expected Customers: 500  
- Previous Day Consumption: 420  
- Previous Week Same Day: 430  

**Output:**  
`Recommended Meals to Prepare: 435`

---

## ⚠️ Challenges Faced
- Ensuring consistent encoding between training and deployment.  
- Handling empty form inputs gracefully without breaking the app.  
- Balancing model accuracy vs interpretability for stakeholders.  
- Designing a credible UI (blue + black theme, compact columns).  
- Considering data drift for real‑world deployment.

---

## 📈 Future Improvements
- Real‑time data ingestion (weather API, reservations).  
- Automated retraining pipeline.  
- Dashboard with analytics (weekly trends, waste reduction metrics).  
- Cloud deployment (Heroku/AWS).  

---

## 👨‍💻 Author
**Emmanuel Baidoo**  
Level 300 Computer Science Student, University of Energy and Natural Resources  
Internship Program – LearnDepth Academy LLP  

Linkedin - 
