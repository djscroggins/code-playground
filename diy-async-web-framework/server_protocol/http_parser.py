class HttpParserMixin:
    def on_body(self, data):
        self._body = data

    def on_url(self, url):
        self._url = url

    def on_message_complete(self):
        print(f"Received request to {self._url.decode(self._encoding)}")

    def on_header(self, header, value):
        header = header.decode(self._encoding)
        self._headers[header] = value.decode(self._encoding)