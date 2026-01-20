# Sean Kelly
# CYB 125 | Menu-Driven Console Application
# 


userInput : int
#A centinal controlled loop to bring the user back to the main menu, and to control how the program exits
while userInput != 0:
    print("====================================================")
    print("         CYB 125 | Intro to Scripting Python")
    print("        mySploit Cyber Defense Training Console")
    print("====================================================")
    print("")
    print("Current User   : student")
    print("Execution Mode : Education / Training")
    print("Version        : 0.1")
    print("")
    print("----------------------------------------------------")
    print("                      MAIN MENU")
    print("----------------------------------------------------")
    print("")
    print(" [1] Inventory")
    print("     - Understand what needs to be protected")
    print("     - Identify systems, services, and network components")
    print("     - Learn to automate asset tracking to maintain situational awareness")
    print("")
    print(" [2] Monitoring")
    print("     - Collect data about systems and networks")
    print("     - Explore host logs, network logs, and application events")
    print("     - Learn to automate monitoring to improve visibility and early detection")
    print("")
    print(" [3] Vulnerabilities")
    print("     - Determine weaknesses and misconfiguration that could be exploited")
    print("     - Scan systems for known weaknesses and misconfigurations")
    print("     - Learn how automated scanning helps prioritize defensive actions")
    print("")
    print(" [4] Intrusion Detection")
    print("     - Identify events that indicate potential security incidents")
    print("     - Observe how automated detection identifies suspicious activity")
    print("     - Learn to generate actionable alerts with automated rules")
    print("")
    print(" [5] Response / Remediation")
    print("     - Protect critical systems and limit operation impact of threats")
    print("     - Take action to contain, eradicate, or mitigate threats ")
    print("     - Learn to automate common repetitive tasks for consistency and efficiency")
    print("")
    print(" [9] Help / Glossary / Ethics")
    print("     - Key terminology, frameworks, and ethical guidelines")
    print("")
    print(" [0] Exit Training Console")
    print("")
    print("----------------------------------------------------")
    userInput = int(input(" Select an option (0–9): "))


    match userInput:
        case 0:
            exit(00)
        #case 1:
        #case 2:
        #case 3:
        #case 4:
        #case 5:
        case 9:
            print("----------------------------------------------------")
            print("            HELP / GLOSSARY / ETHICS")
            print("----------------------------------------------------")
            print("")
            print("Welcome to the mySploit Training Console Help Center.")
            print("")
            print("Glossary of Key Terms:")
            print("- Asset: Any system, device, or application you are responsible for protecting.")
            print("- Observability: The ability to collect and view system and network activity data.")
            print("- Vulnerability: A weakness or misconfiguration that could be exploited by an attacker.")
            print("- Indicator of Compromise (IOC): Evidence that a system may have been breached.")
            print("- Automation: Using scripts or rules to perform repetitive or time-critical tasks.")
            print("")
            print("Ethical Guidelines:")
            print("1. Never attempt to access or compromise systems without explicit permission.")
            print("2. All exercises in this console are simulated and safe.")
            print("3. Always maintain confidentiality of sensitive data.")
            print("4. Follow your organization’s or instructor’s rules for responsible cybersecurity practice.")
            print("5. Report any observed issues or bugs in the training environment to your instructor.")
            print("")
            print("Navigation Tips:")
            print("- Use the numeric menu to return to the main screen.")
            print("- Select [0] from any menu to exit the console safely.")
            print("- Read the descriptions carefully to understand the purpose of each module.")
            print("")
            print("Press Enter to return to the Main Menu...")
            input("----------------------------------------------------")
        case _:
            continue