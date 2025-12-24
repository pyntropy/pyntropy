class Step:
    title: str
    content: str

    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content


    def __str__(self):
        return self.title + "\n" + self.content