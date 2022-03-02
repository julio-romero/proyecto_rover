
from random import randint as rd

from PyProbs import Probability as pr


def crea_mapa_base(alto=15, largo=30, agua=20, obs=50, mostrar_niveles=False):
    '''
    Parameters
    ----------
    alto: La altura del mapa
    largo: El largo del mapa 
    agua: La cantidad aproximada de agua
    obs: La cantidad aproximada de obstaculos
    mostrar_niveles: Si se muestra el mapa topografico

    Returns
    --------
    mapa: str del mapa xd
    '''
    NIVELES = (0, 1, 2, 3, 4, 5)
    nave = [rd(0, alto-1), rd(0, largo-1)]
    totales = alto*largo
    prob_agua = agua / totales
    prob_obs = obs / totales
    agua_dentro = 0
    obs_dentro = 0
    mapa = ""
    for i in range(alto+2):  # filas
        for j in range(largo+2):  # columnas
            if i == 0 or i == alto+1 or j == 0 or j == largo+1:
                mapa = mapa + "#"
            elif i == nave[0] and j == nave[1]:
                mapa = mapa + "N"
            elif pr.Prob(prob_agua) and agua_dentro < agua:
                mapa = mapa + "*"
                agua_dentro += 1
            elif pr.Prob(prob_obs) and obs_dentro < obs:
                mapa = mapa + "-"
                obs_dentro += 1
            else:
                if mostrar_niveles:
                    n = rd(0, 5)
                    mapa = mapa + str(NIVELES[n])
                else:
                    mapa = mapa + ' '
        mapa = mapa + '\n'
    print("Nave ubicada en fila:", nave[0], 'columna:', nave[1])
    print("Agua ", agua_dentro)
    print("Obs ", obs_dentro)
    return mapa


def run():
    print(crea_mapa_base(15, 30, 20, 50, True))


if __name__ == '__main__':
    run()
