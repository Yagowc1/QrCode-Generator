# Gerador de QR Code

Este é um aplicativo web simples que gera QR Codes a partir de textos fornecidos pelo usuário. Os QR Codes gerados podem ser escaneados para redirecionar os usuários para os links específicos.

![image](https://github.com/Yagowc1/QrCode-Generator/assets/143226127/d33bec9d-4b68-4b97-9ae8-1339755db405)


## Tecnologias Utilizadas

- **Python**: Linguagem de programação utilizada para a lógica do servidor.
- **Flask**: Framework web em Python utilizado para criar o servidor web.
- **qrcode**: Biblioteca Python para a geração de QR Codes.
- **HTML e CSS**: Utilizados para a estruturação e estilização da página web.
- **JavaScript**: Utilizado para interações no lado do cliente.

## Pré-requisitos

- Python 3.x instalado em sua máquina. Você pode baixá-lo [aqui](https://www.python.org/downloads/).

## Como Usar

1. Clone este repositório em sua máquina local:

    ```bash
    git clone https://github.com/yagowc1/QrCode-Generator.git
    ```

2. Instale as dependências Python usando pip:

    ```bash
    pip install Flask qrcode
    ```

3. Navegue até o diretório do projeto:

    ```bash
    cd app
    ```

4. Execute o aplicativo:

    ```bash
    python app.py
    ```

5. Abra um navegador da web e visite `http://127.0.0.1:5000/` para acessar o aplicativo.

6. No formulário apresentado, digite o texto desejado para o QR Code e pressione o botão "Gerar QR Code".

7. O QR Code gerado será exibido na página. Você pode escaneá-lo com um aplicativo de leitura de QR Code em seu dispositivo móvel para acessar o texto fornecido.

## Contribuindo

Contribuições são bem-vindas! Se você tiver sugestões de melhorias, novos recursos ou encontrar algum problema, por favor, abra uma issue ou envie um pull request.
