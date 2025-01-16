import pandas as pd
import os #sistema operacional usar o pythom
import glob  
#  implementar log
#função de extração

pasta = 'data'

def extrair_dados(pasta:str) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(pasta,'*.json'))
    #navega nas pastas do path, dá join em tudo que é json
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
     #criando lista de dataframes

    df_total = pd.concat(df_list,ignore_index= True)

    return df_total




# função de transformação

def calcular_kpi_de_total_de_vendas (df: pd.DataFrame) -> pd.DataFrame:
    df["Total"] =      df["Quantidade"]   * df["Venda"]
    return df

# função de carregamento em csv ou parquet  : sem saída
def carregar_dados(df: pd.DataFrame, format_saida:list): 

    for item in format_saida:
        if item  == "csv":
         df.to_csv("dados.csv")
        if item  == "parquet":
         df.to_parquet("dados.parquet")
        

def pipeline_calcular_kpi_de_vendas_consolidado(pasta:str, formato_de_saida: list):
    data_frame = (extrair_dados(pasta = pasta))
    data_frame_transformado =  (calcular_kpi_de_total_de_vendas(data_frame))
    carregar_dados(data_frame_transformado, formato_de_saida)





                   ## quando trabalha com parquet, poetry add fastparquet ou pyarrow
                   # poetry run python elt.py