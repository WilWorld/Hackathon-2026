import streamlit as st

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

# Header
st.markdown('<h1 style="font-family:\'Freckle Face\'; color:#ffbe45;">GAME</h1>', text_alignment="center", unsafe_allow_html=True)
st.divider()

# Sidebar Logo
st.sidebar.image("assets/logo1.png")

#==================== Haggerty Code ====================#

# Persistent variables (safe until referesh)
if 'uncoveredRules' not in st.session_state:
    st.session_state['uncoveredRules'] = []
if 'ruleSet' not in st.session_state:
    st.session_state['ruleSet'] = ["rule1", "rule2", "rule3"] ## Call function to get rules

# Check if a new rule is correct
def find_uncovered(ruleResults):
    start = len(st.session_state['uncoveredRules'])
    for rule in ruleResults[len(st.session_state['uncoveredRules']):]:
        if rule:
            st.session_state['uncoveredRules'].append(st.session_state['ruleSet'][start])
            start += 1
        else:
            break

# Referesh every password attempt
passwordAttempt = st.text_input("Put in that p-ass (word)")
if passwordAttempt != "":
    ruleResults = [True, False, False] ## Call function to recieve results
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
        st.badge(st.session_state['ruleSet'][index], color="red")
else:
    for rule in st.session_state['uncoveredRules']:
        st.badge(rule, color="red")
    if len(st.session_state['uncoveredRules']) < len(st.session_state['ruleSet']):
        st.badge(st.session_state['ruleSet'][len(st.session_state['uncoveredRules'])], color="red")
