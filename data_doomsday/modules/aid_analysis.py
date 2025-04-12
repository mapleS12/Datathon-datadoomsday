# File: modules/aid_analysis.py
import matplotlib.pyplot as plt
import seaborn as sns


def aid_vs_impact(emdat):
    aid_data = emdat.groupby('country').agg({
        'total_affected': 'sum',
        'aid_contribution': 'sum'
    }).fillna(0)
    
    aid_data['aid_per_affected'] = aid_data['aid_contribution'] / aid_data['total_affected'].replace(0, 1)
    aid_data.sort_values('aid_per_affected').plot.scatter(x='total_affected', y='aid_contribution', c='aid_per_affected', colormap='viridis')
    plt.title('Aid Received vs Total Affected')
    plt.xlabel('Total Affected')
    plt.ylabel('Aid Contribution')
    plt.tight_layout()
    plt.show()
