import os
import ast


def list_functions_in_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        node = ast.parse(f.read())
    return [n.name for n in ast.walk(node) if isinstance(n, ast.FunctionDef)]


def main():
    readme_lines = ["# Project Functions\n"]

    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".py") and not file.startswith("__"):
                path = os.path.join(root, file)
                functions = list_functions_in_file(path)
                if functions:
                    readme_lines.append(f"## {file}\n")
                    for func in functions:
                        readme_lines.append(f"- `{func}`")
                    readme_lines.append("\n")

    with open("README.md", "w", encoding="utf-8") as f:
        f.write("\n".join(readme_lines))


if __name__ == "__main__":
    main()
