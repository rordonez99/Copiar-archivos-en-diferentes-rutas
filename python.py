# Copiar-archivos-en-diferentes-rutas
# Copias de archivos
import os
import shutil
from datetime import datetime, timedelta

# Constantes
FILES_PATH_CONEXUS = 'H:/Suiche7B/Recibido/TLf_s7b/archivos/ftp/'
FILES2_PATH_CONEXUS = 'H:/Suiche7B/Recibido/TLf_s7b/archivos/ftp/integra/'
SFTP_PATH_CONEXUS = '//192.168.10.15//sftp//prueba//'
SFTP_PATH_SUICHE = '//192.168.10.15//sftp//prueba//'
TXT_EXTENSION = '.txt'

# Funciones
def copy_file(source_path, destination_path):
    if os.path.isfile(source_path):
        try:
            shutil.copy(source_path, destination_path)
            print(f"Copiado archivo {source_path} a {destination_path}")
        except FileNotFoundError:
            print(f"No se encontró el archivo en la ruta normal {source_path}")
    else:
        print(f"No se encontró el archivo en la ruta normal {source_path}")

def copy_file2(source_path, destination_path):
    if os.path.isfile(source_path):
        try:
            shutil.copy(source_path, destination_path)
            print(f"Copiado archivo {source_path} a {destination_path}")
        except FileNotFoundError:
            print(f"No se generó el archivo en la ruta del integra {source_path}")
    else:
        print(f"No se generó el archivo en la ruta del integra {source_path}")

def main():
    #### Variables principales ###

    # Mercantil
    today = datetime.today()
    format_today_mercantil = today.strftime('%m%d')
    format_yesterday_mercantil = (today + timedelta(days=-1)).strftime('%y%m%d')
    format_yesterday_mercantil1 = (today + timedelta(days=-1)).strftime('%m%d')
    # Banco Fondo Común
    format_today_bfc = today.strftime('%m%d')
    format_yesterday_bfc = (today + timedelta(days=-1)).strftime('%y%m%d')
    format_yesterday_bfc1 = (today + timedelta(days=-1)).strftime('%m%d')
    # Banplus
    format_today_banplus= today.strftime('%m%d')
    format_yesterday_banplus = (today + timedelta(days=-1)).strftime('%y%m%d')
    format_yesterday_banplus1 = (today + timedelta(days=-1)).strftime('%m%d')
    # 100 Banco
    format_today_cienbanco = today.strftime('%m%d')
    format_yesterday_cienbanco = (today + timedelta(days=-1)).strftime('%y%m%d')
    format_yesterday_cienbanco1 = (today + timedelta(days=-1)).strftime('%m%d')
    # Mi Banco
    format_today_mibanco = today.strftime('%m%d')
    format_yesterday_mibanco = (today + timedelta(days=-1)).strftime('%y%m%d')
    format_yesterday_mibanco1 = (today + timedelta(days=-1)).strftime('%m%d')
    
    ### Nombres de archivos ####
    # MERCANTIL
    mercantil_catsw_files = ['faxp2p105', 'faxp2c105', 'faxc2p105', 'revp2p105', 'revp2c105']
    mercantil_suiche_files = ['A105', 'D105', 'AS7B105', 'DS7B105', 'AS7BP2P105', 'DS7BP2P105', 'AS7BP2C105', 'DS7BP2C105', 'AS7BC2P105', 'DS7BC2P105']
    mercantil_integra_archive1 = ['A105']
    mercantil_integra_archive2 = ['D105']
    # BANCO FONDO COMÚN
    bfc_catsw_files = ['faxp2p151', 'faxp2c151', 'faxc2p151', 'revp2p151', 'revp2c151']
    bfc_suiche_files = ['A151', 'D151', 'AS7B151', 'DS7B151', 'AS7BP2P151', 'DS7BP2P151', 'AS7BP2C151', 'DS7BP2C151', 'AS7BC2P151', 'DS7BC2P151', 'P151']
    bfc_integra_archive1 = ['A151']
    bfc_integra_archive2 = ['D151']
    # BANPLUS
    banplus_catsw_files = ['faxp2p174', 'faxp2c174', 'faxc2p174', 'revp2p174', 'revp2c174']
    banplus_suiche_files = ['A174', 'D174', 'AS7B174', 'DS7B174', 'AS7BP2P174', 'DS7BP2P174', 'AS7BP2C174', 'DS7BP2C174', 'AS7BC2P174', 'DS7BC2P174', 'P174']
    banplus_integra_archive1 = ['A174']
    banplus_integra_archive2 = ['D174']
    # 100% BANCO
    cienbanco_catsw_files = ['faxp2p156', 'faxp2c156', 'faxc2p156', 'revp2p156', 'revp2c156']
    cienbanco_suiche_files = ['A156', 'D156', 'AS7B156', 'DS7B156', 'AS7BP2P156', 'DS7BP2P156', 'AS7BP2C156', 'DS7BP2C156', 'AS7BC2P156', 'DS7BC2P156', 'P156']
    cienbanco_integra_archive1 = ['A156']
    cienbanco_integra_archive2 = ['D156']
    # MI BANCO
    mibanco_catsw_files = ['faxp2p169', 'faxp2c169', 'faxc2p169', 'revp2p169', 'revp2c169']
    mibanco_suiche_files = ['A169', 'D169', 'AS7B169', 'DS7B169', 'AS7BP2P169', 'DS7BP2P169', 'AS7BP2C169', 'DS7BP2C169', 'AS7BC2P169', 'DS7BC2P169', 'P169']
    mibanco_integra_archive1 = ['A169']
    mibanco_integra_archive2 = ['D169']
    
