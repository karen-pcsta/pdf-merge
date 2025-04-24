
# PDF Merger - Unificador de PDFs

Uma aplicação desktop simples e intuitiva para unir múltiplos arquivos PDF em um único documento.

## Sobre o Projeto

O PDF Merger é uma ferramenta de desktop desenvolvida em Python com PySide6 que permite aos usuários:

- Selecionar múltiplos arquivos PDF
- Organizar a ordem dos documentos por arrastar e soltar
- Unir os PDFs em um único arquivo
- Visualizar automaticamente o arquivo resultante

## Funcionalidades

- **Interface gráfica amigável**: Design simples e funcional
- **Seleção múltipla**: Adicione vários PDFs de uma só vez
- **Reordenação por drag-and-drop**: Organize os documentos na ordem desejada
- **Remoção seletiva**: Exclua arquivos da lista facilmente
- **Visualização automática**: Abre o PDF criado assim que o processo é concluído

## Como Instalar

1. Clone o repositório:
   ```
   git clone https://github.com/seu-usuario/pdf-merge.git
   cd pdf-merge
   ```

2. Instale as dependências necessárias:
   ```
   pip install PySide6 pypdf
   ```

3. Execute o programa:
   ```
   python main.py
   ```

## Dependências

- PySide6: Para a interface gráfica
- PyPDF (pypdf): Para manipulação de PDFs

## Como Usar

1. Clique em "Adicionar PDFs" para selecionar os arquivos que deseja unir
2. Organize os arquivos na ordem desejada arrastando-os na lista
3. Selecione um item e clique em "Remover" caso queira excluí-lo da lista
4. Clique em "Unir PDFs" quando estiver satisfeito com a seleção e ordem
5. Escolha o local e nome do arquivo resultante
6. O PDF unificado será criado e aberto automaticamente

## 🔧 Compilando o Executável

Para criar um executável, você pode usar o PyInstaller:

```
pip install pyinstaller
pyinstaller --onefile --windowed main.py
```

O executável estará disponível na pasta `dist`.
