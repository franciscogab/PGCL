import streamlit as st

def principal():
    st.title('ROHP')
    st.write('''A ferramenta ROHP é uma ferramenta que realizará o diagnóstico de sua organização/setor a fim de conhecer sua situação atual, isto é, qual é o seu grau de maturidade em Gestão de Conhecimento (GC) e, assim, possa definir seu planejamento para implementar ou aperfeiçoar a GC.''')
    st.subheader('Instruções para preenchimento')
    '''Cada uma das 8 características presentes nas 4 dimensões deve ser minuciosamente analisada e pontuada com base em evidências, utilizando a seguinte escala:
    \n\n1= Discordo Totalmente
    \n2= Discordo
    \n3= Discordo Parcialmente
    \n4= Concordo
    \n5= Concordo Totalmente 
    '''

    if st.button('Iniciar diagnóstico'):
        diagnostico()

def diagnostico():
    st.title('Diagnostico')
    t1,t2,t3,t4 = st.colums(4)
    with st.form():
        with t1:
            st.title('Relacional')
        with t2:
            st.title('Organizacional')
        with t3:
            st.title('Humana')
        with t4:
            st.title('Processual')


principal()