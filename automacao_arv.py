import os
import shutil

desktop = os.path.join(os.path.expanduser("~"), "OneDrive\Área de Trabalho")
pasta_arquivos = os.path.join(desktop, "Arquivos")
os.makedirs(pasta_arquivos, exist_ok=True)
arquivos_exemplo = ["relatorio.txt", "tarefas.txt", "planilha.txt", "notas.txt", "dados.txt"]

for arquivo in arquivos_exemplo:
    caminho_arquivo = os.path.join(pasta_arquivos, arquivo)
    with open(caminho_arquivo, "w", encoding='utf-8') as f:
        f.write(f"Conteúdo do arquivo {arquivo}\n")
    print(f"Criado: {arquivo}")
print(f"\nArquivos criados na pasta: {pasta_arquivos}")

print("\n--- Setup Concluído! ---")

print("-"*50)

print("--- Iniciando Projeto de Automação ---")
try:
    desktop = os.path.join(os.path.expanduser("~"), "OneDrive", "Área de Trabalho")
    pasta_original = os.path.join(desktop, "Arquivos")
    pasta_copia = os.path.join(desktop, "arquivos_renomeados")

    
    
    print(f"Verificando se a pasta '{pasta_original}' existe...")
    if not os.path.exists(pasta_original):
        print(f"\nERRO: A pasta original não foi encontrada em:")
        print(pasta_original)
        print("Por favor, rode o script 'setup_arquivos.py' primeiro.")
        exit() 
    
    print("   -> Pasta original encontrada!")

    print(f"Criando cópia de segurança em '{pasta_copia}'...")
    if os.path.exists(pasta_copia):
        print(f"   -> A pasta de cópia antiga já existe. Removendo...")
        shutil.rmtree(pasta_copia)
        print(f"   -> Pasta antiga removida.")
    shutil.copytree(pasta_original, pasta_copia)
    print(f"Cópia criada com sucesso em: {pasta_copia}")

    print("\nIniciando renomeação dos arquivos na pasta cópia...")
    
    lista_de_arquivos = os.listdir(pasta_copia)
    
    contador = 1
    total_arquivos = 0

    for nome_arquivo_antigo in lista_de_arquivos:
        caminho_antigo_completo = os.path.join(pasta_copia, nome_arquivo_antigo)
        
        if os.path.isfile(caminho_antigo_completo):
            nome_base, extensao = os.path.splitext(nome_arquivo_antigo)
            
            novo_nome = f"documento_{contador:02d}{extensao}"
            caminho_novo_completo = os.path.join(pasta_copia, novo_nome)
            os.rename(caminho_antigo_completo, caminho_novo_completo)
            
            print(f"Renomeado: {nome_arquivo_antigo} -> {novo_nome}")
            
            contador += 1
            total_arquivos += 1

    print("\n--- Processo Concluído! ---")
    print(f"Pasta original (intacta): {pasta_original}")
    print(f"Pasta com arquivos renomeados: {pasta_copia}")
    print(f"Total de arquivos processados: {total_arquivos}")

except Exception as e:
    print(f"\n--- !!! OCORREU UM ERRO INESPERADO !!! ---")
    print(f"Detalhes: {e}")
    print("O script foi interrompido.")