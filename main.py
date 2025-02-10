import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time

# Configuração do WebDriver
url = "https://www.uece.br/uece/noticias/"
driver = webdriver.Firefox()
driver.get(url)
driver.implicitly_wait(5)  # Aguarda carregamento inicial

# Lista para armazenar notícias
all_titles = []
all_descriptions = []

# Tentar extrair todas as notícias disponíveis
for _ in range(10):  # Tentamos 10 vezes para garantir que pegamos tudo
    # Capturar os posts da página
    posts = driver.find_element(By.CLASS_NAME, "cc-posts")
    posts_html = posts.get_attribute('innerHTML')

    # Analisar com BeautifulSoup
    soup = BeautifulSoup(posts_html, 'html.parser')
    posts_title = soup.find_all("h3")
    posts_description = soup.find_all(class_="cc-post-excerpt")

    # Adicionar novos itens sem duplicação
    for title, desc in zip(posts_title, posts_description):
        title_text = title.text.strip()
        desc_text = desc.text.strip()
        if title_text not in all_titles:
            all_titles.append(title_text)
            all_descriptions.append(desc_text)

        if len(all_titles) >= 50:
            break

    # Se não encontrou notícias suficientes, imprime HTML para debug
    if len(all_titles) < 10:
        print("Menos de 10 notícias encontradas. Exibindo HTML para depuração:")
        print(driver.page_source[:2000])  # Mostra os primeiros 2000 caracteres da página

    # Clicar no botão "Veja Mais" se existir
    try:
        see_more_button = driver.find_element(By.CLASS_NAME, "cc-button")  # Correção do seletor
        if see_more_button.is_displayed():
            driver.execute_script("arguments[0].click();", see_more_button)
            print("Botão 'Veja Mais' clicado.")
            time.sleep(5)  # Tempo extra para carregar novas notícias
        else:
            print("Botão 'Veja Mais' não encontrado ou visível.")
            break
    except:
        print("Não há mais notícias disponíveis.")
        break

# Criar DataFrame e salvar em JSON
df = pd.DataFrame({"Title": all_titles[:50], "Description": all_descriptions[:50]})
df.to_json('results.json', orient="records", force_ascii=False, indent=4)

print(f'Success! {len(df)} notícias extraídas e salvas em "results.json".')
driver.quit()