# Día normal 

    # Copia de archivos mercantil_conexus
    for file_name in mercantil_catsw_files:
        origen = FILES_PATH_CONEXUS + f'mercantil/{file_name}{format_yesterday_mercantil}'
        destino = SFTP_PATH_CONEXUS + f'mercantil/{file_name}{format_yesterday_mercantil}{TXT_EXTENSION}'
        copy_file(origen, destino)

    # Copia de archivos mercantil_suiche
    for file_name in mercantil_suiche_files:
        origen = FILES_PATH_CONEXUS + f'mercantil/{file_name}{format_yesterday_mercantil1}{TXT_EXTENSION}'
        destino = SFTP_PATH_SUICHE + f'mercantil/{file_name}{format_yesterday_mercantil1}{TXT_EXTENSION}'
        copy_file(origen, destino)
  
    # Copia de archivos bfc_conexus
    for file_name in bfc_catsw_files:
        origen = FILES_PATH_CONEXUS + f'bfc/{file_name}{format_yesterday_bfc}'
        destino = SFTP_PATH_CONEXUS + f'bfc/{file_name}{format_yesterday_bfc}{TXT_EXTENSION}'
        copy_file(origen, destino)

    # Copia de archivos bfc_suiche
    for file_name in bfc_suiche_files:
        origen = FILES_PATH_CONEXUS + f'bfc/{file_name}{format_yesterday_bfc1}{TXT_EXTENSION}'
        destino = SFTP_PATH_SUICHE + f'bfc/{file_name}{format_yesterday_bfc1}{TXT_EXTENSION}'
        copy_file(origen, destino)
    
    # Copia de archivos banplus_conexus
    for file_name in banplus_catsw_files:
        origen = FILES_PATH_CONEXUS + f'banplus/{file_name}{format_yesterday_banplus}'
        destino = SFTP_PATH_CONEXUS + f'banplus/{file_name}{format_yesterday_banplus}{TXT_EXTENSION}'
        copy_file(origen, destino)

    # Copia de archivos banplus_suiche
    for file_name in banplus_suiche_files:
        origen = FILES_PATH_CONEXUS + f'banplus/{file_name}{format_yesterday_banplus1}{TXT_EXTENSION}'
        destino = SFTP_PATH_SUICHE + f'banplus/{file_name}{format_yesterday_banplus1}{TXT_EXTENSION}'
        copy_file(origen, destino)
    
    # Copia de archivos 100banco_conexus
    for file_name in cienbanco_catsw_files:
        origen = FILES_PATH_CONEXUS + f'100banco/{file_name}{format_yesterday_cienbanco}'
        destino = SFTP_PATH_CONEXUS + f'100banco/{file_name}{format_yesterday_cienbanco}{TXT_EXTENSION}'
        copy_file(origen, destino)

    # Copia de archivos 100banco_suiche
    for file_name in cienbanco_suiche_files:
        origen = FILES_PATH_CONEXUS + f'100banco/{file_name}{format_yesterday_cienbanco1}{TXT_EXTENSION}'
        destino = SFTP_PATH_SUICHE + f'100banco/{file_name}{format_yesterday_cienbanco1}{TXT_EXTENSION}'
        copy_file(origen, destino)

    # Copia de archivos mibanco_conexus
    for file_name in mibanco_catsw_files:
        origen = FILES_PATH_CONEXUS + f'mibanco/{file_name}{format_yesterday_mibanco}'
        destino = SFTP_PATH_CONEXUS + f'mibanco/{file_name}{format_yesterday_mibanco}{TXT_EXTENSION}'
        copy_file(origen, destino)

    # Copia de archivos mibanco_suiche
    for file_name in mibanco_suiche_files:
        origen = FILES_PATH_CONEXUS + f'mibanco/{file_name}{format_yesterday_mibanco1}{TXT_EXTENSION}'
        destino = SFTP_PATH_SUICHE + f'mibanco/{file_name}{format_yesterday_mibanco1}{TXT_EXTENSION}'
        copy_file(origen, destino)

