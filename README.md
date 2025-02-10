Web Scraper de Notícias da UECE

Este projeto é um Web Scraper desenvolvido em Python que extrai notícias do portal da UECE.
O código utiliza Selenium e BeautifulSoup para automatizar a coleta de notícias e salvar os dados em um arquivo JSON.

📌 Objetivo

O script acessa a página de notícias da UECE, extrai os títulos e descrições, e clica no botão "Veja Mais" até coletar 50 notícias ou até que não haja mais notícias disponíveis.

🚀 Tecnologias Utilizadas

Python 3.x

Selenium (para automação do navegador)

BeautifulSoup (para parsing do HTML)

Pandas (para manipulação e exportação dos dados)

Geckodriver (para controle do Firefox via Selenium)

📂 Instalação

Antes de rodar o script, certifique-se de instalar as dependências necessárias. Execute:

pip install selenium beautifulsoup4 pandas

Além disso, o Firefox e o Geckodriver devem estar instalados no seu sistema.

▶️ Como Executar

Clone este repositório:

git clone https://github.com/italofre/Web_Scraping.git
cd Web_Scraping

Execute o script principal:

python main.py

Após a execução bem-sucedida, um arquivo results.json será gerado com os dados extraídos.

📑 Saída dos Dados

O script salva os dados coletados no arquivo results.json no seguinte formato:

[
    {
        "Title": "Título da Notícia 1",
        "Description": "Descrição da Notícia 1"
    },
    {
        "Title": "Título da Notícia 2",
        "Description": "Descrição da Notícia 2"
    }
]

🛠 Possíveis Problemas e Soluções

Erro: ModuleNotFoundError: No module named 'selenium'👉 Execute pip install selenium para instalar a biblioteca.

O script para com menos de 50 notícias👉 O site pode ter um número limitado de notícias. Verifique a saída do terminal para depuração.

O botão "Veja Mais" não funciona👉 O site pode ter alterado a estrutura. Inspecione o HTML e ajuste os seletores no código.

🤝 Contribuição

Sinta-se à vontade para contribuir com melhorias! Faça um fork do repositório, crie uma branch e envie um pull request. 😊

📝 Licença
Este projeto é de uso acadêmico e não possui licença específica.