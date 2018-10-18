# -*- coding: utf-8 -*-

def concatenaArq(init_year, end_year):
    arq_name_concat = "cot_hist_" + init_year + "_a_" + end_year + ".txt"
    ref_arquivo_concatenado = open(arq_name_concat,"w")

    count = int(init_year)

    load = "."

    while count <= int(end_year) :
        load += "."
        print load

        arq_name = "DadosBrutosporAno/COTAHIST_A" + str(count) + ".TXT"

        ref_arquivo = open(arq_name,"r")
        for linha in ref_arquivo:
            ref_arquivo_concatenado.write(linha)
        ref_arquivo.close()
        count += 1
    ref_arquivo_concatenado.close()
    return arq_name_concat
