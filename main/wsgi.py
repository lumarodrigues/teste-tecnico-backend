"""
WSGI config for main project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from django.core.management import call_command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')

application = get_wsgi_application()

if os.getenv("RUN_MIGRATIONS", "false").lower() == "true":
    try:
        print("Executando migrações...")
        call_command("migrate")
        print("Migrações concluídas.")
        
        print("Executando o comando create_company...")
        call_command("create_company")
        print("Comando create_company concluído.")
    except Exception as e:
        print(f"Erro ao rodar migrações ou create_company: {e}")
