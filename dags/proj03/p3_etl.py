#!/usr/bin/env python
#!/usr/bin/env python
# coding: utf-8

# Importando bibliotecas necessárias
import os
import sqlite3
import requests
import datetime
import pandas as pd

# Definição da função para extrair dados da API
def extrai_dados_api():

    # Obtendo a data e hora atual
    hoje = datetime.datetime.now()
    
    # Fazendo uma solicitação GET para a API do tempo (coloque aqui sua chave da API)
    dados_api = requests.get("http://api.weatherapi.com/v1/current.json?key=5cd2efcafe404423a6e204917252111&q=Cataguases&aqi=yes")
    
    # Convertendo a resposta da API em JSON
    dados = dados_api.json()

    # Criando um dicionário a partir dos dados JSON
    dicionario_dados = {
        "temperature": [dados["current"]["temp_c"]],
        "wind_speed": [dados["current"]["wind_kph"]],
        "condition": [dados["current"]["condition"]["text"]],
        "precipitation": [dados["current"]["precip_mm"]],
        "humidity": [dados["current"]["humidity"]],
        "feels_like_temp": [dados["current"]["feelslike_c"]],
        "pressure": [dados["current"]["pressure_mb"]],
        "visibility": [dados["current"]["vis_km"]],
        "is_day": [dados["current"]["is_day"]],
        "timestamp": [hoje]
    }

    # Convertendo o dicionário em um DataFrame do Pandas
    return pd.DataFrame(dicionario_dados)

# Definição da função para verificar a qualidade dos dados
def data_quality(df_dados):
    
    # Verifica se o DataFrame está vazio
    if df_dados.empty:
        print("Os dados não foram extraídos")
        return False
    
    # Verifica se há valores nulos no DataFrame
    if df_dados.isnull().values.any():
        print("Valores ausentes detectados. Tratamento dos dados será necessário.")

# Definição da função para transformar os dados
def transforma_dados(df_dados):
    
    # Convertendo a coluna 'is_day' para tipo booleano
    df_dados["is_day"] = df_dados["is_day"].astype(bool)
    
    # Criando uma nova coluna 'ID' combinando 'timestamp' e 'temperature'
    df_dados["ID"] = df_dados['timestamp'].astype(str) + "-" + df_dados["temperature"].astype(str)
    
    return df_dados

# Definição da função para realizar a extração e transformação dos dados
def extrai_transforma():
    
    # Chamando a função de extração de dados da API
    df_dados = extrai_dados_api()
    
    # Chamando a função de transformação dos dados
    df_dados = transforma_dados(df_dados)

    # Chamando a função de verificação da qualidade dos dados
    data_quality(df_dados)
    
    return df_dados

# Definição da função principal para realizar o processo ETL
def processo_etl():
    
    # Chamando a função de extração e transformação dos dados
    df = extrai_transforma()
    
    # Definindo o caminho do arquivo CSV
    file_path = "/opt/airflow/dags/proj03/projeto3_dados.csv"
    
    # Verifica se o arquivo CSV já existe para decidir se inclui o cabeçalho
    header = not os.path.isfile(file_path)
    
    # Salvando o DataFrame no arquivo CSV no modo append
    df.to_csv(file_path, mode='a', index=False, header=header)

    # Conectando ao banco de dados SQLite (isso criará o arquivo de banco de dados se ele não existir)
    conn = sqlite3.connect('/opt/airflow/dags/proj03/projeto3_database.db')

    # Salvando o DataFrame no banco de dados SQLite
    df.to_sql('projeto3_tabela', conn, if_exists='append', index=False)

    # Fechando a conexão com o banco de dados
    conn.close()


