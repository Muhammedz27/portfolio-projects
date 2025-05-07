# Resume Chatbot with Detailed Projects

def respond_to_input(user_input):
    user_input = user_input.lower()

    # Education
    if any(word in user_input for word in ["education", "school", "university", "study"]):
        return (
            "I studied Computer Technology at Bowie State University "
            "from September 2020 to May 2025."
        )

    # Skills
    elif any(word in user_input for word in ["skills", "technologies", "tools"]):
        return (
            "Here are some of the technical skills I have:\n"
            "- Microsoft Office Suite\n"
            "- TCP/IP\n"
            "- Hyper V\n"
            "- Windows, Linux, and Mac OS troubleshooting\n"
            "- Software and OS security\n"
            "- Computer networking\n"
            "- Active Directory\n"
            "- WireShark, DNS Configuration, and Nmap\n"
            "- Vulnerability scans\n"
            "- Java and Python coding"
        )

    # General project inquiry
    elif "project" in user_input or "projects" in user_input:
        return (
            "I completed several course projects:\n"
            "1. Wireshark Filter to Analyze Packets\n"
            "2. Running Containerized Applications with Docker\n"
            "3. Vulnerability Analysis, Patch Management & Service Configuration\n"
            "Ask me about any one of them for more details!"
        )

    # Wireshark project
    elif "wireshark" in user_input or "analyze packets" in user_input:
        return (
            "In the 'Wireshark Filter to Analyze Packets' project, I used Wireshark "
            "filter expressions to analyze common internet traffic. I was tasked with capturing "
            "network packets while visiting sites like YouTube.com and CNN.com within a specific time frame."
        )

    # Docker project
    elif "docker" in user_input or "container" in user_input:
        return (
            "In the 'Running Containerized Applications with Docker' project, I installed Docker and "
            "managed containers on several Linux-based systems including Ubuntu, Linux Mint, Ubuntu Server, "
            "and CentOS Server. I ran containerized applications and worked on managing their environments."
        )

    # Vulnerability analysis project
    elif "vulnerability" in user_input or "patch" in user_input or "service configuration" in user_input:
        return (
            "For the 'Vulnerability Analysis, Patch Management & Service Configuration' project, I performed a "
            "vulnerability scan on a virtual machine and identified system weaknesses. I applied the latest patches, "
            "configured firewalls, closed unused ports, and created detailed logs and documentation for all service configurations."
        )

    # Exit
    elif user_input in ["exit", "quit", "bye"]:
        return "Goodbye! Thanks for chatting."

    # Fallback response
    else:
        return (
            "I'm here to talk about my Education, Skills, or Projects. "
            "You can also ask about specific projects like the Wireshark one or the Docker one."
        )


def resume_chatbot():
    print("👋 Hi, I'm your Resume Chatbot! Ask me about my Education, Skills, or Projects.")
    print("Type 'exit' to leave the chat.\n")

    while True:
        user_input = input("You: ")
        response = respond_to_input(user_input)
        print(f"Bot: {response}")
        if "goodbye" in response.lower():
            break


if __name__ == "__main__":
    resume_chatbot()
