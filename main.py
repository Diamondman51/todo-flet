import flet as ft

def main(page: ft.Page):
    page.title = "To-Do App"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.AUTO

    # Task List
    task_list = ft.Column()

    # Function to Add Task
    def add_task(e):
        if task_input.value.strip():
            task_item = ft.Row(
                controls=[
                    ft.Checkbox(label=task_input.value, on_change=update_task),
                    ft.IconButton(icon=ft.icons.DELETE, on_click=lambda e: remove_task(task_item)),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            )
            task_list.controls.append(task_item)
            task_input.value = ''
            page.update()

    # Function to Remove Task
    def remove_task(task_item):
        task_list.controls.remove(task_item)
        page.update()

    # Function to Update Task Status
    def update_task(e):
        checkbox = e.control
        if checkbox.value:  # Task marked as complete
            checkbox.label = f"[DONE] {checkbox.label}"
        else:  # Task marked as incomplete
            checkbox.label = checkbox.label.replace("[DONE] ", "")
        page.update()

    # Input Field and Add Button
    task_input = ft.TextField(hint_text="Enter a new task", width=300)
    add_button = ft.FloatingActionButton(icon=ft.icons.ADD, on_click=add_task)

    # Main Layout
    page.add(
        ft.Column(
            controls=[
                ft.Text("To-Do App", style="headlineLarge"),
                ft.Row([task_input, add_button]),
                task_list,
            ],
            alignment=ft.MainAxisAlignment.START,
            spacing=20
        )
    )

# Run the App
ft.app(target=main, view=ft.WEB_BROWSER)
