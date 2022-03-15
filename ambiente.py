from random import randint as rd

from PyProbs import Probability as pr


#COPIA DEL PROGRAMA "ambiente.py" PERO SIN PONER LA NAVE
def crea_mapa_base(alto=15, largo=30, agua=20, obs=50, mostrar_niveles=False):
    '''
    PROGRAMA DE AMBIENTE PERO SIN LA NAVE
    Esta funcion crea un mapa con strings, el cual esta delimitado por #,
    el simbolo * se refiere al agua y el simbolo - a los obstaculos, 
    tambien puede llevar un numero que representa el nivel topografico del terreno
    ademas de representar a la nave con una letra N.

    Parameters
    ----------
    alto: La altura del mapa
    largo: El largo del mapa 
    agua: La cantidad aproximada de agua
    obs: La cantidad aproximada de obstaculos
    mostrar_niveles: Si se muestra el mapa topografico

    Returns
    --------
    mapa: str del mapa 

    '''
    NIVELES = (0, 1, 2, 3, 4, 5)

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
    if agua_dentro == 0:
        crea_mapa_base()
    else:
        print("Agua ", agua_dentro)
        print("Obs ", obs_dentro)
    return mapa


def run():
    print(crea_mapa_base(15, 30, 20, 50, True))


if __name__ == '__main__':
    run()
