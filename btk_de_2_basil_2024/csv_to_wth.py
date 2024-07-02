import pandas as pd
import os

def run():
 #Get the module directory
    module_dir = os.path.dirname(os.path.abspath(__file__))

    # Cargar el archivo CSV
    csv_data = pd.read_csv(os.path.join(module_dir,'weatherdata.csv'))

    # Cargar el contenido del archivo .wth como texto
    wth_file_path = os.path.join(module_dir,'weatherdata_format.wth')
    with open(wth_file_path, 'r') as file:
        wth_content = file.read()

    # Preparar el encabezado del archivo .wth, manteniendo el texto original hasta "Daily weather data:"
    wth_header = wth_content.split("Daily weather data:")[0] + "Daily weather data:\n"

    # Ajustar los datos del CSV: excluir columnas redundantes y reemplazar valores faltantes con 'NaN'
    csv_data_adjusted = csv_data.drop(columns=['Date', 'Srad Wh/m2']).fillna('NaN')

    # Ajustar la función para conservar dos decimales
    def format_with_two_decimals(value):
        try:
            # Verificar si el valor es numérico y formatear a dos decimales
            return "{:.2f}".format(float(value))
        except ValueError:
            # Devolver el valor original si no es numérico
            return value

    # Aplicar el formateo a todas las columnas numéricas
    for col in csv_data_adjusted.columns:
        if col not in ['year-DOY', 'MorP']:
            csv_data_adjusted[col] = csv_data_adjusted[col].apply(format_with_two_decimals)
        
    # Definir los nombres de las columnas para el archivo .wth, basándose en las variables proporcionadas
    column_names = 'Year-DOY    Srad   Tmax   Tmin   Vapr   Tdew   RHmax   RHmin   Wndsp   Rain   ETref   MorP\n'

    # Convertir el DataFrame ajustado a un formato de texto alineado a la derecha para cada valor
    data_text = csv_data_adjusted.to_string(header=False, index=False, formatters={
        'year-DOY': '{:>8}'.format,
        'Srad': '{:>6}'.format,
        'Tmax': '{:>6}'.format,
        'Tmin': '{:>6}'.format,
        'Vapr': '{:>6}'.format,
        'Tdew': '{:>6}'.format,
        'RHmax': '{:>6}'.format,
        'RHmin': '{:>6}'.format,
        'Wndsp': '{:>6}'.format,
        'Rain': '{:>6}'.format,
        'ETref': '{:>6}'.format,
        'MorP': '{:>6}'.format
    })

    # Combinar el encabezado, los nombres de las columnas y los datos para formar el contenido completo del archivo .wth
    wth_content_complete = wth_header + column_names + data_text

    # Guardar el nuevo contenido en un archivo .wth
    new_wth_file_path = os.path.join(module_dir,'transformed_weather_data.wth')
    with open(new_wth_file_path, 'w') as new_file:
        new_file.write(wth_content_complete)

if __name__ == '__main__':
    run()