import numpy as np
import matplotlib as mpl
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d
import argparse

# adapted from https://stackoverflow.com/a/43681906/4607079

def make_random_voronoi_diagrams(N):
    
    for i in range(N):
        # generate data/speed values
        points = np.random.uniform(size=[50, 2])
        speed = np.random.uniform(low=0.0, high=5.0, size=50)

        # generate Voronoi tessellation
        vor = Voronoi(points)

        # find min/max values for normalization
        minima = min(speed)
        maxima = max(speed)

        # normalize chosen colormap
        norm = mpl.colors.Normalize(vmin=minima, vmax=maxima, clip=True)
        mapper = cm.ScalarMappable(norm=norm, cmap=cm.Blues_r)

        # plot Voronoi diagram, and fill finite regions with color mapped from speed value
        voronoi_plot_2d(vor, show_points=True, show_vertices=False, s=1)
        for r in range(len(vor.point_region)):
            region = vor.regions[vor.point_region[r]]
            if not -1 in region:
                polygon = [vor.vertices[i] for i in region]
                plt.fill(*zip(*polygon), color=mapper.to_rgba(speed[r]))
               
        img_file = f"voronoi-{i}.png"
        plt.savefig(img_file)
        print(f"saved {img_file}")


def main():
    parser = argparse.ArgumentParser(description='Process an optional integer.')
    parser.add_argument('-N', type=int, choices=range(1, 10), default=3,
                        help='an optional integer argument (default: 3)')

    args = parser.parse_args()
    print('Received argument:', args.N)
    
    make_random_voronoi_diagrams(args.N)

if __name__ == "__main__":
    main()