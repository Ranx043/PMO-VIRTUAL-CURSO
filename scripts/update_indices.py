#!/usr/bin/env python3
"""
PAIDEIA - Script de Auto-actualización de INDICE_MAESTRO.md
Escanea el repositorio y actualiza el índice automáticamente.

Ejecutar: python scripts/update_indices.py
"""

import os
import datetime
from pathlib import Path

# Configuración
ROOT_DIR = Path(__file__).parent.parent
OUTPUT_FILE = ROOT_DIR / "INDICES" / "INDICE_MAESTRO_AUTO.md"

# Carpetas a ignorar
IGNORE_DIRS = {'.git', 'node_modules', '__pycache__', '.github', 'venv', '.venv'}

# Extensiones a contar
CODE_EXTENSIONS = {'.py', '.js', '.ts', '.tsx', '.html', '.css', '.md', '.yml', '.yaml', '.json'}


def count_lines(file_path: Path) -> int:
    """Cuenta líneas de un archivo."""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            return sum(1 for _ in f)
    except:
        return 0


def scan_directory(directory: Path, depth: int = 0) -> dict:
    """Escanea un directorio recursivamente."""
    results = {
        'files': [],
        'dirs': [],
        'total_lines': 0,
        'total_files': 0
    }

    try:
        for item in sorted(directory.iterdir()):
            if item.name in IGNORE_DIRS:
                continue

            if item.is_dir():
                results['dirs'].append({
                    'name': item.name,
                    'path': str(item.relative_to(ROOT_DIR)),
                    'depth': depth
                })
                # Recursión
                sub_results = scan_directory(item, depth + 1)
                results['files'].extend(sub_results['files'])
                results['dirs'].extend(sub_results['dirs'])
                results['total_lines'] += sub_results['total_lines']
                results['total_files'] += sub_results['total_files']

            elif item.is_file() and item.suffix in CODE_EXTENSIONS:
                lines = count_lines(item)
                results['files'].append({
                    'name': item.name,
                    'path': str(item.relative_to(ROOT_DIR)),
                    'extension': item.suffix,
                    'lines': lines,
                    'depth': depth
                })
                results['total_lines'] += lines
                results['total_files'] += 1

    except PermissionError:
        pass

    return results


def generate_tree(results: dict) -> str:
    """Genera árbol visual del proyecto."""
    tree_lines = ["```", "PMO-VIRTUAL-CURSO/"]

    # Agrupar por directorio
    dirs_seen = set()
    for file in sorted(results['files'], key=lambda x: x['path']):
        parts = file['path'].split('/')

        # Mostrar directorios padre
        for i, part in enumerate(parts[:-1]):
            dir_path = '/'.join(parts[:i+1])
            if dir_path not in dirs_seen:
                indent = "│   " * i + "├── "
                tree_lines.append(f"{indent}{part}/")
                dirs_seen.add(dir_path)

        # Mostrar archivo
        indent = "│   " * (len(parts) - 1) + "├── "
        tree_lines.append(f"{indent}{file['name']} ({file['lines']} líneas)")

    tree_lines.append("```")
    return '\n'.join(tree_lines)


def generate_stats(results: dict) -> str:
    """Genera estadísticas del proyecto."""
    # Contar por extensión
    by_extension = {}
    for file in results['files']:
        ext = file['extension']
        if ext not in by_extension:
            by_extension[ext] = {'count': 0, 'lines': 0}
        by_extension[ext]['count'] += 1
        by_extension[ext]['lines'] += file['lines']

    stats = f"""
## 📊 Estadísticas Automáticas

**Generado**: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

### Totales

| Métrica | Valor |
|---------|-------|
| **Archivos** | {results['total_files']} |
| **Líneas de código** | {results['total_lines']:,} |
| **Directorios** | {len(set(d['name'] for d in results['dirs']))} |

### Por Extensión

| Extensión | Archivos | Líneas |
|-----------|----------|--------|
"""

    for ext, data in sorted(by_extension.items(), key=lambda x: -x[1]['lines']):
        stats += f"| `{ext}` | {data['count']} | {data['lines']:,} |\n"

    return stats


def generate_report(results: dict) -> str:
    """Genera el reporte completo."""
    report = f"""# INDICE MAESTRO - GENERACIÓN AUTOMÁTICA

**Generado automáticamente por**: `scripts/update_indices.py`
**Fecha**: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Consciencia**: PAIDEIA

---

{generate_stats(results)}

---

## 🗂️ Estructura del Proyecto

{generate_tree(results)}

---

## 📁 Lista de Archivos

| Archivo | Ubicación | Líneas |
|---------|-----------|--------|
"""

    for file in sorted(results['files'], key=lambda x: x['path']):
        report += f"| `{file['name']}` | `{file['path']}` | {file['lines']} |\n"

    report += f"""

---

🧬💎∞ **PAIDEIA - Índice Auto-generado**

*Este archivo se regenera automáticamente. No editar manualmente.*
"""

    return report


def main():
    """Función principal."""
    print("🔄 PAIDEIA: Escaneando repositorio...")

    results = scan_directory(ROOT_DIR)

    print(f"✅ Encontrados: {results['total_files']} archivos, {results['total_lines']:,} líneas")

    report = generate_report(results)

    # Escribir archivo
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(report)

    print(f"✅ Índice actualizado: {OUTPUT_FILE}")

    return 0


if __name__ == '__main__':
    exit(main())
