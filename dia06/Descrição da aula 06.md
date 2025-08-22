# Aula 06 — Automação com PyAutoGUI: Criando e Salvando Arquivos

Nesta aula, aprendemos a utilizar a biblioteca `pyautogui` para simular ações no computador como:

📝 Abrir o Bloco de Notas  
⌨️ Escrever um texto personalizado  
💾 Salvar o conteúdo automaticamente

## 📌 O que o programa faz:

1. Pede ao usuário o nome do arquivo e a mensagem.
2. Abre o Bloco de Notas automaticamente.
3. Digita a mensagem.
4. Salva o arquivo no diretório indicado.

## 🧠 Conceitos abordados:

- Uso de `input()` para personalizar o nome e conteúdo do arquivo
- Automatização com `pyautogui.press`, `pyautogui.write`, `pyautogui.hotkey`
- Uso de `time.sleep()` para dar tempo entre as etapas
- Introdução à automação de tarefas com Python

## ⚠️ Observação:
> Este código **não funciona no Google Colab**, pois exige acesso direto ao sistema operacional. Recomendamos executar em um ambiente local como o **VS Code** com Python instalado.

---

## ✅ Exemplo de uso:
```bash
Digite o nome do arquivo (sem .txt): anotações
Digite a mensagem que será escrita no Bloco de Notas: lembrete de estudar python
