import streamlit as st
import random

st.set_page_config(page_title="Jogo da Senha", page_icon="🔐")

st.title("🔐 Jogo da Senha")
st.write("Escolha 4 cores na ordem correta para adivinhar a senha secreta!")

CORES = ["🔴", "🔵", "🟢", "🟡", "🟠", "🟣"]

# Inicializa o estado do jogo
if "senha" not in st.session_state:
    st.session_state.senha = random.sample(CORES, k=4)
    st.session_state.historico = []
    st.session_state.tentativas = 0

st.subheader("Monte seu palpite:")
col1, col2, col3, col4 = st.columns(4)

with col1:
    c1 = st.selectbox("Cor 1", CORES, key="c1")
with col2:
    c2 = st.selectbox("Cor 2", CORES, key="c2")
with col3:
    c3 = st.selectbox("Cor 3", CORES, key="c3")
with col4:
    c4 = st.selectbox("Cor 4", CORES, key="c4")

if st.button("Enviar Palpite",use_container_width=True):
    palpite = [c1, c2, c3, c4]
    st.session_state.tentativas += 1
    lugar_certo = 0
    lugar_errado = 0
    
    senha_temp = list(st.session_state.senha)
    palpite_temp = list(palpite)
    
    for i in range(4):
        if palpite_temp[i] == senha_temp[i]:
            lugar_certo += 1
            senha_temp[i] = None
            palpite_temp[i] = None
            
    for i in range(4):
        if palpite_temp[i] is not None:
            if palpite_temp[i] in senha_temp:
                lugar_errado += 1
                senha_temp[senha_temp.index(palpite_temp[i])] = None

    resultado = f"Tentativa {st.session_state.tentativas}: {' '.join(palpite)} ➡️ {lugar_certo} no lugar certo | {lugar_errado} no lugar errado"
    st.session_state.historico.insert(0, resultado)

    if lugar_certo == 4:
        st.balloons()
        st.success(f" Parabéns! Você acertou a senha em {st.session_state.tentativas} tentativas!")

st.divider()
col_reset, col_desistir = st.columns(2)

with col_reset:
    if st.button("🔄 Reiniciar Jogo", use_container_width=True):
        # Sorteia uma nova senha e limpa o histórico
        st.session_state.senha = random.sample(CORES, k=4)
        st.session_state.historico = []
        st.session_state.tentativas = 0
        st.rerun()  # Recarrega a página com o novo estado

with col_desistir:
    if st.button("🏳️ Desistir", use_container_width=True):
        senha_revelada = " ".join(st.session_state.senha)
        st.warning(f"Você desistiu! A senha secreta era: **{senha_revelada}**")

st.divider()
st.subheader("Histórico de Palpites:")
for registro in st.session_state.historico:
    st.write(registro)
