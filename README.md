# Launcher de Modpack (uso legal)

Este repositorio incluye un launcher simple en Python para abrir **un único modpack/instancia** en Prism Launcher.

> ⚠️ Este proyecto **no** incluye ni enseña a evadir autenticación/licencias de Minecraft. Para jugar, usa una cuenta oficial y el software que corresponda.

## Qué hace

- Solo permite lanzar la instancia configurada.
- No deja elegir otros modpacks desde este launcher.
- Ejecuta Prism Launcher con `--launch <instancia>`.

## Requisitos

- Python 3.10+
- Prism Launcher instalado y disponible en PATH (o ruta completa al ejecutable)

## Uso rápido

1. Copia el archivo de ejemplo y personalízalo:

```bash
cp launcher_config.example.json launcher_config.json
```

2. Edita `launcher_config.json`:

- `launcher_command`: comando o ruta de Prism Launcher.
- `instance_name`: nombre exacto de tu instancia/modpack en Prism.
- `window_title`: título de la ventana.

3. Ejecuta:

```bash
python3 launcher.py
```

## Cómo poner tu modpack y abrirlo

1. Abre **Prism Launcher** normalmente.
2. Importa tu modpack:
   - Opción A: `Add Instance` → busca el modpack (CurseForge/Modrinth).
   - Opción B: `Import from zip` si tienes el archivo del modpack.
3. Verifica el nombre exacto de la instancia creada (por ejemplo: `Cobblemon-Server`).
4. En este proyecto, crea tu config y pon ese nombre exacto:

```bash
cp launcher_config.example.json launcher_config.json
```

Edita `launcher_config.json` y cambia:
- `instance_name`: al nombre exacto de la instancia en Prism.
- `launcher_command`: `prismlauncher` (o ruta completa al ejecutable si no está en PATH).

5. Ejecuta tu launcher:

```bash
python3 launcher.py
```

6. Pulsa **Jugar**. El botón solo abre la instancia definida en `instance_name`.

### Ejemplo real

Si en Prism tu instancia se llama `BetterMC-Fabric`, tu `launcher_config.json` debería quedar así:

```json
{
  "launcher_command": "prismlauncher",
  "instance_name": "BetterMC-Fabric",
  "window_title": "Mi Launcher"
}
```

### Si no abre

- Revisa que Prism abra desde terminal con `prismlauncher`.
- Si no abre, usa la ruta completa del ejecutable en `launcher_command`.
- Confirma que `instance_name` coincide **exactamente** con el nombre visible en Prism.

## Configuración de ejemplo

```json
{
  "launcher_command": "prismlauncher",
  "instance_name": "MiModpackPrivado",
  "window_title": "Launcher privado"
}
```

## Notas

- La autenticación de Minecraft se gestiona dentro de Prism Launcher.
- Este wrapper únicamente automatiza abrir una instancia concreta.
