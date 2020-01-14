"""
Plot the result of optimal quantization of the von Mises Fisher distribution
on the sphere
"""

import matplotlib.pyplot as plt
import os

import geomstats.visualization as visualization

from geomstats.geometry.hypersphere import Hypersphere
from geomstats.learning.quantization import Quantization


def main():
    sphere = Hypersphere(dimension=2)

    data = sphere.random_von_mises_fisher(kappa=10, n_samples=1000)

    n_clusters = 4
    clustering = Quantization(metric=sphere.metric, n_clusters=n_clusters)
    clustering = clustering.fit(data)

    plt.figure(0)
    ax = plt.subplot(111, projection="3d")
    visualization.plot(points=clustering.cluster_centers_, ax=ax,
            space='S2', c='r')
    plt.show()

    plt.figure(1)
    ax = plt.subplot(111, projection="3d")
    sphere_plot = visualization.Sphere()
    sphere_plot.draw(ax=ax)
    for i in range(n_clusters):
        cluster = data[clustering.labels_==i, :]
        sphere_plot.draw_points(ax=ax, points=cluster)
    plt.show()


if __name__ == "__main__":
    if os.environ['GEOMSTATS_BACKEND'] == 'tensorflow':
        print('Examples with visualizations are only implemented '
              'with numpy backend.\n'
              'To change backend, write: '
              'export GEOMSTATS_BACKEND = \'numpy\'.')
    else:
        main()