import hashlib 

class Helpers:
    @staticmethod
    def hash(dados:str) -> str :  # sourcery skip: remove-unnecessary-cast
        # Cria um objeto SHA256
        hash_object = hashlib.sha256()      
        # Atualiza o objeto SHA256 com os dados        
        hash_object.update(str(dados).encode('utf-8'))
        
        return str(hash_object.hexdigest())
    
    @staticmethod
    def hash_validado(hash:str, dificuldade:int = 4, prefixo:str ='0') -> bool:
        check = prefixo * dificuldade      
        return  hash.startswith(check)
    
    