tasks = []
task_list = Element("items")
todo_input = Element("todo_input")
template = Element("task-template").select(".task", from_content=True)
error = Element("error")

def add_todo(*args):
    todo_text = todo_input.element.value    
    if todo_text:
        error.element.innerHTML = ""
        todo_id = f"todo-{len(tasks)}"
        todo = {
            "id": todo_id,
            "text": todo_text,
            "done": False,
        }

        tasks.append(todo)

        task_html = template.clone(todo_id, to=task_list)
        task_html_content = task_html.select("p")
        task_html_content.element.innerText = todo["text"]
        task_html_checkbox = task_html.select("input")
        task_list.element.appendChild(task_html.element)
        todo_input.clear()

        def check_task(event = None):
            todo["done"] = True
            task_html_checkbox.element.checked = todo["done"]
            task_html_content.element.style.setProperty("text-decoration", "line-through")
            task_html_checkbox.element.disabled = True

        task_html_checkbox.element.onclick = check_task
    else:
        error.element.innerText = "Please enter a task"