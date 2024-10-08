import streamlit as st
from PIL import Image
from menu import menu


st.set_page_config(page_title="Home", layout="wide")
# Open the logo file
img = Image.open('Logo_SFMR_Horizontal_Centralizado.png')
st.sidebar.image(img, use_column_width=True)
    

 
# TODO: Implementar a funcionalidade de recuperação de senha e usuário com API do Gmail           
    # if 'forgot_password_clicked' not in st.session_state:
    #     st.session_state['forgot_password_clicked'] = False
    # if 'forgot_username_clicked' not in st.session_state:
    #     st.session_state['forgot_username_clicked'] = False
        
    # def forgot_password_button():
    #     st.session_state['forgot_password_clicked'] = True
    #     st.session_state['forgot_username_clicked'] = False
    # def forgot_username_button():
    #     st.session_state['forgot_username_clicked'] = True
    #     st.session_state['forgot_password_clicked'] = False
        
    # col1, col2 = st.columns([1, 3.4])
    
    # with col1:
    #     st.button('Esqueceu a senha?', type='primary', key='forgot_password', on_click=forgot_password_button)
    # if st.session_state['forgot_password_clicked'] and not st.session_state['forgot_username_clicked']:
    #     user_management.forgot_password_widget()
    # with col2:
    #     st.button('Esqueceu o usuário?', type='primary', key='forgot_username', on_click=forgot_username_button)
    # if st.session_state['forgot_username_clicked'] and not st.session_state['forgot_password_clicked']:
    #     user_management.forgot_username_widget()
    

st.write('Bem-vindo')
st.write('''
        <div style="text-align: justify;">
        Este aplicativo foi desenvolvido para a análise de dados dos exames realizados e para a gestão do Programa de Controle de Qualidade dos equipamentos
        de imagem do Serviço de Medicina Nuclear do Hospital de Clínicas de Porto Alegre. Desenvolvido por Leandro Souza. Caso encontre algum problema ou
        deseje fornecer alguma sugestão, por favor, entre em contato através do e-mail: <b>leandro.souza.159@gmail.com</b>.
        </div>
            ''', unsafe_allow_html=True)
st.write('') # small space between

    

menu()
