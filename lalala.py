import PySimpleGUI as sg


def generate_email(name):
    email = name.lower().replace(" ", ".") + "@uncc.edu"
    return email


def main():
    email_list = []

    layout = [
        [sg.Text("Enter student's name:")],
        [sg.InputText(key="-NAME-")],
        [sg.Button("Generate Email"), sg.Button("Quit")],
        [sg.Text(size=(40, 1), key="-OUTPUT-")],
        [sg.Listbox(values=email_list, size=(40, 10), key="-LISTBOX-")],
    ]

    window = sg.Window("UNC Charlotte Student Email Generator", layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == "Quit":
            break

        if event == "Generate Email":
            name = values["-NAME-"]
            email = generate_email(name)
            email_list.append(email)

            window["-OUTPUT-"].update(f"Generated email address: {email}")
            window["-LISTBOX-"].update(values=email_list)

    window.close()


if __name__ == "__main__":
    main()