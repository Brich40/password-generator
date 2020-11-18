from pylab import *
import matplotlib.pyplot as plt


class Graph:

    @staticmethod
    def draw_pwd_symbol_stats(stats):
        x = []
        y = []

        for key, value in stats.items():
            x.append(key.split('_')[0])
            y.append(value)

        plot(x, y)
        plt.xlabel("Taille de mot de passe")
        plt.ylabel("Fréquence")

        show()  # affiche la figure a l'ecran

    @staticmethod
    def draw_bar_graph(contains_stats):
        height = []

        for key, value in contains_stats.items():
            height.append(int(value))

        bars = ('Lettres', 'Numérique', 'Char speciaux ', 'Mixte')

        plt.bar(bars, [x for x in height], label="Usage of the user")
        plt.ylabel("Nombre de mot de passe")
        plt.xlabel("Type de mot de passe")
        plt.title('Statistique général')
        plt.show()
