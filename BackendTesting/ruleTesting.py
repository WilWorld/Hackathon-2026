from abc import ABC, abstractmethod
from typing import List
import random, re

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
        self.subscribe(ruleTen())
        self.subscribe(ruleEleven())
        self.subscribe(ruleTwelve())
#        self.subscribe(ruleThirteen())
        self.subscribe(ruleWeaponType())
        self.subscribe(ruleReplaceTenthChar())
        self.subscribe(romanNumTest())

    def subscribe(self, rule: passwordRule) -> None:
        self._rules.append(rule)
    
    def unsub(self, rule: passwordRule) -> None:
        self._rules.remove(rule)
    
    # Validates all the rules built into the validator, will return arrays of descriptions and booleans
    def validate(self, password: str) -> dict:
        results = {}
        rule_name = []
        descriptions = []
        all_valid = True
        
        index = 0
        for rule in self._rules:
            is_valid = rule.check(password)
            rule_name = rule.__class__.__name__
            results[index] = is_valid

            index += 1

            desc = getattr(rule, 'description', rule_name)
            descriptions.append(desc)

            if not is_valid:
                all_valid = False
        
        # print("/// DESCTIPTION ///", descriptions)

        return {
            'all_valid': all_valid,
            'results': results,
            'descriptions': descriptions,
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

        def __init__(self, specialChar: str = "!@#$%^&*-_=+():[]"):
             self.specialChar = specialChar
        def check(self, password: str) -> bool:
            return any(c in self.specialChar for c in password)
              
# Rule 6 - Must include one of the following caveman noises (ug, gr, oga)
class ruleSix(passwordRule):
        description = "Includes caveman noise" #(ug, gr, or oga)
        def check(self, password: str) -> bool:
            cavemanNoise = ["ug", "gr", "oga", "ooga", "booga", "grr"]
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
            answer = ["asteroid", "bigrock", "meteor", "meteoroid", "meteorite"]
            originalPas = password.lower()
            return any(noise in originalPas for noise in answer)

# Rule 9 - Password must be LESS than 50 characters
class ruleNine(passwordRule):
        description = "Less than 50 characters"
        def check(self, password: str) -> bool:
            return len(password) <= 50
        
# Rule 10 - Password must include a food caveman would eat (choose one of them): meat, insect, and fruits
class ruleTen(passwordRule):
     description = "The password must include a food caveman would eat" #(choose one of them): meat, insect, and fruits
     def check(self, password: str) -> bool:
          answer = ["meat", "insect", "fruits", "plant", "animal", "bug"]
          originalPas = password.lower()
          return any(food in originalPas for food in answer)

# Rule 11 - Choose from the following 
class ruleEleven(passwordRule):
     description = "The password must include a prehistoric animal" #animals: Megatherium, Camelops, and Aurochs
     def check(self, password: str) -> bool:
          answer = ["megatherium", "camelops","aurochs", "sabertooth", "mammoth", "t-rex", "trex", "bear", "rhino", "Elk", "dino", "saber-tooth", "stego", "lion", "tiger", "wolf", "alligator"]
          originalPas = password.lower()
          return any(animals in originalPas for animals in answer)

# Rule 12 - Must include a place where caveman live
class ruleTwelve(passwordRule):
     description = "The password must include a place where caveman live"
     def check(self, password: str) -> bool:
          answer = ["den", "cave", "hut"]
          originalPas = password.lower()
          return any(live in originalPas for live in answer)
     
# Rule 13 - Password must include a word in reverse order like moon -> noom
class ruleThirteen(passwordRule):
    description = "The password must include a word in reverse order like moon → noom"
    def check(self, password: str) -> bool:
        word = ''.join(c.lower() for c in password if c.isalpha())
        length = len(word)

        for i in range(length):
            for j in range(i + 3, length + 1):
                org = word[i:j]
                reversed = org[::-1]

                if reversed in word and org != reversed:
                    print(f"Match: {org} ↔ {reversed}")
                    return True

        return False
    
# What weapon?
class ruleWeaponType(passwordRule):
    weapons = list(zip(
        ["A weapon with a long shaft and a pointed tip, typically of metal, used for thrusting or throwing.",
         "A short, blunt melee weapon crafted from wood, designed for striking, bashing, or bludgeoning in close-quarters combat",
         "A gun causing injury or damage by the emission of rays."],
        ["spear", "club", "raygun"]
    ))

    def __init__(self):
        self.choice = random.choice(self.weapons)
        self.description = "What weapon is this? " + self.choice[0]

    def check(self, password: str) -> bool:
        return self.choice[1] in password.lower()
    
# Replace 10th character
class ruleReplaceTenthChar(passwordRule):
     symbol = ["z", "o", "i", "a", "l", "c"]

     def __init__(self):
          self.choice = random.randint(0, 5)
          self.description = "The tenth character must be " + self.symbol[self.choice]

     def check(self, password: str) -> bool:
        chosen = self.symbol[self.choice]
        if len(password) < 10:
            return False

        return password[9].lower() == chosen

class romanNumTest(passwordRule):
    description = "Contains Roman numerals that create a product of 50 [I, V, X, L, C, D, M]"
    TARGET_PRODUCT = 50

    def check(self, password: str) -> bool:
        roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        found = [roman_values[c] for c in password if c in roman_values]
        if not found:
            return False
        product = 1
        for value in found:
            product *= value
        return product == self.TARGET_PRODUCT