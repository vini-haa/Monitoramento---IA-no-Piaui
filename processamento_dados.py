import pandas as pd
import re # Regex
import html
from coleta_dados import coleta_dados   

palavras_positivas = [
    'avança', 'crescimento', 'melhora', 'investimento', 'oportunidades', 'sucesso',
    'inaugura', 'expansão', 'fortalece', 'inovação', 'solução', 'eficiência',
    'parceria', 'lança', 'desenvolve', 'aumenta', 'positiva',
    'anuncia', 'autoriza', 'apoia', 'beneficia', 'capacitação', 'celebra', 
    'digital', 'destaque', 'economia', 'educação', 'empregos', 'fomento', 
    'futuro', 'garante', 'impulsiona', 'incentiva', 'modernização', 
    'otimização', 'pioneirismo', 'polo', 'potencial', 'promove', 'qualidade', 
    'recorde', 'referência', 'avanço', 'tecnologia', 'transformação'
]
palavras_negativas = [
    'risco', 'ameaça', 'desemprego', 'problema', 'crise', 'alerta', 'dificuldades',
    'queda', 'preocupação', 'impacto negativo', 'falha', 'atraso', 'golpe',
    'perigo', 'ilegal', 'fraude', 'negativa',
    'acusa', 'abandono', 'barreira', 'caos', 'corte', 'crítica', 'corrupção',
    'controvérsia', 'desafio', 'desigualdade', 'dívida', 'engana', 'erro', 
    'escândalo', 'esquecimento', 'falta', 'insegurança', 'investigação', 
    'obstáculo', 'pobreza', 'polêmica', 'precariedade', 'substituição', 
    'vigilância', 'viés'
]

def sentimento(texto):
    score = 0
    texto = texto.lower()

    for palavra in palavras_positivas:
        if palavra in texto:
            score += 1

    for palavra in palavras_negativas:
        if palavra in texto:
            score -= 1

    if score > 0:
        return 'Positivo'  
    elif score < 0:
        return 'Negativo'
    else:
        return 'Neutro'

def sem_html(texto):
    texto = html.unescape(texto)
    return re.sub(r'<.*?>', '', texto)



noticias_brutas = coleta_dados()

if not noticias_brutas:
    print("Nenhuma notícia coletada.")
else:
    print(f"{len(noticias_brutas)} notícias.")
    df = pd.DataFrame(noticias_brutas)
    
    df['descricao'] = df['descricao'].apply(sem_html)
    df['titulo'] = df['titulo'].apply(sem_html)

    df["texto_completo"] = df["titulo"] + " " + df["descricao"]
    df['sentimento'] = df['texto_completo'].apply(sentimento)

    print(df[['titulo', 'descricao', 'sentimento']])
          
