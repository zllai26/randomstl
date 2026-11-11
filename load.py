from stl import mesh
from pathlib import Path

folder = Path("stls")

for name in ["triangle", "square", "circle"]:
    path = folder / f"{name}.stl"
    try:
        m = mesh.Mesh.from_file(path)
        print(f"{name}.stl: {len(m)} triangles")
    except FileNotFoundError:
        print(f"{path}.stl: - -")