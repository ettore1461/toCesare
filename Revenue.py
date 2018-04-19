"""
Classe per calcolare la Revenue
"""


class Revenue():

    def __init__(self,Diff_data,PBTC_data,RfB_data):
        """
        Carico i dati (Passati come DataFrame).
        Ogni DataFrame deve avere le colonne Values e Days_from_start
        """
        import pandas as pd
        import numpy as np
        import statsmodels.api as sm
        lm_Diff=sm.OLS()



    def N_BTC(self,t,N_block,P):
        """
        Calcolo il numero di BTC prodotti
        :param t: giorni impostati dallo start-point
        :param N_block: Numero di blocchi nel mondo
        :param P: Potenza assorbita
        :return: numero di BTC prodotti
        """
        return (self.RfB(t,N_block)*self.HP(P)*(1000*3600*24))/(self.Diff(t)*(2**32)*10**-9)

    def HP(self,P):
        """
        calcola Hashing Power
        :param P: Potenza ceduta
        :return: Hashing Power
        """
        return 10.22*P

    def RfB(self,t,N_block):pass


    def Diff(self,t):pass


    def P_BTC(self,t):pass


    def Rev(self,P_BTC,t,N_block,P,Pe,CoP=1,Sc=0):

        return (self.P_BTC(t)*self.N_BTC(t,N_block,P))+(Pe*P)(-1+(1-Sc)/CoP)

    def Bokeh_plot(self):
        from bokeh.plotting import figure, show
        from bokeh.models import ColumnDataSource