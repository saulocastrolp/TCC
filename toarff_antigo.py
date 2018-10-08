# -*- coding: utf-8 -*-

ref_arquivo = open("COTAHIST_A2018.TXT","r")
ref_arquivo_arrf = open("cot_hist_2008-new.arff","w")

# ref_arquivo = open("cot_hist_2008_a_2018","r")
# ref_arquivo_arrf = open("cot_hist_2008_a_2018.arff","w")

ref_arquivo_arrf.write("@relation historico_cot_diario\n\n")

ref_arquivo_arrf.write("@attribute data_pregao DATE \"yyyyMMdd\"\n")
ref_arquivo_arrf.write("@attribute cod_bdi numeric\n")
ref_arquivo_arrf.write("@attribute cod_negociacao string\n")
ref_arquivo_arrf.write("@attribute tipo_mercado numeric\n")
ref_arquivo_arrf.write("@attribute nome_papel string\n")
ref_arquivo_arrf.write("@attribute especificacao_papel string\n")
ref_arquivo_arrf.write("@attribute prazo_dias_mercado numeric\n")
#ref_arquivo_arrf.write("@attribute moeda_ref string\n")
ref_arquivo_arrf.write("@attribute preco_abertura numeric\n")
ref_arquivo_arrf.write("@attribute preco_maximo numeric\n")
ref_arquivo_arrf.write("@attribute preco_minimo numeric\n")
ref_arquivo_arrf.write("@attribute preco_medio numeric\n")
ref_arquivo_arrf.write("@attribute preco_ultima_neg numeric\n")
ref_arquivo_arrf.write("@attribute preco_oferta_compra numeric\n")
ref_arquivo_arrf.write("@attribute preco_oferta_venda numeric\n")
ref_arquivo_arrf.write("@attribute negocios_efetuados numeric\n")
ref_arquivo_arrf.write("@attribute total_negociado numeric\n")
ref_arquivo_arrf.write("@attribute volume_total numeric\n")
#ref_arquivo_arrf.write("@attribute preco_exercicio numeric\n")
ref_arquivo_arrf.write("@attribute indicador_correcao numeric\n")
#ref_arquivo_arrf.write("@attribute data_vencimento DATE \"yyyyMMdd\"\n")
#ref_arquivo_arrf.write("@attribute fator_cotacao numeric\n")
#ref_arquivo_arrf.write("@attribute preco_exercicio_pts numeric\n")
ref_arquivo_arrf.write("@attribute cod_papel string\n")
ref_arquivo_arrf.write("@attribute numero_distribuicao numeric\n\n")
ref_arquivo_arrf.write("@data\n")
ref_arquivo_arrf.write("\n")

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
        preco_aber = str(float(linha[56:69].strip()) / 100)      # PREABE - PREÇO DE ABERTURA DO PAPEL- MERCADO NO PREGÃO
        preco_max = str(float(linha[69:82].strip()) / 100)      # PREMAX - PREÇO MÁXIMO DO PAPEL- MERCADO NO PREGÃO
        preco_min = str(float(linha[82:95].strip()) / 100)      # PREMIN - PREÇO MÍNIMO DO PAPEL- MERCADO NO PREGÃO
        preco_med = str(float(linha[95:108].strip()) / 100)     # PREMED - PREÇO MÉDIO DO PAPEL- MERCADO NO PREGÃO
        preco_ult = str(float(linha[108:121].strip()) / 100)    # PREULT - PREÇO DO ÚLTIMO NEGÓCIO DO PAPEL- MERCADO NO PREGÃO
        preco_oft_c = str(float(linha[121:134].strip()) / 100)   # PREOFC - PREÇO DA MELHOR OFERTA DE COMPRA DO PAPEL- MERCADO
        preco_oft_v = str(float(linha[134:147].strip()) / 100)   # PREOFV - PREÇO DA MELHOR OFERTA DE VENDA DO PAPEL- MERCADO
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
        ref_arquivo_arrf.write("\"" \
            + data_pregao + "\"" + ", " \
            + cod_bdi + ", " \
            + "'" + cod_neg + "'" + ", " \
            + tp_merc + ", " \
            + "'" + nom_res + "'" + ", " \
            + "'" + especi + "'" + ", " \
            + prazo_merc_t + ", " \
            #+ "'" + mod_ref + "'" + ", " \
            + preco_aber + ", " \
            + preco_max + ", " \
            + preco_min + ", " \
            + preco_med + ", " \
            + preco_ult + ", " \
            + preco_oft_c + ", " \
            + preco_oft_v + ", " \
            + tot_neg + ", " \
            + qtd_neg_tot + ", " \
            + vol_neg_tot + ", " \
            #+ pre_exe + ", " \
            #+ ind_opc + ", " \
            #+ "\"" + dat_venc + "\"" + ", " \
            #+ fator_cot + ", " \
            #+ pto_exe + ", " \
            + "'" + cod_isi + "'" + ", " \
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
