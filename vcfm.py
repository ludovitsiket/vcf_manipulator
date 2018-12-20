# extract Android contacts from vcf file
import sys

def read_file(contact_file):
    with open(contact_file, 'r') as raw_content:
        content = raw_content.read()
    return content

def extract(content):
    unnecessary_stuffs = ["VERSION:2.1", ";CELL",
            "N;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:;",
            "FN;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:", ";;;", "END:VCARD"]
    to_replace = "BEGIN:VCARD"
    
    for item in range(len(unnecessary_stuffs)):
        content = content.replace(unnecessary_stuffs[item], "")
        content = content.replace(to_replace, "---")
    return content

def main():
    kontakty = sys.argv[1]
    origin_content = read_file(kontakty)
    content = extract(origin_content)
    print(content)

main()

