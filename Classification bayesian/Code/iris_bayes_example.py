import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from scipy.stats import norm
from sklearn.datasets import load_iris

# Set the style to ggplot
plt.style.use('ggplot')

def main():
    # 1. Load and Filter Data
    iris = load_iris()
    data = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    data['target'] = iris.target
    data['target_names'] = data['target'].map(lambda x: iris.target_names[x])

    # Filter for only first two classes (0: setosa, 1: versicolor)
    filtered_data = data[data['target'].isin([0, 1])].reset_index(drop=True)
    class_names = filtered_data['target_names'].unique()
    features = iris.feature_names
    
    print("--- Naive Bayes Manual Calculation & Visualization ---")
    print(f"Classes: {class_names}")
    
    # 2. Training Phase: Caclulate Stats
    stats = {}
    priors = {}
    total_samples = len(filtered_data)
    
    for cls in class_names:
        subset = filtered_data[filtered_data['target_names'] == cls]
        priors[cls] = len(subset) / total_samples
        stats[cls] = {}
        for feature in features:
            stats[cls][feature] = {
                'mean': subset[feature].mean(),
                'std': subset[feature].std()
            }
            
    print("\n1. Computed Priors:")
    for cls, prob in priors.items():
        print(f"   P({cls}) = {prob:.4f}")

    print("\n2. Computed Means and Stds:")
    for cls in stats:
        print(f"   Class '{cls}':")
        for feature in features:
            s = stats[cls][feature]
            print(f"     {feature}: mean={s['mean']:.4f}, std={s['std']:.4f}")

    # 3. Choose a Sample
    # Taking a sample (e.g., from class 1 'versicolor' to see how it classifies)
    # The first 50 are setosa (0-49), next 50 are versicolor (50-99). 
    # Let's pick index 55 (should be versicolor).
    sample_index = 55 
    sample = filtered_data.iloc[sample_index]
    true_label = sample['target_names']
    
    print(f"\n3. Analysis for Sample Index {sample_index} (True Class: {true_label})")
    print(f"   Values: {sample[features].to_dict()}")
    
    # 4. Calculate Likelihoods and Posteriors
    posteriors = {}
    likelihoods_trace = {} # To store individual feature likelihoods for printing
    
    for cls in class_names:
        class_likelihood = 1.0
        likelihoods_trace[cls] = {}
        
        for feature in features:
            mu = stats[cls][feature]['mean']
            sigma = stats[cls][feature]['std']
            x = sample[feature]
            
            # Probability Density Function (Likelihood of this feature value given class)
            pdf_val = norm.pdf(x, mu, sigma)
            
            likelihoods_trace[cls][feature] = pdf_val
            class_likelihood *= pdf_val
            
        # Unnormalized Posterior = Prior * Likelihood
        unnormalized_posterior = priors[cls] * class_likelihood
        posteriors[cls] = unnormalized_posterior
        
    # Normalize Posteriors
    total_posterior = sum(posteriors.values())
    normalized_posteriors = {k: v / total_posterior for k, v in posteriors.items()}
    
    print("\n4. Step-by-Step Probability Calculation:")
    for cls in class_names:
        print(f"\n   Class: {cls}")
        print(f"   Prior P({cls}): {priors[cls]:.4f}")
        print("   Feature Likelihoods P(x_i | C):")
        for feat, val in likelihoods_trace[cls].items():
            print(f"     P({feat} = {sample[feat]} | {cls}) = {val:.4f}")
        print(f"   Total Likelihood P(x | {cls}) = {np.prod(list(likelihoods_trace[cls].values())):.6e}")
        print(f"   Unnormalized Posterior P({cls} | x) ~ {posteriors[cls]:.6e}")
        print(f"   -> Final Probability P({cls} | x) = {normalized_posteriors[cls]:.4f}")

    predicted_class = max(normalized_posteriors, key=normalized_posteriors.get)
    print(f"\nPredicted Class: {predicted_class} (Correct: {predicted_class == true_label})")

    # 5. Visualization
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle(f'Naive Bayes Likelihood Visualization for Sample #{sample_index}\n(True: {true_label}, Pred: {predicted_class})', fontsize=16)
    axes_flat = axes.flatten()
    colors = {'setosa': 'tab:red', 'versicolor': 'tab:blue'}
    
    for i, feature in enumerate(features):
        ax = axes_flat[i]
        
        # Plot distributions
        x_min = filtered_data[feature].min() - 0.5
        x_max = filtered_data[feature].max() + 0.5
        x_range = np.linspace(x_min, x_max, 1000)
        
        for cls in class_names:
            mu = stats[cls][feature]['mean']
            std = stats[cls][feature]['std']
            pdf = norm.pdf(x_range, mu, std)
            ax.plot(x_range, pdf, label=f'{cls}', color=colors[cls])
            ax.fill_between(x_range, pdf, alpha=0.1, color=colors[cls])
            
            # Plot the sample point's likelihood on this curve
            sample_val = sample[feature]
            sample_pdf = likelihoods_trace[cls][feature]
            
            # Draw vertical line for the sample value
            ax.axvline(sample_val, color='black', linestyle='--', alpha=0.3)
            
            # Mark the point on the curve
            ax.plot(sample_val, sample_pdf, 'o', color=colors[cls], markersize=8)
            
            # Annotate
            ax.annotate(f'{sample_pdf:.2f}', xy=(sample_val, sample_pdf), xytext=(5, 5), 
                        textcoords='offset points', fontsize=8, color=colors[cls])

        ax.set_title(f"{feature} (val={sample[feature]})")
        ax.set_xlabel(feature)
        ax.set_ylabel('Density / Likelihood')
        if i == 0: ax.legend()

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    
    output_file = 'iris_bayes_likelihood_example.png'
    plt.savefig(output_file)
    print(f"\nPlot saved to {output_file}")

if __name__ == "__main__":
    main()
