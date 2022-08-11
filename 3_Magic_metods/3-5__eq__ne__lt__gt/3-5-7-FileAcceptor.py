class FileAcceptor:
    def __init__(self, *args):
        self.lst_file_ext = list(args)

    def __call__(self, filename, *args, **kwargs):
        return filename.split('.')[-1] in self.lst_file_ext

    def __add__(self, other):
        lst = [ls for ls in other.lst_file_ext if ls not in self.lst_file_ext]
        for st in lst:
            self.lst_file_ext.append(st)
        return FileAcceptor(*self.lst_file_ext)


filenames = ["boat.jpg", "ans.web.png", "text.txt1", "www.python.doc", "my.ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.xls"]
acceptor_images = FileAcceptor("jpg", "jpeg", "png")
acceptor_docs = FileAcceptor("txt", "doc", "xls")
w=acceptor_images + acceptor_docs

filenames = list(filter(acceptor_images + acceptor_docs, filenames))
print(filenames)