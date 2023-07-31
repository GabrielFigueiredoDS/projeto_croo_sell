import streamlit as st
from PIL import Image
import pandas as pd
import plotly.express as px

# ==================================
# DataSet
# ==================================
df = pd.read_csv('dataset/dados.csv', sep=';')

# ==================================
# Tratamento DataSet
# ==================================

# Visto que em 92% casos o item investimento de trata de poupança vamos remove-lo na analise
df = df.drop(columns='INVESTIMENTO')

# Criando coluna QUANTIDADE PRODUTOS
df['QUANTIDADE DE PRODUTOS'] = df.apply(lambda row: row.str.count('s').sum(), axis=1)


# ==================================
# Configurações Página 
# ==================================
st.set_page_config(page_title='Home', page_icon="📊", layout='wide')

image = Image.open('sr.png')
st.sidebar.image(image, width=220)

st.sidebar.markdown('# Relatório Cross Sell Habitação')
st.sidebar.markdown('## SR BRASÍLIA SUL')
st.sidebar.markdown('Time de milhões!!!')
st.sidebar.markdown("""---""")

# ==================================
# Sidebar > Filtro data
# ==================================
st.sidebar.markdown("# Filtros")

opcao_sev = st.sidebar.multiselect(
    'SEVs',
    df.loc[:, "SEV"].unique().tolist(),
    default=df.loc[:, "SEV"].unique().tolist())

st.sidebar.markdown("""---""")

opcao_ag = st.sidebar.multiselect(
    'Agências',
    df[(df['SEV'].isin(opcao_sev))][['AG']].squeeze().unique().tolist(),
    default=df[(df['SEV'].isin(opcao_sev))][['AG']].squeeze().unique().tolist())

# Filtro data
linhas_selecionadas = df['SEV'].isin(opcao_sev)
df = df.loc[linhas_selecionadas, :]

# Filtro transito
linhas_selecionadas = df['AG'].isin(opcao_ag)
df = df.loc[linhas_selecionadas, :]

st.title('📊 Visão Geral')

# ==================================
# Visão Incial
# ==================================
with st.container():
        
        st.title('Visão Geral')
        
col1, col2 = st.columns(2)

with col1:
    quant_contratos = df.shape[0]
    col1.metric('Quantidade de Contratos', quant_contratos)
    
with col2:
    valor_total_contratado = df['Valor Financ.'].sum().round(2)
    
    col2.metric('Valor Total Contratado R$', valor_total_contratado)
        
# ==================================
# CROS SELL
# ==================================

with st.container():
    st.markdown('### Quantidade de Cross Sell por Contrato')

    quant_prod = (df.loc[:,['QUANTIDADE DE PRODUTOS', 'ID']]
        .groupby(['QUANTIDADE DE PRODUTOS'])
        .count()
        .sort_values(by='ID')
        .reset_index())

    quant_prod = quant_prod.rename(columns={'ID': 'QUANT. CONTRATO', 'QUANTIDADE DE PRODUTOS': 'CROSS SELL (QUANT. PROD)'})

    fig = px.bar(quant_prod, x='CROSS SELL (QUANT. PROD)', y='QUANT. CONTRATO')

    # adicionando valores em cima da barra
    fig.update_traces(text=quant_prod['QUANT. CONTRATO'], textposition='auto')

    st.plotly_chart(fig, use_container_width=True)

with st.container():
    
    st.markdown('### Cross Sell por Contrato')
        
    quant_prod = quant_prod[['QUANT. CONTRATO', 'CROSS SELL (QUANT. PROD)']]
         
    st.dataframe(quant_prod)

# ==================================
# Conta Corrente
# ==================================

with st.container():

    st.markdown('### Quatidade de Contas Correntes por Contratos') 

    col1, col2 = st.columns(2)

    with col1:
        quant_conta = (df.loc[:,['CONTA', 'ID']]
                .groupby(['CONTA'])
                .count()
                .sort_values(by='ID')
                .reset_index())

        quant_conta = quant_conta.rename(columns={'ID': 'QUANT. CONTRATO'})

        quant_conta.replace({'n': 'não contrato', 's': 'contratado'}, inplace=True)

        fig = px.bar(
            quant_conta,
            x="CONTA",
            y="QUANT. CONTRATO",
            text="QUANT. CONTRATO",
            color="CONTA")
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown('###')
        st.markdown('###')
        st.markdown('###')
        st.dataframe(quant_conta)

# ==================================
# CROT
# ==================================

with st.container():
    st.markdown('### Quatidade de CROT por Contratos') 
    col1, col2 = st.columns(2)
        
    with col1:

        quant_crot = (df.loc[:,['CROT', 'ID']]
              .groupby(['CROT'])
              .count()
              .sort_values(by='ID')
              .reset_index())

        quant_crot = quant_crot.rename(columns={'ID': 'QUANT. CONTRATO'})

        quant_crot.replace({'n': 'não contrato', 's': 'contratado'}, inplace=True)

        fig = px.bar(
            quant_crot,
            x="CROT",
            y="QUANT. CONTRATO",
            text="QUANT. CONTRATO",
            color="CROT")
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown('###')
        st.markdown('###')
        st.markdown('###')
        st.dataframe(quant_crot)

# ==================================
# Cesta de Serviço
# ==================================

