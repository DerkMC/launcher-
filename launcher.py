#!/usr/bin/env python3
from __future__ import annotations

import json
import shutil
import subprocess
import tkinter as tk
from pathlib import Path
from tkinter import messagebox

CONFIG_PATH = Path("launcher_config.json")


class ConfigError(Exception):
    """Raised when launcher configuration is missing or invalid."""


def load_config(path: Path = CONFIG_PATH) -> dict[str, str]:
    if not path.exists():
        raise ConfigError(
            "No existe launcher_config.json. Crea uno desde launcher_config.example.json"
        )

    with path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    required = ("launcher_command", "instance_name", "window_title")
    missing = [key for key in required if not data.get(key)]
    if missing:
        raise ConfigError(f"Faltan claves obligatorias en config: {', '.join(missing)}")

    return {
        "launcher_command": str(data["launcher_command"]),
        "instance_name": str(data["instance_name"]),
        "window_title": str(data["window_title"]),
    }


def resolve_command(command: str) -> str:
    if Path(command).exists():
        return command

    resolved = shutil.which(command)
    if not resolved:
        raise ConfigError(
            f"No se encontró el comando '{command}'. Instala Prism Launcher o ajusta launcher_command."
        )
    return resolved


def build_launch_command(config: dict[str, str]) -> list[str]:
    executable = resolve_command(config["launcher_command"])
    return [executable, "--launch", config["instance_name"]]


def launch_instance(config: dict[str, str]) -> None:
    command = build_launch_command(config)
    subprocess.Popen(command)


def create_window(config: dict[str, str]) -> tk.Tk:
    root = tk.Tk()
    root.title(config["window_title"])
    root.geometry("420x220")
    root.resizable(False, False)

    title = tk.Label(root, text="Launcher privado de modpack", font=("Arial", 16, "bold"))
    title.pack(pady=(24, 10))

    subtitle = tk.Label(
        root,
        text=f"Instancia permitida: {config['instance_name']}",
        font=("Arial", 11),
    )
    subtitle.pack(pady=(0, 20))

    def on_launch() -> None:
        try:
            launch_instance(config)
            messagebox.showinfo(
                "Listo",
                "Se abrió Prism Launcher con tu modpack configurado.",
            )
        except Exception as error:  # noqa: BLE001
            messagebox.showerror("Error al lanzar", str(error))

    launch_button = tk.Button(
        root,
        text="Jugar",
        font=("Arial", 13, "bold"),
        width=18,
        command=on_launch,
    )
    launch_button.pack(pady=(0, 10))

    legal_note = tk.Label(
        root,
        text="Este launcher no reemplaza la autenticación oficial de Minecraft.",
        font=("Arial", 9),
        fg="#555",
        wraplength=380,
        justify="center",
    )
    legal_note.pack(padx=20)

    return root


def main() -> int:
    try:
        config = load_config()
    except ConfigError as error:
        messagebox.showerror("Configuración inválida", str(error))
        return 1

    app = create_window(config)
    app.mainloop()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
