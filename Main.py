import streamlit as st
import pandas as pd
import unicodedata

Parte1=[['ABRAÃO BARROS DA SILVA', 10, 10, 10, 10, 9, 9.33333333333333, 9.56666666666667, 'Excelente'],
['ALEX GUTEMBERG FIGUEIREDO', 10, 10, 10, 10, 7, 6.0, 7.7, 'Bom'],
['ARYANNE REIS DOS SANTOS', 10, 10, 10, 10, 8, 6.66666666666667, 8.13333333333333, 'Bom'],
['CAMILA VITORIA LUCAS BEZERRA DA SILVA', 0, 0, 10, 10, 0, 8.0, 6.0, 'Ainda não suficiente'],
['CONCEIÇÃO DE MARIA TEIXEIRA MENDES DE SOUZA', 0, 0, 0, 10, 0, 0.0, 1.0, 'Insuficiente'],
['DIOGO DANIEL SENA COSTA', 0, 0, 0, 0, 9, 0.0, 0.9, 'Insuficiente'],
['ERNANI JOÃO DE MELO', 10, 10, 10, 10, 9, 8.66666666666667, 9.23333333333333, 'Ótimo'],
['FERNANDA GABRIELA SOBRINHO DOS ANJOS', 10, 10, 10, 10, 10, 8.66666666666667, 9.33333333333333, 'Ótimo'],
['GABRIEL EZIDIO DA SILVA BRILHANTE', 10, 10, 10, 10, 10, 8.66666666666667, 9.33333333333333, 'Ótimo'],
['GABRIEL WINICIUS DE OLIVEIRA LIMA', 0, 10, 10, 10, 10, 3.33333333333333, 5.66666666666667, 'Ainda não suficiente'],
['GEORGE JOSÉ DOS SANTOS VERA CRUZ FILHO', 10, 10, 10, 10, 9, 7.33333333333333, 8.56666666666667, 'Ótimo'],
['GUILHERME DE SANTANA NASCIMENTO', 10, 0, 10, 10, 10, 8.66666666666667, 8.33333333333333, 'Bom'],
['ITALO ROBERT RODRIGUES DA SILVA', 0, 0, 0, 0, 4, 6.66666666666667, 3.73333333333333, 'Insuficiente'],
['JADSON DA SILVA', 0, 0, 0, 10, 0, 8.0, 5.0, 'Ainda não suficiente'],
['JAIR LUIZ DOS SANTOS', 0, 10, 10, 10, 6, 4.66666666666667, 5.93333333333333, 'Ainda não suficiente'],
['JEANE MARIA BARBOSA E SILVA', 10, 10, 10, 10, 7, 6.66666666666667, 8.03333333333333, 'Bom'],
['JEFFERSON DOS SANTOS FIGUEIRA', 0, 10, 10, 10, 9, 5.33333333333333, 6.56666666666667, 'Ainda não suficiente'],
['JOSÉ CARLOS OLIVEIRA DA SILVA', 10, 0, 0, 10, 6, 7.33333333333333, 6.26666666666667, 'Ainda não suficiente'],
['JOSE GLEBSON MONTEIRO', 10, 10, 10, 10, 9, 7.33333333333333, 8.56666666666667, 'Ótimo'],
['KAUÃ SILVA DE LIMA', 10, 10, 10, 10, 9, 8.0, 8.9, 'Ótimo'],
['KAYO MANOEL PEREIRA BATISTA', 10, 10, 10, 10, 0, 7.33333333333333, 7.66666666666667, 'Bom'],
['LAIS MICAELE RAMOS BRASIL', 10, 10, 0, 10, 0, 7.33333333333333, 6.66666666666667, 'Ainda não suficiente'],
['LINDOBERTO ABIDIJAN MOTA DOS SANTOS', 10, 10, 10, 10, 10, 6.66666666666667, 8.33333333333333, 'Bom'],
['LUCAS DANIEL ROQUE DE LIMA', 0, 0, 0, 10, 10, 0.0, 2.0, 'Insuficiente'],
['MARIA DAS GRAÇAS DE LIMA TAVARES', 10, 10, 10, 10, 9, 6.0, 7.9, 'Bom'],
['Maria Gabriela de Moura', 0, 0, 0, 10, 0, 4.0, 3.0, 'Insuficiente'],
['MAX DIOGO FERREIRA DE SOUZA', 10, 10, 10, 10, 10, 0.0, 5.0, 'Ainda não suficiente'],
['MAYSA CRISTINA DA SILVA', 10, 0, 0, 10, 0, 0.0, 2.0, 'Insuficiente'],
['MELQUISEDEQUE ANDRADE SILVA', 0, 0, 0, 0, 0, 0.0, 0.0, 'Insuficiente'],
['NICOLLAS VIDAL HOLANDA', 10, 0, 0, 10, 9, 8.66666666666667, 7.23333333333333, 'Bom'],
['PEDRO LUCAS SILVA DE SOUZA', 10, 10, 10, 10, 9, 6.0, 7.9, 'Bom'],
['PEDRO MOURA CAVALCANTE', 0, 10, 0, 10, 0, 0.0, 2.0, 'Insuficiente'],
['RENATO SILVESTRE DE LIMA', 10, 10, 10, 10, 7, 7.33333333333333, 8.36666666666667, 'Bom'],
['ROBERTA BATISTA LIMA DA SILVA', 10, 0, 0, 10, 0, 0.0, 2.0, 'Insuficiente'],
['VÍCTOR LUCAS NUNES DE ALMEIDA', 10, 10, 10, 10, 9, 0.0, 4.9, 'Insuficiente'],
['WEDSON TRAJANO DA SILVA', 10, 10, 10, 10, 0, 5.33333333333333, 6.66666666666667, 'Ainda não suficiente']]

