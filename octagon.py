import math

import matplotlib.pyplot as plt
from matplotlib import patches


class Octagon:
    def __init__(self, side):

        self.side = side
        self.angle = 135 
        self.k = 1 + math.sqrt(2) 
#===========================================Area&Perimetre
    def square(self):
        
        return 2 * self.k * (self.side ** 2)
        
    def perimeter(self):
        return 8 * self.side


#==============================================Circles
    def circumscribed_radius(self):
    
            return self.side * math.sqrt(1 + 1 / math.sqrt(2))
    
    def circumscribed_area(self):
    
        r = self.circumscribed_radius()
        return math.pi * (r ** 2)
    
    def inscribed_radius(self):
           
            return (self.side / 2) * self.k
    
    def inscribed_area(self):
        
        r = self.inscribed_radius()
        return math.pi * (r ** 2)

    #====================================DRAWING
    def draw(self):
        
        
        
        _ , ax = plt.subplots(figsize=(7, 7))
        
        R = self.circumscribed_radius() 
        r = self.inscribed_radius()     
        
        x_coords = []
        y_coords = []
        for i in range(8):

            angle_rad = math.radians(22.5 + i * 45)
            x_coords.append(R * math.cos(angle_rad))
            y_coords.append(R * math.sin(angle_rad))
            

        x_coords.append(x_coords[0])
        y_coords.append(y_coords[0])


        outer_circle = patches.Circle((0, 0), R, color='blue', fill=False, linestyle='--', linewidth=1.5, label='Описанная окружность')
        ax.add_patch(outer_circle)

        
        inner_circle = patches.Circle((0, 0), r, color='green', fill=False, linestyle='--', linewidth=1.5, label='Вписанная окружность')
        ax.add_patch(inner_circle)

       
        ax.plot(x_coords, y_coords, color='red', linewidth=2.5, label='Октагон')

       
        ax.set_aspect('equal') 
        
    
        margin = R * 1.2
        ax.set_xlim(-margin, margin)
        ax.set_ylim(-margin, margin)


        ax.axhline(0, color='grey', linewidth=0.5)
        ax.axvline(0, color='grey', linewidth=0.5)
        ax.grid(True, linestyle=':', alpha=0.6)
        ax.set_title(f'Октагон со стороной a = {self.side}', fontsize=12)
        ax.legend(loc='upper right')

        
        plt.show()