# Cuando se realiza el integra

    # Copia de archivos mercantil_integra_A105
    for file_name in mercantil_integra_archive1:
        origen = FILES2_PATH_CONEXUS + f'mercantil/{file_name}{format_today_mercantil}{TXT_EXTENSION}'
        destino = SFTP_PATH_SUICHE + f'mercantil/{file_name}{format_yesterday_mercantil1}{TXT_EXTENSION}'
        copy_file2(origen, destino)
        archive_old_mercantil_A105 = FILES2_PATH_CONEXUS + f'mercantil/{file_name}{format_today_mercantil}{TXT_EXTENSION}'
        archive_new_mercantil_A105 = FILES2_PATH_CONEXUS + f'mercantil/{file_name}{format_yesterday_mercantil1}{TXT_EXTENSION}'
    if os.path.exists(archive_old_mercantil_A105) == True:
        os.rename(archive_old_mercantil_A105,archive_new_mercantil_A105)
        #print("Se renombró los archivos integra mercantil A105 en la ruta " + FILES2_PATH_CONEXUS + f'mercantil/' )

    # Copia de archivos mercantil_integra_D105
    for file_name in mercantil_integra_archive2:
        origen = FILES2_PATH_CONEXUS + f'mercantil/{file_name}{format_today_mercantil}{TXT_EXTENSION}'
        destino = SFTP_PATH_SUICHE + f'mercantil/{file_name}{format_yesterday_mercantil1}{TXT_EXTENSION}'
        copy_file2(origen, destino)
        archive_old_mercantil_D105 = FILES2_PATH_CONEXUS + f'mercantil/{file_name}{format_today_mercantil}{TXT_EXTENSION}'
        archive_new_mercantil_D105 = FILES2_PATH_CONEXUS + f'mercantil/{file_name}{format_yesterday_mercantil1}{TXT_EXTENSION}'
    if os.path.exists(archive_old_mercantil_D105) == True:
        os.rename(archive_old_mercantil_D105,archive_new_mercantil_D105)
        #print("Se renombró los archivos integra mercantil D105 en la ruta " + FILES2_PATH_CONEXUS + f'mercantil/' )

    # Copia de archivos bfc_integra_A151
    for file_name in bfc_integra_archive1:
        origen = FILES2_PATH_CONEXUS + f'bfc/{file_name}{format_today_bfc}{TXT_EXTENSION}'
        destino = SFTP_PATH_SUICHE + f'bfc/{file_name}{format_yesterday_bfc1}{TXT_EXTENSION}'
        copy_file2(origen, destino)
        archive_old_bfc_A151 = FILES2_PATH_CONEXUS + f'bfc/{file_name}{format_today_bfc}{TXT_EXTENSION}'
        archive_new_bfc_A151 = FILES2_PATH_CONEXUS + f'bfc/{file_name}{format_yesterday_bfc1}{TXT_EXTENSION}'
    if os.path.exists(archive_old_bfc_A151) == True:
        os.rename(archive_old_bfc_A151,archive_new_bfc_A151)
        #print("Se renombró los archivos integra BFC A151 en la ruta " + FILES2_PATH_CONEXUS +  f'bfc/' )

    # Copia de archivos bfc_integra_D151
    for file_name in bfc_integra_archive2:
        origen = FILES2_PATH_CONEXUS + f'bfc/{file_name}{format_today_bfc}{TXT_EXTENSION}'
        destino = SFTP_PATH_SUICHE + f'bfc/{file_name}{format_yesterday_bfc1}{TXT_EXTENSION}'
        copy_file2(origen, destino)
        archive_old_bfc_D151 = FILES2_PATH_CONEXUS + f'bfc/{file_name}{format_today_bfc}{TXT_EXTENSION}'
        archive_new_bfc_D151 = FILES2_PATH_CONEXUS + f'bfc/{file_name}{format_yesterday_bfc1}{TXT_EXTENSION}'
    if os.path.exists(archive_old_bfc_D151) == True:
        os.rename(archive_old_bfc_D151,archive_new_bfc_D151)
        #print("Se renombró los archivos integra BFC D151 en la ruta " + FILES2_PATH_CONEXUS + f'bfc/' )

    # Copia de archivos banplus_integra_A174
    for file_name in banplus_integra_archive1:
        origen = FILES2_PATH_CONEXUS + f'banplus/{file_name}{format_today_banplus}{TXT_EXTENSION}'
        destino = SFTP_PATH_SUICHE + f'banplus/{file_name}{format_yesterday_banplus1}{TXT_EXTENSION}'
        copy_file2(origen, destino)
        archive_old_banplus_A174 = FILES2_PATH_CONEXUS + f'banplus/{file_name}{format_today_banplus}{TXT_EXTENSION}'
        archive_new_banplus_A174 = FILES2_PATH_CONEXUS + f'banplus/{file_name}{format_yesterday_banplus1}{TXT_EXTENSION}'
    if os.path.exists(archive_old_banplus_A174) == True:
        os.rename(archive_old_banplus_A174,archive_new_banplus_A174)
        #print("Se renombró los archivos integra Banplus A174 en la ruta " + FILES2_PATH_CONEXUS + f'banplus/')

    # Copia de archivos banplus_integra_D174
    for file_name in banplus_integra_archive2:
        origen = FILES2_PATH_CONEXUS + f'banplus/{file_name}{format_today_banplus}{TXT_EXTENSION}'
        destino = SFTP_PATH_SUICHE + f'banplus/{file_name}{format_yesterday_banplus1}{TXT_EXTENSION}'
        copy_file2(origen, destino)
        archive_old_banplus_D174 = FILES2_PATH_CONEXUS + f'banplus/{file_name}{format_today_banplus}{TXT_EXTENSION}'
        archive_new_banplus_D174 = FILES2_PATH_CONEXUS + f'banplus/{file_name}{format_yesterday_banplus1}{TXT_EXTENSION}'
    if os.path.exists(archive_old_banplus_D174) == True:
        os.rename(archive_old_banplus_D174,archive_new_banplus_D174)
        #print("Se renombró los archivos integra Banplus D174 en la ruta " + FILES2_PATH_CONEXUS + f'banplus/')

    # Copia de archivos 100banco_integra_A156
    for file_name in cienbanco_integra_archive1:
        origen = FILES2_PATH_CONEXUS + f'100banco/{file_name}{format_today_cienbanco}{TXT_EXTENSION}'
        destino = SFTP_PATH_SUICHE + f'100banco/{file_name}{format_yesterday_cienbanco1}{TXT_EXTENSION}'
        copy_file2(origen, destino) 
        archive_old_cien_A156 = FILES2_PATH_CONEXUS + f'100banco/{file_name}{format_today_cienbanco}{TXT_EXTENSION}'
        archive_new_cien_A156 = FILES2_PATH_CONEXUS + f'100banco/{file_name}{format_yesterday_cienbanco1}{TXT_EXTENSION}'
    if os.path.exists(archive_old_cien_A156) == True:
        os.rename(archive_old_cien_A156,archive_new_cien_A156)      
        #print("Se renombró los archivos integra 100banco A156 en la ruta " + FILES2_PATH_CONEXUS + f'100banco/')

    # Copia de archivos 100banco_integra_D156
    for file_name in cienbanco_integra_archive2:
        origen = FILES2_PATH_CONEXUS + f'100banco/{file_name}{format_today_cienbanco}{TXT_EXTENSION}'
        destino = SFTP_PATH_SUICHE + f'100banco/{file_name}{format_yesterday_cienbanco1}{TXT_EXTENSION}'
        copy_file2(origen, destino) 
        archive_old_cien_D156 = FILES2_PATH_CONEXUS + f'100banco/{file_name}{format_today_cienbanco}{TXT_EXTENSION}'
        archive_new_cien_D156 = FILES2_PATH_CONEXUS + f'100banco/{file_name}{format_yesterday_cienbanco1}{TXT_EXTENSION}'
    if os.path.exists(archive_old_cien_D156) == True:
        os.rename(archive_old_cien_D156,archive_new_cien_D156)      
        #print("Se renombró los archivos integra 100banco D156 en la ruta " + FILES2_PATH_CONEXUS + f'100banco/')

    # Copia de archivos mibanco_integra_A169
    for file_name in mibanco_integra_archive1:
        origen = FILES2_PATH_CONEXUS + f'mibanco/{file_name}{format_today_mibanco}{TXT_EXTENSION}'
        destino = SFTP_PATH_SUICHE + f'mibanco/{file_name}{format_yesterday_mibanco1}{TXT_EXTENSION}'
        copy_file2(origen, destino)
        archive_old_mibanco_A169 = FILES2_PATH_CONEXUS + f'mibanco/{file_name}{format_today_mibanco}{TXT_EXTENSION}'
        archive_new_mibanco_A169 = FILES2_PATH_CONEXUS + f'mibanco/{file_name}{format_yesterday_mibanco1}{TXT_EXTENSION}'
    if os.path.exists(archive_old_mibanco_A169) == True:
        os.rename(archive_old_mibanco_A169,archive_new_mibanco_A169)
        #print("Se renombró los archivos integra MiBanco A169 en la ruta " + FILES2_PATH_CONEXUS + f'mibanco/' )

     # Copia de archivos mibanco_integra_D169
    for file_name in mibanco_integra_archive2:
        origen = FILES2_PATH_CONEXUS + f'mibanco/{file_name}{format_today_mibanco}{TXT_EXTENSION}'
        destino = SFTP_PATH_SUICHE + f'mibanco/{file_name}{format_yesterday_mibanco1}{TXT_EXTENSION}'
        copy_file2(origen, destino)
        archive_old_mibanco_D169 = FILES2_PATH_CONEXUS + f'mibanco/{file_name}{format_today_mibanco}{TXT_EXTENSION}'
        archive_new_mibanco_D169 = FILES2_PATH_CONEXUS + f'mibanco/{file_name}{format_yesterday_mibanco1}{TXT_EXTENSION}'
    if os.path.exists(archive_old_mibanco_D169) == True:
        os.rename(archive_old_mibanco_D169,archive_new_mibanco_D169)
        #print("Se renombró los archivos integra MiBanco D169 en la ruta " + FILES2_PATH_CONEXUS + f'mibanco/' )      

if __name__ == '__main__':
    main()
