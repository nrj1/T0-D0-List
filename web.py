import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo_local = st.session_state["new_todo"] + "\n"
    todos.append(todo_local)
    functions.write_todos(todos)



st.title("TO-DO LIST")
st.subheader("Created by NRJ_2001")
st.write("A web app to keep a list of day to day activities that need to be completed at the earliest!!")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

added_task = st.text_input(label="", placeholder="Add a new todo...", on_change=add_todo, key="new_todo")




