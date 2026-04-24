import os
import subprocess


def crear_proyecto():
    # Pregunta el nombre del proyecto
    nombre = input("¿Cómo se llamará tu proyecto? ").strip()

    if not nombre:
        print("❌ Debes ingresar un nombre.")
        return

    # Pregunta dónde quiere guardar el proyecto
    print("\n¿Dónde quieres guardar tu proyecto?")
    print("(Ejemplo: C:\\Users\\SABIN\\Documents\\Analitica_De_Datos)")
    print("(Si presionas Enter sin escribir nada, se creará aquí mismo)")
    ubicacion = input("Ruta: ").strip()

    # Si no escribe nada, se crea en la carpeta actual
    if not ubicacion:
        ubicacion = os.getcwd()

    # Verifica que la ubicación existe
    if not os.path.exists(ubicacion):
        print(f"❌ La ruta '{ubicacion}' no existe. Verifica e intenta de nuevo.")
        return

    # Ruta completa del proyecto
    ruta_proyecto = os.path.join(ubicacion, nombre)

    # Lista de carpetas a crear
    carpetas = [
        "data/raw",
        "data/processed",
        "data/external",
        "notebooks",
        "diagrams",
        "docs",
        "grafics",
        "src/services",
        "src/routes",
        "scripts",
    ]

    # Crea la carpeta raíz
    os.makedirs(ruta_proyecto, exist_ok=True)
    print(f"\n✅ Proyecto '{nombre}' creado.")

    # Crea todas las subcarpetas
    for carpeta in carpetas:
        os.makedirs(os.path.join(ruta_proyecto, carpeta), exist_ok=True)
    print("✅ Carpetas creadas.")

    # Crea el main.py
    with open(os.path.join(ruta_proyecto, "main.py"), "w") as f:
        f.write(
            f'# Proyecto: {nombre}\n# Autor: Sabín Areiza\n\ndef main():\n    print("Hola, {nombre}!")\n\nif __name__ == "__main__":\n    main()\n')
    print("✅ main.py creado.")

    # Crea el README.md
    with open(os.path.join(ruta_proyecto, "README.md"), "w") as f:
        f.write(f"# {nombre}\n\n## Descripción\nAgrega aquí la descripción de tu proyecto.\n\n## Autor\nSabín Areiza\n")
    print("✅ README.md creado.")

    # Crea el .gitignore
    with open(os.path.join(ruta_proyecto, ".gitignore"), "w") as f:
        f.write(".venv/\n__pycache__/\n*.pyc\n.env\n*.csv\n*.xlsx\n")
    print("✅ .gitignore creado.")

    # Inicializa el proyecto con uv
    print("\n⏳ Inicializando uv...")
    subprocess.run(["uv", "init", "--no-workspace"], cwd=ruta_proyecto)

    # Crea el entorno virtual con uv
    print("\n⏳ Creando entorno virtual...")
    subprocess.run(["uv", "venv"], cwd=ruta_proyecto)

    print(f"\n🎉 ¡Todo listo! Tu proyecto '{nombre}' está completamente configurado.")
    print(f"👉 Ubicación: {ruta_proyecto}")
    print(f"👉 Ahora abre esa carpeta en PyCharm y empieza a trabajar.")


crear_proyecto()