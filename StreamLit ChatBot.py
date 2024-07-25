import streamlit as st

# with st.chat_message(name="user",avatar="😊"): # name = "assistant" for bot icon
#     st.write("Hello")


st.title("Chat Bot")

# Initialize Chat history
if 'messages' not in st.session_state:
    #session state keep record of data between user and bot
    st.session_state.messages = []
    # it will contain dictionaries like below

    # messages = [ {"role": "user", "content": "Our Prompt"}, {"role": "assistant", "content": "The Response"},...]

# Dispaly chat msgs from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

# Ouputs same as input


# React to user input
prompt = st.chat_input("Whats up")
if prompt:
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
        # Add user message to chat history
    st.session_state.messages.append({"role":"user","content":prompt})

    # Now for the response
    response = f"Echo : {prompt}"

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state.messages.append({'role':"assistant","content":response})