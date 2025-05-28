#nome: bot_prenotami.py
# Descrição: Este script carrega as variáveis de ambiente necessárias para o bot Prenotami.
# Autor: Vito Buzzella

import os
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

# Pega as variáveis de ambiente
PRENOTAMI_URL = os.getenv("https://prenotami.esteri.it/")  # URL do serviço Prenotami
PRENOTAMI_USERNAME = os.getenv("victorcontroller8@gmail.com") # Nome de usuário do Prenotami
PRENOTAMI_PASSWORD = os.getenv("Vic@5466") # Senha do Prenotami

# Verifica se as variáveis foram carregadas
if not all([PRENOTAMI_URL, PRENOTAMI_USERNAME, PRENOTAMI_PASSWORD]):
    print("Erro: Verifique se as variáveis PRENOTAMI_URL, PRENOTAMI_USERNAME e PRENOTAMI_PASSWORD estão definidas no seu arquivo .env")
    exit()