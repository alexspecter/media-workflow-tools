#!/usr/bin/env python3
import argparse
from pathlib import Path

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("project_name", help="Input the name of the project here so the folders have unique names")
    parser.add_argument("-p", "--path", help="Input the path of where you would like to generate these folders")
    args = parser.parse_args()

    if args.path:
        path = Path(args.path) / args.project_name
    else:
        path = Path(args.project_name)
    
    create_folders(args.project_name, path)


def create_folders(name, path):
    folders = [f"10_RAW_VIDEO_{name}", f"20_RAW_AUDIO_{name}", f"30_ASSETS_{name}", f"40_PROJECTS_{name}", f"50_EXPORTS_{name}", f"60_PROXIES_{name}", f"70_SCRATCH_{name}"]
    asset_folder = [f"31_MUSIC_{name}", f"32_SFX_{name}", f"33_MOTION_GRAPHICS_{name}", f"34_PHOTOS_{name}", f"35_LOWERTHIRDS_{name}", f"36_OVERLAYS_{name}", f"37_OTHER_{name}"]
    for folder in folders:
        target = path / folder
        target.mkdir(parents=True, exist_ok=True)
    for folder in asset_folder:
        target_assets = path / f"30_ASSETS_{name}" / folder
        target_assets.mkdir(parents=True, exist_ok=True) 
if __name__ == "__main__":
    main() 