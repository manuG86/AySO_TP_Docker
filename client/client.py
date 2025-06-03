import requests
import time

def main():
    # Esperar a que el servidor esté disponible
    for i in range(30):
        try:
            respuesta = requests.get("http://server:5000/endpoint")
            print("Respuesta del servidor:", respuesta.text)
            return
        except Exception as e:
            print("Esperando al servidor... intento", i + 1)
            print("Error:", e)
            time.sleep(1)

    print("No se pudo conectar al servidor.")

if __name__ == "__main__":
    main()