class Sidd:
    # Constructor method
    # Jab bhi object create hota hai, __init__ automatically call hota hai
    def __init__(self, name):
        # Instance variable jo object ke saath store hota hai
        self.name = name
    
    # __len__ magic method
    # Jab hum len(object) likhte hain, tab yeh method call hota hai
    def __len__(self):
        i = 0
        # name string ke har character par loop
        for c in self.name:
            i = i + 1   # Counter increase kar rahe hain
        return i       # Total length return karega
        
    # __str__ magic method
    # Jab hum print(object) karte hain, tab yeh method call hota hai
    # User-friendly string representation deta hai
    def __str__(self):
        return f"the name of coder is {self.name}"
    
    # __repr__ magic method
    # Developer-friendly representation deta hai
    # Debugging ke time useful hota hai
    def __repr__(self):
        return f"name('{self.name}')"
    
    # __call__ magic method
    # Agar object ko function ki tarah call karein (obj()),
    # to yeh method execute hota hai
    def __call__(self):
        print("Well here I am !")
