import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.metrics import classification_report, accuracy_score, precision_score
from scipy.stats import norm

# Set style
plt.style.use('ggplot')

def main():
    print("--- Iris PCA and Gaussian NB Optimization ---")
    
    # 1. Load Data
    iris = load_iris()
    X = iris.data
    y = iris.target
    target_names = iris.target_names

    # Filter for first two classes (0 and 1)
    mask = np.isin(y, [0, 1])
    X = X[mask]
    y = y[mask]
    
    print(f"Filtered Dataset Shape: {X.shape}")
    print(f"Classes: {target_names[0]}, {target_names[1]}")

    # 2. PCA
    # Standardize first
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Apply PCA
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_scaled)
    
    # Create DataFrame for plotting
    df_pca = pd.DataFrame(X_pca, columns=['PC1', 'PC2'])
    df_pca['target'] = y
    df_pca['class'] = df_pca['target'].map(lambda x: target_names[x])
    
    print(f"Explained Variance Ratio: {pca.explained_variance_ratio_}")

    # 3. Scatter Plot
    plt.figure(figsize=(10, 8))
    sns.scatterplot(data=df_pca, x='PC1', y='PC2', hue='class', style='class', s=100, alpha=0.9, palette={'setosa': 'tab:red', 'versicolor': 'tab:blue'})
    plt.title('PCA Scatter Plot of Iris Dataset (2 Classes)')
    plt.savefig('iris_pca_scatter.png')
    print("Saved 'iris_pca_scatter.png'")

    # 4. Gaussian Distributions of PCs
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    fig.suptitle('Theoretical Gaussian Distributions of Principal Components', fontsize=16)
    
    classes = df_pca['class'].unique()
    colors = {'setosa': 'tab:red', 'versicolor': 'tab:blue'}
    
    for i, pc in enumerate(['PC1', 'PC2']):
        ax = axes[i]
        
        # Determine range
        x_min = df_pca[pc].min() - 1
        x_max = df_pca[pc].max() + 1
        x = np.linspace(x_min, x_max, 1000)
        
        for cls in classes:
            subset = df_pca[df_pca['class'] == cls]
            mu = subset[pc].mean()
            std = subset[pc].std()
            
            pdf = norm.pdf(x, mu, std)
            ax.plot(x, pdf, label=f'{cls}', color=colors[cls])
            ax.fill_between(x, pdf, alpha=0.3, color=colors[cls])
            
        ax.set_title(f'Distribution of {pc}')
        ax.set_xlabel(pc)
        ax.set_ylabel('Density')
        ax.legend()
        
    plt.tight_layout()
    plt.savefig('iris_pca_gaussian.png')
    print("Saved 'iris_pca_gaussian.png'")

    # 5. Train Gaussian NB with Optimization for Precision
    print("\n--- Training GaussianNB with Optimization ---")
    
    # Split data (though specific datasets like this are small, good practice)
    X_train, X_test, y_train, y_test = train_test_split(X_pca, y, test_size=0.3, random_state=42, stratify=y)
    
    # Grid Search
    param_grid = {
        'var_smoothing': np.logspace(-9, -1, 50) # Searching over several magnitudes
    }
    
    gnb = GaussianNB()
    # precision_macro because we have 2 classes, can also use binary if we treat one as positive.
    # Since classes are 0 and 1, precision_score default pos_label=1. 
    # Use 'precision' scorer which defaults to binary for binary classification.
    grid = GridSearchCV(gnb, param_grid, cv=5, scoring='precision', verbose=1)
    grid.fit(X_train, y_train)
    
    best_model = grid.best_estimator_
    print(f"Best var_smoothing: {grid.best_params_['var_smoothing']:.2e}")
    print(f"Best Cross-Val Precision: {grid.best_score_:.4f}")
    
    # Evaluate on Test
    y_pred = best_model.predict(X_test)
    
    print("\nTest Set Evaluation:")
    print(classification_report(y_test, y_pred, target_names=[target_names[0], target_names[1]]))
    
    # Confirm precision
    prec = precision_score(y_test, y_pred)
    print(f"Final Test Precision (Class 1 - {target_names[1]}): {prec:.4f}")

if __name__ == "__main__":
    main()
