

class CsvReader(object):

    def __init__(self, file, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.filename = file
        self.sep = sep
        self.header = header
        self.skip_bottom = skip_bottom
        self.skip_top = skip_top

    def __enter__(self):
        self.file = open(self.filename)
        if self.file is None:
            return None
        self.lines = self.file.readlines()
        first_data = self.skip_top
        if self.header:
            first_data += 1
        last_data = len(self.lines) - self.skip_bottom
        self.data = []
        maxlen = len(self.getheader())
        for i in range(first_data, last_data):
            for elems in self.lines[i].split(self.sep):
                if len(elems) < maxlen:
                    return None
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        self.file.close()

    def getdata(self):
        first_data = self.skip_top + 1
        if self.header:
            first_data += 1
        last_data = len(self.lines) - self.skip_bottom
        self.data = []
        for i in range(first_data, last_data):
            self.data.append(self.lines[i].split(self.sep))
        for y, each in enumerate(self.data):
            for x, each in enumerate(self.data[y]):
                self.data[y][x] = self.data[y][x].replace('\'', '') \
                    .replace('\"', '').strip()
        return self.data

    def getheader(self):
        if self.header:
            header = self.lines[0]
        else:
            header = self.lines[self.skip_top]
        header = header.rstrip("\n\r").split(self.sep)
        for i, value in enumerate(header):
            header[i] = value.replace('\"', '').replace('\'', '').strip()
        return header
