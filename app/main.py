def copy_file(command):
    parts = command.split()

    # якщо команда порожня або неправильний формат (немає 3 частин)
    if len(parts) != 3:
        return

    # якщо перше слово не "cp"
    if parts[0] != "cp":
        return

    # якщо файл не існує
    import os
    if not os.path.exists(parts[1]):
        return

    # якщо імена однакові
    if parts[1] == parts[2]:
        return

    with open(parts[1], "r") as file_in, open(parts[2], "w") as file_out:
        content = file_in.read()
        file_out.write(content)
