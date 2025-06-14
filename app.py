from dotenv import load_dotenv
load_dotenv()

import streamlit as st

st.title("LLMを使ったテストアプリ")

st.write("このアプリは、LLMを使ったテストアプリです。2種類の専門家を選択し、質問することができます。")
st.write("以下から質問したい専門家の種類を選択し、質問を入力して下さい")


selected_item = st.radio(
    "専門家の種類を選択して下さい",
    ["宇宙物理学の専門家", "株式投資の専門家"]
)

input_message = st.text_input(label="専門家への質問を入力してください。")

def get_expert_response(expert_type, question):
    from langchain_openai import ChatOpenAI
    from langchain.schema import SystemMessage, HumanMessage

    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=1)

    messages = [
        SystemMessage(content=f"あなたは{expert_type}です。あなたの専門知識を活かして、質問に答えてください。専門外の質問には、答えられないことを明確に伝えてください。"),
        HumanMessage(content=f"質問: {question}"),
    ]

    result = llm(messages)
    return result.content

if st.button("質問する"):
    if input_message:
        response = get_expert_response(selected_item, input_message)
        st.subheader("回答")
        st.write(f"**{selected_item}の回答:** {response}")
    else:
        st.warning("質問を入力してください。")