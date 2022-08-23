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
    st.write('')

    with st.form('ROHP'):
        st.subheader('Relacional')
        st.markdown('<hr>', unsafe_allow_html=True)
        c1,c2 = st.columns([6,2])
        with c1:
            st.write('**Conduta etica**')
            st.write('Os servidores detem total conhecimento sobre os conceitos envolvidos nas condtas eticas e sempre os aplicam.')    
        with c2:
            conduta_etica = st.radio('',(1,2,3,4,5), key='conduta', horizontal=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        c1,c2 = st.columns([6,2])
        with c1:
            st.write('**Transmissão de conhecimentos e experiências via rede**')
            st.write('Existe um canal de transmissão do conhecimento e troca de experiências entre os militares do setor bem como das demais áreas interessadas e este canal sempre é utilizado.')    
        with c2:
            transmissao_conhecimento = st.radio('',[1,2,3,4,5], key='transmissao', horizontal=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        c1,c2 = st.columns([6,2])
        with c1:
            st.write('**Comunicação**')
            st.write('A comunicação entre os servidores do setor, bem como das demais áreas interessadas ocorre sem falhas e de forma objetiva.')    
        with c2:
            comunicacao = st.radio('',[1,2,3,4,5], key='comunicacao', horizontal=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        c1,c2 = st.columns([6,2])
        with c1:
            st.write('**Práticas de integração**')
            st.write('São realizados eventos que permitem a integração entre a tripulação.')    
        with c2:
            praticas_integracao = st.radio('',[1,2,3,4,5], key='praticas', horizontal=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        c1,c2 = st.columns([6,2])
        with c1:
            st.write('**Integração entre setores**')
            st.write('Os setores são totalmente integrados entre si, ou seja, os setores se complementam em busca do alcance da missão da OM.')    
        with c2:
            integracao_setores = st.radio('',[1,2,3,4,5], key='integracao', horizontal=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        c1,c2 = st.columns([6,2])
        with c1:
            st.write('**Programa de integração com organizações participantes**')
            st.write('Existe um programa bem definido e atualizado sobre a integração entre a OM apoiadora e as demais OM apoiadas.')    
        with c2:
            programa_integracao = st.radio('',[1,2,3,4,5], key='programa', horizontal=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        c1,c2 = st.columns([6,2])
        with c1:
            st.write('**Comprometimento de todos os valores e comportamentos éticos na organização**')
            st.write('É visível o comprometimento de todos os envolvidos no processo com os valores e comportamentos éticos na oraganização.')    
        with c2:
            comprometimento = st.radio('',[1,2,3,4,5], key='comprometimento', horizontal=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        c1,c2 = st.columns([6,2])
        with c1:
            st.write('**Programa de integridade**')
            st.write('Todos os envolvidos conhecem e prezam pelo Programa de Integridade da Marinha do Brasil.')    
        with c2:
            integridade = st.radio('',[1,2,3,4,5], key='integridade', horizontal=True)
        
        c1,c2,c3=st.columns([1,10,1])
        with c1:
            voltar = st.button('Voltar')
        with c2:
            st.write('')
        with c3:
            avancar = st.form_submit_button('Avançar')

principal()