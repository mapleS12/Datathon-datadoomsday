import pandas as pd
import matplotlib.pyplot as plt


def analyze_trends(emdat):
    t1 = emdat[emdat['year'].between(2000, 2010)]
    t2 = emdat[emdat['year'].between(2011, 2024)]

    freq1 = t1.groupby('country').size()
    freq2 = t2.groupby('country').size()
    trend = pd.DataFrame({'2000–2010': freq1, '2011–2024': freq2}).fillna(0)
    trend['change'] = trend['2011–2024'] - trend['2000–2010']

    trend.sort_values('change', ascending=False).head(10).plot(kind='bar', figsize=(10, 6))
    plt.title('Top Countries by Disaster Frequency Increase')
    plt.ylabel('Number of Disasters')
    plt.tight_layout()
    plt.show()
