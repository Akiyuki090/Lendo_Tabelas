import tabula


df = tabula.read_pdf("arquivo.pdf", pages="all")
display(df)
tabula.convert_into("arquivo.pdf", "arquivo.csv", output_format = "csv", pages = "all")[0]
