import html
import json
import os
import socket
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


class AppHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            body = json.dumps({"status": "ok"}).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return

        if self.path != "/":
            body = b"Not found\n"
            self.send_response(404)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return

        hostname = html.escape(socket.gethostname())
        page = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Project 08 | Docker App</title>
  <style>
    :root {{ color-scheme: light; font-family: system-ui, sans-serif; }}
    body {{ margin: 0; min-height: 100vh; display: grid; place-items: center;
           background: #f1f5f9; color: #172033; }}
    main {{ max-width: 38rem; margin: 1.5rem; padding: 2.5rem; border-radius: 1rem;
            background: white; box-shadow: 0 1rem 3rem #17203318; }}
    .badge {{ display: inline-block; padding: .35rem .7rem; border-radius: 999px;
              background: #dcfce7; color: #166534; font-weight: 700; }}
    h1 {{ margin-bottom: .5rem; }}
    code {{ padding: .2rem .4rem; border-radius: .3rem; background: #f1f5f9; }}
  </style>
</head>
<body>
  <main>
    <span class="badge">App is running</span>
    <h1>Project 08: Docker App</h1>
    <p>This web app is ready to run locally in a Docker container.</p>
    <p>Container hostname: <code>{hostname}</code></p>
    <p>Health check: <code>/health</code></p>
  </main>
</body>
</html>
"""
        body = page.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format_string, *args):
        print("%s - %s" % (self.address_string(), format_string % args))


def main():
    port = int(os.environ.get("PORT", "8000"))
    server = ThreadingHTTPServer(("0.0.0.0", port), AppHandler)
    print("Serving Project 08 on port %s" % port)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
