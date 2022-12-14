import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
from plotly.subplots import make_subplots



st.set_page_config(layout='wide', page_icon='https://firebasestorage.googleapis.com/v0/b/prodesex-8e59f.appspot.com/o/Imagens%2Fimage.png?alt=media&token=3bf4e428-fd29-47b3-9fc3-223fe66e8631')
st.markdown('<style>a{text-decoration:none;}</style>', unsafe_allow_html=True)
def principal():
    st.markdown("<img src='https://firebasestorage.googleapis.com/v0/b/prodesex-8e59f.appspot.com/o/Imagens%2FGRUPO%2007.png?alt=media&token=88307934-0c21-4e23-9b95-f8b8c0996242' alt='ROHP logo' style='display:block; margin-left:auto;margin-right:auto; width:100%'>", unsafe_allow_html=True)
    st.write('##')
    st.write('##')
    st.write('''A Matriz ROHP é uma ferramenta que realizará o diagnóstico de sua organização/setor, a fim de identificar qual é o seu grau de maturidade em Gestão de Conhecimento (GC) e, assim, definir seu planejamento para implementar ou aperfeiçoar a GC.''')
    st.write('##')

    col1, col2, col3, col4 = st.columns(4)
    with col2:
        st.markdown("<a href='https://www.google.com'><img src='https://firebasestorage.googleapis.com/v0/b/prodesex-8e59f.appspot.com/o/Imagens%2Fpgclnovo.png?alt=media&token=f1a8b5d3-6f22-4ac6-a758-98ee17f4125d' alt='PGCL' style='width:10em'></a>", unsafe_allow_html=True)
    with col3:
        st.markdown("<a href='https://firebasestorage.googleapis.com/v0/b/prodesex-8e59f.appspot.com/o/Documentos%2FDIAGN%C3%93STICO%20GC.xlsx?alt=media&token=422c4fd4-5cac-4d09-a22a-1db3ed2a22bc'><img src='https://firebasestorage.googleapis.com/v0/b/prodesex-8e59f.appspot.com/o/Imagens%2F20220825_105542_0000.png?alt=media&token=4a6f6087-4e2c-47d8-b4c5-dd67034f4e95' alt='download' style='width:10em'></a>", unsafe_allow_html=True)
    st.write('##')

    st.subheader('Instruções para preenchimento')
    '''Cada uma das 8 características presentes nas 4 dimensões deve ser minuciosamente analisada e pontuada com base em evidências, utilizando a seguinte escala:
    \n\n1= Discordo Totalmente
    \n2= Discordo
    \n3= Discordo Parcialmente
    \n4= Concordo
    \n5= Concordo Totalmente
    '''
    st.write('##')
    col1, col2 = st.columns([8,4])
    with col1:
        if st.button('Iniciar diagnóstico'):
            st.session_state['pagina_atual']='diagnostico'
            st.experimental_rerun()


