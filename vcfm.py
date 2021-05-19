# extract Android contacts from vcf file
import sys


def read_file(contact_file):
    with open(contact_file, 'r') as raw_content:
        return raw_content.read()


def write_file(contact_file, content):
    with open(contact_file, 'w') as c:
        return c.write(str(content))


def cont_repl(value, content, value2):
    for item in range(len(value)):
        content = content.replace(value[item], "")
        content = content.replace(value2, "---")
    return content


def extract(content):
    unnecessary_stuffs = [
        "VERSION:2.1",
        ";CELL",
        "N;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:;",
        "FN;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:",
        ";;;",
        "END:VCARD"]
    to_replace = "BEGIN:VCARD"
    content = cont_repl(unnecessary_stuffs, content, to_replace)
    return content


def control_extension(value):
    if value.lower().endswith('.vcf'):
        return True
    else:
        return False


def main():
    try:
        if control_extension(sys.argv[1]) is True:
            origin_content = read_file(sys.argv[1])
            write_file("phone.txt", extract(origin_content))
            print('OK')
        else:
            print('Argument is not valid file')
            sys.exit()
    except (IndexError, FileNotFoundError) as e:
        print(e)


main()
