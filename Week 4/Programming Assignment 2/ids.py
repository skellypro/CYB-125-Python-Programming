# Sean Kelly
# CYB125
# mySploit Intrusion Detection Module
# Complete Phase 2. Data Processing
# You do not need to modify any code in Phase 1 or Phase 2.

import sys



print("""
----------------------------------------------------
             INTRUSION DETECTION MODULE
----------------------------------------------------

Welcome to the mySploit Intrusion Detection Module.

This exercise simulates how an intrusion detection system (IDS)
evaluates security-related events using simple rules and contextual data.

Select an event type to analyze:
  - login: Authentication and access activity
  - file: File system access or modification
  - network: Network traffic and connection behavior

    """)
event_type = input("Enter event type: \n>>> ")


if event_type not in ("login", "file", "network"):
    sys.exit(1)  # exit program on invalid user input

print("""
----------------------------------------------------

Identify the source of the event. Did the event originate
from inside or outside of the network?

Source Options:
  - internal: Originating from within the organization
  - external: Originating from outside the organization

    """)
event_source = input("Enter event source (internal/external):\n>>> ")

if event_source not in ("internal", "external"):
    sys.exit(1)  # exit program on invalid user input


risk = ""  # default

# -------------------------
# LOGIN EVENT TYPE
# -------------------------
if event_type == "login":
    print("""
----------------------------------------------------

Login Event Details:

Enter the username of the account that attempted
and failed to login:""")

    username = input(">>> ")

    if username == "":
        sys.exit(1)  # invalid username
    else:
        username = username.strip().lower()

    str_attempts = input("\nEnter the number of failed login attempts observed:\n>>> ").strip()

    if not str_attempts.isdigit():
        sys.exit(1)  # invalid number
    else:
        attempts = int(str_attempts)

    # PHASE 2. DATA PROCESSING - Write your if / elif / else statements here.

    # My solution will use a normalized score to determine how high the risk is.
    # The scope of the score starts here so all 3 conditions can use the scoring system
    # My scoring system is a float type so the interpreter can utilize any FPU that
    # may be present on the hosting machine.

    # Check to see if the user is privileged (admin or root)
    # for my score multipliers, I am using ternary expressions
    # Unlike C, where it starts with the expression like so: expression ? true value : false value;
    # Pyton's are structured like so: true value if expression else false value
    userMult : float = float(3 if (username in ["admin", "root"]) else 1)

    # Check if internal or external
    # If ternary expressions weren't used, the total lines needed for multiplier assignment
    # Would have added 4 lines of code per multiplier.
    # Future versions of this implementations might see this function of the formula
    # run after event_source has been verified as valid, or as part of the validation
    # Process
    sourceMult : float = float(3 if "external" == event_source  else 1)

    # Calculate a risk score to weigh the severity
    # The scoring system is a way to normalize the attempts
    # In this instance, the score is the product of the login
    # attempts and each multiplier.
    # A call to abs() is used to prevent a score below zero
    eventScore : float = abs(attempts) * userMult * sourceMult

    # Check if in critical bounds
    if 10.0 <= eventScore:
        risk = "Critical"
    # Check if in high bounds
    elif 5.0 <= eventScore:
        risk = "High"
    # Check if in medium bounds
    elif 3.0 <= eventScore:
        risk = "Medium"
    # Otherwise it's in low bounds
    else:
        risk = "Low"

# -------------------------
# FILE EVENT TYPE
# -------------------------
elif event_type == "file":
    print("Not implemented") # You do not need to implement this for Programming Assignment #2

# -------------------------
# NETWORK EVENT TYPE
# -------------------------
elif event_type == "network":
    print("Not implemented") # You do not need to implement this for Programming Assignment #2




# PHASE 3. Final output
print("")
print("----------------------------------------------------")
print("RISK ASSESSMENT RESULT")
print("----------------------------------------------------")
print("Risk Level:", risk) # output risk calculated above
