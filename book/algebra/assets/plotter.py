import matplotlib.pyplot as plt
import numpy as np


def diofantea():
    
    # t = np.arange(0.0, 2.0, 0.01)
    # s = 1 + np.sin(2 * np.pi * t)

    # ax + by = c
    # y = (c - ax) / b
    a, b, c = 2, 3, 10

    top, bottom = -10, 10

    x = np.arange(top, bottom, 1)
    y = (c - a * x) / b

    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.scatter(x, (c - a * x) / b, s=10, c='black')
    ax.set(
        title='Equazione Diofantea',
        xlabel='x', 
        ylabel='y',
        ylim=(top, bottom),
    )
    ax.grid()

    fig.savefig("diofantea.png", transparent=True)
    plt.show()
    pass


diofantea()

# plt.style.use('_mpl-gallery')
#
# # make the data
# np.random.seed(3)
# x = 4 + np.random.normal(0, 2, 24)
# y = 4 + np.random.normal(0, 2, len(x))
# # size and color:
# sizes = np.random.uniform(15, 80, len(x))
# colors = np.random.uniform(15, 80, len(x))
#
# # plot
# fig, ax = plt.subplots()
#
# ax.scatter(x, y, s=sizes, c=colors, vmin=0, vmax=100)
#
# ax.set(
#     title="Diofantea",
#     xlabel="x", ylabel="y",
#     xlim=(-8, 8), xticks=np.arange(-8, 8),
#     ylim=(-8, 8), yticks=np.arange(-8, 8),
# )
#
# plt.savefig("diofantea.png", transparent=False)
# plt.show()
