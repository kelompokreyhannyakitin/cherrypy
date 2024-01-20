import cherrypy
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa

class MyApp:
    def __init__(self):
        self.private_key, self.public_key = self.generate_rsa_key_pair()

    @staticmethod
    def generate_rsa_key_pair():
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )

        public_key = private_key.public_key()

        n = private_key.private_numbers().public_numbers.n
        e = private_key.private_numbers().public_numbers.e
        d = private_key.private_numbers().d
        p = private_key.private_numbers().p
        q = private_key.private_numbers().q

        return private_key, public_key

    @cherrypy.expose
    def index(self):
        return f'''
                <!DOCTYPE html>
                <html lang="id">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Encryption</title>
                    <link rel="stylesheet" href="https://luthfiarian.my.id/task/style-chat.css">
                    <link rel="preconnect" href="https://fonts.googleapis.com">
                    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                    <link href="https://fonts.googleapis.com/css2?family=Montserrat+Alternates&display=swap" rel="stylesheet">
                    <link rel="shortcut icon" href="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Morning_Star_flag.svg/1920px-Morning_Star_flag.svg.png" type="image/x-icon">
                </head>
                <body class="bg-gradient-to-r from-teal-900 to-teal-950 text-teal-400">
                    <main class="pt-10">
                        <section id="hero">
                            <div class="container">
                                <div class="w-full px-4">
                                    <h1 class="text-2xl font-semibold">Enkripsi! 🔐</h1>
                                    <p class="text-sm">PABW-7A2-GS2324</p>
                                    <div class="w-full px-4 flex flex-warp">
                                        <div class="w-full px-4 py-2 rounded-lg shadow-lg mx-auto bg-teal-800 mt-10 h-full">
                                            <div class="w-full py-2 flex flex-warp">
                                                <button type="button" data-modal-target="key-modal" data-modal-toggle="key-modal" class="w-full text-center rounded-full py-2 bg-teal-950 ease-in-out duration-300 hover:bg-opacity-80 hover:shadow-xl">Tampilkan Public Key dan Private Key</button>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </section>
                    </main>
                    <footer class="pt-20">
                        <section>
                            <div class="container">
                                <div class="w-full flex flex-warp">
                                    <div class="bg-teal-800 px-4 py-2 rounded-lg shadow-lg mx-auto text-center">
                                       <h1 class="text-lg">Framework <a class="ease-in-out duration-300 transition hover:text-teal-200" href="https://docs.cherrypy.dev/en/latest/" target="_blank" rel="noopener noreferrer">CherryPy</a></h1>
                                       <small>Dibuat Kelompok  oleh Reyhan Nyakitin 🤭</small>
                                    </div>
                                </div>
                            </div>
                        </section>
                        <section class="pt-10">
                            <div class="container">
                                <div class="w-full flex flex-warp">
                                    <div class="bg-teal-800 px-4 py-2 rounded-lg shadow-lg mx-auto text-center">
                                        <img src="https://static.promediateknologi.id/crop/0x0:0x0/750x500/webp/photo/2023/06/02/Screenshot_11-515522556.png" alt="Megawati Mati" class="!h-[150px] rounded-lg">
                                    </div>
                                </div>
                            </div>
                        </section>
                    </footer>

                    <!-- Modal Key -->
                    <div id="key-modal" tabindex="-1" aria-hidden="true" class="hidden transition overflow-y-auto overflow-x-hidden fixed top-0 right-0 left-0 z-50 justify-center items-center w-full md:inset-0 h-[calc(100%-1rem)] max-h-full">
                        <div class="relative p-4 w-full max-w-2xl max-h-full">
                            <!-- Modal content -->
                            <div class="relative bg-teal-950 text-teal-100 rounded-lg shadow">
                                <!-- Modal header -->
                                <div class="flex items-center justify-between p-4 md:p-5 border-b border-teal-500 rounded-t">
                                    <h3 class="text-xl font-semibold">
                                        Data Enkripsi
                                    </h3>
                                    <button type="button" class=" bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ms-auto inline-flex justify-center items-center" data-modal-hide="key-modal">
                                        <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 14">
                                            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6"/>
                                        </svg>
                                        <span class="sr-only">Close modal</span>
                                    </button>
                                </div>
                                <!-- Modal body -->
                                <div class="p-4 md:p-5 space-y-4">                                    
                                    <p style="word-break: break-all;" class="text-sm leading-relaxed">Angka Prima Pertama (p) :<br>{self.private_key.private_numbers().p}</p>
                                    <p style="word-break: break-all;" class="text-sm leading-relaxed">Angka Prima Kedua (q) :<br>{self.private_key.private_numbers().q}</p>
                                    <p style="word-break: break-all;" class="text-sm leading-relaxed">Public Key (n, e) :<br>{self.private_key.private_numbers().public_numbers.n}, {self.private_key.private_numbers().public_numbers.e}</p>
                                    <p style="word-break: break-all;" class="text-sm leading-relaxed">Private Key (n, d) :<br>{self.private_key.private_numbers().public_numbers.n}, {self.private_key.private_numbers().d}</p>
                                </div>
                                <!-- Modal footer -->
                                <div class="flex items-center p-4 md:p-5 rounded-b">
                                    <button data-modal-hide="key-modal" type="button" class="text-yellow-500 fill-current bg-teal-700 hover:bg-teal-800 focus:ring-4 focus:outline-none focus:ring-teal-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center">👍</button>
                                </div>
                            </div>
                        </div>
                    </div>
                    <!-- Flowbite -->
                    <script src="https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.2.1/flowbite.min.js"></script>
                </body>
                </html>
        '''

if __name__ == '__main__':
    port = 8080
    host = '127.0.0.1'
    cherrypy.config.update({'server.socket_host': host, 'server.socket_port': port})
    cherrypy.quickstart(MyApp())
