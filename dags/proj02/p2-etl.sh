#!/bin/bash
# A linha acima é o shebang, que indica que este script deve ser executado em um shell bash.

# Imprime a string "etl" no terminal.
echo "etl"

# Usa o comando cut para extrair as colunas 1 e 4 do arquivo p2-entrada.txt localizado em /opt/airflow/dags, 
# delimitadas por '#', e redireciona a saída para p2-saida.txt no mesmo diretório.
cut -f1,4 -d"#" /opt/airflow/dags/proj02/p2-entrada.txt > /opt/airflow/dags/proj02/p2-saida.txt

# Utiliza o comando tr para converter todas as letras minúsculas em maiúsculas 
# do conteúdo de p2-saida.txt e redireciona a saída para p2-saida-capitalized.txt no mesmo diretório.
tr "[a-z]" "[A-Z]" < /opt/airflow/dags/proj02/p2-saida.txt > /opt/airflow/dags/proj02/p2-saida-capitalized.txt
# Empacota e comprime o arquivo p2-saida-capitalized.txt em um arquivo tar.gz chamado p2-log.tar.gz,
# armazenando no diretório /opt/airflow/dags.
tar -czvf /opt/airflow/dags/proj02/p2-log.tar.gz /opt/airflow/dags/proj02/p2-saida-capitalized.txt
