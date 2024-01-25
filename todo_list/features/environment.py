# features/environment.py

from todo_list.app import TodoList

def before_scenario(context, scenario):
    context.todo_list = TodoList()

def after_scenario(context, scenario):
    del context.todo_list
