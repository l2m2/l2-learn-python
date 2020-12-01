'''
@File: gen-qdoc.py
@Description: Gen qdoc classes comment
@Author: leon.li(l2m2lq@gmail.com)
@Date: 2020-07-28 15:10:26
'''

import os, glob, re

module = 'topdfm'

fixup = r"""
/*!
 * \class {cls}
 * \inmodule {module}
 */

"""

def gen(path):
    cpps = [y for x in os.walk(path) for y in glob.glob(os.path.join(x[0], '*.cpp'))]
    for cpp in cpps:
        with open(cpp, 'r+', encoding = 'utf-8-sig') as fd:
            code = fd.read()
            if re.search("thread.cpp$", cpp): continue
            if not r"\class" in code:
                lines = code.splitlines()
                pos = next(i for i,v in enumerate(lines) if v != '' and not re.search("^#include", v))
                classes = set([ re.match(r'^(\w+)::(\1)', line).group(1) for line in lines if re.search(r'^(\w+)::(\1)', line) ])
                if len(classes) == 0: continue
                print(cpp, classes)
                for cls in classes:
                    temp = fixup.format(cls=cls, module=module)
                    lines[pos:pos] = temp.splitlines()
                fd.seek(0)
                fd.truncate()
                fd.write('\n'.join(lines))

if __name__ == "__main__":
    gen(r"F:\workspace\toplinker\gitlab\topikm6\topikm6-topwms\src\class\plugin")