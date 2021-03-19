###################### Indíce ####################### 
#---- Instruções
#---- Imports
#---- Funções
#---- Leitura de Ficheiros
#---- Correcções à Base de Dados
#---- Tabelas Descritivas
#     ---- Nrº Ciclistas por País
#     ---- Média, Moda, Mediana, etc
#     ---- Nome dos Vencedores por Edição
#---- Gráficos
#     ---- Ciclistas por Continente
#     ---- Média de Tempo por Ronda e Edição
#     ---- Média de km/H por Edição
#     ---- Média de Idade por Edição
#     ---- Média de Tempo por Corrida 
#---- Testes
#     ---- Tempo para correr código
#===============================================================
#======================== Instruções ===========================
#===============================================================
""" CORRER NA CONSOLA: pip install dataframe_image """

#================= Erros em versões antigas =====================
"""# Garantir que se usa a última versões do Pandas:
# Pandas updated to 1.2.0 or above

# Pandas <= 1.2.0, origina: 
#   'DataFrame' object has no attribute 'to_frame'
# Corrigido com:
# XYZ = XYZ.to_frame()
# XYZ = XYZ.reset_index()

#https://pandas.pydata.org/docs/whatsnew/v1.2.0.html"""

#===============================================================
#========================= Imports =============================
#===============================================================
import matplotlib.pyplot as plt
import dataframe_image as dfi
import seaborn as sns
import pandas as pd
import numpy as np
import unittest
import time
import os
start = time.time()

#===============================================================
#========================= Funções =============================
#===============================================================
#================= Validate Image Directory =====================
def directoryValidator():
    if os.path.isdir("./images/") == False: #check if directory exists
        os.makedirs(os.path.dirname("./images/")) #create directory
    else:
        pass #if it exists, all good.

#================= Image Saver =====================
image_counter = 0
def saveImages(category, graph_name, variable):
    global image_counter, table_counter 
    directoryValidator()
    image_counter += 1
    if (category) == "graph":
        (graph_name).savefig("./images/{}_{}.png".format(str(category),str(image_counter)))
        print("\n\t Graph image saved to 'images' folder as {}_{}.png".format(str(category),str(image_counter)))
    elif (category) == "table":
        (graph_name).export((variable), "./images/{}_{}.png".format(str(category),str(image_counter)))
        print("\n\t Table image saved to 'images' folder as {}_{}.png".format(str(category),str(image_counter)))
    else:
        print("\n No valid image Category found.")

#================= Athlete Age =====================
def obterIdade(nome,pais_jogo): #pais_jogo->host_country
    athlete_id = 0
    idade = None
    contain= False
    for i in athletes["Name"]:
         if i == nome:
            athlete_id = athletes[athletes["Name"]==nome]["Athlete_id"]
            athlete_id = int(athlete_id)
    contagem = sport_events["Host Country"].str.contains(pais_jogo).sum()
    if contagem > 0:
        contain = True
    if athlete_id != 0 and contain == True:
        data_nasc = athletes[athletes["Athlete_id"] == athlete_id]["Date of Birth"].values[0]
        ano_nasc = str(data_nasc[-4:])
        ano_nasc = int(ano_nasc)
        data_jogo = int(sport_events.loc[(sport_events["Athlete_id"] == athlete_id) &
                                         (sport_events["Host Country"] == pais_jogo), ["Year"]].values[0])
        ano_jogo = int (data_jogo)
        idade = ano_jogo-ano_nasc
    return idade

#=============================================================================
#=================== Respective Continents, from "nation" ====================
#---- Caribbean Countries have been put into south_america
asia = ["China", "Japan", "Malaysia", "South Korea"]
africa = ["South Africa"]
europe = ["Czech Republic", "Estonia", "France", "Germany", "Great Britain", "Greece", "Italy",
          "Latvia", "Netherlands", "Poland", "Russia", "Slovakia", "Spain"]
north_america = ["United States"]
oceania = ["Australia", "New Zealand"]
south_america = ["Barbados", "Colombia", "Cuba", "Trinidad and Tobago", "Venezuela"]

#================= Assign Country to a Continent =====================
def getContinent(country):
    if country in asia:
        continent = "Asia"
    elif country in africa:
        continent = "Africa"
    elif country in europe:
        continent = "Europe"
    elif country in north_america:
        continent = "North America"
    elif country in oceania:
        continent = "Oceania"
    elif country in south_america:
        continent = "South America"
    else:
        continent = None
    return continent

#===============================================================
#================== Leitura de Ficheiros =======================
#===============================================================
#================= athletes.csv =====================
athletes = pd.read_csv ("./csv_files/athletes.csv")

