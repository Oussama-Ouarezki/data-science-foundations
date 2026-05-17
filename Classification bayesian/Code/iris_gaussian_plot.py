import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from scipy.stats import norm
from sklearn.datasets import load_iris

# Set the style to ggplot
plt.style.use('ggplot')

def main():
    # Load Iris dataset
    iris = load_iris()
    data = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    data['target'] = iris.target
    data['target_names'] = data['target'].map(lambda x: iris.target_names[x])

    # Filter for only two classes (0: setosa, 1: versicolor)
    filtered_data = data[data['target'].isin([0, 1])]
    
    # Get the two class names
    class_names = filtered_data['target_names'].unique()
    print(f"Plotting theoretical Gaussian distributions for classes: {class_names}")

    # Create a figure with 2x2 subplots
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    fig.suptitle('Theoretical Gaussian Distributions of Iris Variables', fontsize=16)

    # Flatten axes for easy iteration
    axes_flat = axes.flatten()
    
    features = iris.feature_names
    colors = {'setosa': 'tab:red', 'versicolor': 'tab:blue'} # manually assigning colors for clarity

    for i, feature in enumerate(features):
        ax = axes_flat[i]
        
        # Determine the range for the x-axis for this feature
        x_min = filtered_data[feature].min() - 1.0
        x_max = filtered_data[feature].max() + 1.0
        x = np.linspace(x_min, x_max, 1000)
        
        for class_name in class_names:
            subset = filtered_data[filtered_data['target_names'] == class_name]
            
            # Calculate mean and standard deviation
            mu = subset[feature].mean()
            std = subset[feature].std()
            
            # Calculate the PDF
            pdf = norm.pdf(x, mu, std)
            
            # Plot
            ax.plot(x, pdf, label=f'{class_name} ($\mu$={mu:.2f}, $\sigma$={std:.2f})', color=colors.get(class_name))
            ax.fill_between(x, pdf, alpha=0.3, color=colors.get(class_name))

        ax.set_title(feature)
        ax.set_xlabel(feature)
        ax.set_ylabel('Probability Density')
        ax.legend()

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    
    output_file = 'iris_gaussian_theoretical.png'
    plt.savefig(output_file)
    print(f"Plot saved to {output_file}")

if __name__ == "__main__":
    main()
