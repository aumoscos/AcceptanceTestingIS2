from behave import given, when, then
import sys
sys.path.append(r'C:\Users\andre\Documents\GitHub\AcceptanceTestingIS2')  # Adjust the path accordingly

from todo_list.app import TodoList




@given('the to-do list is empty')
def step_empty_todo_list(context):
    context.todo_list = TodoList()

@when('the user adds a task "{task}"')
def step_add_task(context, task):
    context.todo_list.add_task(task)

@then('the to-do list should contain "{task}"')
def step_check_task(context, task):
    assert task in context.todo_list.list_tasks()

@given('the to-do list contains tasks:')
def step_populate_todo_list(context):
    context.todo_list = TodoList()
    for row in context.table:
        context.todo_list.add_task(row['Task'])

@when('the user lists all tasks')
def step_list_all_tasks(context):
    context.list_output = context.todo_list.list_tasks()

@then('the output should contain:')
def step_check_list_output(context):
    expected_output = context.text.strip()
    actual_output = '\n'.join(context.list_output)
    assert expected_output == actual_output

@when('the user marks task "{task}" as completed')
def step_mark_completed(context, task):
    context.todo_list.mark_as_completed(task)

@then('the to-do list should show task "{task}" as completed')
def step_check_completed(context, task):
    for t in context.todo_list.tasks:
        if t["name"] == task:
            assert t["status"] == "Completed"

@when('the user clears the to-do list')
def step_clear_list(context):
    context.todo_list.clear_tasks()

@when('the user deletes task "{task}"')
def step_delete_task(context, task):
    context.todo_list.delete_task(task)

@then('the to-do list should not contain "{task}"')
def step_check_deleted_task(context, task):
    assert task not in context.todo_list.list_tasks()

@when('the user marks all tasks as completed')
def step_mark_all_completed(context):
    context.todo_list.mark_all_completed()

@then('all tasks in the to-do list should be marked as completed')
def step_check_all_completed(context):
    for t in context.todo_list.tasks:
        assert t["status"] == "Completed"