#================= sport_events.csv =====================
sport_events = pd.read_csv ("./csv_files/sport_events.csv")
sport_events.drop(sport_events.tail(1).index,inplace=True) #remover o ano de 1896
athletes.drop(athletes.tail(1).index,inplace=True)
#===============================================================
#============ Correcções à Base de Dados =======================
#===============================================================
#---- Mudar tipo de dados e Renomear Colunas
sport_events.columns = ["Year","Athlete_id","Race_id","Rounds","Heat","Time","Average Km/H",
                        "Rank","Result","Record","Host Country","Venue"]

athletes.columns = ["Athlete_id","Name","Date of Birth","Nation","Sex"]

sport_events["Time"] = sport_events["Time"].str.replace(',', '.')
sport_events["Time"] = pd.to_numeric(sport_events["Time"],errors='coerce')

sport_events["Average Km/H"] = sport_events["Average Km/H"].str.replace(',', '.')
sport_events["Average Km/H"] = pd.to_numeric(sport_events["Average Km/H"],errors='coerce')

sport_events["Rounds"] = sport_events["Rounds"].astype("category")
sport_events["Record"] = sport_events["Record"].astype("category")

#---- Verificações
#print(athletes.dtypes)
#print(sport_events.dtypes)

#===============================================================
#=================== Tabelas Descritivas =======================
#===============================================================
#================= Na´s (valores omissos) por coluna da df sport_events ===========
valores_omissos_sport_events = sport_events.isna().sum()
valores_omissos_sport_events = valores_omissos_sport_events.to_frame()
valores_omissos_sport_events.columns=["Sum"]
valores_omissos_sport_events = valores_omissos_sport_events[valores_omissos_sport_events["Sum"] > 0]
saveImages("table", dfi, valores_omissos_sport_events)

#================= Média, Moda, Mediana, etc =====================
time_avg = sport_events[["Time","Average Km/H"]]
summary_sport_events = time_avg.describe()
saveImages("table",dfi, summary_sport_events)

#================= Nrº Ciclistas por País =====================
athlete_countries = athletes.groupby('Nation', as_index=False).size().sort_index(ascending=True)
athlete_countries = athlete_countries.rename(columns={athlete_countries.keys()[0]: "Nation", athlete_countries.keys()[1]: "NºCiclistas"})
athlete_countries = athlete_countries.sort_values(by=["NºCiclistas"])

#---- Criar listas de atletas por país
cols = athlete_countries.columns.tolist()
cols = cols[-1:] + cols[:-1]
athlete_countries = athlete_countries[cols]
saveImages("table",dfi, athlete_countries)

#================= Nome dos Vencedores por Edição =====================
df = pd.DataFrame(sport_events, columns = ["Athlete_id","Result","Time","Record"])

df_2 = df[df["Result"] == "1"]
df_2 = df_2.drop(columns=["Result"])

lista=[]
for i in range(df_2.shape[0]):
    lista.append(1)
array1 = np.array(lista)
df_2["Result"] = array1
#print(df_2)

#---- Agregar Linhas de Colunas
df_2 = df_2.groupby('Athlete_id', as_index=False).agg(
    Victories=pd.NamedAgg(column='Result', aggfunc='sum'), 
    Average_Time=pd.NamedAgg(column='Time', aggfunc='mean'),
    Record=pd.NamedAgg(column='Record', aggfunc='first'))

lista_vencedores=[]
for j in df_2["Athlete_id"]:
    for i in athletes["Athlete_id"]:
        if i == j and athletes["Name"][i-1] not in lista_vencedores:
            lista_vencedores.append(athletes["Name"][i-1])

df_2.drop(df_2.columns[0], axis = 1, inplace = True)
df_2.insert(0, "Name", lista_vencedores)
saveImages("table",dfi, df_2)

#===============================================================
#======================== Gráficos =============================
#===============================================================
#================= Ciclistas por Continente =====================
country = athletes["Nation"]
#---- Add Continent column to dataframe
athletes['Continent'] = country.apply(lambda x: getContinent(x))
athletes["Continent"] = athletes["Continent"].astype('category')
#---- Create Piechart
athlete_continents = athletes.groupby("Continent", as_index=False).size().sort_index(ascending=False)
athlete_continents = athlete_continents.rename(columns={athlete_continents.keys()[0]: "Continente", athlete_continents.keys()[1]: "NºCiclistas"})
athlete_continents = athlete_continents.sort_values(by=["NºCiclistas"], ascending = True)
cols = athlete_continents.columns.tolist()
cols = cols[-1:] + cols[:-1]
athlete_continents = athlete_continents[cols]

