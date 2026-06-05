#!/usr/bin/env python3
import sys
import argparse
from pathlib import Path
from collections import defaultdict

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", help="Input the name of the project here so the files have same name and numbered sequence", default=None)
    parser.add_argument('-fr', '--folder_rename', help='rename folders with project name', action='store_true')
    parser.add_argument('-x', '--exclude_filetype', nargs='*', help="Input any filetype you dont want organized (Ex. '.mp4')", default=[])
    parser.add_argument('--source', help='add this if you want the source folder to be included in the file name', action='store_true')
    args = parser.parse_args()
    dir_path = Path.cwd()
    groups, folders = scan(dir_path, args.exclude_filetype)
    analyze(groups, folders)
    user_confirm("Do you wish to continue? ")
    organize(dir_path, groups, args.name, args.folder_rename,args.source)
    print("Organize complete!")
    user_confirm("Would you like to delete remaining empty subfolders? ")
    folder_remove(folders)

def scan(dir_path, exclusions):
    groups = defaultdict(list)
    filetypes = {"VIDEO" : {".mp4", ".mov"}, "PHOTO": {".jpg", ".png", ".jpeg"}, "RAW_PHOTO": {".dng", ".arw", '.cr3'}, "AUDIO": {".mp3", ".wav"}, "TEXT": {".txt", ".doc", ".docx", ".pages", ".pdf", ".fadein"}, "SPREADSHEETS": {".csv", ".numbers", ".xlsx", ".xls"}}
    folders = []
    print(f"Scanning directory: {dir_path}")
    for child in dir_path.iterdir():
        if child.name.startswith('.'):
            continue
        if child.is_dir():
            folders.append(child)
            sub_groups, subfolders = scan(child, exclusions)
            for key, paths in sub_groups.items():
                groups[key].extend(paths)
            folders.extend(subfolders)
        if child.is_file():
            for f_type, ext in filetypes.items():
                if child.suffix.lower() in ext and child.suffix.lower() not in exclusions:
                    groups[f_type].append(child)
    return groups, folders

def analyze(results, folders):
    print('Scanner found')
    for key, path in results.items():
        print(key, len(path), 'files')
    print (len(folders), "subfolders")
    print("All of these files will be impacted")

def user_confirm(prompt):
    while True:
        response = input(prompt) 
        if response.lower() == 'yes':
            return True
        elif response.lower() in ['n', 'no']:
            sys.exit()
        else:
            print("Response must either be 'yes' or 'no'") 

def folder_create(path, dir_dict, name, folder_rename):
    for key in dir_dict.keys():
        if folder_rename:
            target = path / f'{name}_{key}'
        else:
            target = path / key
        target.mkdir(parents=True, exist_ok=True)

def folder_remove(folders):
    folders.sort(key=lambda f: len(f.parts), reverse=True)
    for folder in folders:
        try:
            folder.rmdir()
        except OSError:
            print(f"Skipping {folder}, because it has files")

def organize(dir_path, paths_dict, arg_name, folder_rename, source):
    folder_create(dir_path, paths_dict, arg_name, folder_rename)
    counter = 0 
    for key, paths in paths_dict.items():
        folder_name = f'{arg_name}_{key}' if folder_rename and arg_name else key
        for path in paths:
            suffix = path.suffix
            if arg_name is None:
                base_name = path.stem if not source else f'{path.parent.name}_{path.stem}'
            else:
                base_name = f'{arg_name}_{key}' if not source else f'{path.parent.name}_{arg_name}_{key}'
            target = dir_path / folder_name / f'{base_name}{suffix}'
            print(f"Moving: {path} -> {target}")
            while True:
                if not target.exists():
                    path.rename(target)
                    counter += 1
                    break
                else:
                    target = dir_path / folder_name / f'{base_name}-{counter}{suffix}'
                    counter += 1

if __name__ == "__main__":
    main()
