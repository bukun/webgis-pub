from pathlib import Path

inws = Path('webgis-rst/webgis-src/part2')

for wfile in inws.rglob('*.rst'):
    print(wfile)
    cnts = open(wfile).readlines()
    for cnt in cnts:
        cnt = cnt.strip()
        if cnt.startswith('.. literal'):
            file_name = cnt.split('/')[-1]
            print(file_name)
            raw_file = wfile.parent.parent / file_name
            dst_file = wfile.parent / file_name
            if raw_file.exists():
                dst_file.write_text(raw_file.read_text())
