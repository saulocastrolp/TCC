# -*- coding: utf-8 -*-
import concatena_arq
import argparse

parser = argparse.ArgumentParser(description = 'Conversor de txt de dados históricos para arff para uso no WEKA.')
parser.add_argument('--init_year', action = 'store', dest = 'init_year',
                           default = '2008', required = False,
                           help = 'ano inicial a se considerar.')
parser.add_argument('--end_year', action = 'store', dest = 'end_year',
                           default = '2018', required = False,
                           help = 'limite de anos a serem considerados.')
parser.add_argument('--limit', action = 'store', dest = 'limite',
                           default = None, required = False,
                           help = 'limite de linhas a serem convertidas.')
arguments = parser.parse_args()

limite = int(arguments.limite) if arguments.limite else None
init_year = arguments.init_year
end_year = arguments.end_year

### Declaração dos arquivos que seram utilizados ###
print "Concatenando arquivos txt. Aguarde!"
arq_entrada = concatena_arq.concatenaArq(init_year, end_year)
print arq_entrada
arq_saida = arq_entrada.split('.')[0] + '.arff'
ref_arquivo = open(arq_entrada,"r")
ref_arquivo_arrf = open(arq_saida,"w")

countLinhas = 0

### Declaração das Variaveis Colhidas ###
cod_neg         = "{"        # CODNEG - CÓDIGO DE NEGOCIAÇÃO DO PAPEL
tp_merc         = "{"        # TPMERC - TIPO DE MERCADO
nom_res         = "{"        # NOMRES - NOME RESUMIDO DA EMPRESA EMISSORA DO PAPEL
especi          = "{"        # ESPECI - ESPECIFICAÇÃO DO PAPEL
cod_isi         = "{"        # CODISI - CÓDIGO DO PAPEL NO SISTEMA ISIN OU CÓDIGO INTERNO DO PAPEL

### Recolhendo valores nominais ###
tam_arq = ref_arquivo.readlines()
count = len(tam_arq)
for l in tam_arq:
    if (count < len(tam_arq)):
        add = "," if count > 1 else ""

        if (not cod_neg.__contains__("\"" + l[12:24].strip() + "\"")):
            cod_neg += "\"" + l[12:24].strip() + "\"" + add     # CODNEG - CÓDIGO DE NEGOCIAÇÃO DO PAPEL
        if (not tp_merc.__contains__("\"" + l[24:27].strip() + "\"")):
            tp_merc += "\"" + l[24:27].strip() + "\"" + add     # TPMERC - TIPO DE MERCADO
        if (not nom_res.__contains__( "\"" +l[27:39].strip() + "\"")):
            nom_res += "\"" + l[27:39].strip() + "\"" + add     # NOMRES - NOME RESUMIDO DA EMPRESA EMISSORA DO PAPEL
        if (not especi.__contains__( "\"" +l[39:49].strip() + "\"")):
            especi += "\"" + l[39:49].strip() + "\"" + add      # ESPECI - ESPECIFICAÇÃO DO PAPEL
        if (not cod_isi.__contains__( "\"" + l[230:242].strip()+ "\"")):
            cod_isi += "\"" + l[230:242].strip() + "\"" + add   # CODISI - CÓDIGO DO PAPEL NO SISTEMA ISIN OU CÓDIGO INTERNO DO PAPEL

    count -= 1
    countLinhas += 1
    if (limite and countLinhas == limite):
        break
ref_arquivo.close()
ref_arquivo = open(arq_entrada,"r")


### Lambda para conversão de data ###
formDt = lambda d: "{}-{}-{} 00:00:00".format(d[0:4], d[4:6], d[6:8])
fecha_nominais = " }\n"

### Cabeçalho do ARFF ###
ref_arquivo_arrf.write("@RELATION historico_cot_diario\n\n")

