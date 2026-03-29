import streamlit as st
from BackendTesting.ruleTesting import passwordValidator
from BackendTesting.zxcvbnTesting import password_test
import re
import random

# Page styling
st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {
        background-color: #8C5F1E;  
    }
    [data-testid="stSidebar"] span,
    [data-testid="stSidebar"] .stText {
        font-size: 110%;
        font-weight: bold;
    }
    [class="stVerticalBlock st-emotion-cache-1gz5zxc e12zf7d53"] {
        background-color: #8C5F1E;  
    }
    [data-testid="stSidebar"] * {
        color: #fff;  
    }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Freckle+Face" rel="stylesheet">
    """,
    unsafe_allow_html=True
)

# Page setup
st.set_page_config(
    page_title="GRUG", 
    page_icon="🗿", 
    layout="wide",
)

# Sidebar Logo
st.sidebar.image("assets/logo1.png")

# Header
st.markdown('<h1 style="font-family:\'Freckle Face\'; color:#ffbe45;">GAME</h1>', text_alignment="center", unsafe_allow_html=True)
st.divider()

#==================== Haggerty Code ====================#
# Win: o|m|l|s|h|E|!|😀ugbigrock

validator = passwordValidator()

# Persistent variables (safe until referesh)
if 'ruleSet' not in st.session_state:
    st.session_state['ruleSet'] = validator.validate("initial")["descriptions"]
if 'uncoveredRules' not in st.session_state:
    st.session_state['uncoveredRules'] = []
if 'lastRule' not in st.session_state:  
    st.session_state['lastRule'] = 'null'
if 'numberOfAttempts' not in st.session_state:
    st.session_state['numberOfAttempts'] = 0

# Check if a new rule is correct
def find_uncovered(ruleResults):
    start = len(st.session_state['uncoveredRules'])
    if get_ruleResults_sum(ruleResults, start) == start:
        print("IT CONTINUED AFTER PRECHECK")
        print("Results: ", get_ruleResults_sum(ruleResults, start), "Start: ", start)
        indexRange = len(ruleResults)
        for index in range(start, indexRange):
            if ruleResults[index]:
                print("index: ", index, "ruleresult of index: ", ruleResults[index])
                st.session_state['uncoveredRules'].append(st.session_state['ruleSet'][index])
                print(" New Rule ")
            else:
                st.session_state['lastRule'] = st.session_state['ruleSet'][index]
                break

# Sum for range of rules
def get_ruleResults_sum(ruleResults, ruleRange):
    rrsum = 0
    for index in range(ruleRange):
        rrsum += ruleResults[index]
    print("ruleResults", ruleResults)
    print("rrsum: ", rrsum)
    return rrsum

# Refreshes every password attempt
passwordAttempt = st.text_input(label="", placeholder="Type password here")
if passwordAttempt != "":
    ruleResults = validator.validate(passwordAttempt)["results"]
    find_uncovered(ruleResults)

    print("LENGTH OF RULERESULTS", len(ruleResults))

    Failmessages = [
        "INCREDIBLE! I never see a password so horrid!",
        "Weak password bring shame to tribe",
        "Password so bad meal escape cage",
        "Mammoth child make better password than this",
        "Password weak. Even sleepy mammoth guess this.",
        "Bad password. Cave baby break in.",
        "You make soft password. No keep tribe safe.",
        "Tiny brain password. Enemy laugh.",
        "Password weak like wet stick.",
        "This password weak. One bonk and enemy inside cave.",
        "You choose bad password. Even slow turtle guess.",
        "Tribe not safe. Password crumble like old bone.",
        "Hunter spot this password from far away.",
        "No good. Password softer than mud.",
        "Enemy guess this fast. You must think harder.",
        "Too easy. Even rock know this password.",
        "Password small. Danger come.",
        "Weak password bring shame to tribe.",
        "No. Try again. Use bigger brain.",
        "Password weak. Tribe in danger.",
        "Bad password. Mammoth walk right in.",
        "Too easy. Cave door wide open.",
        "Enemy guess this before fire start.",
        "Weak. Try again with big brain."
    ]

    # Win/fail message
    if get_ruleResults_sum(ruleResults, len(ruleResults)) == len(ruleResults):
        st.write("WOW! You did it! Now your rocks and stone are secure")
    else:
        st.caption(random.choice(Failmessages))

    # Display
    index = len(st.session_state['uncoveredRules'])-1
    if len(st.session_state['uncoveredRules']) < len(st.session_state['ruleSet']):
        st.badge(st.session_state['lastRule'], color="red",  icon="❌")
    for rule in reversed(st.session_state['uncoveredRules']):
        if ruleResults[index]:
            st.badge(rule, color="green", icon="✅")
        else:
            st.badge(rule, color="red", icon="❌")
        index -= 1

    ### CHARLIE MAKE THE SPACE BETWEEN THE LINES SMALLER!!!!!!
            # -ME
    passwordStatistics = password_test(passwordAttempt)
    if len(passwordStatistics) > 2:
        with st.container(border=True, gap="small"):
            col1, col2, col3 = st.columns(3)
            with col1:
                st.caption(passwordStatistics[0])
            with col2:
                st.caption(passwordStatistics[1])
            with col3:
                match = re.search(r"\[(.*?)\]", passwordStatistics[2])
                
                if match:
                    if match.group(1) == "very weak":
                        st.caption("Score: :violet[very weak]")
                    elif match.group(1) == "weak":
                        st.caption("Score: :red[weak]")
                    elif match.group(1) == "fair":
                        st.caption("Score: :orange[fair]")
                    elif match.group(1) == "strong":
                        st.caption("Score: :yellow[strong]")
                    elif match.group(1) == "very strong":
                        st.caption("Score: :green[very strong]")
                    else:
                        st.caption("error!")
                        print(match.group(1))
    else:
        st.caption(passwordStatistics[0])
        st.caption(passwordStatistics[1])
else:
    if len(st.session_state['uncoveredRules']) < len(st.session_state['ruleSet']) and st.session_state['lastRule'] != 'null':
        st.badge(st.session_state['lastRule'], color="red")
    for rule in reversed(st.session_state['uncoveredRules']):
        st.badge(rule, color="red")

