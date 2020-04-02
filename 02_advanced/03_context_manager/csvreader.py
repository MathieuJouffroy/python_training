class CsvReader():
    def __init__(self, filename, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.filename = filename
        #self.file = None
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
    
    def __enter__(self):
        try:
            self.file = open(self.filename, 'r')
            tmp = open(self.filename, 'r')
            head_len = len(tmp.readline().split(sep=self.sep))
            nb_lines = 1
            for line in tmp:
                line_lst = line.rstrip('\n\r').split(sep = self.sep)
                data_len = len([x for x in line_lst if x != ''])
                nb_lines += 1
                if data_len != head_len:
                    self.file = None
                    return self.file
            if self.header is True:
                next(self.file)
            if self.skip_top != 0:
                if self.skip_top < nb_lines:
                    for top in range(0, self.skip_top):
                        next(self.file)
                else:
                    print(f"Could not skip {self.skip_top} from top : exceeds file size")
        except OSError as error:
            print(f"{error}\nCould not open file {str(self)}")
            self.file = None
        return self
    
    def __exit__(self, type, value, traceback):
        if self.file:
            if not self.file.closed:
                self.file.close()

    def getheader(self):
        try:
            f = open(self.filename, 'r')
            head = f.readline().split(sep=self.sep)
            head[len(head) - 1] = head[len(head) - 1].replace("\n", "")
        except OSError as error:
            print(f"{error}\nCould not open file {str(self)}")
            head = None
        return head

    def getdata(self):
        data = []
        nb_lines = 1
        try:
            for line in self.file:
                data.append(list(line.rstrip('\n\r').split(sep = self.sep)))
                nb_lines += 1
            if self.skip_bottom != 0:
                if self.skip_bottom < nb_lines :
                    data_len = len(data) - self.skip_bottom
                    data = data[:data_len]
                else:
                    print(f"Could not skip {self.skip_bottom} from bottom : exceeds file size")
        except OSError as error:
            print(f"{error}\nCould not open file {str(self)}")
            data = None
        return data



print("--- Good --")
with CsvReader("good.csv", ',', False, 1, 19) as reader:
    if reader == None:
        print("File corrupted!")
    else:
        print(f"Header:\n{reader.getheader()}\n\nData:")
        for val in reader.getdata():
            print(val)
            
print("\n--- Bad ---")
with CsvReader("bad.csv", ',', False, 1) as reader:
    if reader == None:
        print("File corrupted!")
    else:
        print(f"Header:\n{reader.getheader()}\nData:")
        for val in reader.getdata():
            print(val)