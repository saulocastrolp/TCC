# -*- coding: utf-8 -*-

ref_arquivo = open("COTAHIST_A2018.TXT","r")
ref_arquivo_arrf = open("cot_hist_2018-sem conversão de valores.csv","w")

# ref_arquivo = open("cot_hist_2008_a_2018","r")
# ref_arquivo_arrf = open("cot_hist_2008_a_2018.arff","w")

#ref_arquivo_arrf.write("@relation historico_cot_diario\n\n")

ref_arquivo_arrf.write("data_pregao;")
ref_arquivo_arrf.write("cod_bdi;")
ref_arquivo_arrf.write("cod_negociacao;")
ref_arquivo_arrf.write("tipo_mercado;")
ref_arquivo_arrf.write("nome_papel;")
ref_arquivo_arrf.write("especificacao_papel;")
ref_arquivo_arrf.write("prazo_dias_mercado;")
#ref_arquivo_arrf.write("moeda_ref;")
ref_arquivo_arrf.write("preco_abertura;")
ref_arquivo_arrf.write("preco_maximo;")
ref_arquivo_arrf.write("preco_minimo;")
ref_arquivo_arrf.write("preco_medio;")
ref_arquivo_arrf.write("preco_ultima_neg;")
ref_arquivo_arrf.write("preco_oferta_compra;")
ref_arquivo_arrf.write("preco_oferta_venda;")
ref_arquivo_arrf.write("negocios_efetuados;")
ref_arquivo_arrf.write("total_negociado;")
ref_arquivo_arrf.write("volume_total;")
#ref_arquivo_arrf.write("preco_exercicio;")
#ref_arquivo_arrf.write("indicador_correcao;")
#ref_arquivo_arrf.write("data_vencimento;")
#ref_arquivo_arrf.write("fator_cotacao;")
#ref_arquivo_arrf.write("preco_exercicio_pts;")
ref_arquivo_arrf.write("cod_papel;")
ref_arquivo_arrf.write("numero_distribuicao;\n")
#ref_arquivo_arrf.write("@data")

