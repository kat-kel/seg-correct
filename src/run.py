import re
import click
import os

from lxml import etree

NS = {'a':"http://www.loc.gov/standards/alto/ns-v4#"}  # namespace for the Alto xml

@click.command()
@click.option('--log', default=None, prompt='Path to the GitHub Action log folder downloaded on your machine')
@click.option('--data', default=None, prompt='Path to the directory which contains the files the GitHub Action processed')
def main(log, data):
    print("=======================")
    print(f"-----> parsing HTRVX/5_Run HTRVX.txt in {log}")
    file_path = os.path.join(log, 'HTRVX', '5_Run HTRVX.txt')
    check ={}
    with open(file_path, "r") as f:
        reader = f.readlines()
        for count, line in enumerate(reader):
            if "empty zone(s)" in line:
                ansi_escape = re.compile(r'(?:\x1B[@-_]|[\x80-\x9F])[0-?]*[ -/]*[@-~]')
				# remove ansi code from log line
                line = ansi_escape.sub('', line)
				# list all empty zones named in the line
                zones = [z[1:] for z in re.split(r"[,\s+]", line) if z!='' and z[0]=="#"]
                doc_in_log = [d for d in re.split(r"\s|\:", reader[count-1]) if d!='' and d[:7]=="./data/"][0]
                doc_local = os.path.join(data, f"{doc_in_log[7:]}")
                check[doc_local] = zones
    retag = []
    print(f"-----> decoding TAGREF identifiers for documents in {data}")
    for doc, blocks in check.items():
        root = etree.parse(doc).getroot()  # get root of xml Etree
        ok_empty_names = ["DamageZone", "DropCapitalZone", "GraphicZone", "MusicZone", "SealZone", "StampZone", "TableZone"]
        ok_empty_id = []
        # get names of zones that should not be empty
        for name in ok_empty_names:
            if root.find(f'.//a:OtherTag[@LABEL="{name}"]', namespaces=NS) is not None:
                ok_empty_id.append(root.find(f'.//a:OtherTag[@LABEL="{name}"]', namespaces=NS).get("ID"))
        # check if empty zone is of a kind that should not be empty
        for block in blocks:
            tagref = root.find(f'.//a:TextBlock[@ID="{block}"]', namespaces=NS).get("TAGREFS")  # find the @TAGREF of TextBlock element with block ID
            if tagref == "BT":
                retag.append(f"document {doc}, TextBlock {block} is not properly tagged. The bad tag is {tagref}.\n\n")
            elif tagref not in ok_empty_id:
                tagname = root.find(f'.//a:OtherTag[@ID="{tagref}"]', namespaces=NS).get("LABEL")
                retag.append(f"Document {doc} | TextBlock {block} should not be empty. It is {tagname}.\n\n")
    print(f"-----> writing corrections.txt to your current directory: {os.path.abspath(os.path.curdir)}")
    with open("corrections.txt", "w") as f:
        f.writelines(retag)
    print("")


if __name__ == '__main__':
    main()