ref_arquivo_arrf.write("@ATTRIBUTE data_pregao date \"yyyy-MM-dd HH:mm:ss\"\n")
ref_arquivo_arrf.write("@ATTRIBUTE cod_bdi numeric\n")
ref_arquivo_arrf.write("@ATTRIBUTE cod_negociacao " + cod_neg + fecha_nominais)
ref_arquivo_arrf.write("@ATTRIBUTE tipo_mercado " + tp_merc + fecha_nominais)
#ref_arquivo_arrf.write("@ATTRIBUTE nome_papel " + nom_res + fecha_nominais)
ref_arquivo_arrf.write("@ATTRIBUTE especificacao_papel " + especi + fecha_nominais)
ref_arquivo_arrf.write("@ATTRIBUTE prazo_mercado_termo numeric\n")
#ref_arquivo_arrf.write("@ATTRIBUTE preco_abertura numeric\n")
#ref_arquivo_arrf.write("@ATTRIBUTE preco_maximo numeric\n")
#ref_arquivo_arrf.write("@ATTRIBUTE preco_minimo numeric\n")
ref_arquivo_arrf.write("@ATTRIBUTE preco_medio numeric\n")
#ref_arquivo_arrf.write("@ATTRIBUTE preco_ultima_neg numeric\n")
#ref_arquivo_arrf.write("@ATTRIBUTE preco_oferta_compra numeric\n")
#ref_arquivo_arrf.write("@ATTRIBUTE preco_oferta_venda numeric\n")
#ref_arquivo_arrf.write("@ATTRIBUTE negocios_efetuados numeric\n")
#ref_arquivo_arrf.write("@ATTRIBUTE total_negociado numeric\n")
#ref_arquivo_arrf.write("@ATTRIBUTE volume_total numeric\n")
#ref_arquivo_arrf.write("@ATTRIBUTE indicador_correcao numeric\n")
#ref_arquivo_arrf.write("@ATTRIBUTE cod_papel " + cod_isi + fecha_nominais)
#ref_arquivo_arrf.write("@ATTRIBUTE numero_distribuicao numeric\n\n")
ref_arquivo_arrf.write("@DATA\n")
ref_arquivo_arrf.write("\n")