with st.container():
    st.markdown('### Quatidade de Cesta de Serviço por Contratos') 

    col1, col2 = st.columns(2)
        
    with col1:
        quant_cesta = (df.loc[:,['CESTA', 'ID']]
              .groupby(['CESTA'])
              .count()
              .sort_values(by='ID')
              .reset_index())

        quant_cesta = quant_cesta.rename(columns={'ID': 'QUANT. CONTRATO'})

        quant_cesta.replace({'n': 'não contrato', 's': 'contratado'}, inplace=True)

        fig = px.bar(
            quant_cesta,
            x="CESTA",
            y="QUANT. CONTRATO",
            text="QUANT. CONTRATO",
            color="CESTA")
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown('###')
        st.markdown('###')
        st.markdown('###')
        st.dataframe(quant_cesta)

# ==================================
# Seg. Vida 
# ==================================

with st.container():

    st.markdown('### Quatidade de Seguro de Vida por Contratos') 

    col1, col2 = st.columns(2)
        
    with col1:
        quant_seg_vida = (df.loc[:,['SEGURO VIDA', 'ID']]
              .groupby(['SEGURO VIDA'])
              .count()
              .sort_values(by='ID')
              .reset_index())

        quant_seg_vida = quant_seg_vida.rename(columns={'ID': 'QUANT. CONTRATO'})

        quant_seg_vida.replace({'n': 'não contrato', 's': 'contratado'}, inplace=True)

        fig = px.bar(
            quant_seg_vida,
            x="SEGURO VIDA",
            y="QUANT. CONTRATO",
            text="QUANT. CONTRATO",
            color="SEGURO VIDA")
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown('###')
        st.markdown('###')
        st.markdown('###')
        st.dataframe(quant_seg_vida)

# ==================================
# Seg. Patrimonial 
# ==================================

with st.container():

    st.markdown('### Quatidade de Seguro de Patrimonial por Contratos') 

    col1, col2 = st.columns(2)
        
    with col1:
        quant_seg_patrim = (df.loc[:,['SEG PATRIMONIAL', 'ID']]
              .groupby(['SEG PATRIMONIAL'])
              .count()
              .sort_values(by='ID')
              .reset_index())

        quant_seg_patrim = quant_seg_patrim.rename(columns={'ID': 'QUANT. CONTRATO'})

        quant_seg_patrim.replace({'n': 'não contrato', 's': 'contratado'}, inplace=True)

        fig = px.bar(
            quant_seg_patrim,
            x="SEG PATRIMONIAL",
            y="QUANT. CONTRATO",
            text="QUANT. CONTRATO",
            color="SEG PATRIMONIAL")
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown('###')
        st.markdown('###')
        st.markdown('###')
        st.dataframe(quant_seg_patrim)

# ==================================
# PREV
# ==================================

with st.container():

    st.markdown('### Quatidade de Previdência por Contratos') 

    col1, col2 = st.columns(2)
        
    with col1:
        quant_prev= (df.loc[:,['PREVIDÊNCIA', 'ID']]
              .groupby(['PREVIDÊNCIA'])
              .count()
              .sort_values(by='ID')
              .reset_index())

        quant_prev = quant_prev.rename(columns={'ID': 'QUANT. CONTRATO'})

        quant_prev.replace({'n': 'não contrato', 's': 'contratado'}, inplace=True)

        fig = px.bar(
            quant_prev,
            x="PREVIDÊNCIA",
            y="QUANT. CONTRATO",
            text="QUANT. CONTRATO",
            color="PREVIDÊNCIA")
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown('###')
        st.markdown('###')
        st.markdown('###')
        st.dataframe(quant_prev)

# ==================================
# CAP
# ==================================

with st.container():

    st.markdown('### Quatidade de CAP por Contratos') 

    col1, col2 = st.columns(2)
        
    with col1:
        quant_cap= (df.loc[:,['CAPTALIZAÇÃO', 'ID']]
              .groupby(['CAPTALIZAÇÃO'])
              .count()
              .sort_values(by='ID')
              .reset_index())

        quant_cap = quant_cap.rename(columns={'ID': 'QUANT. CONTRATO'})

        quant_cap.replace({'n': 'não contrato', 's': 'contratado'}, inplace=True)

        fig = px.bar(
            quant_cap,
            x="CAPTALIZAÇÃO",
            y="QUANT. CONTRATO",
            text="QUANT. CONTRATO",
            color="CAPTALIZAÇÃO")

        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown('###')
        st.markdown('###')
        st.markdown('###')
        st.dataframe(quant_cap)

# ==================================
# Consórcio 
# ==================================

with st.container():

    st.markdown('### Quatidade de Consrcio por Contratos') 

    col1, col2 = st.columns(2)
        
    with col1:

        quant_cons= (df.loc[:,['CONSÓRCIO', 'ID']]
              .groupby(['CONSÓRCIO'])
              .count()
              .sort_values(by='ID')
              .reset_index())

        quant_cons = quant_cons.rename(columns={'ID': 'QUANT. CONTRATO'})

        quant_cons.replace({'n': 'não contrato', 's': 'contratado'}, inplace=True)

        fig = px.bar(
            quant_cons,
            x="CONSÓRCIO",
            y="QUANT. CONTRATO",
            text="QUANT. CONTRATO",
            color="CONSÓRCIO")
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown('###')
        st.markdown('###')
        st.markdown('###')
        st.dataframe(quant_cons)