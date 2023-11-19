from html.parser import HTMLParser

class BookmarkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.bookmarks = []
        self.recording = 0
    
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            self.recording = 1
            self.bookmarks.append("<" + tag)
            for name, value in attrs:
                self.bookmarks[-1] += f' {name}="{value}"'
            self.bookmarks[-1] += ">"

    def handle_endtag(self, tag):
        if tag == 'a':
            self.recording = 0
            self.bookmarks[-1] += f"</{tag}>"

    def handle_data(self, data):
        if self.recording:
            self.bookmarks[-1] += data

def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(filename, bookmarks):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("<html><body>")
        for bookmark in bookmarks:
            f.write(bookmark)
            f.write("\n")
        f.write("</body></html>")

file1 = 'C:/Users/echo2/Desktop/brave_bookmarks.html'
file2 = 'C:/Users/echo2/Desktop/edge_bookmarks.html'
output_file = 'C:/Users/echo2/Desktop/merged_bookmarks.html'

brave_content = read_file(file1)
edge_content = read_file(file2)

brave_parser = BookmarkParser()
edge_parser = BookmarkParser()

brave_parser.feed(brave_content)
edge_parser.feed(edge_content)

merged_bookmarks = brave_parser.bookmarks + edge_parser.bookmarks

write_file(output_file, merged_bookmarks)

print(f"Merged bookmarks written to {output_file}")
