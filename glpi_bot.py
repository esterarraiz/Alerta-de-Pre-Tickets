from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time

class GLPIBot:
    def __init__(self, usuario, senha, url="URL_DO_GLPI"):
        self.usuario = usuario
        self.senha = senha
        self.url = url
        self.driver = webdriver.Firefox()

    def login(self):
        self.driver.get(self.url)
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="login_name"]')))
        self.driver.find_element(By.XPATH, '//*[@id="login_name"]').send_keys(self.usuario)
        self.driver.find_element(By.XPATH, '//*[@id="login_password"]').send_keys(self.senha)

        login_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, "submit")))
        login_button.click()

        WebDriverWait(self.driver, 20).until(
            lambda driver: driver.execute_script("return document.readyState") == "complete"
        )

    def extrair_chamados(self):
        self.driver.get(self.url + "Caminho para o filtro de pré-tickets")

        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "search-results")))

        chamados = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.XPATH, '//table[contains(@class, "search-results")]//tbody/tr'))
        )

        lista_chamados = []

        if not chamados:
            print("Nenhum chamado encontrado.")
            return 0  

        for chamado in chamados:
            try:
                numero = chamado.find_element(By.XPATH, './td[2]/span').text.strip().replace(" ", "")
                if numero.isdigit():
                    lista_chamados.append(numero)
            except NoSuchElementException:
                continue 

        if not lista_chamados:
            print("Nenhum número de chamado válido encontrado.")
        else:
            print(f"Total de chamados encontrados: {len(lista_chamados)}")

        self.driver.quit()

        return len(lista_chamados)

