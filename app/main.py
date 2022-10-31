import utils
import read_csv
import charts
import pandas as pd

def run():
  '''
  data = list(filter(lambda item : item['Continent'] == 'South America',data))
  countries = list(map(lambda x: x['Country'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  '''

  # primera accion: Crear una grafica con los paises y porcentajes de un solo continente 
  # Leer el .csv con pandas y alojarlo en la variable df (dataframe)
  df = pd.read_csv('data.csv')

  # Filtrar todos los datos que en su columna sea south america para reducir la data a un grupo mas analizable 
  df = df[df['Continent'] == 'North America']

  # Obtener los paises junto ocn su porcentaje 
  countries = df['Country'].values
  percentages = df['World Population Percentage'].values

  # Genera grafica con los paises y porcentages a partir del modulo creado charts.py
  charts.generate_pie_chart(countries, percentages)

  # Accion 2: Imprimir un pais 
  data = read_csv.read_csv('data.csv')
  country = input('Type Country => ')
  print(country)

  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    print(country)
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country'], labels, values)
  

if __name__ == '__main__':
  run()