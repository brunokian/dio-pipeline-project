import pandas as pd

df = pd.read_csv('clientList.csv')

# Exibir as primeiras linhas do DataFrame

def add_publicity(capacidade_de_pagamento):
    if capacidade_de_pagamento == 'alta':
        return 'Oferta especial para você!'
    elif capacidade_de_pagamento == 'media':
        return 'Receba um desconto exclusivo!'
    elif capacidade_de_pagamento == 'baixa':
        return 'Economize ainda mais!'
    else:
        return 'Desconto incrível para todos!'

# Aplicar a função para criar o campo "propaganda"
df['publicidade'] = df['capacidade_de_pagamento'].apply(add_publicity)

print(df)
df.to_csv('clientList_with_publicity.csv', index=False)
df.to_json('clientList_with_publicity.json', orient='records')






