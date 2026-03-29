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
       #self.subscribe(ruleOne())
       #self.subscribe(ruleTwo())
       #self.subscribe(ruleThree())
       #self.subscribe(ruleFour())
       #self.subscribe(ruleFive())
       #self.subscribe(ruleSix())
       #self.subscribe(ruleSeven())
       #self.subscribe(ruleEight())
       #self.subscribe(ruleNine())
       #self.subscribe(ruleNeighborStick())
       #self.subscribe(ruleWeaponType())

    def init_random_select(self):
        # Add rule to be randomly selected
        ruleLister = [ruleOne(),
                    ruleTwo(),
                    ruleThree(),
                    ruleFour(),
                    ruleFive(),
                    ruleSix(),
                    ruleSeven(),
                    ruleEight(),
                    ruleNine(),
                    ruleNeighborStick(),
                    ruleWeaponType()]
        
        for need in range(9): # 9 Random Rules are chosen
            left = len(ruleLister)
            print(left)
            randnum = random.randrange(0, left)
            self.subscribe(ruleLister[randnum])
            ruleLister.remove(ruleLister[randnum])
        return True
            
    def subscribe(self, rule: passwordRule) -> None:
        self._rules.append(rule)
        print("new rule added")
    
    def unsub(self, rule: passwordRule) -> None:
        self._rules.remove(rule)
        print("Removed rule")
    
    # Validates all the rules built into the validator, will return arrays of descriptions and booleans
    def validate(self, password: str) -> dict:
        """Notify all rules and collect results"""
        print("::HE HAS ACTIVATED VALIDATE:: ", password)
        print("his rules: ", self._rules)
        results = []
        rule_name = []
        descriptions = []
        all_valid = True
        
        index = 0
        for rule in self._rules:
            is_valid = rule.check(password)
            rule_name = rule.__class__.__name__
            results.append(is_valid)

            print("The result should have been appended: ", results[index])

            index += 1

            desc = getattr(rule, 'description', rule_name)
            descriptions.append(desc)

            if not is_valid:
                all_valid = False
        
        print("///THIS IS THE FINAL RESULT///", results)
        # print("/// DESCTIPTION ///", descriptions)

        return {
            'all_valid': all_valid,
            'results': results,
            'descriptions': descriptions
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
        description = "At least one emoji"
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
        description = "What wiped out the dinos?"
        def check(self, password: str) -> bool:
            answer = ["asteroid", "bigrock"]
            originalPas = password.lower()
            return any(noise in originalPas for noise in answer)

# Rule 9 - Password must be LESS than 45 characters
class ruleNine(passwordRule):
        description = "Less than 35 characters"
        def check(self, password: str) -> bool:
            return len(password) <= 35

#Must include the word "stick"
class ruleNeighborStick(passwordRule):
        description = "Must include the word stick"
        def check(self, password: str) -> bool:
            originalPas = password.lower()
            return "stick" in originalPas
        
# What weapon?
class ruleWeaponType(passwordRule):
    weapon = ["A weapon with a long shaft and a pointed tip, typically of metal, used for thrusting or throwing.",
              "A short, blunt melee weapon crafted from wood, designed for striking, bashing, or bludgeoning in close-quarters combat",
              "A gun causing injury or damage by the emission of rays."]
    weapon_words = ["spear", "club", "raygun"]

    def __init__(self):
        self.choice = random.randint(0, 2)
        self.description = "What weapon is this? " + self.weapon[self.choice]

    def check(self, password: str) -> bool:
        word = self.weapon_words[self.choice]
        originalPas = password.lower()
        return word in originalPas
    
