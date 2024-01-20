import os.path
import cherrypy
import json

class Api:
    def __init__(self):
        self.read_data()

    @cherrypy.expose
    def index(self, data=None):
        if data == 'chat':
            try:
                call_data = self.print_data()
                return f""" 
                    <title>GET /?data={data}</title>
                    <link rel="shortcut icon" href="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Morning_Star_flag.svg/1920px-Morning_Star_flag.svg.png" type="image/x-icon">
                    <script src="https://cdn.jsdelivr.net/npm/json-viewer-js@1.0.8/lib/json-viewer.min.js"></script>
                    <link href="https://cdnjs.cloudflare.com/ajax/libs/jquery-jsonview/1.2.3/jquery.jsonview.css" rel="stylesheet">
                    <body style="font-family: monospace, monospace;" class="jsonview">
                    <div id="json">{call_data}</div>
                    <script>
                        var data = {call_data};
                        document.getElementById('json').appendChild(jsonViewer(data, {{collapsed: false}}));
                    </script>
                    </body>
                    """
            except Exception as e:
                return """ 
                    <title>Error</title>
                    <link rel="shortcut icon" href="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Morning_Star_flag.svg/1920px-Morning_Star_flag.svg.png" type="image/x-icon">
                    <body style="font-family: monospace, monospace;">
                    <p> Can't Read JSON File: {0}</p>
                    </body>
                    """.format(e)
        elif data:
            return f""" 
            <title>Error GET /?data={data}</title>
            <link rel="shortcut icon" href="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Morning_Star_flag.svg/1920px-Morning_Star_flag.svg.png" type="image/x-icon">
            <body style="font-family: monospace, monospace;">
            <p> Cannot GET /?data={data} </p>
            </body>
            """
        else:
            return """ 
            <title>Error</title>
            <link rel="shortcut icon" href="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Morning_Star_flag.svg/1920px-Morning_Star_flag.svg.png" type="image/x-icon">
            <body style="font-family: monospace, monospace;">
            <p> Cannot GET / </p>
            </body>
            """

    def print_data(self):
        return json.dumps(self.data, indent=2)

    def read_data(self):
        try:
            with open("chat_data.json", "r") as file:
                self.data = json.load(file)
        except FileNotFoundError:
            self.data = []

if __name__ == '__main__':
    port = 8080
    host = '127.0.0.1'
    print(f"⚡ Your Api Running on {host}:{port}")
    cherrypy.config.update({'server.socket_host': host, 'server.socket_port': port})
    cherrypy.quickstart(Api())