pie, ax = plt.subplots(figsize=[10,6])
labels = []
for i in athlete_continents["Continente"]:
    labels.append(i)
x_data = []
for j in athlete_continents["NºCiclistas"]:
    x_data.append(j)
plt.title("Cyclists per Continent", fontsize=14)
pie_chart = plt.pie(x=x_data, autopct="%.1f%%", explode=[0.05]*6, labels=labels, pctdistance=0.5)
saveImages("graph",pie,None)

#================= Média de Tempo por Ronda e Edição =====================
avg_t_per_round_year = pd.DataFrame(data=sport_events.groupby(["Year","Rounds"], as_index=False)["Time"].mean())

#---- Renomear e Agregar Rondas Similares
avg_t_per_round_year = avg_t_per_round_year.replace("1/16 Finals Repechages", "16th-Finals Repechages")
avg_t_per_round_year = avg_t_per_round_year.replace("1/8 Finals Repechages", "Eighth-Finals Repechages")
avg_t_per_round_year = avg_t_per_round_year.replace(["Final for Gold - Race 1","Final for Gold - Race 2",
                                                     "Final for Gold - Race 3"], "Final for Gold")
avg_t_per_round_year = avg_t_per_round_year.replace(["Final for bronze - Race 1",
                                                     "Final for bronze - Race 2","Final for bronze - Race 3"], "Final for Bronze")
avg_t_per_round_year = avg_t_per_round_year.replace(["Quarter Final 1 - Race 1","Quarter Final 1 - Race 2",
                                                     "Quarter Final 2 - Race 1","Quarter Final 2 - Race 2",
                "Quarter Final 3 - Race 1","Quarter Final 3 - Race 2","Quarter Final 4 - Race 1",
                "Quarter Final 4 - Race 2"], "Quarterfinals")
avg_t_per_round_year = avg_t_per_round_year.replace(["Semifinals 1 - Race 1","Semifinals 1 - Race 2",
                                                     "Semifinals 1 - Race 3","Semifinals 2 - Race 1",
                "Semifinals 2 - Race 2","Semifinals 2 - Race 3"], "Semifinals")
avg_t_per_round_year = avg_t_per_round_year.replace("Qualifying", "Qualifying")
avg_t_per_round_year = avg_t_per_round_year.replace("Race for 5th-8th Places", "5-8th Place Race")
avg_t_per_round_year = avg_t_per_round_year.replace("Race for 9th-12th Places", "9-12th Place Race")

avg_t_per_round_year = avg_t_per_round_year.replace("1/16 Finals", "16th-Finals")
avg_t_per_round_year = avg_t_per_round_year.replace("1/8 Finals", "Eighth-Finals")

avg_t_per_round_year = avg_t_per_round_year.groupby(["Year","Rounds"],as_index=False).mean()

#---- Line Plot setup - Order races from earlier to last round
lg_avg_t_per_round_year = sns.catplot(x="Rounds", y="Time", hue="Year", 
                                      kind="point", data = avg_t_per_round_year, 
                                      order=['Qualifying','16th-Finals','16th-Finals Repechages',
                                             '9-12th Place Race','Eighth-Finals',
                                             'Eighth-Finals Repechages','5-8th Place Race',
                                             'Quarterfinals', 'Semifinals', 'Final for Bronze',
                                             'Final for Gold'])

lg_avg_t_per_round_year.fig.set_figheight(10)
lg_avg_t_per_round_year.fig.set_figwidth(20)
lg_avg_t_per_round_year.set_yticklabels(size = 10)
lg_avg_t_per_round_year.set_xticklabels(size = 8.25)
saveImages("graph",lg_avg_t_per_round_year,None)

#================= Média de km/H por Edição =====================
avg_kmh_per_round_year = pd.DataFrame(data=sport_events.groupby(["Average Km/H","Year"], 
                                                                as_index=False)["Average Km/H"].mean())
avg_kmh_per_round_year = pd.DataFrame(data=sport_events.groupby("Year")["Average Km/H"].mean())
avg_kmh_per_round_year["Year"] = avg_kmh_per_round_year.index
#---- Line Plot setup
lg_avg_kmh_per_round_year = sns.catplot(x="Year", y="Average Km/H", kind="point", data = avg_kmh_per_round_year)
lg_avg_kmh_per_round_year.fig.set_figheight(10)
lg_avg_kmh_per_round_year.fig.set_figwidth(20)

lg_avg_kmh_per_round_year.set_yticklabels(size = 12.5).set_xticklabels(size = 12.5)
saveImages("graph",lg_avg_kmh_per_round_year,None)

