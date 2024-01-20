import cherrypy
import json

class CarApp:
    def __init__(self):
        with open('cars.json', 'r') as file:
            self.cars = json.load(file)
        self.editing_index = None

    @cherrypy.expose
    def index(self):
        return f"""
                <!doctype html>
                <html lang=id>
                <head>
                    <meta charset=UTF-8>
                    <meta name=viewport content="width=device-width,initial-scale=1">
                    <title>CRUD Mobil!</title>
                    <link rel="stylesheet" href="https://luthfiarian.my.id/task/style-cars.css">
                    <link rel=preconnect href=https://fonts.googleapis.com>
                    <link rel=preconnect href=https://fonts.gstatic.com crossorigin>
                    <link href="https://fonts.googleapis.com/css2?family=Montserrat+Alternates&display=swap" rel=stylesheet>
                    <link rel="shortcut icon" href=https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Morning_Star_flag.svg/1920px-Morning_Star_flag.svg.png type=image/x-icon>
                <head>
                <body class="bg-gradient-to-r from-teal-900 to-teal-950 text-teal-400">
                    <main class=pt-10>
                        <section id=hero>
                            <div class=container>
                                <div class="w-full px-4">
                                    <h1 class="text-2xl font-semibold">CRUD Data Car! 🖐</h1>
                                    <p class=text-sm>PABW-7A2-GS2324</p>
                                    <div class="w-full px-4 py-5 mt-10 bg-teal-800 shadow-lg rounded-xl">
                                        <table class="w-full table table-auto mx-auto">
                                            <thead class="font-semibold text-center">
                                                <tr><td>Merk</td><td>Jenis</td><td>Tahun</td><td>Nama</td><td>Aksi</td></tr>
                                            </thead>
                                            <tbody>
                                                {self.generate_table_rows()}
                                            </tbody>
                                        </table>
                                        {self.generate_edit_form()}
                                        <form action="/add_or_update" method="post" class="w-full flex flex-wrap">
                                            <div class="w-1/5">
                                                <input type="text" name="merk" required class="bg-teal-950 px-4 py-1 w-full rounded-full" placeholder="Merk Mobil">
                                            </div>
                                            <div class="w-1/5">
                                                <input type="text" name="jenis" required class="bg-teal-950 px-4 py-1 w-full rounded-full" placeholder="Jenis Mobil">
                                            </div>
                                            <div class="w-1/5">
                                                <input type="text" name="tahun" required class="bg-teal-950 px-4 py-1 w-full rounded-full" placeholder="Tahun Mobil">
                                            </div>
                                            <div class="w-1/5">
                                                <input type="text" name="nama" required class="bg-teal-950 px-4 py-1 w-full rounded-full" placeholder="Nama Mobil">
                                            </div>
                                            <div class="w-1/5">
                                                <input type="submit" value="Aksi Mobil" class="w-full bg-teal-900 mx-auto py-1 px-2 lg:px-4 rounded-full ease-in-out duration-300 hover:shadow-xl hover:bg-opacity-80">
                                            </div>
                                        </form>
                                    </div>
                                </div>
                            </div>
                        </section>
                    </main>
                    <footer class=pt-20>
                        <section>
                            <div class=container>
                                <div class="w-full flex flex-warp">
                                    <div class="bg-teal-800 px-4 py-2 rounded-lg shadow-lg mx-auto text-center">
                                        <h1 class=text-lg>Framework <a class="ease-in-out duration-300 transition hover:text-teal-200" href=https://docs.cherrypy.dev/en/latest/ target=_blank rel="noopener noreferrer">CherryPy</a></h1>
                                        <small>Dibuat Kelompok oleh Reyhan Nyakitin 🤭</small>
                                    </div>
                                </div>
                            </div>
                        </section>
                        <section class=pt-10>
                            <div class=container>
                                <div class="w-full flex flex-warp">
                                    <div class="bg-teal-800 px-4 py-2 rounded-lg shadow-lg mx-auto text-center">
                                        <img src=https://static.promediateknologi.id/crop/0x0:0x0/750x500/webp/photo/2023/06/02/Screenshot_11-515522556.png alt="Megawati Mati" class="!h-[150px] rounded-lg">
                                    </div>
                                </div>
                            </div>
                        </section>
                    </footer>
                </body>
                </html>
            """

    @cherrypy.expose
    def add_or_update(self, merk=None, jenis=None, tahun=None, nama=None):
        if merk and jenis and tahun and nama:
            if self.editing_index is not None:
                # Update existing car
                index = self.editing_index
                self.cars[index]["merk"] = merk
                self.cars[index]["jenis"] = jenis
                self.cars[index]["tahun"] = tahun
                self.cars[index]["nama"] = nama
                self.editing_index = None
            else:
                # Add new car
                new_car = {
                    "merk": merk,
                    "jenis": jenis,
                    "tahun": tahun,
                    "nama": nama
                }
                self.cars.append(new_car)
            self.save_to_json()
        raise cherrypy.HTTPRedirect('/')

    @cherrypy.expose
    def edit(self, index):
        index = int(index)
        if 0 <= index < len(self.cars):
            car = self.cars[index]
            self.editing_index = index
            raise cherrypy.HTTPRedirect('/#edit_form')

    @cherrypy.expose
    def cancel_edit(self):
        self.editing_index = None
        raise cherrypy.HTTPRedirect('/')

    def generate_table_rows(self):
        rows = ""
        for i, car in enumerate(self.cars):
            rows += """
                <tr><td class="px-4 text-center">%s</td><td class="px-4 text-center">%s</td><td class="px-4 text-center">%s</td><td class="px-4 text-center">%s</td><td class="px-4 text-center"><a class="bg-teal-900 mx-auto py-1 px-2 lg:px-4 rounded-lg ease-in-out duration-300 hover:shadow-xl hover:bg-opacity-80" href="/edit?index=%s">Edit</a><span class="px-4"></span><a class="bg-teal-900 mx-auto py-1 px-2 lg:px-4 rounded-lg ease-in-out duration-300 hover:shadow-xl hover:bg-opacity-80" href="/delete?index=%s">Hapus</a></td></tr>
            """ % (car["merk"], car["jenis"], car["tahun"], car["nama"], i, i)
        return rows

    def generate_edit_form(self):
        if self.editing_index is not None:
            car = self.cars[self.editing_index]
            return """
                <form action="/add_or_update#edit_form" method="post" class="w-full flex flex-wrap">
                    <div class="w-1/5">
                        <input type="text" name="merk" required class="bg-teal-950 px-4 py-1 w-full rounded-full" placeholder="Merk Mobil">
                    </div>
                    <div class="w-1/5">
                        <input type="text" name="jenis" required class="bg-teal-950 px-4 py-1 w-full rounded-full" placeholder="Jenis Mobil">
                    </div>
                    <div class="w-1/5">
                        <input type="text" name="tahun" required class="bg-teal-950 px-4 py-1 w-full rounded-full" placeholder="Tahun Mobil">
                    </div>
                    <div class="w-1/5">
                        <input type="text" name="nama" required class="bg-teal-950 px-4 py-1 w-full rounded-full" placeholder="Nama Mobil">
                    </div>
                    <div class="w-1/5">
                        <input type="submit" value="Aksi Mobil" class="w-full bg-teal-900 mx-auto py-1 px-2 lg:px-4 rounded-full ease-in-out duration-300 hover:shadow-xl hover:bg-opacity-80">
                    </div>
                </form>
            """ % (car["merk"], car["jenis"], car["tahun"], car["nama"])
        else:
            return ""

    def save_to_json(self):
        with open('cars.json', 'w') as file:
            json.dump(self.cars, file, indent=4)

if __name__ == '__main__':
    port = 8088
    host = '127.0.0.1'
    cherrypy.config.update({'server.socket_host': host, 'server.socket_port': port})
    cherrypy.quickstart(CarApp())
