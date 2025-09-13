import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def scattered(df, last_col):
    columns = df.columns.to_list()
    for item in columns[:last_col]:
        plt.ylabel(f'Column \'{item}\'')
        plt.xticks(rotation=45, horizontalalignment='center')
        plt.minorticks_on()
        plt.grid()
        plt.title('PLOT PER COLUMN')
        plt.scatter(df.index, df[item], label=item.upper(), color='slateblue', marker='.')
        plt.legend()
        plt.show()

def boxplot(data_frame, last_col):
    columnas = data_frame.columns.to_list()
    fig, ax = plt.subplots(last_col, 1, figsize=(10, 20))
    fig.subplots_adjust(hspace=0.75)
    for i in range(last_col):
        sns.boxplot(x=data_frame[columnas[i]], data=data_frame, ax=ax[i])
    plt.show()

def catplot(data_frame, last_col=1, hue=None):
    if hue == None:
        return 'No se especifico una columna de comparacion. => hue=\'{columna en funcion de la que se quiera graficar}\''
    columns = data_frame.columns.to_list()
    del columns[-1]
    plt.figure(figsize=(10,5))
    for item in columns[:last_col]:
        sns.catplot(x = data_frame[hue], y = data_frame[item], data=data_frame, palette='crest')
    plt.show()

def histograms(df, last_col):
    new_df = df.copy()
    columns = new_df.columns.to_list()
    for item in columns[:last_col]:
        
        media = new_df[item].mean()
        desv_est = new_df[item].std()
        array = new_df[item].to_numpy()

        plt.xlabel(f'Column \'{item}\'')
        plt.ylabel('Index')
        plt.xticks(rotation=45, horizontalalignment='center')
        plt.minorticks_on()
        plt.grid()
        plt.title('PLOT PER COLUMN')

        cont, bins, patches = plt.hist(array, color='slateblue', edgecolor='black', density=True, alpha=0.6, label=item.upper())
        x_densidad = np.linspace(bins[0], bins[-1], 100)

        funcion = 1/(desv_est*np.sqrt(2*np.pi)) * np.exp(-0.5*((x_densidad - media)/desv_est)**2)

        plt.plot(x_densidad, funcion, linewidth=2, color='black')
        plt.legend()
        plt.show()

def matrix_corr(df):
    plt.figure(figsize=(10, 8))
    matriz_corr = df.corr()
    sns.heatmap(matriz_corr, annot=True, cmap='inferno', linewidths=0.3, vmin=-1)
    plt.xticks(horizontalalignment='center')
    plt.title('Correlation Matrix')
    plt.show()

def pplot(data_frame, hue):
    sns.pairplot(data_frame, hue=hue, corner=True, palette='plasma')
    plt.show()