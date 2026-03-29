from abc import ABC, abstractmethod
from typing import List

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

    def subscribe(self, rule: passwordRule) -> None:
        self._rules.append(rule)
        print("new rule added")
    
    def unsub(self, rule: passwordRule) -> None:
        self._rules.remove(rule)
        print("Removed rule")
    
    def validate(self, password: str) -> dict:
        """Notify all rules and collect results"""
        results = {}
        all_valid = True
        
        for rule in self._rules:
            is_valid = rule.check(password)
            rule_name = rule.__class__.__name__
            results[rule_name] = is_valid
            if not is_valid:
                all_valid = False
        
        return {
            'all_valid': all_valid,
            'results': results,
        }
    
    def checkRule(self, rule: passwordRule, password: str) -> bool:
        return rule.check(password)
              
# Concrete Observers
# Rule 1 - at Least 12 characters
class ruleOne(passwordRule):
        def check(self, password: str) -> bool:
            return len(password) >= 12
        
# Rule 2 - Must have a big letter
class ruleTwo(passwordRule):
        def check(self, password: str) -> bool:
            return any(c.isupper() for c in password)
             
# Rule 3 - Must have an emoji
class ruleThree(passwordRule):
        def check(self, password: str) -> bool:
            return any(ord(c) > 127 for c in password)
             
# Rule 4 - no repeating characters
class ruleFour(passwordRule):
        def check(self, password: str) -> bool:
            for i in range(len(password) - 1):
                if password[i] == password[i+1]:
                    return False
            return True
             
# Rule 5 - special characters
class ruleFive(passwordRule):
        def __init__(self, specialChar: str = "!@#$%^&*-_=+"):
             self.specialChar = specialChar
        def check(self, password: str) -> bool:
            return any(c in self.specialChar for c in password)
              
# Rule 6 - Must include one of the following caveman noises (ug, gr, oga)
class ruleSix(passwordRule):
        def check(self, password: str) -> bool:
            cavemanNoise = ["ug", "gr", "oga"]
            originalPas = password.lower()
            return any(noise in originalPas for noise in cavemanNoise)
              
# Rule 7 - Tallies must equal 7
class ruleSeven(passwordRule):
        def check(self, password: str) -> bool:
            tallyCount = password.count('|')
            return tallyCount == 7

# Rule 8 - what killed the dinosaurs?
class ruleEight(passwordRule):
        def check(self, password: str) -> bool:
            answer = ["astroid", "bigrock"]
            originalPas = password.lower()
            return any(noise in originalPas for noise in answer)

# Rule 9 - Password must be LESS than 25 characters
class ruleNine(passwordRule):
        def check(self, password: str) -> bool:
            return len(password) < 25


# TESTING STUFF FOR RULES
validator = passwordValidator()

validator.subscribe(ruleOne())
validator.subscribe(ruleTwo())
validator.subscribe(ruleThree())
validator.subscribe(ruleFour())
validator.subscribe(ruleFive())
validator.subscribe(ruleSix())
validator.subscribe(ruleSeven())
validator.subscribe(ruleEight())
validator.subscribe(ruleNine())


password = "oga"
print(validator.validate(password))

print(validator.checkRule(ruleOne(), password))