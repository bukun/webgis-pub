from pathlib import Path

def chuli_a():
    inws = Path('webgis-rst/webgis-src')
    outws = Path('_pub/xx_rst')
    if outws.exists():
        pass
    else:
        outws.mkdir()

    for wfile in inws.rglob('*'):
        if wfile.name == 'index.rst':
            dst = outws / 'index.rst'

            cnts = open(wfile).readlines()
            with open(dst,'w') as fo:
                for cnt in cnts:
                    cnt_strip = cnt.strip()
                    if cnt_strip.startswith('part') and cnt_strip.endswith('part'):
                        sig = cnt_strip.split('/')[0].split('_')[-1]
                        print(sig)
                        fo.write(f'   {sig}\n'.lower())
                    else:
                        fo.write(cnt)

        elif wfile.name == 'part.rst':
            dst = outws / (wfile.parent.name.split('_')[-1] + '.rst').lower()

            cnts = open(wfile).readlines()
            with open(dst,'w') as fo:
                for cnt in cnts:
                    cnt_strip = cnt.strip()
                    if cnt_strip.startswith('ch') and cnt_strip.endswith('chapter'):
                        sig = cnt_strip.split('/')[0].split('_')[-1]
                        # print(sig)
                        fo.write(f'   {sig}\n'.lower())
                    else:
                        fo.write(cnt)
        elif wfile.name == 'chapter.rst':
            dst = outws / ( wfile.parent.name.split('_')[-1] + '.rst').lower()
            cnts = open(wfile).readlines()
            with open(dst,'w') as fo:
                for cnt in cnts:
                    cnt_strip = cnt.strip()
                    if cnt_strip.startswith('sec') and cnt_strip.endswith('section'):
                        sig = wfile.parent.name.split('_')[-1] + '-' + cnt_strip.split('/')[0].split('_')[-1]
                        # print(sig)
                        fo.write(f'   {sig}\n'.lower())
                    else:
                        fo.write(cnt)

        elif wfile.name == 'section.rst':
            dst = outws / (wfile.parent.parent.name.split('_')[-1] + '-' + wfile.parent.name.split('_')[-1] + '.rst').lower()

            dst.write_text(wfile.read_text())
        elif wfile.is_file():
            dst = outws / wfile.name
            dst.write_bytes(wfile.read_bytes())
        else:
            pass
def chuli_b():
    inws = Path('webgis-rst/webgis-src/_static')
    outws = Path('_pub/xx_rst/_static')
    if outws.exists():
        pass
    else:
        outws.mkdir()

    for wfile in inws.rglob('*'):
        if wfile.is_file():
            dst = outws / wfile.name
            dst.write_bytes(wfile.read_bytes())
        else:
            pass

if __name__ == '__main__':
    chuli_a()
    chuli_b()
