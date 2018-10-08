i = 8;
ref_arquivo_concatenado = open("cot_hist_2008_a_2016.txt","w")

while i <= 16 :
     
    if i <= 9 :
        arq_name = "COTAHIST_A200" + str(i) + ".TXT"
    else :
        arq_name = "COTAHIST_A20" + str(i) + ".TXT"
    ref_arquivo = open(arq_name,"r")
    linha = ref_arquivo.readline()
    while linha :
        ref_arquivo_concatenado.write(linha)
        linha = ref_arquivo.readline()
    ref_arquivo.close()
    i += 1
