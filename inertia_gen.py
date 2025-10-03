import sys
import math

def compute_inertia(shape, mass, size):
    if shape == "box":
        x, y, z = size["x"], size["y"], size["z"]
        ixx = (1/12) * mass * (y**2 + z**2)
        iyy = (1/12) * mass * (x**2 + z**2)
        izz = (1/12) * mass * (x**2 + y**2)

    elif shape == "cylinder":
        r, h = size["r"], size["h"]
        ixx = (1/12) * mass * (3 * r**2 + h**2)
        iyy = ixx
        izz = (1/2) * mass * r**2

    elif shape == "sphere":
        r = size["r"]
        ixx = iyy = izz = (2/5) * mass * r**2

    else:
        raise ValueError("Unsupported shape: " + shape)

    return ixx, iyy, izz


def generate_sdf_inertial(mass, shape, size):
    ixx, iyy, izz = compute_inertia(shape, mass, size)

    sdf = f"""
    <inertial>
      <mass>{mass}</mass>
      <inertia>
        <ixx>{ixx}</ixx>
        <ixy>0</ixy>
        <ixz>0</ixz>
        <iyy>{iyy}</iyy>
        <iyz>0</iyz>
        <izz>{izz}</izz>
      </inertia>
    </inertial>

"""
    return sdf


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("用法:")
        print("  python inertia_gen.py box mass x y z")
        print("  python inertia_gen.py cylinder mass r h")
        print("  python inertia_gen.py sphere mass r")
        sys.exit(1)

    shape = sys.argv[1].lower()
    mass = float(sys.argv[2])

    if shape == "box" and len(sys.argv) == 6:
        size = {"x": float(sys.argv[3]), "y": float(sys.argv[4]), "z": float(sys.argv[5])}
    elif shape == "cylinder" and len(sys.argv) == 5:
        size = {"r": float(sys.argv[3]), "h": float(sys.argv[4])}
    elif shape == "sphere" and len(sys.argv) == 4:
        size = {"r": float(sys.argv[3])}
    else:
        print("输入参数错误，请检查格式！")
        sys.exit(1)

    
    print(generate_sdf_inertial(mass, shape, size))
