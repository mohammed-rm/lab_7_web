import http.server

if __name__ == "__main__":
    PORT = 8000
    server_address = ("", PORT)

    server = http.server.HTTPServer
    handler = http.server.CGIHTTPRequestHandler
    handler.cgi_directories = ["/"]
    print(f"Serveur actif sur le port {PORT}")

    httpd = server(server_address, handler)
    httpd.serve_forever()
