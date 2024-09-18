def delete_html_tags(html_file, result_file='cleaned.txt'):
    with open(html_file, encoding='utf-8') as file:
        input_data = file.readlines()

    output_data = []
    for line in input_data:
        line = line.strip('\n').strip()
        if line:
            new_line = ''
            tag = False
            for symbol in line:
                if symbol == '<':
                    tag = True
                    continue
                if symbol == '>':
                    tag = False
                    continue
                if tag is False:
                    new_line += symbol

            if new_line:
                output_data.append(new_line)

    with open(result_file, 'w', encoding='utf-8') as file:
        file.write('\n'.join(output_data))


delete_html_tags('draft.html')

