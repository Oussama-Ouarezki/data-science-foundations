# 📊 Fondements de la Science des Données / Data Science Foundations

---

## 🇫🇷 Français

Une collection de rapports pratiques et d'implémentations couvrant les thèmes fondamentaux de la science des données et du machine learning — des modèles classiques de ML aux simulations de probabilités en R.

> 📌 **Tous les rapports sont organisés par thème. Cliquez sur le titre pour ouvrir le PDF.**

---

### 📁 Structure du dépôt

```
data-science-foundations/
├── Classification bayesian/
├── Machine Learning Models/
└── Probabilty Distribution with R/
```

---

### 🧠 Classification Bayésienne

#### 📄 [Rapport — Classificateur Bayésien](https://github.com/Oussama-Ouarezki/data-science-foundations/blob/main/Classification%20bayesian/Rapport7.pdf)

> 🎬 **[Regarder la vidéo explicative](https://youtu.be/ZLY2h3qgQ_A)**

Un rapport approfondi sur la **classification bayésienne**, incluant les fondements mathématiques et l'implémentation pratique.

---

### 🤖 Modèles de Machine Learning

#### 📄 [Régression Linéaire — Salaire & Profit de Startup](https://github.com/Oussama-Ouarezki/data-science-foundations/blob/main/Machine%20Learning%20Models/Regression_models.pdf)

Couvre la **régression linéaire simple et multiple** — prédiction du salaire selon l'expérience, et du profit d'une startup selon les dépenses en R&D, marketing et localisation.

**Thèmes abordés :**
- Régression linéaire simple avec visualisation en nuage de points
- Encodage des variables catégorielles avec `OneHotEncoder(drop='first')`
- Régression linéaire multiple
- Prédiction du salaire pour 15 ans d'expérience et du profit pour une nouvelle startup

---

#### 📄 [Classification SVM — Publicités sur Réseaux Sociaux](https://github.com/Oussama-Ouarezki/data-science-foundations/blob/main/Machine%20Learning%20Models/Classification_models.pdf)

Prédit si un utilisateur achètera un produit selon son âge et son salaire estimé, à l'aide d'un **SVM à noyau linéaire**.

**Thèmes abordés :**
- Prétraitement des données et mise à l'échelle (StandardScaler)
- Séparation train/test et visualisation
- Entraînement du SVM et tracé de la frontière de décision
- Évaluation : matrice de confusion, accuracy et F1-score

---

#### 📄 [Arbre de Décision — Survie sur le Titanic](https://github.com/Oussama-Ouarezki/data-science-foundations/blob/main/Machine%20Learning%20Models/Decesion_tree.pdf)

Prédit la survie des passagers du Titanic avec un **arbre de décision**, optimisé via GridSearchCV pour éviter le surapprentissage.

**Thèmes abordés :**
- Prétraitement : valeurs manquantes, encodage des variables
- Construction et visualisation de l'arbre par défaut
- Évaluation : accuracy, précision, rappel, F1-score
- Optimisation avec GridSearchCV et comparaison des modèles

---

#### 📄 [Régression Polynomiale — Prédiction de Salaire](https://github.com/Oussama-Ouarezki/data-science-foundations/blob/main/Machine%20Learning%20Models/Polynomial_regression.pdf)

Compare la **régression linéaire et polynomiale** (degré 4) pour prédire le salaire à partir de l'expérience, en utilisant le R² comme métrique.

**Thèmes abordés :**
- Visualisation de relations non linéaires
- Transformation avec `PolynomialFeatures`
- Comparaison des courbes de régression
- Prédiction pour un nouveau point de données

---

#### 📄 [Alignement de Séquences ADN — Programmation Dynamique](https://github.com/Oussama-Ouarezki/data-science-foundations/blob/main/Machine%20Learning%20Models/Matching%20DNA%20Sequences%20Step%20by%20Step%20Using%20Python.pdf)

Aligne deux séquences ADN (`GCGTATGC` et `GCTATAC`) via l'**algorithme de distance d'édition** (programmation dynamique).

**Thèmes abordés :**
- Principe formel de la programmation dynamique
- Construction de la matrice des coûts (insertion, suppression, substitution)
- Retour en arrière pour trouver l'alignement optimal
- Calcul de la distance minimale et du nombre d'opérations

---

### 📈 Distributions de Probabilités avec R

#### 📄 [Simulation — Loi Géométrique par Méthode de Rejet](https://github.com/Oussama-Ouarezki/data-science-foundations/blob/main/Probabilty%20Distribution%20with%20R/Simulation%20de%20lois%20de%20probabilit%C3%A9%20par%20g%C3%A9n%C3%A9rateur%20congruent%20lin%C3%A9aire%20et%20m%C3%A9thode%20de%20rejet%20sous%20R.pdf)

Simule une **loi géométrique** à l'aide d'un générateur congruent linéaire (GCL) et de la **méthode de rejet** en R.

**Thèmes abordés :**
- Implémentation d'un GCL personnalisé
- Détermination de la taille du support de la loi géométrique
- Boucle de rejet avec condition d'acceptation
- Comparaison avec `rgeom()` via histogrammes et graphiques ACF

---

#### 📄 [Simulation — Loi de Cauchy via Box-Muller & Rejet](https://github.com/Oussama-Ouarezki/data-science-foundations/blob/main/Probabilty%20Distribution%20with%20R/Simulation%20of%20Random%20Data%20Using%20Simple%20Sampling%20Methods%20in%20R.pdf)

Simule une **loi de Cauchy** en générant d'abord des échantillons normaux via la **transformation de Box-Muller**, puis en appliquant la méthode de rejet.

**Thèmes abordés :**
- Transformation de Box-Muller pour générer des échantillons N(0,9)
- Calcul de la constante M telle que M·f_normale ≥ f_cauchy
- Méthode de rejet pour produire des réalisations de Cauchy(0,1)
- Analyse du taux d'acceptation et comparaison ACF

---

#### 📄 [Données des Peintres — Applications Probabilistes en R](https://github.com/Oussama-Ouarezki/data-science-foundations/blob/main/Probabilty%20Distribution%20with%20R/nalyse%20des%20donn%C3%A9es%20des%20peintres%20et%20applications%20probabilistes%20en%20R.pdf)

Explore le jeu de données `painters` de la bibliothèque MASS, en combinant statistiques descriptives, calculs de probabilités et implémentation d'une loi personnalisée.

**Thèmes abordés :**
- Histogrammes par critère (Composition, Dessin, Couleur, Expression)
- Calcul manuel vs fonctions intégrées : moyenne, variance, écart-type
- Calculs de probabilités avec `pnorm`, `dbinom`, `pbinom`, `qnorm`, `qf`
- Implémentation d'une loi L(b) : densité `dloi`, répartition `ploi`, quantile `qloi`, simulateur `rloi`
- Méthode de l'inversion et visualisation de la convergence

---

### 🛠️ Technologies utilisées

| Langage | Bibliothèques |
|---------|---------------|
| Python | `scikit-learn`, `numpy`, `pandas`, `matplotlib` |
| R | `MASS`, stats de base (`dnorm`, `dpois`, `rgeom`, `acf`) |

---

### 👤 Auteur

**Ouarezki Abde Rahim Oussama** 

---
---

## 🇬🇧 English

A collection of practical reports and implementations covering core data science and machine learning topics — from classical ML models to probability simulations in R.

> 📌 **All reports are organized by topic. Click any title to open the PDF.**

---

### 📁 Repository Structure

```
data-science-foundations/
├── Classification bayesian/
├── Machine Learning Models/
└── Probabilty Distribution with R/
```

---

### 🧠 Bayesian Classification

#### 📄 [Bayesian Classifier Report](https://github.com/Oussama-Ouarezki/data-science-foundations/blob/main/Classification%20bayesian/Rapport7.pdf)

> 🎬 **[Watch the video explanation](https://youtu.be/ZLY2h3qgQ_A)**

An in-depth report on **Bayesian classification**, including the mathematical foundations and practical implementation.

---

### 🤖 Machine Learning Models

#### 📄 [Linear Regression — Salary & Startup Profit](https://github.com/Oussama-Ouarezki/data-science-foundations/blob/main/Machine%20Learning%20Models/Regression_models.pdf)

Covers **simple and multiple linear regression** — predicting employee salary from experience, and startup profit from R&D, marketing, and location spending.

**Topics covered:**
- Simple linear regression with scatter plot visualization
- One-hot encoding of categorical variables with `OneHotEncoder(drop='first')`
- Multiple linear regression
- Predicting salary for 15 years of experience and profit for a new startup

---

#### 📄 [SVM Classification — Social Network Ads](https://github.com/Oussama-Ouarezki/data-science-foundations/blob/main/Machine%20Learning%20Models/Classification_models.pdf)

Predicts whether a user will purchase a product based on their age and estimated salary using a **linear kernel SVM**.

**Topics covered:**
- Data preprocessing and feature scaling (StandardScaler)
- Train/test split and scatter plot visualization
- Training a linear SVM and drawing the decision boundary
- Evaluating with confusion matrix, accuracy, and F1-score

---

#### 📄 [Decision Tree — Titanic Survival](https://github.com/Oussama-Ouarezki/data-science-foundations/blob/main/Machine%20Learning%20Models/Decesion_tree.pdf)

Predicts Titanic passenger survival using a **Decision Tree classifier**, with hyperparameter tuning via GridSearchCV to prevent overfitting.

**Topics covered:**
- Data preprocessing: handling missing values, encoding categorical variables
- Building a default decision tree and visualizing it
- Evaluating accuracy, precision, recall, and F1-score
- Tuning with GridSearchCV and comparing base vs. optimized model

---

#### 📄 [Polynomial Regression — Salary Prediction](https://github.com/Oussama-Ouarezki/data-science-foundations/blob/main/Machine%20Learning%20Models/Polynomial_regression.pdf)

Compares **linear vs. polynomial regression** (degree 4) for predicting salary from years of experience, using R² as the evaluation metric.

**Topics covered:**
- Visualizing non-linear relationships
- Applying `PolynomialFeatures` transformation
- Plotting and comparing regression curves
- Predicting salary for a new data point

---

#### 📄 [DNA Sequence Alignment — Dynamic Programming](https://github.com/Oussama-Ouarezki/data-science-foundations/blob/main/Machine%20Learning%20Models/Matching%20DNA%20Sequences%20Step%20by%20Step%20Using%20Python.pdf)

Aligns two DNA sequences (`GCGTATGC` and `GCTATAC`) using the **edit distance algorithm** (dynamic programming).

**Topics covered:**
- Formal principle of dynamic programming
- Building the cost matrix (insert, delete, substitute)
- Traceback to find the optimal alignment
- Computing minimum edit distance and operation count

---

### 📈 Probability Distributions with R

#### 📄 [Probability Simulation — Geometric Distribution via Rejection Sampling](https://github.com/Oussama-Ouarezki/data-science-foundations/blob/main/Probabilty%20Distribution%20with%20R/Simulation%20de%20lois%20de%20probabilit%C3%A9%20par%20g%C3%A9n%C3%A9rateur%20congruent%20lin%C3%A9aire%20et%20m%C3%A9thode%20de%20rejet%20sous%20R.pdf)

Simulates a **geometric distribution** using a Linear Congruential Generator (LCG) and the **rejection sampling method** in R.

**Topics covered:**
- Implementing a custom LCG pseudo-random number generator
- Finding the support size for the geometric law
- Rejection sampling loop with acceptance condition
- Comparing simulated sequence to `rgeom()` via histograms and ACF plots

---

#### 📄 [Probability Simulation — Cauchy Distribution via Box-Muller & Rejection](https://github.com/Oussama-Ouarezki/data-science-foundations/blob/main/Probabilty%20Distribution%20with%20R/Simulation%20of%20Random%20Data%20Using%20Simple%20Sampling%20Methods%20in%20R.pdf)

Simulates a **Cauchy distribution** by first generating Normal samples via the **Box-Muller transform**, then applying rejection sampling.

**Topics covered:**
- Box-Muller transform to generate N(0,9) samples
- Finding the envelope constant M such that M·f_normal ≥ f_cauchy
- Rejection sampling to produce Cauchy(0,1) realizations
- Acceptance ratio analysis and ACF comparison

---

#### 📄 [Painters Dataset — Probability Applications in R](https://github.com/Oussama-Ouarezki/data-science-foundations/blob/main/Probabilty%20Distribution%20with%20R/nalyse%20des%20donn%C3%A9es%20des%20peintres%20et%20applications%20probabilistes%20en%20R.pdf)

Explores the `painters` dataset from the MASS library, combining descriptive statistics with hands-on probability calculations and a custom distribution implementation.

**Topics covered:**
- Histograms for each painter criterion (Composition, Drawing, Colour, Expression)
- Manual vs. built-in mean, variance, and standard deviation
- Probability calculations with `pnorm`, `dbinom`, `pbinom`, `qnorm`, `qf`
- Implementing a custom distribution L(b): density `dloi`, CDF `ploi`, quantile `qloi`, sampler `rloi`
- Inverse transform sampling and convergence visualization

---

### 🛠️ Tech Stack

| Language | Libraries |
|----------|-----------|
| Python | `scikit-learn`, `numpy`, `pandas`, `matplotlib` |
| R | `MASS`, base stats (`dnorm`, `dpois`, `rgeom`, `acf`) |

---

