import os
import requests
import json
from dotenv import load_dotenv

# Carrega as variáveis de ambiente
load_dotenv()

def setup_netlify():
    """Configura o deploy no Netlify"""
    netlify_token = os.getenv('NETLIFY_TOKEN')
    if not netlify_token:
        print("Token do Netlify não encontrado. Configure a variável NETLIFY_TOKEN no arquivo .env")
        return

    headers = {
        'Authorization': f'Bearer {netlify_token}',
        'Content-Type': 'application/json'
    }

    # Cria um novo site
    site_data = {
        'name': 'investor-aix-docs',
        'repo': {
            'provider': 'github',
            'repo': 'InvestorAix/InvestorAix.github.io',
            'branch': 'main'
        }
    }

    try:
        response = requests.post(
            'https://api.netlify.com/api/v1/sites',
            headers=headers,
            json=site_data
        )
        response.raise_for_status()
        print("Site criado com sucesso no Netlify!")
        print(f"URL: {response.json()['url']}")
    except Exception as e:
        print(f"Erro ao criar site no Netlify: {str(e)}")

def setup_render():
    """Configura o deploy no Render"""
    render_token = os.getenv('RENDER_TOKEN')
    if not render_token:
        print("Token do Render não encontrado. Configure a variável RENDER_TOKEN no arquivo .env")
        return

    headers = {
        'Authorization': f'Bearer {render_token}',
        'Content-Type': 'application/json'
    }

    # Cria um novo serviço
    service_data = {
        'name': 'investor-aix-docs',
        'type': 'web',
        'env': 'static',
        'repo': 'https://github.com/InvestorAix/InvestorAix.github.io',
        'branch': 'main'
    }

    try:
        response = requests.post(
            'https://api.render.com/v1/services',
            headers=headers,
            json=service_data
        )
        response.raise_for_status()
        print("Serviço criado com sucesso no Render!")
        print(f"URL: {response.json()['url']}")
    except Exception as e:
        print(f"Erro ao criar serviço no Render: {str(e)}")

if __name__ == "__main__":
    setup_netlify()
    setup_render() 