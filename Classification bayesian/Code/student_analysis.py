
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import precision_score, classification_report, confusion_matrix
import warnings

warnings.filterwarnings('ignore')

# Set ggplot theme
plt.style.use('ggplot')

def load_and_preprocess_data(filepath):
    """
    Loads data and performs preprocessing:
    1. Creates binary target 'passed_math' (>= 60)
    2. Encodes categorical variables
    """
    df = pd.read_csv(filepath)
    
    # Create target variable (1 if Math Score >= 60, else 0)
    target_col = 'math score'
    df['passed_math'] = (df[target_col] >= 60).astype(int)
    
    # Encode categorical variables
    label_encoders = {}
    categorical_cols = df.select_dtypes(include=['object']).columns
    
    df_encoded = df.copy()
    
    for col in categorical_cols:
        le = LabelEncoder()
        df_encoded[col] = le.fit_transform(df[col])
        label_encoders[col] = le
        
    return df_encoded, label_encoders

from scipy.stats import gaussian_kde

# ... (imports are fine, just adding this one is implied or I need to add it to top)

def plot_variable_distributions(df):
    """
    Plots Gaussian distribution (KDE) for each variable using ggplot theme.
    Uses scipy.stats.gaussian_kde to avoid seaborn/matplotlib/pandas version conflicts.
    """
    print("Generating distribution plots...")
    # Select numeric columns (including encoded ones) excluding the binary target
    cols_to_plot = [c for c in df.columns if c != 'passed_math' and c != 'math score']
    
    plt.figure(figsize=(20, 15))
    for i, col in enumerate(cols_to_plot):
        plt.subplot(3, 3, i + 1)
        
        data = df[col].to_numpy()
        
        # Plot Histogram
        plt.hist(data, density=True, alpha=0.5, bins=15, label='Hist')
        
        try:
            # Plot KDE
            density = gaussian_kde(data)
            xs = np.linspace(data.min(), data.max(), 200)
            plt.plot(xs, density(xs), label='KDE (Gaussian)')
        except Exception as e:
            print(f"Could not plot KDE for {col}: {e}")
            
        plt.title(f'Distribution of {col}')
        plt.legend()
    
    plt.tight_layout()
    plt.savefig('variable_distributions.png')
    print("Plots saved to 'variable_distributions.png'")

def perform_pca_and_train(df):
    """
    Performs PCA to reduce to 1 component and trains GaussianNB maximizing precision.
    """
    # Features X: all columns except 'passed_math' (and original 'math score')
    drop_cols = ['passed_math', 'math score']
    X = df.drop(columns=drop_cols)
    y = df['passed_math']
    
    # Standardize features before PCA
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # PCA to reduce to 1 component (as requested: "reduce all the variables ot one")
    pca = PCA(n_components=1)
    X_pca = pca.fit_transform(X_scaled)
    
    print(f"Explained Variance Ratio by 1st PC: {pca.explained_variance_ratio_[0]:.4f}")
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X_pca, y, test_size=0.2, random_state=42)
    
    # Train Model with Hyperparameter Tuning
    # Goal: Maximize Precision
    print("Training Gaussian Naive Bayes with Grid Search for Precision...")
    
    # GaussianNB only has 'var_smoothing' as a main hyperparameter
    param_grid = {
        'var_smoothing': np.logspace(-9, 0, 100)
    }
    
    model = GaussianNB()
    grid_search = GridSearchCV(
        estimator=model,
        param_grid=param_grid,
        scoring='precision',
        cv=5
    )
    
    grid_search.fit(X_train, y_train)
    
    best_model = grid_search.best_estimator_
    print(f"Best Hyperparameters: {grid_search.best_params_}")
    
    # Evaluate
    y_pred = best_model.predict(X_test)
    precision = precision_score(y_test, y_pred)
    
    print(f"\nModel Performance on Test Set:")
    print(f"Precision Score: {precision:.4f}")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
    
    return best_model, pca, scaler

if __name__ == "__main__":
    filepath = '/home/oussama/Desktop/aed_project/StudentsPerformance.csv'
    
    # 1. Load and Clean
    df_encoded, encoders = load_and_preprocess_data(filepath)
    
    # 2. Plot Distributions
    plot_variable_distributions(df_encoded)
    
    # 3. PCA & Modeling
    perform_pca_and_train(df_encoded)
