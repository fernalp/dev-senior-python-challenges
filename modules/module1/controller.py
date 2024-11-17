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

from model import ExperimentManagement
from view import View


class Controller:
    
    def __init__(self):
        self.experiment_management = ExperimentManagement()
        self.view = View()
        
    
    def execute(self):
        self.view.show_main_menu()
    
    def add_experiment( self, name, date, type_experiment, results):
        ## Se reciben los datos para crear el experimento en ExperimentManagement
        pass
     
    def get_experiments(self):
        ## Se traen los experimentos de ExperimentManagement
        pass
 
    def analysis_of_results(self):
        ## Se traen los experimentos y se realizan el analisis de resultados
        ## Promedio, Minimo, Maximo - Comparacion
        pass
     
    def generate_report(self):
        ## Se genera un resumen de los experimentos
        ## Estadisticas
        ## Conclusiones
        pass
    
    def export_report_to_txt(self, report):
        ## Se exporta el reporte generado
        pass
 
