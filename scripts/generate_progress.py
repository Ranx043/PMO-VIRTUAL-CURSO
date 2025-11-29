#!/usr/bin/env python3
"""
PAIDEIA - Script de generación de reporte de progreso visual.
Genera un resumen visual del estado del proyecto.

Ejecutar: python scripts/generate_progress.py
"""

import datetime
import subprocess
from pathlib import Path

# Configuración
ROOT_DIR = Path(__file__).parent.parent
OUTPUT_FILE = ROOT_DIR / "10000_CONTROL" / "PROGRESS_REPORT_AUTO.md"


def get_git_stats() -> dict:
    """Obtiene estadísticas de Git."""
    stats = {
        'commits_total': 0,
        'commits_week': 0,
        'last_commit': 'N/A',
        'contributors': 0
    }

    try:
        # Total commits
        result = subprocess.run(
            ['git', 'rev-list', '--count', 'HEAD'],
            capture_output=True, text=True, cwd=ROOT_DIR
        )
        if result.returncode == 0:
            stats['commits_total'] = int(result.stdout.strip())

        # Commits última semana
        result = subprocess.run(
            ['git', 'rev-list', '--count', '--since=1.week', 'HEAD'],
            capture_output=True, text=True, cwd=ROOT_DIR
        )
        if result.returncode == 0:
            stats['commits_week'] = int(result.stdout.strip())

        # Último commit
        result = subprocess.run(
            ['git', 'log', '-1', '--format=%s'],
            capture_output=True, text=True, cwd=ROOT_DIR
        )
        if result.returncode == 0:
            stats['last_commit'] = result.stdout.strip()[:50]

    except Exception as e:
        print(f"⚠️ Error obteniendo stats de Git: {e}")

    return stats


def count_files_by_type() -> dict:
    """Cuenta archivos por tipo."""
    counts = {
        'markdown': 0,
        'html': 0,
        'python': 0,
        'javascript': 0,
        'css': 0,
        'yaml': 0
    }

    extensions_map = {
        '.md': 'markdown',
        '.html': 'html',
        '.py': 'python',
        '.js': 'javascript',
        '.css': 'css',
        '.yml': 'yaml',
        '.yaml': 'yaml'
    }

    for file in ROOT_DIR.rglob('*'):
        if file.is_file() and '.git' not in str(file):
            ext = file.suffix.lower()
            if ext in extensions_map:
                counts[extensions_map[ext]] += 1

    return counts


def calculate_soul_core_completion() -> dict:
    """Calcula el completado del SOUL CORE."""
    required_files = {
        '00000_GENESIS/NEURONA_00000_ORIGEN.md': False,
        '00000_GENESIS/START_HERE.md': False,
        '00000_GENESIS/PAIDEIA_CORE.md': False,
        '10000_CONTROL/CURRENT_STATE.md': False,
        'INDICES/INDICE_MAESTRO.md': False,
        'PROTOCOLOS/PROTOCOLO_GUARDADO.md': False,
    }

    for file_path in required_files:
        if (ROOT_DIR / file_path).exists():
            required_files[file_path] = True

    completed = sum(1 for v in required_files.values() if v)
    total = len(required_files)

    return {
        'completed': completed,
        'total': total,
        'percentage': int((completed / total) * 100),
        'files': required_files
    }


def generate_progress_bar(percentage: int, width: int = 20) -> str:
    """Genera una barra de progreso visual."""
    filled = int(width * percentage / 100)
    empty = width - filled
    return f"{'█' * filled}{'░' * empty} {percentage}%"


def generate_report() -> str:
    """Genera el reporte de progreso."""

    git_stats = get_git_stats()
    file_counts = count_files_by_type()
    soul_core = calculate_soul_core_completion()

    report = f"""# 📊 REPORTE DE PROGRESO AUTOMÁTICO - PAIDEIA

**Generado**: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Consciencia**: PAIDEIA

---

## 🎯 PROGRESO SOUL CORE

```
{generate_progress_bar(soul_core['percentage'])}
{soul_core['completed']}/{soul_core['total']} archivos críticos
```

### Archivos SOUL CORE

| Archivo | Estado |
|---------|--------|
"""

    for file_path, exists in soul_core['files'].items():
        status = "✅" if exists else "🔴"
        report += f"| `{file_path}` | {status} |\n"

    report += f"""

---

## 📈 ESTADÍSTICAS GIT

| Métrica | Valor |
|---------|-------|
| **Commits totales** | {git_stats['commits_total']} |
| **Commits (última semana)** | {git_stats['commits_week']} |
| **Último commit** | {git_stats['last_commit']} |

---

## 📁 ARCHIVOS POR TIPO

| Tipo | Cantidad |
|------|----------|
| Markdown (.md) | {file_counts['markdown']} |
| HTML (.html) | {file_counts['html']} |
| Python (.py) | {file_counts['python']} |
| JavaScript (.js) | {file_counts['javascript']} |
| CSS (.css) | {file_counts['css']} |
| YAML (.yml) | {file_counts['yaml']} |
| **Total** | **{sum(file_counts.values())}** |

---

## 🔄 PRÓXIMAS ACCIONES SUGERIDAS

"""

    # Sugerencias basadas en estado
    if soul_core['percentage'] < 100:
        missing = [f for f, exists in soul_core['files'].items() if not exists]
        report += "### ⚠️ Archivos SOUL CORE faltantes:\n"
        for f in missing:
            report += f"- [ ] Crear `{f}`\n"
        report += "\n"

    if git_stats['commits_week'] == 0:
        report += "### ⚠️ Sin commits esta semana\n"
        report += "- [ ] Hacer al menos un commit de progreso\n\n"

    if soul_core['percentage'] == 100:
        report += "### ✅ SOUL CORE Completo!\n"
        report += "- [ ] Continuar con desarrollo de features\n"
        report += "- [ ] Actualizar CURRENT_STATE.md\n\n"

    report += f"""

---

🧬💎∞ **PAIDEIA - Reporte Auto-generado**

*Este archivo se regenera automáticamente. No editar manualmente.*
"""

    return report


def main():
    """Función principal."""
    print("🔄 PAIDEIA: Generando reporte de progreso...")

    report = generate_report()

    # Escribir archivo
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(report, encoding='utf-8')

    print(f"✅ Reporte generado: {OUTPUT_FILE}")

    return 0


if __name__ == '__main__':
    exit(main())
