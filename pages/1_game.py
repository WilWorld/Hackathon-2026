import streamlit as st

st.title("Game Page")
st.header("Booga Ooga MF")

# Persistent variables (safe until referesh)
if 'ruleSet' not in st.session_state:
    st.session_state['ruleSet'] = ["rule1", "rule2", "rule3"] ## Call function to get rules
if 'uncoveredRules' not in st.session_state:
    st.session_state['uncoveredRules'] = []
if 'lastRule' not in st.session_state:
    st.session_state['lastRule'] = 'null'
if 'numberOfAttempts' not in st.session_state:
    st.session_state['numberOfAttempts'] = 0

# Check if a new rule is correct
def find_uncovered(ruleResults):
    start = len(st.session_state['uncoveredRules'])
    for rule in ruleResults[len(st.session_state['uncoveredRules']):]:
        if rule:
            st.session_state['uncoveredRules'].append(st.session_state['ruleSet'][start])
            start += 1
        else:
            st.session_state['lastRule'] = st.session_state['ruleSet'][len(st.session_state['uncoveredRules'])]
            break

# Referesh every password attempt
passwordAttempt = st.text_input("Put in that p-ass (word)")
if passwordAttempt != "":
    ruleResults = [False, False, False] ## Call function to recieve results
    find_uncovered(ruleResults)

    # Win/fail message
    if sum(ruleResults) == len(ruleResults):
        st.write("WOW! You did it! Now your rocks and stone are secure :L)")
    else:
        st.write("INCREDIBLE! I've never seen a passoword so horrid and insecure!")

    # Display
    index = 0
    for rule in st.session_state['uncoveredRules']:
        if ruleResults[index]:
            st.badge(rule, color="green")
        else:
            st.badge(rule, color="red")
        index += 1
    if len(st.session_state['uncoveredRules']) < len(st.session_state['ruleSet']):
        st.badge(st.session_state['lastRule'], color="red")
else:
    for rule in st.session_state['uncoveredRules']:
        st.badge(rule, color="red")
    if len(st.session_state['uncoveredRules']) < len(st.session_state['ruleSet']) and st.session_state['lastRule'] != 'null':
        st.badge(st.session_state['lastRule'], color="red")

