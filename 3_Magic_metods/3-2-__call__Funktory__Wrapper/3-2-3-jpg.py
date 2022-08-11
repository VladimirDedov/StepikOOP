class ImageFileAcceptor:
    def __init__(self, extensions):
        self.extensions=extensions

    def __call__(self, *args, **kwargs):
        lst=[]
        if args[0].split('.')[1] in self.extensions:
            lst.append(args[0])
        return lst

filenames = ["boat.jpg", "web.bmp", "text.txt", "python.doc", "ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.png"]
acceptor = ImageFileAcceptor(('jpg', 'bmp', 'jpeg'))
print(acceptor.extensions)
image_filenames = filter(acceptor, filenames)
print(list(image_filenames))  # ["boat.jpg", "ava.jpg", "forest.jpeg"]