
# File: modules/clustering.py
from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt


def cluster_disaster_types(emdat):
    disaster_pivot = emdat.pivot_table(index='country', columns='disaster_type', aggfunc='size', fill_value=0)
    model = KMeans(n_clusters=4, random_state=42).fit(disaster_pivot)
    disaster_pivot['cluster'] = model.labels_

    plt.figure(figsize=(10, 6))
    for cluster in sorted(disaster_pivot['cluster'].unique()):
        countries = disaster_pivot[disaster_pivot['cluster'] == cluster].index
        plt.barh(countries, [cluster]*len(countries))
    plt.title('Country Clusters by Disaster Type Frequency')
    plt.tight_layout()
    plt.show()

    print(disaster_pivot.groupby('cluster').mean())
