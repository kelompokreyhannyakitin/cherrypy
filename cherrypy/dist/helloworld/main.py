import os.path
import cherrypy

class HelloWorld:
    @cherrypy.expose
    def index(self):
        return '''
        <!doctype html>
<html lang=id>
<head>
<meta charset=UTF-8>
<meta name=viewport content="width=device-width,initial-scale=1">
<title>Hello World!</title>
<link rel=preconnect href=https://fonts.googleapis.com>
<link rel=preconnect href=https://fonts.gstatic.com crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat+Alternates&display=swap" rel=stylesheet>
<link rel="shortcut icon" href=https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Morning_Star_flag.svg/1920px-Morning_Star_flag.svg.png type=image/x-icon>
<style>/*! tailwindcss v3.4.1 | MIT License | https://tailwindcss.com*/*,:after,:before{box-sizing:border-box;border:0 solid #e5e7eb}:after,:before{--tw-content:""}:host,html{line-height:1.5;-webkit-text-size-adjust:100%;-moz-tab-size:4;-o-tab-size:4;tab-size:4;font-family:ui-sans-serif,system-ui,sans-serif,Apple Color Emoji,Segoe UI Emoji,Segoe UI Symbol,Noto Color Emoji;font-feature-settings:normal;font-variation-settings:normal;-webkit-tap-highlight-color:transparent}body{margin:0;line-height:inherit}hr{height:0;color:inherit;border-top-width:1px}abbr:where([title]){-webkit-text-decoration:underline dotted;text-decoration:underline dotted}h1,h2,h3,h4,h5,h6{font-size:inherit;font-weight:inherit}a{color:inherit;text-decoration:inherit}b,strong{font-weight:bolder}code,kbd,pre,samp{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,Liberation Mono,Courier New,monospace;font-feature-settings:normal;font-variation-settings:normal;font-size:1em}small{font-size:80%}sub,sup{font-size:75%;line-height:0;position:relative;vertical-align:initial}sub{bottom:-.25em}sup{top:-.5em}table{text-indent:0;border-color:inherit;border-collapse:collapse}button,input,optgroup,select,textarea{font-family:inherit;font-feature-settings:inherit;font-variation-settings:inherit;font-size:100%;font-weight:inherit;line-height:inherit;color:inherit;margin:0;padding:0}button,select{text-transform:none}[type=button],[type=reset],[type=submit],button{-webkit-appearance:button;background-color:initial;background-image:none}:-moz-focusring{outline:auto}:-moz-ui-invalid{box-shadow:none}progress{vertical-align:initial}::-webkit-inner-spin-button,::-webkit-outer-spin-button{height:auto}[type=search]{-webkit-appearance:textfield;outline-offset:-2px}::-webkit-search-decoration{-webkit-appearance:none}::-webkit-file-upload-button{-webkit-appearance:button;font:inherit}summary{display:list-item}blockquote,dd,dl,figure,h1,h2,h3,h4,h5,h6,hr,p,pre{margin:0}fieldset{margin:0}fieldset,legend{padding:0}menu,ol,ul{list-style:none;margin:0;padding:0}dialog{padding:0}textarea{resize:vertical}input::-moz-placeholder,textarea::-moz-placeholder{opacity:1;color:#9ca3af}input::placeholder,textarea::placeholder{opacity:1;color:#9ca3af}[role=button],button{cursor:pointer}:disabled{cursor:default}audio,canvas,embed,iframe,img,object,svg,video{display:block;vertical-align:middle}img,video{max-width:100%;height:auto}[hidden]{display:none}*,::backdrop,:after,:before{--tw-border-spacing-x:0;--tw-border-spacing-y:0;--tw-translate-x:0;--tw-translate-y:0;--tw-rotate:0;--tw-skew-x:0;--tw-skew-y:0;--tw-scale-x:1;--tw-scale-y:1;--tw-pan-x: ;--tw-pan-y: ;--tw-pinch-zoom: ;--tw-scroll-snap-strictness:proximity;--tw-gradient-from-position: ;--tw-gradient-via-position: ;--tw-gradient-to-position: ;--tw-ordinal: ;--tw-slashed-zero: ;--tw-numeric-figure: ;--tw-numeric-spacing: ;--tw-numeric-fraction: ;--tw-ring-inset: ;--tw-ring-offset-width:0px;--tw-ring-offset-color:#fff;--tw-ring-color:#3b82f680;--tw-ring-offset-shadow:0 0 #0000;--tw-ring-shadow:0 0 #0000;--tw-shadow:0 0 #0000;--tw-shadow-colored:0 0 #0000;--tw-blur: ;--tw-brightness: ;--tw-contrast: ;--tw-grayscale: ;--tw-hue-rotate: ;--tw-invert: ;--tw-saturate: ;--tw-sepia: ;--tw-drop-shadow: ;--tw-backdrop-blur: ;--tw-backdrop-brightness: ;--tw-backdrop-contrast: ;--tw-backdrop-grayscale: ;--tw-backdrop-hue-rotate: ;--tw-backdrop-invert: ;--tw-backdrop-opacity: ;--tw-backdrop-saturate: ;--tw-backdrop-sepia: }.container{width:100%;margin-right:auto;margin-left:auto;padding-right:16px;padding-left:16px}@media (min-width:640px){.container{max-width:640px}}@media (min-width:768px){.container{max-width:768px}}@media (min-width:1024px){.container{max-width:1024px}}@media (min-width:1280px){.container{max-width:1280px}}@media (min-width:1320px){.container{max-width:1320px}}.mx-auto{margin-left:auto;margin-right:auto}.flex{display:flex}.table{display:table}.\!h-\[150px\]{height:150px!important}.w-full{width:100%}.table-auto{table-layout:auto}.rounded-lg{border-radius:.5rem}.rounded-xl{border-radius:.75rem}.bg-teal-800{--tw-bg-opacity:1;background-color:rgb(17 94 89/var(--tw-bg-opacity))}.bg-gradient-to-r{background-image:linear-gradient(to right,var(--tw-gradient-stops))}.from-teal-900{--tw-gradient-from:#134e4a var(--tw-gradient-from-position);--tw-gradient-to:#134e4a00 var(--tw-gradient-to-position);--tw-gradient-stops:var(--tw-gradient-from),var(--tw-gradient-to)}.to-teal-950{--tw-gradient-to:#042f2e var(--tw-gradient-to-position)}.px-4{padding-left:1rem;padding-right:1rem}.py-2{padding-top:.5rem;padding-bottom:.5rem}.pt-10{padding-top:2.5rem}.pt-20{padding-top:5rem}.text-center{text-align:center}.text-2xl{font-size:1.5rem;line-height:2rem}.text-lg{font-size:1.125rem;line-height:1.75rem}.text-sm{font-size:.875rem;line-height:1.25rem}.font-semibold{font-weight:600}.text-teal-400{--tw-text-opacity:1;color:rgb(45 212 191/var(--tw-text-opacity))}.shadow-lg{--tw-shadow:0 10px 15px -3px #0000001a,0 4px 6px -4px #0000001a;--tw-shadow-colored:0 10px 15px -3px var(--tw-shadow-color),0 4px 6px -4px var(--tw-shadow-color);box-shadow:var(--tw-ring-offset-shadow,0 0 #0000),var(--tw-ring-shadow,0 0 #0000),var(--tw-shadow)}.transition{transition-property:color,background-color,border-color,text-decoration-color,fill,stroke,opacity,box-shadow,transform,filter,-webkit-backdrop-filter;transition-property:color,background-color,border-color,text-decoration-color,fill,stroke,opacity,box-shadow,transform,filter,backdrop-filter;transition-property:color,background-color,border-color,text-decoration-color,fill,stroke,opacity,box-shadow,transform,filter,backdrop-filter,-webkit-backdrop-filter;transition-timing-function:cubic-bezier(.4,0,.2,1);transition-duration:.15s}.duration-300{transition-duration:.3s}.ease-in-out{transition-timing-function:cubic-bezier(.4,0,.2,1)}*{scroll-behavior:smooth;font-family:Montserrat Alternates,sans-serif}.hover\:text-teal-200:hover{--tw-text-opacity:1;color:rgb(153 246 228/var(--tw-text-opacity))}</style>
</head>
<body class="bg-gradient-to-r from-teal-900 to-teal-950 text-teal-400">
<main class=pt-10>
<section id=hero>
<div class=container>
<div class="w-full px-4">
<h1 class="text-2xl font-semibold">Hello World! 🖐</h1>
<p class=text-sm>PABW-7A2-GS2324</p>
<div class="w-full px-4 flex flex-warp pt-10">
<table class="table table-auto mx-auto bg-teal-800 shadow-lg rounded-xl">
<thead class="font-semibold text-center">
<tr>
<td>NAMA</td><td>NIM</td>
</tr>
</thead>
<tbody>
<tr><td class=px-4>Muhammad Alvin Azzamul Azmi</td><td class=px-4>201080200006</td></tr>
<tr><td class=px-4>Davito Rasendriya Rizqullah Putra</td><td class=px-4>201080200009</td></tr>
<tr><td class=px-4>Muhammad Agung Laksono</td><td class=px-4>201080200012</td></tr>
<tr><td class=px-4>Luthfi Arian Nugraha</td><td class=px-4>201080200026</td></tr>
<tr><td class=px-4>Reyhan Adi Saputra</td><td class=px-4>201080200032</td></tr>
<tr><td class=px-4>Muhammad Qosdy Jauharul Arzaq</td><td class=px-4>201080200058</td></tr>
<tr><td class=px-4>M. Purnomo Adji Saputro</td><td class=px-4>201080200089</td></tr>
<tr><td class=px-4>Tara Januar Januar Abwina Tassa</td><td class=px-4>201080200106</td></tr>
<tr><td class=px-4>Emelin Yuan Lorin</td><td class=px-4>201080200142</td></tr>
</tbody>
</table>
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

        '''
    
helloworldconf = os.path.join(os.path.dirname(__file__), 'helloworld.conf')

if __name__ == '__main__':
    # CherryPy always starts with app.root when trying to map request URIs
    # to objects, so we need to mount a request handler root. A request
    # to '/' will be mapped to HelloWorld().index().
    cherrypy.quickstart(HelloWorld(), config=helloworldconf)