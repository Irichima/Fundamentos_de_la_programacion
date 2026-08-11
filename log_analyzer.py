"""
log_analyzer.py
----------------
Analizador de logs de seguridad para detectar posibles ataques
de fuerza bruta (múltiples intentos de inicio de sesión fallidos)
a partir de un archivo de log estilo auth.log (Linux).

Autor: Tu Nombre
Nivel: Proyecto de portafolio - Ciberseguridad

Uso:
    python log_analyzer.py sample_auth.log
    python log_analyzer.py sample_auth.log --umbral 3
"""

import argparse
import re
from collections import defaultdict
from datetime import datetime


# Expresión regular que reconoce líneas de "Failed password" típicas
# de un archivo /var/log/auth.log en sistemas Linux, por ejemplo:
# "Jan 10 03:14:15 server sshd[1234]: Failed password for admin from 192.168.1.50 port 51514 ssh2"
PATRON_FALLO = re.compile(
    r"(?P<mes_dia>\w{3}\s+\d{1,2})\s+(?P<hora>\d{2}:\d{2}:\d{2}).*"
    r"Failed password for (invalid user )?(?P<usuario>\S+) from (?P<ip>\d{1,3}(?:\.\d{1,3}){3})"
)


def analizar_log(ruta_archivo, umbral=5):
    """
    Lee el archivo de log línea por línea y cuenta los intentos
    fallidos de inicio de sesión agrupados por dirección IP.

    Parámetros:
        ruta_archivo (str): ruta al archivo de log a analizar.
        umbral (int): número de fallos a partir del cual se
                       considera una IP como sospechosa.

    Retorna:
        dict: {ip: [lista de intentos fallidos]}
    """
    intentos_por_ip = defaultdict(list)

    with open(ruta_archivo, "r", encoding="utf-8", errors="ignore") as archivo:
        for numero_linea, linea in enumerate(archivo, start=1):
            coincidencia = PATRON_FALLO.search(linea)
            if coincidencia:
                ip = coincidencia.group("ip")
                usuario = coincidencia.group("usuario")
                fecha_hora = f'{coincidencia.group("mes_dia")} {coincidencia.group("hora")}'
                intentos_por_ip[ip].append(
                    {"linea": numero_linea, "usuario": usuario, "fecha_hora": fecha_hora}
                )

    return {ip: intentos for ip, intentos in intentos_por_ip.items() if len(intentos) >= umbral}


def generar_reporte(sospechosos, umbral):
    """Imprime un reporte legible en consola con las IPs sospechosas."""
    print("=" * 60)
    print(" REPORTE DE ANÁLISIS DE LOG DE SEGURIDAD")
    print("=" * 60)
    print(f"Umbral configurado: {umbral} o más intentos fallidos\n")

    if not sospechosos:
        print("✅ No se encontraron IPs sospechosas con ese umbral.")
        return

    print(f"⚠️  Se detectaron {len(sospechosos)} IP(s) sospechosa(s):\n")

    for ip, intentos in sorted(sospechosos.items(), key=lambda x: len(x[1]), reverse=True):
        usuarios = {i["usuario"] for i in intentos}
        print(f"IP: {ip}")
        print(f"  Total de intentos fallidos: {len(intentos)}")
        print(f"  Usuarios probados: {', '.join(usuarios)}")
        print(f"  Primer intento: {intentos[0]['fecha_hora']} (línea {intentos[0]['linea']})")
        print(f"  Último intento: {intentos[-1]['fecha_hora']} (línea {intentos[-1]['linea']})")
        print("-" * 60)


def main():
    parser = argparse.ArgumentParser(
        description="Analiza un archivo de log de autenticación y detecta posibles ataques de fuerza bruta."
    )
    parser.add_argument("archivo", help="Ruta al archivo de log a analizar")
    parser.add_argument(
        "--umbral",
        type=int,
        default=5,
        help="Número mínimo de intentos fallidos para marcar una IP como sospechosa (default: 5)",
    )
    args = parser.parse_args()

    sospechosos = analizar_log(args.archivo, args.umbral)
    generar_reporte(sospechosos, args.umbral)


if __name__ == "__main__":
    main()
