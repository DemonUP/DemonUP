# ¡Hola, soy demonUP! 👋

Soy un programador apasionado por el aprendizaje constante, siempre en busca de nuevos retos tecnológicos. Con ambición y visión, me dedico al pentesting y a explorar vulnerabilidades en sistemas por pasatiempo, adoptando la determinación de un verdadero cazador de recompensas: depredador y enfocado en alcanzar cada meta. Amo la lógica y el crecimiento continuo.

---

## Tecnologías

[![Linux](https://img.shields.io/badge/Linux-FCC624?logo=linux&logoColor=black&style=for-the-badge)](https://www.linux.org)  
[![Bash](https://img.shields.io/badge/Bash-4EAA25?logo=gnu-bash&logoColor=white&style=for-the-badge)](https://www.gnu.org/software/bash/)  
[![PHP](https://img.shields.io/badge/PHP-777BB4?logo=php&logoColor=white&style=for-the-badge)](https://www.php.net)  
[![Laravel](https://img.shields.io/badge/Laravel-FF2D20?logo=laravel&logoColor=white&style=for-the-badge)](https://laravel.com)  
[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white&style=for-the-badge)](https://www.python.org)

---

## Hack The Box

Aquí se mostrarán mis métricas de Hack The Box, actualizadas automáticamente mediante GitHub Actions:

![HTB Stats](htb_stats.svg)
<!-- Asegúrate de configurar el script y la acción para actualizar este archivo -->

---

## Contacto

Puedes contactarme en: [tu-email@example.com](mailto:tu-email@example.com)

---

## Configuración de GitHub Actions para Actualizar HTB Stats

Si deseas automatizar la actualización de tus métricas de Hack The Box, crea el archivo `.github/workflows/update-htb-stats.yml` en tu repositorio con el siguiente contenido:

```yaml
name: Actualizar métricas de HTB

on:
  schedule:
    - cron: '0 * * * *'  # Se ejecuta cada hora (ajusta la frecuencia según necesites)
  workflow_dispatch:   # Permite ejecutar manualmente el workflow

jobs:
  update-stats:
    runs-on: ubuntu-latest
    steps:
      - name: Clonar repositorio
        uses: actions/checkout@v2

      - name: Configurar Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.x'

      - name: Instalar dependencias
        run: pip install requests beautifulsoup4

      - name: Ejecutar script de HTB
        run: python htb_stats.py

      - name: Commit de cambios
        run: |
          git config --local user.email "action@github.com"
          git config --local user.name "GitHub Action"
          git add htb_stats.svg
          git diff --cached --quiet || (git commit -m "Actualización automática de métricas HTB" && git push)
