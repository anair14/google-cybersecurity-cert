### How intrusions compromise your system

In this section of the course, you learned that every network has inherent vulnerabilities and could become the target of a network attack.

Attackers could have varying motivations for attacking your organization’s network. They may have financial, personal, or political motivations, or they may be a disgruntled employee or an activist who disagrees with the company's values and wants to harm an organization’s operations. Malicious actors can target any network. Security analysts must be constantly alert to potential vulnerabilities in their organization’s network and take quick action to mitigate them.

In this reading, you’ll learn about network interception attacks and backdoor attacks, and the possible impacts these attacks could have on an organization.

#### Network interception attacks 

Network interception attacks work by intercepting network traffic and stealing valuable information or interfering with the transmission in some way.

Malicious actors can use hardware or software tools to capture and inspect data in transit. This is referred to as packet sniffing. In addition to seeing information that they are not entitled to, malicious actors can also intercept network traffic and alter it. These attacks can cause damage to an organization’s network by inserting malicious code modifications or altering the message and interrupting network operations. For example, an attacker can intercept a bank transfer and change the account receiving the funds to one that the attacker controls.

Later in this course you will learn more about malicious packet sniffing, and other types of network interception attacks: on-path attacks and replay attacks.

#### Backdoor attacks

A backdoor attack is another type of attack you will need to be aware of as a security analyst. An organization may have a lot of security measures in place, including cameras, biometric scans and access codes to keep employees from entering and exiting without being seen. However, an employee might work around the security measures by finding a backdoor to the building that is not as heavily monitored, allowing them to sneak out for the afternoon without being seen. 

In cybersecurity, backdoors are weaknesses intentionally left by programmers or system and network administrators that bypass normal access control mechanisms. Backdoors are intended to help programmers conduct troubleshooting or administrative tasks. However, backdoors can also be installed by attackers after they’ve compromised an organization to ensure they have persistent access.

Once the hacker has entered an insecure network through a backdoor, they can cause extensive damage: installing malware, performing a denial of service (DoS) attack, stealing private information or changing other security settings that leaves the system vulnerable to other attacks. A DoS attack is an attack that targets a network or server and floods it with network traffic.

#### Possible impacts on an organization

As you’ve learned already, network attacks can have a significant negative impact on an organization. Let’s examine some potential consequences.

-   **Financial:** When a system is taken offline with a DoS attack, or business operations are halted or slowed down by some other tactic, they prevent a company from performing the tasks that generate revenue. Depending on the size of an organization, interrupted operations can cost millions of dollars. In addition, if a malicious actor gets access to the personal information of the company’s clients or customers, the company may face heavy litigation and settlement costs if customers seek legal recourse.

-   **Reputation:** Attacks can also have a negative impact on the reputation of an organization. If it becomes public knowledge that a company has experienced a cyber attack, the public may become concerned about the security practices of the organization. They may stop trusting the company with their personal information and choose a competitor to fulfill their needs.

-   **Public safety:** If an attack occurs on a government network, this can potentially impact the safety and welfare of the citizens of a country. In recent years, defense agencies across the globe are investing heavily in combating cyber warfare tactics. If a malicious actor gained access to a power grid, a public water system, or even a military defense communication system, the public could face physical harm due to a network intrusion attack.


Terms and definitions from Course 3, Module 3

Active packet sniffing: A type of attack where data packets are manipulated in transit

Botnet: A collection of computers infected by malware that are under the control of a single threat actor, known as the “bot-herder"

Denial of service (DoS) attack: An attack that targets a network or server and floods it with network traffic

Distributed denial of service (DDoS) attack: A type of denial of service attack that uses multiple devices or servers located in different locations to flood the target network with unwanted traffic

Internet Control Message Protocol (ICMP): An internet protocol used by devices to tell each other about data transmission errors across the network

Internet Control Message Protocol (ICMP) flood: A type of DoS attack performed by an attacker repeatedly sending ICMP request packets to a network server

IP spoofing: A network attack performed when an attacker changes the source IP of a data packet to impersonate an authorized system and gain access to a network

On-path attack: An attack where a malicious actor places themselves in the middle of an authorized connection and intercepts or alters the data in transit

Packet sniffing: The practice of capturing and inspecting data packets across a network 

Passive packet sniffing: A type of attack where a malicious actor connects to a network hub and looks at all traffic on the network

Ping of death: A type of DoS attack caused when a hacker pings a system by sending it an oversized ICMP packet that is bigger than 64KB

Replay attack: A network attack performed when a malicious actor intercepts a data packet in transit and delays it or repeats it at another time

Smurf attack: A network attack performed when an attacker sniffs an authorized user’s IP address and floods it with ICMP packets

Synchronize (SYN) flood attack: A type of DoS attack that simulates a TCP/IP connection and floods a server with SYN packets