import streamlit as st
from main import run_compliance_assistant

st.title(" Assistente IA de Conformidade Farmacêutica do Kaio")
st.write("Esta IA auxilia você com **conformidade GMP da ANVISA** com base nas regulamentações RDC 301, RDC 658 e BPF")

# Sidebar para usuário selecionar
with st.sidebar:
    st.header("Selecione uma tarefa:")
    tipo_tarefa = "Responder Pergunta sobre Conformidade"

    pergunta_usuario = st.text_area("Digite sua pergunta sobre conformidade")

    if st.button("Executar verificação de Conformidade"):
        if not pergunta_usuario.strip():
            st.warning("Por favor, digite sua pergunta antes de executar")
        else:
            st.write("Processando sua solicitação... Aguarde, por favor.")

            resultado = run_compliance_assistant(pergunta_usuario)

            st.subheader(" Resposta da IA sobre Conformidade: ")
            st.write(resultado)