# extract Android contacts from vcf file
import sys


def read_file(contact_file):
    with open(contact_file, 'r') as raw_content:
        return raw_content.read()


def write_file(contact_file, content):
    with open(contact_file, 'w') as c:
        return c.write(content)


def extract(content):
    unnecessary_stuffs = [
        "VERSION:2.1",
        ";CELL",
        "N;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:;",
        "FN;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:",
        ";;;",
        "END:VCARD"]
    to_replace = "BEGIN:VCARD"

    for item in range(len(unnecessary_stuffs)):
        content = content.replace(unnecessary_stuffs[item], "")
        content = content.replace(to_replace, "---")
    return content


def main():
    try:
        origin_content = read_file(sys.argv[1])
        content = extract(origin_content)
        write_file("phone.txt", content)
        print('OK')
    except IndexError as e:
        print(e)
        sys.exit()


main()