countLinhas = 0
### Percorrendo arquivo para colher os dados ###
for l in ref_arquivo:
    tipo_reg = l[0:2]                      # TIPREG - TIPO DE REGISTRO

    ### Cabeçalho do arquivo (Desnecessário para o Proposto) ###
    if tipo_reg == '00':
        nome_arq = l[2:15]         # NOME DO ARQUIVO
        cod_origem = l[15:23]      # CODIGO DA ORIGEM
        dt_ger_arq = l[23:31]      # DATA DA GERAÇÃO DO ARQUIVO
        reserva = l[31:245]        # RESERVA
        print(tipo_reg, nome_arq, cod_origem, dt_ger_arq, reserva)
    ### Inicio dos descritivos dos dados aqui cruciais ###
    elif tipo_reg == '01':
        data_pregao     = formDt(l[2:10].strip())          # DATA DO PREGÃO
        cod_bdi         = l[10:12].strip()                 # CODBDI - CÓDIGO BDI
        cod_neg         = l[12:24].strip()                 # CODNEG - CÓDIGO DE NEGOCIAÇÃO DO PAPEL
        tp_merc         = l[24:27].strip()                 # TPMERC - TIPO DE MERCADO
        nom_res         = l[27:39].strip()                 # NOMRES - NOME RESUMIDO DA EMPRESA EMISSORA DO PAPEL
        especi          = l[39:49].strip()                 # ESPECI - ESPECIFICAÇÃO DO PAPEL
        prazo_merctermo = l[49:52].strip()                 # PRAZOT - PRAZO EM DIAS DO MERCADO A TERMO
        mod_ref         = l[52:56].strip()                          # MODREF - MOEDA DE REFERÊNCIA
        preco_aber      = str(float(l[56:69].strip()) / 100)        # PREABE - PREÇO DE ABERTURA DO PAPEL- MERCADO NO PREGÃO
        preco_max       = str(float(l[69:82].strip()) / 100)        # PREMAX - PREÇO MÁXIMO DO PAPEL- MERCADO NO PREGÃO
        preco_min       = str(float(l[82:95].strip()) / 100)        # PREMIN - PREÇO MÍNIMO DO PAPEL- MERCADO NO PREGÃO
        preco_med       = str(float(l[95:108].strip()) / 100)       # PREMED - PREÇO MÉDIO DO PAPEL- MERCADO NO PREGÃO
        preco_ult       = str(float(l[108:121].strip()) / 100)      # PREULT - PREÇO DO ÚLTIMO NEGÓCIO DO PAPEL- MERCADO NO PREGÃO
        preco_oft_c     = str(float(l[121:134].strip()) / 100)      # PREOFC - PREÇO DA MELHOR OFERTA DE COMPRA DO PAPEL- MERCADO
        preco_oft_v     = str(float(l[134:147].strip()) / 100)      # PREOFV - PREÇO DA MELHOR OFERTA DE VENDA DO PAPEL- MERCADO
        tot_neg         = str(float(l[147:152].strip()) / 100)      # TOTNEG - NEG. - NÚMERO DE NEGÓCIOS EFETUADOS COM O PAPEL- MERCADO NO PREGÃO
        qtd_neg_tot     = str(float(l[152:170].strip()) / 100)      # QUATOT - QUANTIDADE TOTAL DE TÍTULOS NEGOCIADOS NESTE PAPEL- MERCADO
        vol_neg_tot     = str(float(l[170:188].strip()) / 100)      # VOLTOT - VOLUME TOTAL DE TÍTULOS NEGOCIADOS NESTE PAPEL- MERCADO
        pre_exe         = str(float(l[188:201].strip()) / 100)      # PREEXE - PREÇO DE EXERCÍCIO PARA O MERCADO DE OPÇÕES OU VALOR DO CONTRATO PARA O MERCADO DE TERMO SECUNDÁRIO
        ind_opc         = l[201:202].strip()        # INDOPC - INDICADOR DE CORREÇÃO DE PREÇOS DE EXERCÍCIOS OU VALORES DE CONTRATO PARA OS MERCADOS DE OPÇÕES OU TERMO SECUNDÁRIO
        dat_venc        = l[202:210].strip()        # DATVEN - DATA DO VENCIMENTO PARA OS MERCADOS DE OPÇÕES OU TERMO SECUNDÁRIO
        fator_cot       = l[210:217].strip()        # FATCOT - FATOR DE COTAÇÃO DO PAPEL
        pto_exe         = str(float(l[217:230].strip()) / 100)         # PTOEXE - PREÇO DE EXERCÍCIO EM PONTOS PARA OPÇÕES REFERENCIADAS EM DÓLAR OU VALOR DE CONTRATO EM PONTOS PARA TERMO SECUNDÁRIO
        cod_isi         = l[230:242].strip()        # CODISI - CÓDIGO DO PAPEL NO SISTEMA ISIN OU CÓDIGO INTERNO DO PAPEL
        dis_med         = l[242:245].strip()        # DISMES - NÚMERO DE DISTRIBUIÇÃO DO PAPEL

        ref_arquivo_arrf.write("\"" \
            + data_pregao + "\"" + ", " \
            + cod_bdi + ", " \
            + "'" + cod_neg + "'" + ", " \
            + tp_merc + ", " \
            #+ "'" + nom_res + "'" + ", " \
            + "'" + especi + "'" + ", " \
            + "'" + prazo_merctermo + "'" + ", " \
            #+ preco_aber + ", " \
            #+ preco_max + ", " \
            #+ preco_min + ", " \
            + preco_med \
            #+ preco_ult + ", " \
            #+ preco_oft_c + ", " \
            #+ preco_oft_v + ", " \
            #+ tot_neg + ", " \
            #+ qtd_neg_tot + ", " \
            #+ vol_neg_tot + ", " \
            #+ ind_opc + ", " \
            #+ "'" + cod_isi + "'" + ", " \
            #+ dis_med 
            + "\n")

    ### Cabeçalho para arquivo de reserva (Desnecessário para o Proposto) ###  
    elif tipo_reg == '99':
	    nome_arq = l[2:15]        # NOME DO ARQUIVO
	    cod_origem = l[15:23]      # CÓDIGO DA ORIGEM
	    dt_ger_arq = l[23:31]      # DATA DA GERAÇÃO DO ARQUIVO
	    total_reg = l[31:42]       # TOTAL DE REGISTROS
	    reserva = l[42:245]        # RESERVA
    countLinhas += 1
    if (limite and countLinhas == limite):
        break

### Fechando os arquivos ###
ref_arquivo.close()
ref_arquivo_arrf.close()
