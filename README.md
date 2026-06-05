# media-workflow-tools

Python CLI tools for organizing footage and scaffolding video project folders — zero dependencies, pure standard library.

Two command-line tools I built to automate the repetitive parts of my video post-production workflow:

- **`folders.py`** — generates a clean, standardized, numbered project folder structure.
- **`file_organizer.py`** — recursively scans a directory and sorts media files by type, with optional renaming and sequential numbering.

## Requirements

- Python 3.6+
- No third-party packages — everything uses the standard library (`argparse`, `pathlib`, `collections`).

```bash
git clone https://github.com/<your-username>/media-workflow-tools.git
cd media-workflow-tools
```

Optionally make the scripts executable so you can run them directly:

```bash
chmod +x folders.py file_organizer.py
```

---

## `folders.py` — project scaffolding

Creates a numbered folder structure for a new project so every project starts organized the same way.

```
<project>/
├── 10_RAW_VIDEO_<project>/
├── 20_RAW_AUDIO_<project>/
├── 30_ASSETS_<project>/
│   ├── 31_MUSIC_<project>/
│   ├── 32_SFX_<project>/
│   ├── 33_MOTION_GRAPHICS_<project>/
│   ├── 34_PHOTOS_<project>/
│   ├── 35_LOWERTHIRDS_<project>/
│   ├── 36_OVERLAYS_<project>/
│   └── 37_OTHER_<project>/
├── 40_PROJECTS_<project>/
├── 50_EXPORTS_<project>/
├── 60_PROXIES_<project>/
└── 70_SCRATCH_<project>/
```

### Usage

```bash
# Create the structure in the current directory
python3 folders.py MyProject

# Create it somewhere specific
python3 folders.py MyProject --path /Volumes/Media/Clients
```

| Argument | Description |
|----------|-------------|
| `project_name` | Name appended to every folder, keeping folders unique per project. |
| `-p`, `--path` | Destination directory. Defaults to the current directory. |

---

## `file_organizer.py` — media sorting

Recursively scans the **current working directory**, groups files by type, previews what it found, and (after you confirm) moves them into typed folders. Can optionally clean up the now-empty subfolders.

Supported categories and extensions:

| Category | Extensions |
|----------|-----------|
| `VIDEO` | `.mp4`, `.mov` |
| `PHOTO` | `.jpg`, `.png`, `.jpeg` |
| `RAW_PHOTO` | `.dng`, `.arw`, `.cr3` |
| `AUDIO` | `.mp3`, `.wav` |
| `TEXT` | `.txt`, `.doc`, `.docx`, `.pages`, `.pdf`, `.fadein` |
| `SPREADSHEETS` | `.csv`, `.numbers`, `.xlsx`, `.xls` |

The tool shows a summary of what it found and asks for confirmation (`yes`/`no`) before moving anything, and again before deleting empty folders — so nothing happens by surprise.

### Usage

```bash
# Sort everything in the current directory by type
python3 file_organizer.py

# Give files a project name + sequential numbering
python3 file_organizer.py --name BeachShoot

# Also prefix the type folders with the project name
python3 file_organizer.py --name BeachShoot --folder_rename

# Skip certain file types
python3 file_organizer.py -x .mp4 .mov

# Keep the source subfolder name as part of each filename
python3 file_organizer.py --source
```

| Flag | Description |
|------|-------------|
| `--name` | Project name; renames files using the name plus a numbered sequence. |
| `-fr`, `--folder_rename` | Prefix the type folders with the project name. |
| `-x`, `--exclude_filetype` | One or more extensions to leave untouched (e.g. `.mp4 .mov`). |
| `--source` | Include the original parent folder's name in each filename. |

> **Note:** `file_organizer.py` moves files in place within the directory you run it from. Run it on a copy first if you want to be safe.

---

## License

MIT — see [LICENSE](LICENSE).
