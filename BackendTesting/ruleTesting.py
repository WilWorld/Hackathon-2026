from abc import ABC, abstractmethod
from typing import List
import random

# observer abstract
class passwordRule:
    @abstractmethod
    def check(self, password: str):
        """Return is_valid"""
        pass
# subject
class passwordValidator:
    def __init__(self):
        self._rules: List[passwordRule] = []
        self.subscribe(ruleOne())
        self.subscribe(ruleTwo())
        self.subscribe(ruleThree())
        self.subscribe(ruleFour())
        self.subscribe(ruleFive())
        self.subscribe(ruleSix())
        self.subscribe(ruleSeven())
        self.subscribe(ruleEight())
        self.subscribe(ruleNine())

    def subscribe(self, rule: passwordRule) -> None:
        self._rules.append(rule)
        print("new rule added")
    
    def unsub(self, rule: passwordRule) -> None:
        self._rules.remove(rule)
        print("Removed rule")
    
    # Validates all the rules built into the validator, will return arrays of descriptions and booleans
    def validate(self, password: str) -> dict:
        """Notify all rules and collect results"""
        results = {}
        rule_name = []
        descriptions = []
        flags = []
        all_valid = True
        
        index = 0
        for rule in self._rules:
            is_valid = rule.check(password)
            rule_name = rule.__class__.__name__
            results[index] = is_valid
            flags.append(is_valid)

            index += 1

            desc = getattr(rule, 'description', rule_name)
            descriptions.append(f"{desc} - {'met' if is_valid else 'not met'}")

            if not is_valid:
                all_valid = False
        
        print("/// DESCTIPTION ///", descriptions)

        return {
            'all_valid': all_valid,
            'results': results,
            'descriptions': descriptions,
            'flags': flags,
        }
              
# Concrete Observers
# Rule 1 - at Least 12 characters
class ruleOne(passwordRule):
        description = "At least 12 characters"
        def check(self, password: str) -> bool:
            return len(password) >= 12
        
# Rule 2 - Must have a big letter
class ruleTwo(passwordRule):
        description = "At least one uppercase letter"
        def check(self, password: str) -> bool:
            return any(c.isupper() for c in password)
             
# Rule 3 - Must have an emoji
class ruleThree(passwordRule):
        description = "At least one non-ASCII character (emoji or symbol)"
        def check(self, password: str) -> bool:
            return any(ord(c) > 127 for c in password)
             
# Rule 4 - no repeating characters
class ruleFour(passwordRule):
        description = "No consecutive repeating characters"
        def check(self, password: str) -> bool:
            for i in range(len(password) - 1):
                if password[i] == password[i+1]:
                    return False
            return True
             
# Rule 5 - special characters
class ruleFive(passwordRule):
        description = "Contains at least one special character"
        def __init__(self, specialChar: str = "!@#$%^&*-_=+"):
             self.specialChar = specialChar
        def check(self, password: str) -> bool:
            return any(c in self.specialChar for c in password)
              
# Rule 6 - Must include one of the following caveman noises (ug, gr, oga)
class ruleSix(passwordRule):
        description = "Includes caveman noise (ug, gr, or oga)"
        def check(self, password: str) -> bool:
            cavemanNoise = ["ug", "gr", "oga"]
            originalPas = password.lower()
            return any(noise in originalPas for noise in cavemanNoise)
              
# Rule 7 - Tallies must equal 7
class ruleSeven(passwordRule):
        description = "Contains exactly 7 tally marks '|'"
        def check(self, password: str) -> bool:
            tallyCount = password.count('|')
            return tallyCount == 7

# Rule 8 - what killed the dinosaurs?
class ruleEight(passwordRule):
        description = "Contains dinosaur killer keyword (astroid or bigrock)"
        def check(self, password: str) -> bool:
            answer = ["astroid", "bigrock"]
            originalPas = password.lower()
            return any(noise in originalPas for noise in answer)

# Rule 9 - Password must be LESS than 25 characters
class ruleNine(passwordRule):
        description = "Less than 25 characters"
        def check(self, password: str) -> bool:
            return len(password) < 25

#Throwback rules
# Tenth character must be Z
class ruleOneCharZ(passwordRule):
        def check(self, password: str) -> bool:    
            return password[9] == "z"

# Must include one non Latin character  
class ruleLatinChar(passwordRule):
        def check(self, password: str) -> bool:
             return any(ord(c) > 127 for c in password)

# No words are longer than 4      
class ruleWordLength:
        def check(self, password: str) -> bool:
             word = password.split()
             for words in word:
                return len(w) > 5

# All neighbor charcters must form word
class ruleNeighborWords:
        def check(self, password: str) -> bool:
             word = password.split()
             for words in word:
                  return words.alpha()
                
# All symbols must neighbor the letter 'b'
class ruleNeighborB:
        def check(self, password: str) -> bool:
             word = password.split()
             for words in word:
                  return words == 'c'
             
#Must include the word "stick"
class ruleNeighborStick:
        def check(self, password: str) -> bool:
             word = password.split()
             for words in word:
                  return words == "stick"   

RANDOM_THROWBACKS_Rules =[
     ruleOneCharZ,
     ruleLatinChar,
     ruleWordLength,
     ruleNeighborWords,
     ruleNeighborB,
     ruleNeighborStick
]
# Randomize the throwbacks 
class RandomThrowbacks:
     def __init__(self):
          self.rule = random.choice(RANDOM_THROWBACKS_Rules)
     
     def check(self, password):
          return self.rule.check(password)
     

# TESTING STUFF FOR RULES
validator = passwordValidator()

#validator.subscribe(ruleOne())
#validator.subscribe(ruleTwo())
#validator.subscribe(ruleThree())
#validator.subscribe(ruleFour())
#validator.subscribe(ruleFive())
#validator.subscribe(ruleSix())
#validator.subscribe(ruleSeven())
#validator.subscribe(ruleEight())
#validator.subscribe(ruleNine())

pas = validator.validate("oga|ogaUG!astroid")
# Get rules
print("///pas - descriptions///", pas["descriptions"])
print(pas["descriptions"][0])
# Get results
print("///pas = results", pas["results"])  
print(pas["results"][0])  
