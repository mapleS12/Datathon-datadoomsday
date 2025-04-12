# File: modules/preprocessing.py
import pandas as pd


def load_and_clean_data(inform_path, emdat_path):
    inform = pd.read_csv(inform_path)
    emdat = pd.read_csv(emdat_path)

    inform.columns = [col.lower().strip().replace(" ", "_") for col in inform.columns]
    emdat.columns = [col.lower().strip().replace(" ", "_") for col in emdat.columns]

    inform.dropna(subset=['country', 'inform_risk'], inplace=True)
    emdat = emdat[emdat['year'].between(2000, 2024)]

    return inform, emdat


# File: modules/eda.py
import matplotlib.pyplot as plt
import seaborn as sns


def run_eda(inform, emdat):
    top_risk = inform.nlargest(5, 'inform_risk')
    print("Top 5 Risk Countries:")
    print(top_risk[['country', 'inform_risk']])

    top3 = top_risk['country'].head(3).tolist()
    emdat_top3 = emdat[emdat['country'].isin(top3)]
    
    plt.figure(figsize=(10, 6))
    sns.countplot(data=emdat_top3, x='year', hue='country')
    plt.title('Disaster Counts (2000–2024) for Top 3 Countries')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Correlation heatmap
    emdat_count = emdat.groupby('country').size().reset_index(name='disaster_count')
    emdat_affected = emdat.groupby('country')['total_affected'].sum().reset_index()
    merged = inform.merge(emdat_count, on='country', how='left').merge(emdat_affected, on='country', how='left')
    
    merged.fillna(0, inplace=True)
    corr = merged[['inform_risk', 'disaster_count', 'total_affected']].corr()

    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix')
    plt.show()
