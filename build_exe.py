#!/usr/bin/env python3
"""
Script para compilar o jogo em um executável standalone (.exe)
Requer PyInstaller instalado: pip install pyinstaller
"""

import PyInstaller.__main__
import os
import sys

# Diretório do script
script_dir = os.path.dirname(os.path.abspath(__file__))
main_file = os.path.join(script_dir, 'main.py')

# Configuração do PyInstaller
args = [
    main_file,
    '--onefile',  # Gera um único arquivo .exe
    '--windowed',  # Remove a janela de console
    '--icon=NONE',  # Sem ícone customizado (opcional)
    '--name=JogoProjetoGrego',  # Nome do executável
    '--distpath=dist',  # Pasta de saída
    '--buildpath=build',  # Pasta temporária de build
]

print("🔨 Compilando o jogo em executável...")
print(f"Processando: {main_file}")

try:
    PyInstaller.__main__.run(args)
    print("\n✅ Sucesso! Executável gerado em: dist/JogoProjetoGrego.exe")
    print("\n📌 Você pode compartilhar o arquivo 'JogoProjetoGrego.exe' com outras pessoas.")
    print("   Elas podem executá-lo sem ter Python instalado!")
except Exception as e:
    print(f"\n❌ Erro ao compilar: {e}")
    sys.exit(1)
