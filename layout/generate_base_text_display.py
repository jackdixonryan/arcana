import textwrap

# "╔════════════════════════════════════╗"
# "║ seedy dock worker                  ║"
# "╟────────────────────────────────────╢"
# "║ "I'm trying to work here!          ║"
# "║                                    ║"
# "║                                    ║"
# "╚════════════════════════════════════╝"

# "╔════════════════════════════════════╗"
# "║ crate                              ║"
# "╟────────────────────────────────────╢"
# "║ I guess you could move this...     ║"
# "║                                    ║"
# "║                                    ║"
# "╚════════════════════════════════════╝"

def generate_dialog_box(title, body):
    space_length = 35
    title_length = len(title)
    difference = space_length - title_length
    title_row_content = title.title() + " " * difference
    title_row = "║ " + title_row_content + " ║"

    top_row = "╔═" + "═" * space_length + "═╗"
    divider_row = "╟─" + "─" * space_length + "─╢"

    body_length = len(body)
    # exceeds box size. Need to split across multiple boxes.
    if body_length > 35 * 6:
        return False
    else:
        body_array = body.split(" ")
        body = line_split(body_array)
        # take the split lines and create a body around them.

    bottom_row = "╚═" + "═" * space_length + "═╝"

    dialog_box_array = [
        top_row,
        title_row,
        divider_row,
        body,
        bottom_row
    ]

    dialog_box = '\n'.join(dialog_box_array)
    return dialog_box


def line_split(array):
    # why? cuz.
    line_length = 38

    # needs to take an array and chunk it by words so
    # the message will line split without cutting words
    # in half.

    lines = []
    new_line = ["║"]
    for word in array:
        word_length = len(word)
        current_line_length = len(" ".join(new_line))
        # if adding the current word to the line doesn't overload the line length, add the word
        if current_line_length + word_length < line_length:
            new_line.append(word)
        # otherwise, get the new line into the lines list
        # and frag the new line array.
        else:
            as_string = " ".join(new_line)
            print(len(as_string))
            if len(as_string) < line_length:
                difference = line_length - len(as_string)
                as_string += " " * difference + "║"
            lines.append(as_string)
            new_line.clear()
            new_line.append("║")
            new_line.append(word)
    # if the final line failed to meet the len requirement, make sure it's also included in the return.
    if len(new_line) > 0:
        as_string = " ".join(new_line)
        if len(as_string) < line_length:
            difference = line_length - len(as_string)
            as_string += " " * difference + "║"
        lines.append(as_string)

    if len(lines) <= 6:
        whitespace_required = 6 - len(lines)
        text_content = "\n".join(lines)
        text_content += "\n║                                     ║" * whitespace_required
        return text_content
    else:
        return "Too long error"

