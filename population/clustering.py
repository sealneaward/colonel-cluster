import itertools
import pandas as pd
import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt
import matplotlib as mpl

from sklearn.mixture import BayesianGaussianMixture, GaussianMixture

#####################
# Data
data = pd.read_csv('./data/zone_shooting.csv')

# clean rows of any NaN values
data = data.dropna()

names = data['PLAYER_NAME'].values
X = data.drop([
    'PLAYER_ID',
    'PLAYER_NAME',
    'TEAM_ID',
    'TEAM_ABBREVIATION',
    'AGE',
    'OPP_FGA',
    'OPP_FGM',
    'OPP_FG_PCT',
],1)

#####################

color_iter = itertools.cycle([
    'b', 'c', 'g', 'y','brown',
    'lightgray', 'salmon', 'moccasin',
    'pink', 'purple', 'lime', 'firebrick'
])

def normalize(frame):
    norm = (frame - frame.mean()) / (frame.max() - frame.min())
    return norm

def plot_results(X, Y_, means, covariances, index, title):
    splot = plt.subplot(2, 1, 1 + index)
    for i, (mean, covar, color) in enumerate(zip(means, covariances, color_iter)):
        v, w = linalg.eigh(covar)
        v = 2. * np.sqrt(2.) * np.sqrt(v)
        u = w[0] / linalg.norm(w[0])
        # as the DP will not use every component it has access to
        # unless it needs it, we shouldn't plot the redundant
        # components.
        if not np.any(Y_ == i):
            continue
        plt.scatter(X[Y_ == i, 0], X[Y_ == i, 1], .8, color=color)

        # Plot an ellipse to show the Gaussian component
        angle = np.arctan(u[1] / u[0])
        angle = 180. * angle / np.pi  # convert to degrees
        ell = mpl.patches.Ellipse(mean, v[0], v[1], 180. + angle, color=color)
        ell.set_clip_box(splot.bbox)
        ell.set_alpha(0.5)
        splot.add_artist(ell)

    plt.title(title)


print 'X shape: ' + str(X.shape)
print 'Names shape: ' + str(len(names))

# normalize all measurements
for column in X:
    X[column] = normalize(X[column])

X = X.as_matrix()

# Fit a Gaussian mixture with EM using five components
gmm = GaussianMixture(n_components=10, covariance_type='full').fit(X)
predictions = gmm.predict(X)

i = 0
for player in names:
    print 'Player: ' + player + ' has class: ' + str(predictions[i])
    i += 1

print 'GMM Labels: ' + str(gmm.predict(X))
plot_results(X, gmm.predict(X), gmm.means_, gmm.covariances_, 0,'Gaussian Mixture')

# # Fit a Dirichlet process Gaussian mixture using five components
# dpgmm = BayesianGaussianMixture(n_components=5, covariance_type='full').fit(X)
# print 'GMM Dirichlet Labels: ' + str(dpgmm.predict(X))
# plot_results(X, dpgmm.predict(X), dpgmm.means_, dpgmm.covariances_, 1,'Bayesian Gaussian Mixture with a Dirichlet process prior')

plt.savefig('./plots/GMM_BGM_clusters.jpg')