#================= Média de Tempo por Edição =====================
avg_time_per_round_year = pd.DataFrame(data=sport_events.groupby(["Time","Year"], 
                                                                as_index=False)["Time"].mean())

avg_time_per_round_year = pd.DataFrame(data=sport_events.groupby("Year")["Time"].mean())
avg_time_per_round_year["Year"] = avg_time_per_round_year.index
avg_time_per_round_year.astype("category")
#---- Line Plot setup
lg_avg_time_per_round_year = sns.catplot(x="Year", y="Time", kind="point", data = avg_time_per_round_year)

lg_avg_time_per_round_year.fig.set_figheight(10)
lg_avg_time_per_round_year.fig.set_figwidth(20)
lg_avg_time_per_round_year.set_yticklabels(size = 12.5).set_xticklabels(size = 12.5)

saveImages("graph",lg_avg_time_per_round_year,None)

#================== Média de Idade por Edição =============================
df_3 = pd.DataFrame(sport_events, columns = ["Host Country"])

lista_nomes_ciclistas=[]
for i in sport_events["Athlete_id"]: # i -> athlete_id
    for j in athletes["Athlete_id"]:
         if i == j:
             lista_nomes_ciclistas.append(athletes["Name"][i-1])
df_3["name"] = lista_nomes_ciclistas        
df_3 = df_3.drop_duplicates()
df_3 = df_3.reset_index(drop=True)
lista_idades = []
for i in range(len(df_3)):
    lista_idades.append(obterIdade(df_3["name"][i],df_3["Host Country"][i]))
df_3["Age"] = lista_idades
mean_age_by_edition = df_3.groupby(["Host Country"], as_index=False)["Age"].mean()

mean_age_by_edition = mean_age_by_edition.replace("Brazil", "2016")
mean_age_by_edition = mean_age_by_edition.replace("United Kingdom", "2012")
mean_age_by_edition = mean_age_by_edition.replace("China", "2008")
mean_age_by_edition = mean_age_by_edition.replace("Greece", "2004")
mean_age_by_edition = mean_age_by_edition.replace("Australia", "2000")
mean_age_by_edition.rename(columns={"Host Country": "Olympic Edition"}, inplace=True)
mean_age_by_edition["Age"] = mean_age_by_edition["Age"].round(3)
mean_age_by_edition.astype("category")

mean_age_by_edition_barplot = sns.catplot(x="Olympic Edition", y="Age", hue="Olympic Edition", 
                                          palette="tab10", kind="bar", dodge=False, data=mean_age_by_edition,
                                          order=["2000", "2004", "2008", "2012", "2016"])

for i in mean_age_by_edition_barplot.ax.patches:
    mean_age_by_edition_barplot.ax.annotate("%.2f" % i.get_height(), (i.get_x() + i.get_width() / 2.,
                                            i.get_height()),ha='center', va='center',
                                            fontsize=13, color='black', xytext=(0, 20),
                                            textcoords='offset points')
      
mean_age_by_edition_barplot.set(ylim=(23.5, None))
mean_age_by_edition_barplot.fig.set_figheight(12)
mean_age_by_edition_barplot.fig.set_figwidth(15)
saveImages("graph",mean_age_by_edition_barplot,None)

#================= Média de Tempo por Corrida  =====================
boxplot_one = sns.catplot(x="Time", y="Rounds", kind="box", data=sport_events)

boxplot_one.fig.set_figheight(12)
boxplot_one.fig.set_figwidth(25)

saveImages("graph",boxplot_one,None)

#===============================================================
#======================== Tests ================================
#===============================================================
#================ Tempo para correr código  ====================
end = time.time()
formatted_float = "{:.2f}".format(end - start)
print("\n Code took "+formatted_float+" seconds to run.")

#================ Test Class  ====================
class testFunctions(unittest.TestCase):

    def test_obterIdade_with_valid_parameters(self):
        self.assertEqual(obterIdade("Jason Kenny","Brazil"), 28)

    def test_obterIdade_with_country_not_in_dataset(self):
        self.assertEqual(obterIdade("Jason Kenny","Portugal"), None)

    def test_obterIdade_with_athlete_not_in_dataset(self):
        self.assertEqual(obterIdade("Max","Brazil"), None)

    def test_obterIdade_with_both_parameters_not_in_dataset(self):
        self.assertEqual(obterIdade("Max","Portugal"), None)

    def test_getContinent_with_both_parameters_not_in_dataset(self):
        self.assertEqual(getContinent("Russia"), "Europe")
    
    def test_getContinent_with_country_not_in_dataset(self):
        self.assertEqual(getContinent("Portugal"), None)

unittest.main(argv=['first-arg-is-ignored'], exit=False) #deve retornar ok!
