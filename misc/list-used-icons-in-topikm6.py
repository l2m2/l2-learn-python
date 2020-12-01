import glob, os, re, json, pathlib

root_dir = r"F:\workspace\toplinker\gitlab\topikm6"
# root_dir = r"F:\workspace\toplinker\gitlab\topikm6\topikm6-pubbasic\src\module\PUBBASIC\pub-ui-form-conf\actions"
# root_dir = r"F:\workspace\toplinker\gitlab\topikm6\topdfm\src\class\toppdm\src\pdmjobmain"
# root_dir = r"F:\workspace\toplinker\gitlab\topikm6\topdfm\src\class\toppdm\src\pdmadvquerymgt"
# root_dir = r"F:\workspace\toplinker\gitlab\topikm6\topdfm\src\class\toppdmlib\src\pdmpanelizer"
# root_dir = r"F:\workspace\toplinker\gitlab\topikm6\topikm6-sysadmin\src\module\DEMO"
resource_dir=r"F:\workspace\toplinker\gitlab\topikm6\topikm6-resource\src\res\icon"

def used_icons():
    icons = set() 
    files = [y for x in os.walk(root_dir) for y in  glob.glob(os.path.join(x[0], '*.cpp')) 
        + glob.glob(os.path.join(x[0], '*.js')) 
        + glob.glob(os.path.join(x[0], '*.xml'))
        + glob.glob(os.path.join(x[0], 'module.conf'))]
    print("Number of files: ", len(files))
    for f in files:
        # print(f"Searching {f}")
        with open(f, 'r', encoding = 'latin-1') as fd:
            code = fd.read()
            lines = code.splitlines()
            line_icons = [ x for line in lines if re.search(r'^ICON:\s*"(\S+)"', line) for x in re.findall(r'^ICON:\s*"(\S+)"', line)]
            icons.update(line_icons)
            # print("Action.js: ", line_icons)
            line_icons = [ x for line in lines if re.search(r'TRES->(?:i|colorI)con\("(\S+)"\)', line) for x in re.findall(r'TRES->(?:i|colorI)con\("(\S+)"\)', line)]
            icons.update(line_icons)
            # print("*.cpp: ", line_icons)
            line_icons = [ x for line in lines if re.search(r'<icon>(\S+)</icon>', line) for x in re.findall(r'<icon>(\S+)</icon>', line)]
            icons.update(line_icons)
            # print("*.xml: ", line_icons)
            line_icons = [ x for line in lines if re.search(r'^sys_icon:\s*"(\S+)"', line) for x in re.findall(r'^sys_icon:\s*"(\S+)"', line)]
            icons.update(line_icons)
            # print("module.conf: ", line_icons)
            line_icons = [ x for line in lines if re.search(r'"icon":\s*"(\S+)"', line) for x in re.findall(r'"icon":\s*"(\S+)"', line)]
            icons.update(line_icons)
            # print("module.conf desktop: ", line_icons)
    return icons

def transform(icons: set):
    icons = list(set([ x.split('.')[0] for x in icons]))
    return icons

def icons_in_resource():
    return [os.path.splitext(os.path.basename(y))[0] for x in os.walk(resource_dir) for y in glob.glob(os.path.join(x[0], '*.svg'))]

def remove_not_used(icons):
    for icon in icons:
        pathlib.Path(f'{resource_dir}/{icon}.svg').unlink()

def move_not_used(icons):
    dist_dir = "F:/not_used"
    pathlib.Path(dist_dir).mkdir(parents=True, exist_ok=True)
    for icon in icons:
        pathlib.Path(f'{resource_dir}/{icon}.svg').rename(f'{dist_dir}/{icon}.svg')

if __name__ == "__main__":
    # Used icons
    icons1 = used_icons()
    print("Number of icons : ", len(icons1))
    icons1 = transform(icons1)
    print("Number of icons after transform: ", len(icons1))
    # Icons in res
    icons2 = icons_in_resource()
    print("Number of icons in resource : ", len(icons2))
    # Not used icons
    icons3 =  [ x for x in icons2 if x not in icons1]
    icons3.sort()
    # print(icons3)
    print("Number of not used : ", len(icons3))
    with open("output.json", 'w') as fd:
        json.dump(icons3, fd)
    move_not_used(icons3)