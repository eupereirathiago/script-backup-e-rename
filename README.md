# 📂 Automação de Renomeação de Arquivos

Este é um script de automação em Python projetado para organizar arquivos de forma segura. Ele localiza uma pasta específica, cria um backup completo dela e, em seguida, renomeia todos os arquivos na cópia de backup para um formato sequencial e padronizado.

O script é dividido em duas partes principais:

1.  **Setup:** Cria uma pasta e arquivos de exemplo para teste.
2.  **Automação:** Executa o processo de backup e renomeação.

-----

## 🚀 Funcionalidades Principais

  * **Setup de Teste:** Cria automaticamente uma pasta `Arquivos` e cinco arquivos `.txt` de exemplo na sua Área de Trabalho (OneDrive) para que o script tenha o que processar.
  * **Backup Seguro:** Antes de qualquer modificação, o script cria uma cópia exata da pasta original (`Arquivos`) para uma nova pasta (`arquivos_renomeados`).
  * **Renomeação em Lote:** Percorre todos os arquivos na pasta de *cópia* e os renomeia seguindo um padrão sequencial (ex: `documento_01.txt`, `documento_02.txt`), mantendo a extensão original.
  * **Preservação de Originais:** A pasta `Arquivos` original permanece 100% intacta, garantindo a segurança dos seus dados.
  * **Limpeza Automática:** Se uma pasta `arquivos_renomeados` de uma execução anterior já existir, ela é removida e recriada para garantir um processo limpo.

-----

## 📋 Requisitos

  * Python 3.x
  * Nenhuma biblioteca externa é necessária. O script utiliza apenas os módulos padrão `os` e `shutil`.

-----

## ▶️ Como Usar

1.  Salve o código em um único arquivo (ex: `automacao.py`).
2.  Abra seu terminal ou prompt de comando.
3.  Navegue até o diretório onde você salvou o arquivo.
4.  Execute o script:
    ```bash
    python automacao.py
    ```
5.  O script cuidará do setup (criação dos arquivos de teste) e da automação (cópia e renomeação) em uma única execução.

-----

## ⚙️ O Fluxo da Automação

Ao ser executado, o script segue estes passos:

1.  **Setup:** Cria a pasta `.../OneDrive/Área de Trabalho/Arquivos`.
2.  **População:** Preenche a pasta `Arquivos` com 5 arquivos de exemplo (`relatorio.txt`, `tarefas.txt`, etc.).
3.  **Verificação:** Confirma se a pasta `Arquivos` existe (o que ela fará, graças ao setup).
4.  **Backup:** Copia toda a estrutura de `ArquIVOS` para uma nova pasta chamada `.../OneDrive/Área de Trabalho/arquivos_renomeados`.
5.  **Renomeação:**
      * Lista os arquivos da pasta `arquivos_renomeados` (em ordem alfabética).
      * Renomeia cada arquivo para `documento_XX.extensao` (ex: `documento_01.txt`, `documento_02.txt`).
6.  **Conclusão:** Imprime um resumo do processo, mostrando o total de arquivos processados e os caminhos das pastas.

-----

## 📁 Estrutura de Pastas (Resultado)

Após a execução do script, sua Área de Trabalho ficará assim:

```
[Sua Área de Trabalho - OneDrive]
|
+-- Arquivos/               (Pasta original, criada pelo setup e INTACTA)
|   |-- dados.txt
|   |-- notas.txt
|   |-- planilha.txt
|   |-- relatorio.txt
|   |-- tarefas.txt
|
+-- arquivos_renomeados/    (Pasta de cópia, com arquivos processados)
    |-- documento_01.txt    (antigo dados.txt)
    |-- documento_02.txt    (antigo notas.txt)
    |-- documento_03.txt    (antigo planilha.txt)
    |-- documento_04.txt    (antigo relatorio.txt)
    |-- documento_05.txt    (antigo tarefas.txt)
```
