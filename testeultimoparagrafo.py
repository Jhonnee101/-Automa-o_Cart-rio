import docx

# Carregar o documento existente
doc = docx.Document('./doc.docx.')

# Obter o último parágrafo
ultimo_paragrafo = doc.paragraphs[-17]

# Exibir o texto do último parágrafo
print(ultimo_paragrafo.text)
