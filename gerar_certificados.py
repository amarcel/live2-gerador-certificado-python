import pdfkit
import csv

# pdfkit.from_url('http://unama.br', 'out.pdf')
opcoes = {
    'page-size': 'A4',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
    'encoding': "UTF-8",
    'orientation': 'landscape'
}

with open('/home/marcel/Documentos/PROJETOS/PYTHON/GerarCertificados/lista_freq_01042020_CSV.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    for row in csv_reader:
        pdfkit.from_string(
            '<!DOCTYPE html><html lang="en"><head> <meta charset="UTF-8"> <meta name="viewport" content="width=device-width, initial-scale=1.0"> <title>Document</title> <style> body { text-align: center; font-family: Arial, Helvetica, sans-serif; } .assinatura { font-size: 10pt; } .descricao { font-size: 18pt; } .certificado { border-style: double; } h1 { font-size: 36pt; } </style></head><body> <div class="certificado"> <br/> <img src="/home/marcel/Documentos/PROJETOS/PYTHON/GerarCertificados/logo_unama.png" alt="Logo Unama" width="300" height="110" /> <br/> <h1>Certificado</h1> <br/> <p class="descricao">Certificamos que NOME_PESSOA participou da palestra "Desvendendo os Poderes da Linguagem de Programação Python" no dia 08/04/2020. A carga horária dessa atividade é de 4h. </p> <br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/> <img src="/home/marcel/Documentos/PROJETOS/PYTHON/GerarCertificados/assinatura.jpg" alt="Assinatura" width="180" height="60" /> <p class="assinatura">Coordenador dos Cursos de Computação</p> <br/><br/> </div></body></html>'.replace("NOME_PESSOA", row[1]), 
            '/home/marcel/Documentos/PROJETOS/PYTHON/GerarCertificados/certificados/certificado_'+str(line_count)+'.pdf',
            options=opcoes)
        print(row[1])
        line_count += 1
    print(f'Processed {line_count} lines.')
