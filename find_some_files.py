from os import walk, listdir


def find_by_ext(path, ext):
    for _, _, filenames in walk(path):
        return [file for file in filenames if file.endswith(ext)]


def main():
    filepath = ""
    ext = ".py"
    print(f"Main function is executing")
    files = find_by_ext(filepath, ext)
    print(files)


if __name__ == "__main__":
    main()
