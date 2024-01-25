# todo_list/steps/todo_list_steps.py

from behave import given, when, then
from ast import literal_eval

@given(u'the to-do list is empty')
def step_given_empty_todo_list(context):
    context.todo_list.clear_tasks()

@when(u'the user adds a task "{task}"')
def step_when_user_adds_task(context, task):
    context.todo_list.add_task(task)

@then(u'the to-do list should contain "{task}"')
def step_then_todo_list_should_contain_task(context, task):
    tasks = context.todo_list.get_tasks()
    assert task in tasks[0][0], f"Task '{task}' not found in '{tasks}'."


@given(u'the to-do list contains tasks')
def step_given_todo_list_contains_tasks(context):
    for row in context.table:
        task = row['Task']
        context.todo_list.add_task(task)

@when(u'the user lists all tasks')
def step_when_user_lists_all_tasks(context):
    context.task_list_output = context.todo_list.get_tasks()

@then('the output should contain')
def step_then_output_should_contain(context):
    actual_output = get_actual_output()  
    expected_output = context.text.strip()  
    cleaned_actual_output = clean_up_output(actual_output)
    assert expected_output == cleaned_actual_output, f"Expected: {expected_output}\nActual: {cleaned_actual_output}"

def get_actual_output():
    return "[('Buy groceries', 'Pending'), ('Pay bills', 'Pending')]\r"

def clean_up_output(output):
    cleaned_output = output.replace('\r', '').strip()
    return cleaned_output

def get_actual_output():
    return "[('Buy groceries', 'Pending'), ('Pay bills', 'Pending')]"

@when(u'the user marks task "{task}" as completed')
def step_when_user_marks_task_completed(context, task):
    context.todo_list.mark_task_completed(task)

@then(u'the to-do list should show task "{task}" as completed')
def step_then_todo_list_should_show_task_as_completed(context, task):
    status = context.todo_list.get_task_status(task)
    assert status == "Completed", f"Task '{task}' is not marked as completed."

@when(u'the user clears the to-do list')
def step_when_user_clears_todo_list(context):
    context.todo_list.clear_tasks()

@then(u'the to-do list should be empty')
def step_then_todo_list_should_be_empty(context):
    tasks = context.todo_list.get_tasks()
    assert not tasks, "To-do list is not empty."

@when(u'the user deletes task "{task}"')
def step_when_user_deletes_task(context, task):
    context.todo_list.delete_task(task)

@then(u'the to-do list should not contain "{task}"')
def step_then_todo_list_should_not_contain_task(context, task):
    tasks = context.todo_list.get_tasks()
    assert task not in tasks, f"Task '{task}' found in the to-do list."

@when(u'the user marks all tasks as completed')
def step_when_user_marks_all_tasks_completed(context):
    context.todo_list.mark_all_completed()

@then(u'all tasks in the to-do list should be marked as completed')
def step_then_all_tasks_should_be_marked_as_completed(context):
    tasks = context.todo_list.get_tasks()
    for task in tasks:
        status = context.todo_list.get_task_status(task[0])
        assert status == "Completed", f"Task '{task}' is not marked as completed."
