import json

def carregar():
    with open("data/pessoas.json", "r", encoding="Utf-8") as file: # "r" = ler
        return json.load(file)

def salvar(pessoas):
    with open("data/pessoas.json", "w", encoding="Utf-8") as file: # "w" = ecrever
        json.dump(pessoas, file, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    print(carregar())