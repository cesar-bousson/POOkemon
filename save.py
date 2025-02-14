import json

class Save():
    def __init__(self,name:str="Save1",pokedex:list=[]):
        self.name = name
        self.pokedex = pokedex
        self.data = """{"Name":self.name,
                     "Pokedex":self.pokedex
                     }"""
    
    # def create(self):
    #     """Create a backup and save it to JSON file"""
    #     save = json.dump({"Name":self.name,"Pokedex":self.pokedex})
    #     with open('pokedex.json','w') as f:
    #         pass
    
            
    def read(self):
        print(type(self.data))
        data = json.loads(self.data)
        print(data)


    def update():
        pass

    def delete():
        pass

sauvegarde = Save("OK",[])
sauvegarde.read()