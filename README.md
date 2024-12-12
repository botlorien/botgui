# BotGUI

BotGUI é uma aplicação Python que implementa uma interface gráfica de usuário (GUI) utilizando `customtkinter`. Este projeto fornece uma interface simples e intuitiva para interagir com um bot por meio de botões, exibindo mensagens e permitindo entradas do usuário.

## Funcionalidades

- Exibição de mensagens do bot na interface gráfica.
- Recebimento de entradas do usuário através de um campo de texto.
- Atualização dinâmica da interface com novas mensagens.

## Requisitos

- Python 3.10 ou superior.

## Instalação

1. Criando o ambiente virtual
```bash
python -m venv venv
.\venv\Scripts\activate
```
1. Instalando o pacote
```bash
pip install botgui
```

## Exemplo de Uso

```python
from botgui.interface import ui
"""
ou 
from botgui.interface import Interface
ui = Interface()
"""

if __name__ == "__main__":
    # Função task de exemplo
    def task1():
        print('Exemplo quando a tarefa executa normalmente!')

    def task2():
        print('Executando task2...')
        raise ValueError('Exemplo quando a tarefa dá erro!')

    def task3(callback):
        print("Chamando galeria de imagens!")
        list_name_img_buttons = ['Avançar', 'Voltar', 'Sair']
        list_func_img_buttons = [ui.next_img, ui.back_img, callback]
        ui.ui_show_imgs(
            'imgs',
            r'venv\Lib\site-packages\botgui\assets',
            list_name_img_buttons,
            list_func_img_buttons,
            width=None,
            height=None
        )

    def gui():
        buttons_name = ['task1', 'task2', 'task3']
        buttons_func = [
            task1,
            task2,
            lambda:task3(gui)
        ]
        ui.ui(buttons_name, buttons_func)
        ui.ui(buttons_name, buttons_func)

    op: str = input("Escolha uma das opções abaixo: \n[1] -> Interface Task Buttons \n[2] -> Interface Show Images \n").strip()

    match op:
        case '1':
            gui()
        case '2':
            task3(gui)
        case _:
            raise ValueError(
                "Opção invalida! Digite o numero 1 ou 2."
            )

```

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo [Licença MIT](LICENSE) para mais detalhes.

## Contribuições

Contribuições são bem-vindas! Caso tenha sugestões, melhorias ou correções, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Contato

Para dúvidas ou suporte, entre em contato com o mantenedor através do [repositório no GitHub](https://github.com/botlorien/botgui).
