import json

class Save():
    def __init__(self,name:str="Save1",pokedex:list=[]):
        self.name = name
        self.pokedex = pokedex
        self.js = { "Name": self.name, "Pokedex":self.pokedex}
            
    def read(self):
        with open('pokedex.json','r') as f:
            read = json.load(f)
            print(read)

    def update(self):
        with open('pokedex.json','w') as f:
            json.dump(self.js,f)

    def modify_name(self,value):
        for i in self.js:
            if i == 'Name':
                self.js[i] = value
        self.update()

    def modify_list(self,option:int,pokemon:str,replace:str):
        for i in self.pokedex:
            if option == 0:
                print("you are useless but getting complexity worse.")
                pass
            if option == 1:
                self.pokedex.append(pokemon)
                self.update()
                break
            if option == 3:
                    if i == pokemon:
                        self.pokedex.remove(pokemon)
                        self.update()
                        break
        if option == 2:
            for i in range(len(self.pokedex)):
                    if self.pokedex[i] == pokemon:
                        self.pokedex[i] = replace
                        self.js['Pokedex'] = self.pokedex
                        self.update()
                        break

    def delete(self):
        self.js['Name'] = "Par default"
        self.js['Pokedex'] = []
        self.update()

if __name__ == "__main__":
    sauvegarde = Save("OK",["Salameche","Pikachu"])
    sauvegarde.update()
    sauvegarde.read()
    sauvegarde.modify_name("YO G SON")
    sauvegarde.read()
    sauvegarde.modify_name("J Is Son")
    sauvegarde.read()
    sauvegarde.modify_list(1,"Bulbizzare",None)
    sauvegarde.read()
    sauvegarde.modify_list(2,'Bulbizzare', 'Florizzare')
    sauvegarde.read()
    sauvegarde.modify_list(3,"Salameche",None)
    sauvegarde.read()
    sauvegarde.modify_name("Nice :)")
    sauvegarde.read()
    sauvegarde.delete()
    sauvegarde.read()