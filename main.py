
from octagon import Octagon


def main():

    side_length = 6.0
    octa = Octagon(side=side_length)

   
    print("\nAttributes:")
    print(f"  Side : {octa.side}")
    print(f"  Angle   : {octa.angle}°")
    print(f"  Const     : {octa.k:.4f}")

    
    print("\nOcto_Parameters:")
    print(f"  Perimeter                  : {octa.perimeter():.2f}")
    print(f"  Area                  : {octa.square():.2f}")

   
    print("\n Circumscribed_Circle (blue):")
    print(f"  Radius         : {octa.circumscribed_radius():.2f}")
    print(f"  Area           : {octa.circumscribed_area():.2f}")

    
    print("\n Inscribed_Circle (green):")
    print(f"  radius              : {octa.inscribed_radius():.2f}")
    print(f"  area               : {octa.inscribed_area():.2f}")

    print("\n" + "=" * 50)
    print("Graphical visualization")
    

    octa.draw()


if __name__ == "__main__":
    main()