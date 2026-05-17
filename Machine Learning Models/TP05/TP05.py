import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv('Social_Network_Ads.csv')

data.head()
##############
X = data[['Age', 'EstimatedSalary']]
y = data['Purchased']
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
################
plt.figure(figsize=(8, 6))
plt.scatter(X_train[y_train == 0][:, 0], X_train[y_train == 0][:, 1], color='red', label='Classe 0 (Non acheté)', alpha=0.7)
plt.scatter(X_train[y_train == 1][:, 0], X_train[y_train == 1][:, 1], color='blue', label='Classe 1 (Acheté)', alpha=0.7)


plt.title("Relation entre Age, EstimatedSalary et Purchased (Ensemble d'entraînement)")
plt.xlabel("Age (normalisé)")
plt.ylabel("Salaire estimé (normalisé)")
plt.legend()
plt.grid(True)
plt.show()

############
from sklearn.svm import SVC

# Création du modèle SVM avec un noyau linéaire
svm_linear = SVC(kernel='linear', random_state=42)

# Entraînement du modèle sur l'ensemble d'entraînement
svm_linear.fit(X_train, y_train)
###############

y_pred = svm_linear.predict(X_test)

print("Classes réelles :")
print(y_test.values)

print("\nClasses prédites :")
print(y_pred)
(y_test.values ==y_pred).sum()
(y_test.values !=y_pred).sum()

################
plt.figure(figsize=(8, 6))
plt.scatter(X_train[y_train == 0][:, 0], X_train[y_train == 0][:, 1], color='red', label='Classe 0 (Non acheté)', alpha=0.7)
plt.scatter(X_train[y_train == 1][:, 0], X_train[y_train == 1][:, 1], color='blue', label='Classe 1 (Acheté)', alpha=0.7)

# Tracer la droite séparatrice
# Calcul des coefficients de la droite (w * X + b = 0)
w = svm_linear.coef_[0]
b = svm_linear.intercept_[0]

# Equation de la droite : x2 = -(w[0] * x1 + b) / w[1]
x1_range = np.linspace(X_train[:, 0].min(), X_train[:, 0].max(), 100)
x2_range = -(w[0] * x1_range + b) / w[1]

# Tracer la droite
plt.plot(x1_range, x2_range, color='green', label='Droite séparatrice', linewidth=2)

# Ajout des titres et légendes
plt.title("SVM - Droite séparatrice et points du dataset")
plt.xlabel("Age (normalisé)")
plt.ylabel("Salaire estimé (normalisé)")
plt.legend()
plt.grid(True)
plt.show()


#########
from sklearn.metrics import confusion_matrix, accuracy_score,f1_score

# Calcul de la matrice de confusion
cm = confusion_matrix(y_test, y_pred)
print("Matrice de confusion :")
print(cm)

# Calcul de l'accuracy
accuracy = accuracy_score(y_test, y_pred)
f1=f1_score(y_test,y_pred)
print("\nAccuracy :")
print(accuracy)
print(f1)