Parte2=[['ABRAÃO BARROS DA SILVA', 10, 10, 10, 10, 10, 10, 0, 0, 10, 9.999],
['ALEX GUTEMBERG FIGUEIREDO', 10, 10, 8, 10, 10, 0, 0, 0, 10, 8.9991],
['ARYANNE REIS DOS SANTOS', 10, 10, 10, 0, 10, 9, 0, 0, 10, 9.082425],
['CAMILA VITORIA LUCAS BEZERRA DA SILVA', 10, 10, 10, 0, 10, 0, 0, 0, 10, 8.3325],
['CONCEIÇÃO DE MARIA TEIXEIRA MENDES DE SOUZA', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0],
['DIOGO DANIEL SENA COSTA', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0],
['ERNANI JOÃO DE MELO', 10, 10, 9, 10, 10, 0, 0, 0, 10, 9.082425],
['FERNANDA GABRIELA SOBRINHO DOS ANJOS', 10, 0, 10, 10, 10, 0, 0, 0, 10, 7.49925],
['GABRIEL EZIDIO DA SILVA BRILHANTE', 10, 10, 10, 10, 10, 0, 0, 0, 10, 9.16575],
['GABRIEL WINICIUS DE OLIVEIRA LIMA', 10, 10, 0, 10, 10, 7, 0, 0, 10, 8.915775],
['GEORGE JOSÉ DOS SANTOS VERA CRUZ FILHO', 0, 10, 10, 10, 10, 9, 0, 0, 10, 8.249175],
['GUILHERME DE SANTANA NASCIMENTO', 0, 10, 10, 10, 10, 0, 0, 0, 10, 7.49925],
['ITALO ROBERT RODRIGUES DA SILVA', 0, 0, 8, 10, 0, 0, 0, 0, 0, 1.49985],
['JADSON DA SILVA', 0, 0, 10, 10, 8, 0, 0, 0, 10, 5.6661],
['JAIR LUIZ DOS SANTOS', 10, 10, 10, 0, 10, 9, 0, 0, 10, 9.082425],
['JEANE MARIA BARBOSA E SILVA', 10, 10, 8, 10, 10, 8, 0, 0, 10, 9.6657],
['JEFFERSON DOS SANTOS FIGUEIRA', 10, 0, 0, 10, 10, 9, 0, 0, 10, 7.415925],
['JOSÉ CARLOS OLIVEIRA DA SILVA', 10, 10, 10, 10, 10, 8, 0, 0, 10, 9.83235],
['JOSE GLEBSON MONTEIRO', 10, 10, 10, 10, 10, 10, 0, 0, 10, 9.999],
['KAUÃ SILVA DE LIMA', 10, 10, 0, 10, 10, 0, 0, 0, 10, 8.3325],
['KAYO MANOEL PEREIRA BATISTA', 0, 0, 0, 10, 0, 0, 0, 0, 10, 4.16625],
['LAIS MICAELE RAMOS BRASIL', 0, 0, 10, 0, 0, 0, 0, 0, 10, 4.16625],
['LINDOBERTO ABIDIJAN MOTA DOS SANTOS', 10, 10, 0, 10, 10, 10, 0, 0, 10, 9.16575],
['LUCAS DANIEL ROQUE DE LIMA', 0, 0, 0, 10, 10, 0, 0, 0, 10, 4.9995],
['MARIA DAS GRAÇAS DE LIMA TAVARES', 10, 10, 9, 10, 10, 10, 0, 0, 10, 9.915675],
['Maria Gabriela de Moura', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0],
['MAX DIOGO FERREIRA DE SOUZA', 10, 10, 7, 10, 10, 8, 0, 0, 10, 9.582375],
['MAYSA CRISTINA DA SILVA', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0],
['MELQUISEDEQUE ANDRADE SILVA', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0],
['NICOLLAS VIDAL HOLANDA', 0, 0, 0, 0, 10, 0, 0, 0, 10, 4.16625],
['PEDRO LUCAS SILVA DE SOUZA', 10, 0, 10, 10, 10, 0, 0, 0, 10, 7.49925],
['PEDRO MOURA CAVALCANTE', 0, 0, 10, 10, 8, 10, 0, 0, 10, 6.49935],
['RENATO SILVESTRE DE LIMA', 0, 10, 10, 10, 10, 0, 0, 0, 10, 7.49925],
['ROBERTA BATISTA LIMA DA SILVA', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0],
['VÍCTOR LUCAS NUNES DE ALMEIDA', 10, 0, 10, 10, 10, 10, 0, 0, 10, 8.3325],
['WEDSON TRAJANO DA SILVA', 10, 0, 10, 10, 10, 0, 0, 0, 10, 7.49925]]

