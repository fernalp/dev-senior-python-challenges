'''

Clases

Gestión De Experimentos
    Creacion - Visualizacion
Análisis de Resultados
    Promedio - Maximo - Minimo - 
    Comparación (Desempeño Relativo)
Generación de Informe
    Resumen de los experimentos
    Estadisticas
    Conclusiones
    Opcion de Exportar en archivo txt
Cerrar el Programa
'''

## Abstracion de experimento
class Experiment:
  def __init__(self, name, date, type_experiment, results):
    self.name = name
    self.date = date
    self.type_experiment = type_experiment
    self.results = results

## Abstracion de gestión de experimentos
class ExperimentManagement:

  ## Variable encargada de la persistencia de experimentos
  experiments = []
  
  def __init__(self):
    pass
  
  def add_experiment(self, experiment):
    ## Se realiza persistencia de experimento
    pass
  
  def get_experiments(self):
    ## Se exponen los experimentos persistidos o guardados
    pass