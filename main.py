import re

# Abrir o arquivo SQL em modo leitura
# O encoding pode variar de acordo com o arquivo
with open('DIRETÓRIO-ARQUIV-ATUAL', 'r', encoding='iso-8859-1') as f:
    sql = f.read()

    # Expressão regular para encontrar datas no formato m/d/yyyy ou mm/dd/yyyy
    pattern = r"'(\d{1,2})/(\d{1,2})/(\d{4})'"

    # Substituir as datas no arquivo SQL pelo formato ano-mes-dia
    sql = re.sub(pattern, lambda match: f"'{match.group(3)}-{match.group(1).zfill(2)}-{match.group(2).zfill(2)}'", sql)

# Abrir o novo arquivo SQL em modo escrita
with open('DIRETÓRIO-NOVO-ARQUIVO', 'w', encoding='utf-8') as f:
    # Escrever o SQL atualizado no arquivo novo.sql
    f.write(sql)
