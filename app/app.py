from flask import Flask, render_template, request, send_file
import qrcode
from io import BytesIO

app = Flask(__name__)

# Rota para página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Rota para gerar QR Code
@app.route('/gerar_qr_code', methods=['POST'])  # Define uma rota para '/gerar_qr_code' que aceita solicitações POST
def gerar_qr_code():
    dados = request.form['dados']  # Obtém os dados enviados pelo formulário HTML

    # Criação e configuração do objeto QRCode
    qr = qrcode.QRCode(
        # error_correction=qrcode.constants.ERROR_CORRECT_L,  # Define o nível de correção de erros (L = 7% de correção)
        box_size=10,  # Define o tamanho do "box" do QR Code (cada "box" é um pixel)
        border=4,  # Define a largura da borda do QR Code (4 "boxes")
    )
    qr.add_data(dados)  # Adiciona os dados ao objeto QRCode
    qr.make(fit=True)  # Gera o QR Code com base nos dados fornecidos

    # Criação de um buffer de bytes em memória para armazenar a imagem do QR Code
    img_io = BytesIO()
    qr.make_image(fill_color="black", back_color="white").save(img_io)  # Salva a imagem do QR Code no buffer de bytes
    img_io.seek(0)  # Move o cursor de leitura para o início do buffer, para garantir que toda a imagem do QR Code seja enviada corretamente como resposta HTTP.

    # Retorna a imagem do QR Code como resposta HTTP
    return send_file(img_io, mimetype='image/png')  # É a resposta HTTP, sendo uma imagem do QR Code como um arquivo PNG

if __name__ == "__main__":
    app.run(debug=True)