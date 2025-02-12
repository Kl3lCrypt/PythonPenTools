# PythonPenTools
🐍 PyPentools

Colección de scripts en Python para automatizar tareas en todas las etapas de un test de intrusión: reconocimiento, explotación y post-explotación.
Diseñado para pentesters y estudiantes, estos scripts son ligeros, prácticos y creados durante retos en plataformas de ciberseguridad.
📁 Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

    🔍 Reconocimiento: Escaneo de puertos, descubrimiento de subdominios, fingerprinting, etc.
    💥 Explotación: Scripts para ataque y explotación de vulnerabilidades.
    🔐 Post-explotación: Herramientas para la recolección de datos, escalación de privilegios y persistencia.
    🛠️ Auxiliar: Scripts de apoyo para tareas generales de pentesting.

⚙️ Instalación

Para comenzar, clona este repositorio en tu máquina local:

git clone https://github.com/TU-USUARIO/PyPentools
cd PyPentools

📌 Requisitos

Todos los scripts están desarrollados en Python 3, por lo que es indispensable tenerlo instalado. También pueden requerir algunas librerías adicionales, que puedes instalar con:

pip install -r requirements.txt

🎯 Ejemplos de Uso

📡 Escaneo de Puertos

python reconocimiento/port_scanner.py -t 192.168.1.1 -p 1-65535

🔓 Fuerza Bruta SSH

python explotacion/ssh_bruteforce.py -t 192.168.1.100 -u usuario -w passwords.txt

📶 Sniffing de Red

python post-explotacion/network_sniffer.py -i eth0

⚠️ Advertencia Legal

Este proyecto está destinado únicamente a fines educativos y de investigación en entornos autorizados.
❌ No se debe usar en sistemas sin permiso expreso del propietario.

El uso indebido de estas herramientas puede ser ilegal y el autor del repositorio no se hace responsable de las consecuencias.

¡Hackea con ética! 🛡️
