import streamlit as st
from BackendTesting.ruleTesting import passwordValidator
from BackendTesting.zxcvbnTesting import password_test

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

# Sidebar Logo
st.sidebar.image("assets/logo1.png")

# Header
st.markdown('<h1 style="font-family:\'Freckle Face\'; color:#ffbe45;">GAME</h1>', text_alignment="center", unsafe_allow_html=True)
st.divider()

#==================== Haggerty Code ====================#
# Win: o|m|l|s|h|E|!|😀ugbigrock

#Smart rock, play evanescence
#Smart rock, play cranberries
#Smart rock, play radiohead

validator = passwordValidator()

# Persistent variables (safe until referesh)
if 'set_rules' not in st.session_state:
    st.session_state['set_rules'] = validator.init_random_select()
if 'ruleSet' not in st.session_state:
    st.session_state['ruleSet'] = validator.validate("initial")["descriptions"]
    print(st.session_state['ruleSet'])
    print(validator.validate("initial"))
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

# Refereshes every password attempt
passwordAttempt = st.text_input("Put in that p-ass (word)")
if passwordAttempt != "":
    ruleResults = validator.validate(passwordAttempt)['results']
    print("password: ", passwordAttempt)
    print("results: ", ruleResults)
    print("the whole thing: ", validator.validate(passwordAttempt))
    print("jsut results: ", validator.validate(passwordAttempt)['results'])
    find_uncovered(ruleResults)

    print("LENGTH OF RULERESULTS", len(ruleResults))

    # Win/fail message
    if get_ruleResults_sum(ruleResults, len(ruleResults)) == len(ruleResults):
        st.write("WOW! You did it! Now your rocks and stone are secure :L)")
    else:
        st.write("INCREDIBLE! I've never seen a passoword so horrid and insecure!")

    # Display
    index = len(st.session_state['uncoveredRules'])-1
    if len(st.session_state['uncoveredRules']) < len(st.session_state['ruleSet']):
        st.badge(st.session_state['lastRule'], color="red")
    for rule in reversed(st.session_state['uncoveredRules']):
        if ruleResults[index]:
            st.badge(rule, color="green")
        else:
            st.badge(rule, color="red")
        index -= 1

    ### CHARLIE MAKE THE SPACE BETWEEN THE LINES SMALLER!!!!!!
            # -ME
    passwordStatistics = password_test(passwordAttempt)
    if len(passwordStatistics) > 2:
        st.caption(passwordStatistics[0])
        st.caption(passwordStatistics[1])
        st.caption(passwordStatistics[2])
    else:
        st.caption(passwordStatistics[0])
        st.caption(passwordStatistics[1])
else:
    if len(st.session_state['uncoveredRules']) < len(st.session_state['ruleSet']) and st.session_state['lastRule'] != 'null':
        st.badge(st.session_state['lastRule'], color="red")
    for rule in reversed(st.session_state['uncoveredRules']):
        st.badge(rule, color="red")

