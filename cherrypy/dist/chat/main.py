import os, os.path
import cherrypy
import json
import random
from cherrypy import HTTPError
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding

class MyApp:
    def __init__(self):
        self.private_key, self.public_key = self.generate_rsa_key_pair()
        try:
            with open("chat_data.json", "r") as file:
                self.chat_data = json.load(file)
        except FileNotFoundError:
            self.chat_data = []

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
    def index(self, name=None, chat=None):
        if name and chat:
            try:
                chat_encrypt = self.encrypt_message_rsa(chat)
                id = "CHT-" + str(random.randrange(19, 30))
                # Serialize the encrypted data to hexadecimal
                encrypted_hex = chat_encrypt.hex()
                print(f"{bytes.fromhex(encrypted_hex)}")
                new_chat = {
                    "id": id,
                    "name": name,
                    "chat": chat,
                    "encrypt": encrypted_hex
                }
                self.chat_data.append(new_chat)

                # Save chat_data to chat_data.json
                with open("chat_data.json", "w") as f:
                    json.dump(self.chat_data, f, indent=4)

                raise cherrypy.HTTPRedirect(self.index)
            except Exception as e:
                print(f"Error saving chat: {e}")
        
        chat_history_html = self.generate_chat_history_html()
        modal_history_html = self.generate_chat_modal_html()

        return f'''
                <!DOCTYPE html>
                <html lang="id">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Chat Rektor</title>
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
                                    <h1 class="text-2xl font-semibold">Chat Rektor! 🖐</h1>
                                    <p class="text-sm">PABW-7A2-GS2324</p>
                                    <div class="w-full px-4 flex flex-warp">
                                        <div class="w-full px-4 py-2 rounded-lg shadow-lg mx-auto bg-teal-800 mt-10 h-full">
                                            <div class="w-full bg-[#031c1b] rounded-t-lg py-1 px-4"><p class="text-lg font-semibold">Riwayat Chat</p></div>
                                            <div class="w-full rounded-b-lg py-2 bg-teal-950 overflow-y-auto mb-2 h-[150px]">
                                                {chat_history_html}
                                            </div>
                                            <form action="" method="get" class="flex flex-wrap">
                                                <div class="w-11/12">
                                                    <input type="text" name="name" required class="bg-teal-950 px-4 py-1 w-full rounded-full mb-1.5" placeholder="Nama anda">
                                                    <input type="text" name="chat" required class="bg-teal-950 px-4 py-1 w-full rounded-full" placeholder="Tambahkan Chat Anda">
                                                </div>
                                                <div class="w-1/12 flex self-center">
                                                    <input type="submit" value="Kirim" class="bg-teal-900 mx-auto py-2 px-2 lg:px-4 rounded-lg ease-in-out duration-300 hover:shadow-xl hover:bg-opacity-80">
                                                </div>
                                            </form>
                                            <div class="w-full py-2 flex flex-warp">
                                                <button type="button" data-modal-target="key-modal" data-modal-toggle="key-modal" class="w-full text-center rounded-full py-2 bg-teal-950 ease-in-out duration-300 hover:bg-opacity-80 hover:shadow-xl">Tentang Public Key dan Private Key</button>
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

                    <!-- Modal Chat -->
                    {modal_history_html}

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

    def generate_chat_history_html(self):
        chat_html = ""
        for chat in self.chat_data:
            decrypted_chat = self.decrypt_message_rsa(bytes.fromhex(chat["encrypt"]))
            chat_html += f"""
                <p class="text-sm w-full my-1 px-4">
                    <span class="font-semibold">{chat["name"]} ({chat["id"]}) : </span>{decrypted_chat} <button data-modal-target="default-modal-{chat["id"]}" data-modal-toggle="default-modal-{chat["id"]}" type="button" class="ml-2 py-1 rounded-md bg-[#031c1b] px-1">Lihat Enkripsi</button>
                </p>
            """
        return chat_html
    
    def generate_chat_modal_html(self):
        modal_chat = ""
        for chat in self.chat_data:
            encrypted_chat = bytes.fromhex(chat["encrypt"])
            modal_chat += f"""
                    <div id="default-modal-{chat["id"]}" tabindex="-1" aria-hidden="true" class="hidden transition overflow-y-auto overflow-x-hidden fixed top-0 right-0 left-0 z-50 justify-center items-center w-full md:inset-0 h-[calc(100%-1rem)] max-h-full">
                        <div class="relative p-4 w-full max-w-2xl max-h-full">
                            <!-- Modal content -->
                            <div class="relative bg-teal-950 text-teal-100 rounded-lg shadow">
                                <!-- Modal header -->
                                <div class="flex items-center justify-between p-4 md:p-5 border-b border-teal-500 rounded-t">
                                    <h3 class="text-xl font-semibold">
                                        Data Enkripsi Chat 
                                    </h3>
                                    <button type="button" class=" bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ms-auto inline-flex justify-center items-center" data-modal-hide="default-modal-{chat["id"]}">
                                        <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 14">
                                            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6"/>
                                        </svg>
                                        <span class="sr-only">Close modal</span>
                                    </button>
                                </div>
                                <!-- Modal body -->
                                <div class="p-4 md:p-5 space-y-4">                                    
                                    <p style="word-break: break-all;" class="text-sm leading-relaxed">Enkripsi :<br>{encrypted_chat}</p>
                                </div>
                                <!-- Modal footer -->
                                <div class="flex items-center p-4 md:p-5 rounded-b">
                                    <button data-modal-hide="default-modal-{chat["id"]}" type="button" class="text-yellow-500 fill-current bg-teal-700 hover:bg-teal-800 focus:ring-4 focus:outline-none focus:ring-teal-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center">👍</button>
                                </div>
                            </div>
                        </div>
                    </div>
            """
        return modal_chat

    def read_chat_data(self):
        try:
            with open("chat_data.json", "r") as f:
                self.chat_data = json.load(f)
        except FileNotFoundError:
            self.chat_data = []
    
    def encrypt_message_rsa(self, message):
        cipher_text = self.public_key.encrypt(
            message.encode('utf-8'),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return cipher_text

    def decrypt_message_rsa(self, cipher_text):
        try:
            decrypted_text = self.private_key.decrypt(
                cipher_text,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )
            return decrypted_text.decode('utf-8')
        except ValueError as e:
            print(f"Error decrypting message: {e}")
            return "Decryption failed"
    

if __name__ == '__main__':
    port = 9992
    host = '127.0.0.1'
    cherrypy.config.update({'server.socket_host': host, 'server.socket_port': port})
    cherrypy.quickstart(MyApp())
