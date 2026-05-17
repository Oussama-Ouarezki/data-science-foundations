# 📊 Data Science Foundations

A collection of practical reports and implementations covering core data science and machine learning topics — from classical ML models to probability simulations in R.

> 📌 **All reports are organized by topic. Click any title to open the PDF.**

---

## 📁 Repository Structure

```
data-science-foundations/
├── Classification bayesian/
├── Machine Learning Models/
└── Probabilty Distribution with R/
```

---

## 🧠 Bayesian Classification

### 📄 [Bayesian Classifier Report](https://github.com/Oussama-Ouarezki/data-science-foundations/blob/main/Classification%20bayesian/Rapport7.pdf)

> 🎬 **[Watch the video explanation](https://youtu.be/ZLY2h3qgQ_A)**

An in-depth report on **Bayesian classification**, including the mathematical foundations and practical implementation.

---

## 🤖 Machine Learning Models

### 📄 [Linear Regression — Salary & Startup Profit](https://github.com/Oussama-Ouarezki/data-science-foundations/blob/main/Machine%20Learning%20Models/Regression_models.pdf)

Covers **simple and multiple linear regression** — predicting employee salary from experience, and startup profit from R&D, marketing, and location spending.

**Topics covered:**
- Simple linear regression with scatter plot visualization
- One-hot encoding of categorical variables to handle location
- Multiple linear regression with `OneHotEncoder(drop='first')`
- Predicting salary for 15 years of experience and profit for a new startup

---

### 📄 [SVM Classification — Social Network Ads](https://github.com/Oussama-Ouarezki/data-science-foundations/blob/main/Machine%20Learning%20Models/Classification_models.pdf)

Predicts whether a user will purchase a product based on their age and estimated salary using a **Support Vector Machine (SVM)** with a linear kernel.

**Topics covered:**
- Data preprocessing and feature scaling (StandardScaler)
- Train/test split and scatter plot visualization
- Training a linear SVM and drawing the decision boundary
- Evaluating with confusion matrix, accuracy, and F1-score

---

### 📄 [Decision Tree — Titanic Survival](https://github.com/Oussama-Ouarezki/data-science-foundations/blob/main/Machine%20Learning%20Models/Decesion_tree.pdf)

Predicts Titanic passenger survival using a **Decision Tree classifier**, with hyperparameter tuning via GridSearchCV to prevent overfitting.

**Topics covered:**
- Data preprocessing: handling missing values, encoding categorical variables
- Building a default decision tree and visualizing it
- Evaluating accuracy, precision, recall, and F1-score
- Tuning with GridSearchCV and comparing base vs. optimized model

---

### 📄 [Polynomial Regression — Salary Prediction](https://github.com/Oussama-Ouarezki/data-science-foundations/blob/main/Machine%20Learning%20Models/Polynomial_regression.pdf)

Compares **linear vs. polynomial regression** (degree 4) for predicting salary from years of experience, using R² as the evaluation metric.

**Topics covered:**
- Visualizing non-linear relationships
- Applying `PolynomialFeatures` transformation
- Plotting and comparing regression curves
- Predicting salary for a new data point

---

### 📄 [DNA Sequence Alignment — Dynamic Programming](https://github.com/Oussama-Ouarezki/data-science-foundations/blob/main/Machine%20Learning%20Models/Matching%20DNA%20Sequences%20Step%20by%20Step%20Using%20Python.pdf)

Aligns two DNA sequences (`GCGTATGC` and `GCTATAC`) using the **edit distance algorithm** (dynamic programming).

**Topics covered:**
- Formal principle of dynamic programming
- Building the cost matrix (insert, delete, substitute)
- Traceback to find the optimal alignment
- Computing minimum edit distance and operation count

---

## 📈 Probability Distributions with R

### 📄 [Probability Simulation — Geometric Distribution via Rejection Sampling](https://github.com/Oussama-Ouarezki/data-science-foundations/blob/main/Probabilty%20Distribution%20with%20R/Simulation%20de%20lois%20de%20probabilit%C3%A9%20par%20g%C3%A9n%C3%A9rateur%20congruent%20lin%C3%A9aire%20et%20m%C3%A9thode%20de%20rejet%20sous%20R.pdf)

Simulates a **geometric distribution** using a Linear Congruential Generator (LCG) and the **rejection sampling method** in R.

**Topics covered:**
- Implementing a custom LCG pseudo-random number generator
- Finding the support size for the geometric law
- Rejection sampling loop with acceptance condition
- Comparing simulated sequence to `rgeom()` via histograms and ACF plots

---

### 📄 [Probability Simulation — Cauchy Distribution via Box-Muller & Rejection](https://github.com/Oussama-Ouarezki/data-science-foundations/blob/main/Probabilty%20Distribution%20with%20R/Simulation%20of%20Random%20Data%20Using%20Simple%20Sampling%20Methods%20in%20R.pdf)

Simulates a **Cauchy distribution** by first generating Normal samples via the **Box-Muller transform**, then applying rejection sampling.

**Topics covered:**
- Box-Muller transform to generate N(0,9) samples
- Finding the envelope constant M such that M·f_normal ≥ f_cauchy
- Rejection sampling to produce Cauchy(0,1) realizations
- Acceptance ratio analysis and ACF comparison

---

### 📄 [Painters Dataset — Probability Applications in R](https://github.com/Oussama-Ouarezki/data-science-foundations/blob/main/Probabilty%20Distribution%20with%20R/nalyse%20des%20donn%C3%A9es%20des%20peintres%20et%20applications%20probabilistes%20en%20R.pdf)

Explores the `painters` dataset from the MASS library, combining descriptive statistics with hands-on probability calculations and a custom distribution implementation.

**Topics covered:**
- Histograms for each painter criterion (Composition, Drawing, Colour, Expression)
- Manual vs. built-in mean, variance, and standard deviation
- Probability calculations with `pnorm`, `dbinom`, `pbinom`, `qnorm`, `qf`
- Implementing a custom distribution L(b): density `dloi`, CDF `ploi`, quantile `qloi`, sampler `rloi`
- Inverse transform sampling and convergence visualization

---

## 🛠️ Tech Stack

| Language | Libraries |
|----------|-----------|
| Python | `scikit-learn`, `numpy`, `pandas`, `matplotlib` |
| R | `MASS`, base stats (`dnorm`, `dpois`, `rgeom`, `acf`) |

---

## 👤 Author

**Ouarezki Abde Rahim Oussama** — G3  
University of Algiers 1, Faculty of Sciences  
Academic Year 2024–2025
