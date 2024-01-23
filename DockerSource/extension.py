##  ████████▄   ███    █▄     ▄████████ ███▄▄▄▄       ███        ▄████████     ███        ▄████████  ▄████████    ▄█   ▄█▄ 
##  ███    ███  ███    ███   ███    ███ ███▀▀▀██▄ ▀█████████▄   ███    ███ ▀█████████▄   ███    ███ ███    ███   ███ ▄███▀ 
##  ███    ███  ███    ███   ███    ███ ███   ███    ▀███▀▀██   ███    █▀     ▀███▀▀██   ███    ███ ███    █▀    ███▐██▀   
##  ███    ███  ███    ███   ███    ███ ███   ███     ███   ▀   ███            ███   ▀   ███    ███ ███         ▄█████▀    
##  ███    ███  ███    ███ ▀███████████ ███   ███     ███     ▀███████████     ███     ▀███████████ ███        ▀▀█████▄    
##  ███    ███  ███    ███   ███    ███ ███   ███     ███              ███     ███       ███    ███ ███    █▄    ███▐██▄   
##  ███  ▀ ███  ███    ███   ███    ███ ███   ███     ███        ▄█    ███     ███       ███    ███ ███    ███   ███ ▀███▄ 
##  ▀██████▀▄█ ████████▀    ███    █▀   ▀█   █▀     ▄████▀    ▄████████▀     ▄████▀     ███    █▀  ████████▀    ███   ▀█▀ 
##                                                                                                             ▀         

### QUANTARMY STACK 3.1
### 2024 - JCX@QUANTARMY.COM
### QUANTARMY.COM - PYTHONPARATRADING.COM
#################################

# DEFINICION DE LOADERS.
# PARA UTILZIAR NUEVOS, CLONAR EL PRIMERO, Y DEJAR EN LA FUNCION ORIGINAL, EN MOBRE DE BSE_DATA DENTRO DE LA FUNCION.
##

import pandas as pd
from zipline.data.bundles import register, qa_datalake  # CARGAMOS AQUI los bundles

register( # lo registramos
 'qa_datalake', # nombre del dataset
 qa_datalake.bse_data, # nombre del dataset . bse data ( no modificar)
 calendar_name='NYSE',)# Asignar Calendario

