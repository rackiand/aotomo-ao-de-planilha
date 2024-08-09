# Inserir cada célula de cada linha em um campo do sistema
import openpyxl
import pyautogui

workbook = openpyxl.load_workbook('vendas_de_produtos.xlsx')
vendas_sheet = workbook['vendas']

for linha in vendas_sheet.iter_rows(min_row=2):
    # nome
    pyautogui.click(1808,452,duration=1.5)
    pyautogui.write(linha[0].value)
    # produto
    pyautogui.click(1815,476,duration=1.5)
    pyautogui.write(linha[1].value)
    # quantidade
    pyautogui.click(1813,497,duration=1.5)
    pyautogui.write(str(linha[2].value))
    # categoria
    pyautogui.click(1883,532,duration=1.5)
    pyautogui.write(linha[3].value)
    pyautogui.click(1752,549,duration=1.5)
    pyautogui.click(1256,581,duration=1.5)
    
    