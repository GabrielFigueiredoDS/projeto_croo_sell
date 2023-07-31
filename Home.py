import streamlit as st
from PIL import Image

# ==================================
# Configurações Página 
# ==================================
st.set_page_config(page_title='Home', page_icon="📈", layout='wide')

image = Image.open('sr.png')
st.sidebar.image(image, width=220)

st.sidebar.markdown('# Relatório Cross Sell Habitação')
st.sidebar.markdown('## SR BRASÍLIA SUL')
st.sidebar.markdown('Time de milhões!!!')
st.sidebar.markdown("""---""")

st.write("# Relatório Cross Sell Habitação do Periodo de 01/07 a 21/07 ")

st.markdown(
    """
    O Dashboard de Cross Sell Habitação foi construído para acompanhar as métricas de concessão de crédito de cada cliente, 
    com o objetivo de observar a fidelização dos clientes e a concessão de crédito sustentável para nossa unidade.
    ### Observações
    - Base de dados:
        - A base de dados dos créditos cedidos foi retirada do SIOPI e os do CROSS SELL foi análisado com base no relacionamento.caixa, 
        podendo assim haver alguns dados divergentes ou que ainda não foram sensibilizados junto ao CPF do cliente. 
        - Vale observar também que o item "investimento" no relacionamento em 90% dos casos se trata de investimentos em
        contas poupanças 1288 ou 3880.
        - Algo a ser levado em consideração é que os CPFs que foram pesquisados o CROS SELL no relacionamento.caixa foi do principal
        participante e não dos coobrigados, podendo assim, alguns produtos e serviços estarem agregados no cpf dos coobrigados. 
""")