def diagnostico():
    st.title('Diagnóstico')
    st.write('')

    with st.form('ROHP'):
        st.subheader('Dimensão Relacional')
        st.markdown('<hr>', unsafe_allow_html=True)
        c1,c2 = st.columns([6,2])
        with c1:
            st.write('**Conduta ética**')
            st.write('Os servidores detém total conhecimento sobre os conceitos envolvidos nas condutas éticas e sempre os aplicam.')    
        with c2:
            st.session_state['conduta_etica'] = st.radio('',(1,2,3,4,5), key='conduta', horizontal=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        c1,c2 = st.columns([6,2])
        with c1:
            st.write('**Transmissão de conhecimentos e experiências via rede**')
            st.write('Existe um canal de transmissão do conhecimento e troca de experiências entre os militares do setor bem como das demais áreas interessadas e este canal sempre é utilizado.')    
        with c2:
            st.session_state['transmissao_conhecimento'] = st.radio('',[1,2,3,4,5], key='transmissao', horizontal=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        c1,c2 = st.columns([6,2])
        with c1:
            st.write('**Comunicação**')
            st.write('A comunicação entre os servidores do setor, bem como das demais áreas interessadas ocorre sem falhas e de forma objetiva.')    
        with c2:
            st.session_state['comunicacao'] = st.radio('',[1,2,3,4,5], key='comunicacao_entre', horizontal=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        c1,c2 = st.columns([6,2])
        with c1:
            st.write('**Práticas de integração**')
            st.write('São realizados eventos que permitem a integração entre a tripulação.')    
        with c2:
            st.session_state['praticas_integracao'] = st.radio('',[1,2,3,4,5], key='praticas', horizontal=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        c1,c2 = st.columns([6,2])
        with c1:
            st.write('**Integração entre setores**')
            st.write('Os setores são totalmente integrados entre si, ou seja, os setores se complementam em busca do alcance da missão da OM.')    
        with c2:
            st.session_state['integracao_setores'] = st.radio('',[1,2,3,4,5], key='integracao', horizontal=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        c1,c2 = st.columns([6,2])
        with c1:
            st.write('**Programa de integração com organizações participantes**')
            st.write('Existe um programa bem definido e atualizado sobre a integração entre a OM apoiadora e as demais OM apoiadas.')    
        with c2:
            st.session_state['programa_integracao'] = st.radio('',[1,2,3,4,5], key='programa_int', horizontal=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        c1,c2 = st.columns([6,2])
        with c1:
            st.write('**Comprometimento de todos os valores e comportamentos éticos na organização**')
            st.write('É visível o comprometimento de todos os envolvidos no processo com os valores e comportamentos éticos na oraganização.')    
        with c2:
            st.session_state['comprometimento'] = st.radio('',[1,2,3,4,5], key='comprometimento_', horizontal=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        c1,c2 = st.columns([6,2])
        with c1:
            st.write('**Programa de integridade**')
            st.write('Todos os envolvidos conhecem e prezam pelo Programa de Integridade da Marinha do Brasil.')    
        with c2:
            st.session_state['integridade'] = st.radio('',[1,2,3,4,5], key='integridade_', horizontal=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        c1,c2,c3=st.columns([1,10,1])
        with c1:
            voltar = st.form_submit_button('Voltar')
        with c2:
            st.write('')
        with c3:
            avancar = st.form_submit_button('Avançar')
        if avancar: 
            st.session_state['pagina_atual']='organizacional'
            st.experimental_rerun()
        elif voltar:
            st.session_state['pagina_atual']='principal'
            st.experimental_rerun()
            
         
        
def organizacional():
    st.title('Diagnóstico')
    st.write('')

    with st.form('ROHP'):
        st.subheader('Dimensão Organizacional')
        st.markdown('<hr>', unsafe_allow_html=True)
        c1,c2 = st.columns([6,2])
        with c1:
            st.write('**Ambiente propício (disseminação de conhecimento**')
            st.write(' Esta Organização apresenta um ambiente totalmente propício para a Disseminação de conhecimento.')    
        with c2:
            st.session_state['ambiente_propicio'] = st.radio('',(1,2,3,4,5), key='ambiente', horizontal=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        c1,c2 = st.columns([6,2])
        with c1:
            st.write('**Infraestrutura física e de processo**')
            st.write('A infraestrutura física e de processo são perfeitamente apropriadas para o alcance da Gestão do Conhecimento.')    
        with c2:
            st.session_state['infraestrutura'] = st.radio('',[1,2,3,4,5], key='infraestrutura_', horizontal=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        c1,c2 = st.columns([6,2])
        with c1:
            st.write('**Liderança formalmente estabelecidas (impoulsionadores da rede)**')
            st.write('As lideranças formalmente estabelecidas nos setores envolvidos impulsionam a rede de conhecimento?')    
        with c2:
            st.session_state['lideranca'] = st.radio('',[1,2,3,4,5], key='lideranca_', horizontal=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        c1,c2 = st.columns([6,2])
        with c1:
            st.write('**Estrutura de comunicação estabelecida**')
            st.write('Existe uma perfeita estrutura de comunicação estabelecida entre os setores.')    
        with c2:
            st.session_state['estrutura_comunicacao'] = st.radio('',[1,2,3,4,5], key='estrutura_com', horizontal=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        c1,c2 = st.columns([6,2])
        with c1:
            st.write('**Design (TMFT = Regimento iterno)**')
            st.write('A TMFT está organizada de forma a permitir o melhor funcionamento dos setores da OM.')    
        with c2:
            st.session_state['design'] = st.radio('',[1,2,3,4,5], key='design_', horizontal=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        c1,c2 = st.columns([6,2])
        with c1:
            st.write('**Alinhamento objetivos estratégicos**')
            st.write('Todas as ações executadas pelos setores visam sempre o alcance dos objetivos estratégicos da OM.')    
        with c2:
            st.session_state['alinhamento'] = st.radio('',[1,2,3,4,5], key='alinhamento_', horizontal=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        c1,c2 = st.columns([6,2])
        with c1:
            st.write('**Normas e valores comunicados**')
            st.write('As normas e os valores da OM são comunicados de forma abrangente para alcançar a todos os envolvidos.')    
        with c2:
            st.session_state['normas'] = st.radio('',[1,2,3,4,5], key='normas_', horizontal=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        c1,c2 = st.columns([6,2])
        with c1:
            st.write('**Estrutura de papéis e responsabilidades**')
            st.write('Existe uma formalização da estrutura de funções e responsabilidades e esta formalização é divulgada para todos os envolvidos.')    
        with c2:
            st.session_state['estrutura'] = st.radio('',[1,2,3,4,5], key='estrutura_', horizontal=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        c1,c2,c3=st.columns([1,10,1])
        with c1:
            voltar = st.form_submit_button('Voltar')
        with c2:
            st.write('')
        with c3:
            avancar = st.form_submit_button('Avançar')
        if avancar: 
            st.session_state['pagina_atual']='humana'
            st.experimental_rerun()

        elif voltar:
            st.session_state['pagina_atual']='diagnostico'
            st.experimental_rerun()
 

def humana():
    st.title('Diagnóstico')
    st.write('')

    with st.form('ROHP'):
        st.subheader('Dimensão Humana')
        st.markdown('<hr>', unsafe_allow_html=True)
        c1,c2 = st.columns([6,2])
        with c1:
            st.write('**Educação Formal**')
            st.write('A educação formal, ou seja, a educação proveniente do período educacional escolar, dos militares e civis envolvidos é adequada.')    
        with c2:
            st.session_state['educacao'] = st.radio('',(1,2,3,4,5), key='educacao_', horizontal=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        c1,c2 = st.columns([6,2])
        with c1:
            st.write('**Treinamento continuado**')
            st.write('A Organização possui calendário rotineiro de treinamentos e estimula a participação das pessoas.')    
        with c2:
            st.session_state['treinamento'] = st.radio('',[1,2,3,4,5], key='treinamento_', horizontal=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        c1,c2 = st.columns([6,2])
        with c1:
            st.write('**Perfil da tripulação: Aproveitamento de conhecimentos e experiências**')
            st.write('A tripulação como um todo possui um perfil de aproveitamento adequado dos conhecimentos e experiências geradas.')    
        with c2:
            st.session_state['perfil'] = st.radio('',[1,2,3,4,5], key='perfil_', horizontal=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        c1,c2 = st.columns([6,2])
        with c1:
            st.write('**Formação dos instrutores internos**')
            st.write('As pessoas responsáveis por realizar treinamentos internos com a tripulação possui formação adequada.')    
        with c2:
            st.session_state['formacao'] = st.radio('',[1,2,3,4,5], key='formacao_', horizontal=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        c1,c2 = st.columns([6,2])
        with c1:
            st.write('**Programa de desenvolvimento de liderança**')
            st.write('A OM busca estimular o programa de desenvolvimento de liderança, ou seja, mostra uma preocupação com o aprendizado das habilidades e competências de líderes, seja Oficial ou Praça.')    
        with c2:
            st.session_state['programa'] = st.radio('',[1,2,3,4,5], key='programa_desen', horizontal=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        c1,c2 = st.columns([6,2])
        with c1:
            st.write('**Preocupação com aspectos motivacionais**')
            st.write('As pessoas investidas de função de liderança demonstra total preocupação com aspectos motivacionais.')    
        with c2:
            st.session_state['preocupacao'] = st.radio('',[1,2,3,4,5], key='preocupacao_', horizontal=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        c1,c2 = st.columns([6,2])
        with c1:
            st.write('**Estímulos à criatividade**')
            st.write('As pessoas investidas de função de liderança, seja Oficial ou Praça, demonstram estímulo à criatividade.')    
        with c2:
            st.session_state['estimulos'] = st.radio('',[1,2,3,4,5], key='estimulos_', horizontal=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        c1,c2 = st.columns([6,2])
        with c1:
            st.write('**Incentivo ao comprometimento**')
            st.write('As pessoas investidas de função de liderança, seja Oficial ou Praça, demonstram total incentivo ao comprometimento perante a missão da OM.')    
        with c2:
            st.session_state['incentivo'] = st.radio('',[1,2,3,4,5], key='incentivo_comp', horizontal=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        c1,c2,c3=st.columns([1,10,1])
        with c1:
            voltar = st.form_submit_button('Voltar')
        with c2:
            st.write('')
        with c3:
            avancar = st.form_submit_button('Avançar')
        if avancar: 
            st.session_state['pagina_atual']='processual'
            st.experimental_rerun()
        elif voltar:
            st.session_state['pagina_atual']='organizacional'
            st.experimental_rerun()
 

def processual():
    st.title('Diagnóstico')
    st.write('')

    with st.form('ROHP'):
        st.subheader('Dimensão Processual')
        st.markdown('<hr>', unsafe_allow_html=True)
        c1,c2 = st.columns([6,2])
        with c1:
            st.write('**Sistematização de conhecimento**')
            st.write('O conhecimento está sistematizado, ou seja, está ordenado, classificado e baseado em um parâmetro para atingir ao objetivo proposto.')    
        with c2:
            st.session_state['sistematizacao'] = st.radio('',(1,2,3,4,5), key='sistematizacao_', horizontal=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        c1,c2 = st.columns([6,2])
        with c1:
            st.write('**Práticas e processos de captação de pessoal (Mapa de competências)**')
            st.write('Existem procedimentos de práticas e processos de captação de pessoal bem definidos e atualizados, como por exemplo, mapas de competências das pessoas que servem na OM.')    
        with c2:
            st.session_state['praticas_competencia'] = st.radio('',[1,2,3,4,5], key='praticas_comp', horizontal=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        c1,c2 = st.columns([6,2])
        with c1:
            st.write('**Processo de codificação**')
            st.write('Existem métodos e incentivos para melhorar a codificação do conhecimento, ou seja, formas de facilitar o aprendizado e conhecimento.')    
        with c2:
            st.session_state['processo_codificacao'] = st.radio('',[1,2,3,4,5], key='processo_cod', horizontal=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        c1,c2 = st.columns([6,2])
        with c1:
            st.write('**Conhecimento institucionalizados e experiências codificadas**')
            st.write('Os conhecimentos atinentes ao setor estão institucionalizados e as experiências adquiridas estão codificadas, de maneira a facilitar o compartilhamento')    
        with c2:
            st.session_state['conhecimento'] = st.radio('',[1,2,3,4,5], key='conhecimento_inst', horizontal=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        c1,c2 = st.columns([6,2])
        with c1:
            st.write('**Programa de desenvolvimento de competências: Esforço em pesquisa e desenvolvimento**')
            st.write('A OM sempre incentiva a área da pesquisa e desenvolvimento visando o desenvolvimento de competências. (Entende-se por desenvolvimento de competências a aquisição do conhecimento e o domínio das habilidades necessárias para desempenhar o seu papel).')    
        with c2:
            st.session_state['programa_competencia'] = st.radio('',[1,2,3,4,5], key='programa_comp', horizontal=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        c1,c2 = st.columns([6,2])
        with c1:
            st.write('**Uso de TIC para a gestão do conhecimento**')
            st.write('Existem recursos tecnológicos direcionados para a Gestão do conhecimento.')    
        with c2:
            st.session_state['tic'] = st.radio('',[1,2,3,4,5], key='tic_', horizontal=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        c1,c2 = st.columns([6,2])
        with c1:
            st.write('**Gestão Documental**')
            st.write('O Setor possui uma Gestão efetiva de documentos. (Considere Gestão de documentos a Organização, produção, uso e destinação dos documentos, de forma a tornar a informação mais acessível e sua guarda sustentável).')    
        with c2:
            st.session_state['gestao_doc'] = st.radio('',[1,2,3,4,5], key='gestao_', horizontal=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        c1,c2 = st.columns([6,2])
        with c1:
            st.write('**Mapeamento de Processos**')
            st.write('Os processos existentes estão inteiramente mapeados e atualizados.')    
        with c2:
            st.session_state['mapeamento'] = st.radio('',[1,2,3,4,5], key='mapeamento_', horizontal=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        c1,c2,c3=st.columns([1,10,1])
        with c1:
            voltar = st.form_submit_button('Voltar')
        with c2:
            st.write('')
        with c3:
            avancar = st.form_submit_button('Avançar')
        if avancar: 
            st.session_state['pagina_atual']='formulario'
            st.experimental_rerun()
        elif voltar:
            st.session_state['pagina_atual']='humana'
            st.experimental_rerun()
 

def formulario():
    st.title('Formulário')
    with st.form('form'):
        st.session_state['om'] = st.text_input('OM', value='')
        st.session_state['nome'] = st.text_input('Nome Completo', value='')
        st.session_state['posto'] = st.text_input('Posto/Graduação')
        st.session_state['funcao'] = st.text_input('Função')
        c1,c2,c3=st.columns([1,10,1])
        with c1:
            voltar = st.form_submit_button('Voltar')
        with c2:
            st.write('')
        with c3:
            avancar = st.form_submit_button('Concluir')
        if avancar: 
            st.session_state['pagina_atual']='relatorio'
            st.experimental_rerun()
        elif voltar:
            st.session_state['pagina_atual']='processual'
            st.experimental_rerun()


def relatorio():
    RELACIONAL={	
        'Dimensão Relacional':['Conduta Ética','Transmissão de conhecimentos e experiências via rede','Comunicação','Práticas de Integração', 'Integração entre setores', 
        'Programa de integração com organizações participantes', 'Comprometimento de todos os valores e comportamentos éticos na organização', 'Programa de Integridade']
       ,'Notas':[st.session_state['conduta_etica'],st.session_state['transmissao_conhecimento'],st.session_state['comunicacao'],st.session_state['praticas_integracao'],
        st.session_state['integracao_setores'],st.session_state['programa_integracao'],st.session_state['comprometimento'],st.session_state['integridade']]}
    relacional = pd.DataFrame(RELACIONAL)
    relacional = pd.concat([relacional, pd.DataFrame({'Dimensão Relacional':['TOTAL'], 'Notas':[relacional.Notas.sum()]})], axis = 0)
    
    ORGANIZACIONAL={
        'Dimensão Organizacional':['Ambiente propício (disseminação de conhecimento)','Infraestrutura física e de processo',
        'Lideranças Formalmente estabelecidas (impulsionadores da rede)','Estrutura de Comunicação estabelecida', 
        'Design (TMFT = Regimento interno)', 'Alinhamento objetivos estratégicos',
        'Normas e valores comunicados','Estrutura de papéis e responsabilidades'],
        'Notas':[st.session_state['ambiente_propicio'],st.session_state['infraestrutura'],
        st.session_state['lideranca'],st.session_state['estrutura_comunicacao'],
        st.session_state['design'],st.session_state['alinhamento'],st.session_state['normas'],st.session_state['estrutura']]}
    organizacional=pd.DataFrame(ORGANIZACIONAL)
    organizacional = pd.concat([organizacional, pd.DataFrame({'Dimensão Organizacional':['TOTAL'], 'Notas':[organizacional.Notas.sum()]})], axis = 0)
    
    HUMANA={
        'Dimensão Humana':['Educação Formal', 'Treinamento continuado', 'Perfil da tripulação: Aproveitamento de conhecimentos e Experiências', 
        'Formação dos Instrutores Internos', 'Programa de desenvolvimento de Liderança', 'Preocupação com aspectos motivacionais', 
        'Estímulos à criatividade', 'Incentivo ao comprometimento'],
        'Notas':[st.session_state['educacao'],st.session_state['treinamento'],st.session_state['perfil'],
        st.session_state['formacao'], st.session_state['programa'], st.session_state['preocupacao'],
        st.session_state['estimulos'], st.session_state['incentivo']]}
    humana=pd.DataFrame(HUMANA)
    humana = pd.concat([humana, pd.DataFrame({'Dimensão Humana':['TOTAL'], 'Notas':[humana.Notas.sum()]})], axis = 0)

    PROCESSUAL={
        'Dimensão Processual':['Sistematização do conhecimento', 'Práticas e processos de captação de pessoal (Mapa de competências)',
        'Processo de codificação', 'Conhecimento institucionalizados e experiências codificadas', 'Programa de desenvolvimento de competências: Esforço em pesquisa e desenvolvimento',
        'Uso de TIC para a gestão do conhecimento', 'Gestão Documental', 'Mapeamento de Processos'],
        'Notas':[st.session_state['sistematizacao'],st.session_state['praticas_competencia'],st.session_state['processo_codificacao'],
        st.session_state['conhecimento'],st.session_state['programa_competencia'],st.session_state['tic'],
        st.session_state['gestao_doc'],st.session_state['mapeamento']]}
    processual=pd.DataFrame(PROCESSUAL)
    processual = pd.concat([processual, pd.DataFrame({'Dimensão Processual':['TOTAL'], 'Notas':[processual.Notas.sum()]})], axis = 0)
    
    st.markdown("<img src='https://firebasestorage.googleapis.com/v0/b/prodesex-8e59f.appspot.com/o/Imagens%2FGRUPO%2007.png?alt=media&token=88307934-0c21-4e23-9b95-f8b8c0996242' alt='ROHP logo' style='display:block; margin-left:auto;margin-right:auto; width:100%'>", unsafe_allow_html=True)

    st.markdown(f"<h1 style='text-align:center;font-weight:bold'>{st.session_state['om']}</h1>", unsafe_allow_html=True)

    st.write('##')
    col1,col2=st.columns(2)
    with col1:
        styler= relacional.reset_index(drop=True).style.hide_index().background_gradient(cmap='Blues', subset=pd.IndexSlice[relacional.index.get_level_values(0)[:-1], 'Notas']).set_properties(subset=['Dimensão Relacional'], **{'width': '95%'})


        st.write(styler.to_html(),unsafe_allow_html=True)
    with col2:
        styler2 = organizacional.reset_index(drop=True).style.hide_index().background_gradient(cmap='Blues', subset=pd.IndexSlice[organizacional.index.get_level_values(0)[:-1], 'Notas']).set_properties(subset=['Dimensão Organizacional'], **{'width': '95%'})
        st.write(styler2.to_html(),unsafe_allow_html=True)

    st.write('###')
    st.write('###')
    col3,col4=st.columns(2)
    with col3:
        styler3 = humana.reset_index(drop=True).style.hide_index().background_gradient(cmap='Blues', subset=pd.IndexSlice[humana.index.get_level_values(0)[:-1], 'Notas']).set_properties(subset=['Dimensão Humana'], **{'width': '95%'})
        st.write(styler3.to_html(),unsafe_allow_html=True)
    with col4:
        styler4 = processual.reset_index(drop=True).style.hide_index().background_gradient(cmap='Blues', subset=pd.IndexSlice[processual.index.get_level_values(0)[:-1], 'Notas']).set_properties(subset=['Dimensão Processual'], **{'width': '95%'})
        st.write(styler4.to_html(),unsafe_allow_html=True)
    
    st.write('##')
    st.markdown('<hr>', unsafe_allow_html=True)

    col5, col6 = st.columns(2)
    with col5:
        sumario = pd.DataFrame({'Dimensão':['Relacional', 'Organizacional', 'Humana', 'Processual'],
        'Soma':[relacional.Notas[:-1].sum(), organizacional.Notas[:-1].sum(), humana.Notas[:-1].sum(), processual.Notas[:-1].sum()],
        '% do total':['{:.2f}%'.format(100*relacional.Notas[:-1].sum()/40), '{:.2f}%'.format(100*organizacional.Notas[:-1].sum()/40), '{:.2f}%'.format(100*humana.Notas[:-1].sum()/40), '{:.2f}%'.format(100*processual.Notas[:-1].sum()/40)]})
        s = sumario.style.hide_index()
        st.write(s.to_html(), unsafe_allow_html=True)
        st.write('##')
        metas_dimensao = st.selectbox('Meta por dimensão', list(range(1,41)))

    with col6:
        plt.rcParams['font.family'] = 'sans-serif'
        fig, ax1 = plt.subplots()
        ax1.set_ylim([0,40])
        ax1.set_ylabel('Pontuação')
        ax1.set_xlabel('Dimensão')
        ax1.bar(sumario['Dimensão'], sumario['Soma'])
        ax1.plot(sumario['Dimensão'], [metas_dimensao]*4, color='black')
        
        ax2 = ax1.twinx()
        ax2.set_ylim([0,100])
        ax2.set_yticks([20,40,60,80,100])
        ax2.set_yticklabels(['20%','40%','60%','80%','100%'])
        ax2.set_ylabel('% do total')
        ax2.plot(sumario['Dimensão'], [float(i[:-1]) for i in  sumario['% do total']], color='tab:red')

        ax1.grid(axis = 'y')

        st.pyplot(fig)
    
    st.markdown("<hr>", unsafe_allow_html=True)
    col1, col2=st.columns(2)
    with col1:
        total_pontos = sumario.Soma.sum()
        if total_pontos <= 63:
            nivel_pontos = [1, 'Reação']
        elif total_pontos <= 95:
            nivel_pontos = [2,'Iniciação']
        elif total_pontos <= 111:
            nivel_pontos = [3,'Introdução']
        elif total_pontos <= 143:
            nivel_pontos = [4,'Refinamento']
        else:
            nivel_pontos = [5, 'Maturidade']
        st.title('Resultado avaliado da OM')
        maturidade={'Nível de Maturidade da Organização':[f'Nível {nivel_pontos[0]}: {nivel_pontos[1]}', f'Soma das dimensões: {total_pontos}']}
        maturidade = pd.DataFrame(maturidade)
        maturidade = maturidade.style.hide_index()
        maturidade.set_properties(**{'width':'100%'})
        st.markdown(maturidade.to_html(), unsafe_allow_html=True)

    with col2:
        niveis = {'Níveis de referência':['Nível 5: Maturidade - A GC está consolidada no setor.', 'Nível 4: Refinamento - A implementação da GC é avaliada e melhorada continuamente.', 'Nível 3: Introdução - Existem práticas de GC.', 'Nível 2: Iniciação - O setor inicia o reconhecimento da importância do gerenciamento do conhecimento.', 'Nível 1: Reação - O setor não possui características e iniciativas que promovam a GC.'],
        'Pontuação':['144 - 160', '112 - 143', '96 - 111','64 - 95', '32 - 63']}
        niveis = pd.DataFrame(niveis)
        niveis = niveis.style.hide_index()
        niveis.set_properties(**{'background-color':'#e0ffff'})
        st.markdown(niveis.to_html(), unsafe_allow_html=True)

    st.write('##')
    st.write('##')

    col1, col2, col3 = st.columns(3)
    with col3:
        st.markdown('''<p style='text-align:right'>Emissão: {}</p><br>
                    <hr style='height:5px';margin-bottom:0>
                    <p style='text-align:center; font-size:20px'>{}<br>
                    {}<br>
                    {}</p>'''.format(datetime.now().strftime('%d/%m/%Y'), st.session_state['nome'], st.session_state['posto'], st.session_state['funcao']), unsafe_allow_html=True)

    st.write('##')
    st.write('##')
    col1, col2 = st.columns(2)
    with col1:
        voltar = st.button('Voltar')
        if voltar:
            st.session_state['pagina_atual']='formulario'
            st.experimental_rerun()
    with col2:
        st.markdown("<a href='https://franciscogab-pgcl-rohp-n7szap.streamlitapp.com/'><button class='css-1cpxqw2 edgvbvh9' style='display:block; margin-left:auto; margin-right:auto'>Novo Relatório</button></a>", unsafe_allow_html=True)
    


        
   
try:
    if st.session_state['pagina_atual']=='diagnostico':
        diagnostico()
    elif st.session_state['pagina_atual']=='organizacional':
        organizacional()
    elif st.session_state['pagina_atual']=='humana':
        humana()
    elif st.session_state['pagina_atual']=='processual':
        processual()
    elif st.session_state['pagina_atual']=='principal':
        principal()
    elif st.session_state['pagina_atual']=='formulario':
        formulario()
    elif st.session_state['pagina_atual']=='relatorio':
        relatorio()
except Exception as error:
    st.write(error)
    principal()

