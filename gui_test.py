from guizero import App, Text, TextBox, PushButton

def say_my_name():
    welcome_message.value = f"Hello, {my_name.value}"

app = App(title="Hello world", bg = "blue")

welcome_message = Text(app, text="Welcome to my app", size=40, font="Sans Serif", color="#555555")

my_name = TextBox(app, width="50")

update_text = PushButton(app, command=say_my_name, text="Submit")
update_text.text_color = "#000000"
update_text.bg = "red"

app.display()
