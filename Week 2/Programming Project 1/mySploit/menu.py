# Sean Kelly
# CYB 125 | Menu-Driven Console Application
# TODO: Simplify this to project specifications (bring it down to week 2) before submitting

# defining a function to print the main menu.
# This will make the sentinel controlled loop in main() cleaner
def print_main_menu():
    print("====================================================")
    print("         CYB 125 | Intro to Scripting Python")
    print("        mySploit Cyber Defense Training Console")
    print("====================================================\n")

    print("Current User   : student")
    print("Execution Mode : Education / Training")
    print("Version        : 0.1\n")

    print("----------------------------------------------------")
    print("                      MAIN MENU")
    print("----------------------------------------------------\n")

    print(" [1] Inventory")
    print("     - Understand what needs to be protected")
    print("     - Identify systems, services, and network components")
    print("     - Learn to automate asset tracking to maintain situational awareness\n")

    print(" [2] Monitoring")
    print("     - Collect data about systems and networks")
    print("     - Explore host logs, network logs, and application events")
    print("     - Learn to automate monitoring to improve visibility and early detection\n")

    print(" [3] Vulnerabilities")
    print("     - Determine weaknesses and misconfiguration that could be exploited")
    print("     - Scan systems for known weaknesses and misconfigurations")
    print("     - Learn how automated scanning helps prioritize defensive actions\n")

    print(" [4] Intrusion Detection")
    print("     - Identify events that indicate potential security incidents")
    print("     - Observe how automated detection identifies suspicious activity")
    print("     - Learn to generate actionable alerts with automated rules\n")

    print(" [5] Response / Remediation")
    print("     - Protect critical systems and limit operation impact of threats")
    print("     - Take action to contain, eradicate, or mitigate threats ")
    print("     - Learn to automate common repetitive tasks for consistency and efficiency\n")

    print(" [9] Help / Glossary / Ethics")
    print("     - Key terminology, frameworks, and ethical guidelines\n")

    print(" [0] Exit Training Console\n")

    print("----------------------------------------------------")
    return int(input(" Select an option (0–9): "))

# defining a function to print the help output. This is simply to make the main program cleaner
def print_help():
    print("----------------------------------------------------")
    print("            HELP / GLOSSARY / ETHICS")
    print("----------------------------------------------------\n")

    print("Welcome to the mySploit Training Console Help Center.\n")

    print("Glossary of Key Terms:")
    print("- Asset: Any system, device, or application you are responsible for protecting.")
    print("- Observability: The ability to collect and view system and network activity data.")
    print("- Vulnerability: A weakness or misconfiguration that could be exploited by an attacker.")
    print("- Indicator of Compromise (IOC): Evidence that a system may have been breached.")
    print("- Automation: Using scripts or rules to perform repetitive or time-critical tasks.\n")

    print("Ethical Guidelines:")
    print("1. Never attempt to access or compromise systems without explicit permission.")
    print("2. All exercises in this console are simulated and safe.")
    print("3. Always maintain confidentiality of sensitive data.")
    print("4. Follow your organization’s or instructor’s rules for responsible cybersecurity practice.")
    print("5. Report any observed issues or bugs in the training environment to your instructor.\n")

    print("Navigation Tips:")
    print("- Use the numeric menu to return to the main screen.")
    print("- Select [0] from any menu to exit the console safely.")
    print("- Read the descriptions carefully to understand the purpose of each module.\n")

    print("Press Enter to return to the Main Menu...")
    input("----------------------------------------------------")
    return None # Returns nothing, but it's a good way to keep track of the end of the function

###############################################
# Creating a main function like this is not   #
#necessary, however this approach can be used #
#if you need a program constructor.           #
#For example:                                 #
#globalVar1: int                              #
#globalVar2: str                              #
#constructor() #set up global variables here  #
#main() #do what the program does             #
#destructor() #do something after the program #
###############################################
def main():
    # This integer variable will handle user input, will be a part of control flow, and is the sentinel variable
    userInput : int

    #A sentinel controlled loop will be used to bring the user back to the main menu, and to control how the program exits
    #Because python does not have do-while loops, sentinel controlled loop is done within an "infinite" loop
    while True:
        ## Prompt the user for some input
        userInput = print_main_menu() ## Print the main menu

        ## Validate the user input. We only have 2 options to validate for now, so continue the loop if the input isn't those 2 options
        if 9 == userInput:
            #calling my user generated function, print_help()
            print_help()
            #input() # "Press Enter to return to the Main Menu"
        ## The sentinel
        elif 0 == userInput:
            # Break from the infinite loop
            break
    return None

main()
