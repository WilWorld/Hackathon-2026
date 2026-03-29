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
    [class="stMarkdownBadge"] {
        white-space: normal !important;
        word-wrap: break-word !important;
        overflow-wrap: anywhere !important;
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

if 'validator' not in st.session_state:
    st.session_state['validator'] = passwordValidator()
validator = st.session_state['validator']

# Persistent variables (safe until referesh)
if 'ruleSet' not in st.session_state:
    st.session_state['ruleSet'] = validator.validate("initial")["descriptions"]
if 'uncoveredRules' not in st.session_state:
    st.session_state['uncoveredRules'] = []
if 'lastRule' not in st.session_state:  
    st.session_state['lastRule'] = 'null'
if 'numberOfAttempts' not in st.session_state:
    st.session_state['numberOfAttempts'] = 0
if "password_saved" not in st.session_state:
    st.session_state["password_saved"] = ""
if 'passwordAttempt' not in st.session_state:
    st.session_state['passwordAttempt'] = st.session_state["password_saved"]

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

# Stats container positioning
statsContainer = st.container(border=True, gap="small")
with statsContainer:
    col1, col2, col3 = st.columns(3)
    
    col1_placeholder = col1.empty()
    col2_placeholder = col2.empty()
    col3_placeholder = col3.empty()

    col1_placeholder.caption("Time: --")
    col2_placeholder.caption("Guesses: --")
    col3_placeholder.caption("Score: --")

# Saves password state across the session
passwordAttempt = st.text_input(
    label="",
    placeholder="Type password to start . . .",
    key="passwordAttempt"
)
st.session_state["password_saved"] = passwordAttempt

if passwordAttempt != "":
    ruleResults = validator.validate(passwordAttempt)["results"]
    find_uncovered(ruleResults)

    print("LENGTH OF RULERESULTS", len(ruleResults))

    # Options for fail messages
    Failmessages = [
        "🧔🏽‍♀️ INCREDIBLE! I never see a password so horrid!",
        "🧔🏽‍♀️ Weak password bring shame to tribe",
        "🧔🏽‍♀️ Password so bad meal escape cage",
        "🧔🏽‍♀️ Mammoth child make better password than this",
        "🧔🏽‍♀️ Password weak. Even sleepy mammoth guess this.",
        "🧔🏽‍♀️ Bad password. Cave baby break in.",
        "🧔🏽‍♀️ You make soft password. No keep tribe safe.",
        "🧔🏽‍♀️ Tiny brain password. Enemy laugh.",
        "🧔🏽‍♀️ Password weak like wet stick.",
        "🧔🏽‍♀️ This password weak. One bonk and enemy inside cave.",
        "🧔🏽‍♀️ You choose bad password. Even slow turtle guess.",
        "🧔🏽‍♀️ Tribe not safe. Password crumble like old bone.",
        "🧔🏽‍♀️ Hunter spot this password from far away.",
        "🧔🏽‍♀️ No good. Password softer than mud.",
        "🧔🏽‍♀️ Enemy guess this fast. You must think harder.",
        "🧔🏽‍♀️ Too easy. Even rock know this password.",
        "🧔🏽‍♀️ Password small. Danger come.",
        "🧔🏽‍♀️ Weak password bring shame to tribe.",
        "🧔🏽‍♀️ No. Try again. Use bigger brain.",
        "🧔🏽‍♀️ Password weak. Tribe in danger.",
        "🧔🏽‍♀️ Bad password. Mammoth walk right in.",
        "🧔🏽‍♀️ Too easy. Cave door wide open.",
        "🧔🏽‍♀️ Enemy guess this before fire start.",
        "🧔🏽‍♀️ Weak. Try again with big brain."
    ]

    # Win/fail message
    if get_ruleResults_sum(ruleResults, len(ruleResults)) == len(ruleResults):
        st.caption("WOW! You did it! Now your rocks and stone are secure")
    else:
        st.caption(random.choice(Failmessages))

    # Columns for splitting rules
    column1, column2 = st.columns(2)

    # Display
    index = len(st.session_state['uncoveredRules'])-1
    if len(st.session_state['uncoveredRules']) < len(st.session_state['ruleSet']):
        with column1:
            st.badge(st.session_state['lastRule'], color="red",  icon="❌")
    
    # Split items here
    bool = False
    for rule in reversed(st.session_state['uncoveredRules']):
        if ruleResults[index]:
            if bool == True:
                with column1:
                    st.badge(rule, color="green", icon="✅")
                bool = False
            else:
                with column2:
                    st.badge(rule, color="green", icon="✅")
                bool = True
        else:
            st.badge(rule, color="red", icon="❌")
        index -= 1

    # Displays meaninful data on password attempts
    passwordStatistics = password_test(passwordAttempt)

    if len(passwordStatistics) > 2:
        col1_placeholder.caption(passwordStatistics[0])
        col2_placeholder.caption(passwordStatistics[1])
        match = re.search(r"\[(.*?)\]", passwordStatistics[2])
        if match:
            score_text = match.group(1)
            color_map = {
                "very weak": "violet",
                "weak": "red",
                "fair": "orange",
                "strong": "yellow",
                "very strong": "green"
            }
            col3_placeholder.caption(f"Score: :{color_map.get(score_text, 'white')}[{score_text}]")
    else:
        col1_placeholder.caption(passwordStatistics[0])
        col2_placeholder.caption(passwordStatistics[1])
        col3_placeholder.caption("Score: --")
else:
    if len(st.session_state['uncoveredRules']) < len(st.session_state['ruleSet']) and st.session_state['lastRule'] != 'null':
        st.badge(st.session_state['lastRule'], color="red", icon="❌")
    for rule in reversed(st.session_state['uncoveredRules']):
        st.badge(rule, color="red", icon="❌")

