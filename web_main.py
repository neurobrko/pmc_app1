import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    st.session_state.new_todo = ""
    todos.append(todo)
    functions.write_todos(todos)


def complete_todo():
    pass


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, on_change=complete_todo, key=index)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[index]
        st.rerun()

st.text_input(
    label="New Todo",
    label_visibility="hidden",
    placeholder="Add new todo...",
    on_change=add_todo,
    key="new_todo",
)

st.session_state
