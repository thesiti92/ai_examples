import numpy as np
from json import load
from scipy.spatial.distance import euclidean
lyrics = load(open('join_freq_vecs.json'))
country = lyrics[8000:10000]
rap = lyrics[-5000:-2000]
print len(rap)
means = np.loadtxt('freq_3means.dat')
print means.shape
def genre_clusters(genre):
    return np.bincount([np.argmin([euclidean(vec, mean) for mean in means]) for vec in lyrics])
print genre_clusters(country)
# print genre_clusters(rap)
# print [1 if euclidean(vec, means[0])<euclidean(vec, means[1]) else 0 for vec in rap]
