import streamlit as st
st.set_page_config(layout='wide')
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

    with st.form('ROHP'):
        st.subheader('Relacional')
        c1,c2 = st.columns([6,2])
        with c1:
            st.write('Conduta etica')
            st.write('Os servidores detem total conhecimento sobre os conceitos envolvidos nas condtas eticas e sempre os aplicam.')    
        with c2:
            conduta_etica = st.radio('',[1,2,3,4,5], index=3, horizontal=True)
    
        enviar = st.form_submit_button('Enviar')

principal()