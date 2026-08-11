# 🔐 Log Security Analyzer

Herramienta en Python que analiza archivos de log de autenticación (estilo `auth.log` de Linux) para **detectar posibles ataques de fuerza bruta**, identificando direcciones IP con múltiples intentos de inicio de sesión fallidos.

## 📌 ¿Por qué este proyecto?

En ciberseguridad, el análisis de logs es una tarea fundamental para detectar actividad sospechosa. Este script simula una tarea real de un analista SOC (Security Operations Center): revisar logs de autenticación y detectar patrones de ataque como el **brute force** (fuerza bruta).

## ⚙️ ¿Qué hace?

- Lee un archivo de log línea por línea.
- Detecta líneas con intentos de autenticación fallidos (`Failed password`).
- Agrupa los intentos por dirección IP.
- Marca como **sospechosa** cualquier IP que supere un umbral configurable de intentos fallidos.
- Genera un reporte en consola con:
  - IP sospechosa
  - Total de intentos fallidos
  - Usuarios que se intentaron usar
  - Hora del primer y último intento

## 🚀 Cómo usarlo

### Requisitos
- Python 3.7 o superior (no requiere librerías externas)

### Ejecución

```bash
python log_analyzer.py sample_auth.log
```

Con un umbral personalizado (por defecto es 5):

```bash
python log_analyzer.py sample_auth.log --umbral 3
```

### Ejemplo de salida

```
============================================================
 REPORTE DE ANÁLISIS DE LOG DE SEGURIDAD
============================================================
Umbral configurado: 3 o más intentos fallidos

⚠️  Se detectaron 2 IP(s) sospechosa(s):

IP: 203.0.113.77
  Total de intentos fallidos: 7
  Usuarios probados: root
  Primer intento: Jan 10 09:15:30 (línea 10)
  Último intento: Jan 10 09:15:54 (línea 16)
------------------------------------------------------------
```

## 📂 Estructura del proyecto

```
log-security-analyzer/
├── log_analyzer.py     # Script principal
├── sample_auth.log     # Log de ejemplo para probar el script
└── README.md           # Este archivo
```

## 🧠 Qué aprendí construyendo esto

- Uso de expresiones regulares (`re`) para extraer datos estructurados de texto libre.
- Manejo de argumentos de línea de comandos con `argparse`.
- Agrupación y conteo de datos con `collections.defaultdict`.
- Cómo se ve un ataque de fuerza bruta en un log real de SSH.

## 🔮 Posibles mejoras futuras

- [ ] Exportar el reporte a CSV o JSON.
- [ ] Soporte para logs de otros formatos (Apache, Nginx, Windows Event Log).
- [ ] Enviar alertas automáticas (correo/Slack) cuando se detecte una IP sospechosa.
- [ ] Integrar con una lista de IPs maliciosas conocidas (threat intelligence feed).

## 📄 Licencia

Este proyecto es de uso libre con fines educativos y de portafolio.
