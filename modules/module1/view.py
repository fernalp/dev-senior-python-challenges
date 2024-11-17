
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

from controller import Controller


class View:
    
    def __init__(self):
        self.controller = Controller()
    
    
    def show_main_menu(self): 
        ##Muestra el Menu Principal
        pass
 
    def show_experiment_management_menu(self): 
        ## Muestra el Menu de agregar y mostrar experimento
        pass
    
    def show_add_experiment_view(self):
        ## Paso a Paso para agregar un experimento
        pass
    
    def show_experiments_view(self):
        ## Mostrar todos los experimentos
        pass
 
    def show_analysis_results_view(self):
        ## Mostrar el analisis de resultados
        pass
    
    def show_generate_report_view(self):
        ## Mostrar vista del reporte generado y preguntar si quiere exportarlo
        pass
 
 
 