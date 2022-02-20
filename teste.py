import codecs
from selenium import webdriver
import json
import time
import re

class calculadora:
    def divisão(valor_1, valor_2):
        resultado = float(valor_1) / float(valor_2)
        return resultado

def regex(str):
    regex = r"\d+,\d+"
    return list(re.findall(regex, str))

def regex2(str):
    regex2 = r"\w$"
    return re.findall(regex2, str)

def convercao(valor1, valor2):
    if valor2 == "M":
        return float(valor1) * 1000000
    elif valor2 == "B":
        return float(valor1) * 1000000000

navegdor = webdriver.Chrome("C:/Users/gusta/anaconda3/chromedriver.exe")
navegdor.get("https://www.infomoney.com.br/cotacoes/magazine-luiza-mglu3/")
divida_liquida = navegdor.find_element_by_xpath('//*[@id="header-quotes"]/div[2]/div[1]/table[2]/tbody/tr[2]/td[2]').get_attribute('innerText')
patrimonio_liquido = navegdor.find_element_by_xpath('//*[@id="header-quotes"]/div[2]/div[1]/table[2]/tbody/tr[3]/td[2]').get_attribute('innerText')
ebitda = navegdor.find_element_by_xpath('//*[@id="header-quotes"]/div[2]/div[1]/table[1]/tbody/tr[4]/td[2]').get_attribute('innerText')
receita_liquida = navegdor.find_element_by_xpath('//*[@id="header-quotes"]/div[2]/div[1]/table[1]/tbody/tr[1]/td[2]').get_attribute('innerText')

divida_liquida_f = (regex2(divida_liquida))
patrimonio_liquido_f = (regex2(patrimonio_liquido))
ebitda_f = (regex2(ebitda))
receita_liquida_f = (regex2(receita_liquida))

# divida_liquida_f = divida_liquida_f[0]
# patrimonio_liquido_f = patrimonio_liquido_f[0]
# ebitda_f = ebitda_f[0]
# receita_liquida_f = receita_liquida_f[0]

divida_liquida = (regex(divida_liquida))
patrimonio_liquido = (regex(patrimonio_liquido))
ebitda = (regex(ebitda))
receita_liquida = (regex(receita_liquida))

divida_liquida = divida_liquida[0].replace(",", ".")
patrimonio_liquido = patrimonio_liquido[0].replace(",", ".")
ebitda = ebitda[0].replace(",", ".")
receita_liquida = receita_liquida[0].replace(",", ".")

divida_liquida = (convercao(divida_liquida, divida_liquida_f[0]))
patrimonio_liquido = (convercao(patrimonio_liquido, patrimonio_liquido_f[0]))
ebitda = (convercao(ebitda, ebitda_f[0]))
receita_liquida = (convercao(receita_liquida, receita_liquida_f[0]))

divida_liquida_pl = round(calculadora.divisão(divida_liquida, patrimonio_liquido),2)
print("Divida Líquida P/L:", divida_liquida_pl,"%")
margem_ebitda = round(calculadora.divisão(ebitda, receita_liquida),2)
print("Margem Ebitda:", margem_ebitda, "%")

dict_ebitda = {"Margem Ebitida": margem_ebitda, 
               "Divida Liquida P/L": divida_liquida_pl}
               
with open(".\\dados.json", 'wb') as outfile:
    json.dump(dict_ebitda, codecs.getwriter("utf-8")(outfile))