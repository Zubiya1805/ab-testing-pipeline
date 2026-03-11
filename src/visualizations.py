import matplotlib.pyplot as plt
import seaborn as sns

def plot_conversion_rates(df, save_path=None):
    """
    Plots conversion rate by group.
    """
    conversion_rates = df.groupby('group')['converted'].mean().reset_index()
    
    sns.barplot(data=conversion_rates, x='group', y='converted',
                palette=['#d9534f', '#5cb85c'])
    plt.title('Conversion Rate by Group', fontsize=14, fontweight='bold')
    plt.ylabel('Conversion Rate')
    plt.xlabel('Group')
    plt.ylim(0, 0.15)
    
    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
    plt.show()