import sys

obj = {
    '${INCDIR_PREFIX}' : "-I",
    '$(APPDIR)' : '/home/gyl/work2/vela/n620314/apps',
    '${APPDIR}' : '/home/gyl/work2/vela/n620314/apps',
    # 'QAPPDIR' : '{APPDIR}/frameworks/quickapp'
    '$(CONFIG_QUICKAPP_LOG_LEVEL)': '3'
}

def main(filename):
    def replace(s):
        for a, b in obj.items():
            s = s.replace(a, b)
        return s

    with open(filename, "r") as f:
        x = [ s for s in f.readlines() if s.strip().startswith("CXXFLAGS")]
        x = [ s.split("+=")[1].strip() for s in x]
        x = [replace(s) for s in x]
        x.sort()
        x.reverse()
        for y in x:
            print(y)


if __name__ == "__main__":
    main(sys.argv[1])
