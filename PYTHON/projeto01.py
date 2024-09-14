from fpdf import FPDF

projeto = input("digite a descriçao do projeto: ")
horas_trabalhadas = input("digite a quantidade de horas prevista: ")
valor_hora = input("valor da hora de trabalho: ")
prazo = input("digite o prazo estimado: ")

valor_total = int(horas_trabalhadas) * int(valor_hora)

pdf = FPDF()

pdf.add_page()
pdf.set_font("Arial")

pdf.image("template.png", x=0, y=0)

pdf.text(115, 145, projeto)
pdf.text(115, 160, horas_trabalhadas)
pdf.text(115, 175, valor_hora)
pdf.text(115, 190, prazo)
pdf.text(115, 205, str(valor_total))

pdf.output("orçamento.pdf")
print("orçamento gerado com sucesso!")