for linha in ref_arquivo:
    tipo_reg = linha[0:2]              # TIPREG - TIPO DE REGISTRO

    if tipo_reg == '00':
        nome_arq = linha[2:15]         # NOME DO ARQUIVO
        cod_origem = linha[15:23]      # CODIGO DA ORIGEM
        dt_ger_arq = linha[23:31]      # DATA DA GERAÇÃO DO ARQUIVO
        reserva = linha[31:245]        # RESERVA
        print(tipo_reg, nome_arq, cod_origem, dt_ger_arq, reserva)
    elif tipo_reg == '01':
        data_pregao = linha[2:10].strip()      # DATA DO PREGÃO
        cod_bdi = linha[10:12].strip()         # CODBDI - CÓDIGO BDI
        cod_neg = linha[12:24].strip()         # CODNEG - CÓDIGO DE NEGOCIAÇÃO DO PAPEL
        tp_merc = linha[24:27].strip()         # TPMERC - TIPO DE MERCADO
        nom_res = linha[27:39].strip()         # NOMRES - NOME RESUMIDO DA EMPRESA EMISSORA DO PAPEL
        especi = linha[39:49].strip()          # ESPECI - ESPECIFICAÇÃO DO PAPEL
        # PRAZOT - PRAZO EM DIAS DO MERCADO A TERMO
        prazo_merc_t = "0"
        if linha[49:52].strip() != "":
            prazo_merc_t = linha[49:52].strip()   
        mod_ref = linha[52:56].strip()         # MODREF - MOEDA DE REFERÊNCIA
        preco_aber = linha[56:69].strip()      # PREABE - PREÇO DE ABERTURA DO PAPEL- MERCADO NO PREGÃO
        preco_max = linha[69:82].strip()       # PREMAX - PREÇO MÁXIMO DO PAPEL- MERCADO NO PREGÃO
        preco_min = linha[82:95].strip()       # PREMIN - PREÇO MÍNIMO DO PAPEL- MERCADO NO PREGÃO
        preco_med = linha[95:108].strip()      # PREMED - PREÇO MÉDIO DO PAPEL- MERCADO NO PREGÃO
        preco_ult = linha[108:121].strip()     # PREULT - PREÇO DO ÚLTIMO NEGÓCIO DO PAPEL- MERCADO NO PREGÃO
        preco_oft_c = linha[121:134].strip()   # PREOFC - PREÇO DA MELHOR OFERTA DE COMPRA DO PAPEL- MERCADO
        preco_oft_v = linha[134:147].strip()   # PREOFV - PREÇO DA MELHOR OFERTA DE VENDA DO PAPEL- MERCADO
        tot_neg = linha[147:152].strip()       # TOTNEG - NEG. - NÚMERO DE NEGÓCIOS EFETUADOS COM O PAPEL- MERCADO NO PREGÃO
        qtd_neg_tot = linha[152:170].strip()   # QUATOT - QUANTIDADE TOTAL DE TÍTULOS NEGOCIADOS NESTE PAPEL- MERCADO
        vol_neg_tot = linha[170:188].strip()   # VOLTOT - VOLUME TOTAL DE TÍTULOS NEGOCIADOS NESTE PAPEL- MERCADO
        pre_exe = linha[188:201].strip()       # PREEXE - PREÇO DE EXERCÍCIO PARA O MERCADO DE OPÇÕES OU VALOR DO CONTRATO PARA O MERCADO DE TERMO SECUNDÁRIO
        ind_opc = linha[201:202].strip()       # INDOPC - INDICADOR DE CORREÇÃO DE PREÇOS DE EXERCÍCIOS OU VALORES DE CONTRATO PARA OS MERCADOS DE OPÇÕES OU TERMO SECUNDÁRIO
        dat_venc = linha[202:210].strip()      # DATVEN - DATA DO VENCIMENTO PARA OS MERCADOS DE OPÇÕES OU TERMO SECUNDÁRIO
        fator_cot = linha[210:217].strip()     # FATCOT - FATOR DE COTAÇÃO DO PAPEL
        pto_exe = linha[217:230].strip()       # PTOEXE - PREÇO DE EXERCÍCIO EM PONTOS PARA OPÇÕES REFERENCIADAS EM DÓLAR OU VALOR DE CONTRATO EM PONTOS PARA TERMO SECUNDÁRIO
        cod_isi = linha[230:242].strip()       # CODISI - CÓDIGO DO PAPEL NO SISTEMA ISIN OU CÓDIGO INTERNO DO PAPEL
        dis_med = linha[242:245].strip()       # DISMES - NÚMERO DE DISTRIBUIÇÃO DO PAPEL
        ref_arquivo_arrf.write(
            data_pregao + ";" \
            + cod_bdi + ";" \
            + cod_neg + ";" \
            + tp_merc + ";" \
            + nom_res + ";" \
            + especi + ";" \
            + prazo_merc_t + ";" \
            #+ mod_ref  ";" \
            + preco_aber + ";" \
            + preco_max + ";" \
            + preco_min + ";" \
            + preco_med + ";" \
            + preco_ult + ";" \
            + preco_oft_c + ";" \
            + preco_oft_v + ";" \
            + tot_neg + ";" \
            + qtd_neg_tot + ";" \
            + vol_neg_tot + ";" \
            #+ pre_exe + ", " \
            #+ ind_opc + ", " \
            #+ dat_venc +";" \
            #+ fator_cot + ", " \
            #+ pto_exe + ", " \
            + cod_isi + ";" \
            + dis_med + "\n")
        #print(tipo_reg, data_pregao, cod_bdi, cod_neg, tp_merc, nom_res, especi, int(prazo_merc_t), mod_ref, float(preco_aber), float(preco_max), float(preco_min, preco_med, preco_ult, preco_oft_c, preco_oft_v, tot_neg, qtd_neg_tot, vol_neg_tot, pre_exe, ind_opc, dat_venc, fator_cot, pto_exe, cod_isi, dis_med)
    elif tipo_reg == '99':
	    nome_arq = linha[02:15]        # NOME DO ARQUIVO
	    cod_origem = linha[15:23]      # CÓDIGO DA ORIGEM
	    dt_ger_arq = linha[23:31]      # DATA DA GERAÇÃO DO ARQUIVO
	    total_reg = linha[31:42]       # TOTAL DE REGISTROS
	    reserva = linha[42:245]        # RESERVA

ref_arquivo.close()
ref_arquivo_arrf.close()
