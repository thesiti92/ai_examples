from sklearn.cluster import KMeans
import json
import numpy as np
from datetime import datetime
startTime = datetime.now()
vecs = json.load(open("join_swear_vecs.json"))
means = KMeans(2)
means.fit(vecs)
np.savetxt("swears_2means.dat", means.cluster_centers_)
print datetime.now() - startTime
