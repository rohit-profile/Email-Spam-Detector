# 📧 Email Spam Detection

[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)](https://www.python.org/) 
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE) 
[![Accuracy](https://img.shields.io/badge/Random%20Forest-100%25-brightgreen)](https://github.com/your-username/email-spam-detection)

A **machine learning-based Email Spam Detection system** that classifies emails as **spam** or **ham (not spam)**. This project uses multiple models and achieves high accuracy with **Random Forest**.  

💻 **Live Deployment:** [Try it online](https://your-deployment-link.com)

---

## 🔹 Dataset

- **Columns Required:**  
  - `text` → content of the email  
  - `label` → spam or ham  

- **Sample Data:**

| text                       | label |
|----------------------------|-------|
| Free money now!!!           | spam  |
| Meeting at 10am tomorrow    | ham   |

> You can use your own dataset or public datasets like the [Enron Spam Dataset](https://www.cs.cmu.edu/~enron/).

---

## 🔹 Models Used

| Model                  | Training Accuracy |
|------------------------|-----------------|
| Logistic Regression     | 96.9%           |
| SVM                     | 99.9%           |
| Random Forest           | 100%             |
| Naive Bayes             | 98.3%           |

> ✅ **Random Forest** is the best performing model and is used for deployment.

---

## 🔹 Features

- Converts email text to numerical data using **TF-IDF vectorization**.  
- Trains **4 machine learning models** for comparison.  
- Saves **trained model and vectorizer** using `pickle` for easy deployment.  
- Ready for **real-time prediction**.

---


