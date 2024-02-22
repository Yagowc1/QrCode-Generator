// Adiciona um ouvinte de evento para o envio do formulário
document.querySelector('form').addEventListener('submit', async function (event) {
    // Evita o comportamento padrão do envio do formulário (recarregar a página)
    event.preventDefault();

    // Obtém os dados do formulário
    const formData = new FormData(this);

    // Itera sobre os dados do formulário e os exibe no console
    // for (const pair of formData.entries()) {
    //     console.log(pair[0], pair[1]);
    // }

    // Envia uma solicitação HTTP POST para a rota '/gerar_qr_code' no servidor
    const response = await fetch('/gerar_qr_code', {
        method: 'POST',  // Define o método como POST
        body: formData   // Define o corpo da requisição como os dados do formulário
    });

    // Extrai o conteúdo da resposta como um objeto blob
    const blob = await response.blob();

    // Exibe a imagem do QR Code na página HTML
    document.getElementById('qr_code').innerHTML = `<img src="${URL.createObjectURL(blob)}" alt="QR Code">`;
});