def normalizar(texto):
    if pd.isna(texto):
        return ""
    texto = str(texto).strip().lower()
    texto = ''.join(c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn')
    return texto

st.set_page_config(page_title="Gestão da Informação-TLOG", layout="wide")

col1, col2 = st.columns([1, 4])

with col1:
    st.image("https://upload.wikimedia.org/wikipedia/commons/8/86/Senac_logo.svg", width=180)

with col2:
    st.title("Gestão da Informação")
    st.markdown("Consulta de notas")

nome_usuario = st.text_input("Digite seu nome completo")


if nome_usuario:
    nome_busca = normalizar(nome_usuario)
    encontrado = False
    for i in range(1, len(Parte1)):
        if normalizar(Parte1[i][0]) == nome_busca:
            encontrado = True
            break
    if not encontrado:
        st.error("Nome não encontrado.")
    else:
        st.success("Aluno encontrado!")
        st.subheader("Parte 1")
        c1,c2,c3,c4,c5,c6,c7,c8=st.columns(8)
        with c1:
            st.write("Fórum 1")
            st.write(Parte1[i][1])
        with c2:
            st.write("Fórum 3")
            st.write(Parte1[i][2])
        with c3:
            st.write("Fórum 5")
            st.write(Parte1[i][3])
        with c4:
            st.write("Atividade 1")
            st.write(Parte1[i][4])
        with c5:
            st.write("Atividade 2")
            st.write(Parte1[i][5])
        with c6:
            st.write("Teste")
            st.write(Parte1[i][6])
        with c7:
            st.write("NF")
            st.write(Parte1[i][7])    
        with c8:
            st.write("Conceito")
            st.write(Parte1[i][8])
        
        st.subheader("Parte 2")
        c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10=st.columns(11)
        with c0:
            st.write("Fórum 7")
            st.write(Parte2[i][1])
        with c1:
            st.write("Fórum 9")
            st.write(Parte2[i][2])
        with c2:
            st.write("Tarefa 3")
            st.write(Parte2[i][3])
        with c3:
            st.write("Tarefa 4")
            st.write(Parte2[i][4])
        with c4:
            st.write("Tarefa 5")
            st.write(Parte2[i][5])
        with c5:
            st.write("Tarefa 6")
            st.write(Parte2[i][6])
        with c6:
            st.write("Tarefa 7")
            st.write(Parte2[i][7])
        with c7:
            st.write("Tarefa 8")
            st.write(Parte2[i][8])
        with c8:
            st.write("Apresentação PI")
            st.write(Parte2[i][9])
        with c9:
            st.write("Nota FInal")
            st.write(Parte2[i][10])            
        with c10:
            if Parte2[i][9]<4.99:
                Conceito="Insuficiente"
            else:
                if Parte2[i][9]<6.99:
                    Conceito="Ainda não Suficiente"
                else:
                    if Parte2[i][9]<8.49:
                        Conceito="Bom"
                    else:
                        if Parte2[i][9]<9.49:
                            Conceito="Ótimo"
                        else:
                            Conceito="Excelente"
            st.write("Conceito")
            st.write(Conceito)
        st.subheader("Conceito Final")
        st.write(0.5*Parte1[i][7]+0.5*Parte2[i][10])
