## Introduction to network protocols

Common network protocols
In this section of the course, you learned about network protocols and how they organize communication over a network. This reading will discuss network protocols in more depth and review some basic protocols that you have learned previously. You will also learn new protocols and discuss some of the ways protocols are involved in network security.

#### Overview of network protocols

A network protocol is a set of rules used by two or more devices on a network to describe the order of delivery and the structure of data. Network protocols serve as instructions that come with the information in the data packet. These instructions tell the receiving device what to do with the data. Protocols are like a common language that allows devices all across the world to communicate with and understand each other.

Even though network protocols perform an essential function in network communication, security analysts should still understand their associated security implications. Some protocols have vulnerabilities that malicious actors exploit. For example, a nefarious actor could use the Domain Name System (DNS) protocol, which resolves web addresses to IP addresses, to divert traffic from a legitimate website to a malicious website containing malware. You’ll learn more about this topic in upcoming course materials.

#### Three categories of network protocols

Network protocols can be divided into three main categories: communication protocols, management protocols, and security protocols. There are dozens of different network protocols, but you don’t need to memorize all of them for an entry-level security analyst role. However, it’s important for you to know the ones listed in this reading.

#### Communication protocols

Communication protocols govern the exchange of information in network transmission. They dictate how the data is transmitted between devices and the timing of the communication. They also include methods to recover data lost in transit. Here are a few of them.

Transmission Control Protocol (TCP) is an internet communication protocol that allows two devices to form a connection and stream data. TCP uses a three-way handshake process. First, the device sends a synchronize (SYN) request to a server. Then the server responds with a SYN/ACK packet to acknowledge receipt of the device's request. Once the server receives the final ACK packet from the device, a TCP connection is established. In the TCP/IP model, TCP occurs at the transport layer.

User Datagram Protocol (UDP) is a connectionless protocol that does not establish a connection between devices before a transmission. This makes it less reliable than TCP. But it also means that it works well for transmissions that need to get to their destination quickly. For example, one use of UDP is for internet gaming transmissions. In the TCP/IP model, UDP occurs at the transport layer.

Hypertext Transfer Protocol (HTTP) is an application layer protocol that provides a method of communication between clients and website servers. HTTP uses port 80. HTTP is considered insecure, so it is being replaced on most websites by a secure version, called HTTPS. However, there are still many websites that use the insecure HTTP protocol. In the TCP/IP model, HTTP occurs at the application layer.

Domain Name System (DNS) is a protocol that translates internet domain names into IP addresses. When a client computer wishes to access a website domain using their internet browser, a query is sent to a dedicated DNS server. The DNS server then looks up the IP address that corresponds to the website domain. DNS normally uses UDP on port 53. However, if the DNS reply to a request is large, it will switch to using the TCP protocol. In the TCP/IP model, DNS occurs at the application layer.

#### Management Protocols

The next category of network protocols is management protocols. Management protocols are used for monitoring and managing activity on a network. They include protocols for error reporting and optimizing performance on the network.

Simple Network Management Protocol (SNMP) is a network protocol used for monitoring and managing devices on a network. SNMP can reset a password on a network device or change its baseline configuration. It can also send requests to network devices for a report on how much of the network’s bandwidth is being used up. In the TCP/IP model, SNMP occurs at the application layer.

Internet Control Message Protocol (ICMP) is an internet protocol used by devices to tell each other about data transmission errors across the network. ICMP is used by a receiving device to send a report to the sending device about the data transmission. ICMP is commonly used as a quick way to troubleshoot network connectivity and latency by issuing the “ping” command on a Linux operating system. In the TCP/IP model, ICMP occurs at the internet layer.

#### Security Protocols

Security protocols are network protocols that ensure that data is sent and received securely across a network. Security protocols use encryption algorithms to protect data in transit. Below are some common security protocols.

Hypertext Transfer Protocol Secure (HTTPS) is a network protocol that provides a secure method of communication between clients and website servers. HTTPS is a secure version of HTTP that uses secure sockets layer/transport layer security (SSL/TLS) encryption on all transmissions so that malicious actors cannot read the information contained. HTTPS uses port 443. In the TCP/IP model, HTTPS occurs at the application layer.

Secure File Transfer Protocol (SFTP) is a secure protocol used to transfer files from one device to another over a network. SFTP uses secure shell (SSH), typically through TCP port 22. SSH uses Advanced Encryption Standard (AES) and other types of encryption to ensure that unintended recipients cannot intercept the transmissions. In the TCP/IP model, SFTP occurs at the application layer. SFTP is used often with cloud storage. Every time a user uploads or downloads a file from cloud storage, the file is transferred using the SFTP protocol.

**Note:** The encryption protocols mentioned do not conceal the source or destination IP address of network traffic. This means a malicious actor can still learn some basic information about the network traffic if they intercept it.

In previous readings and videos, you learned how network protocols organize the sending and receiving of data across a network. You also learned that protocols can be divided into three categories: communication protocols, management protocols, and security protocols.

This reading will introduce you to a few additional concepts and protocols that will come up regularly in your work as a security analyst. Some protocols are assigned port numbers by the Internet Assigned Numbers Authority (IANA). These port numbers are included in the description of each protocol, if assigned.

#### Network Address Translation

The devices on your local home or office network each have a private IP address that they use to communicate directly with each other. In order for the devices with private IP addresses to communicate with the public internet, they need to have a public IP address. Otherwise, responses will not be routed correctly. Instead of having a dedicated public IP address for each of the devices on the local network, the router can replace a private source IP address with its public IP address and perform the reverse operation for responses. This process is known as Network Address Translation (NAT) and it generally requires a router or firewall to be specifically configured to perform NAT. NAT is a part of layer 2 (internet layer) and layer 3 (transport layer) of the TCP/IP model.

#### Dynamic Host Configuration Protocol

Dynamic Host Configuration Protocol (DHCP) is in the management family of network protocols. DHCP is an application layer protocol used on a network to configure devices. It assigns a unique IP address and provides the addresses of the appropriate DNS server and default gateway for each device. DHCP servers operate on UDP port 67 while DHCP clients operate on UDP port 68.

####    Address Resolution Protocol

By now, you are familiar with IP and MAC addresses. You’ve learned that each device on a network has both an IP address that identifies it on the network and a MAC address that is unique to that network interface. A device’s IP address may change over time, but its MAC address is permanent. Address Resolution Protocol (ARP) is mainly a network access layer protocol in the TCP/IP model used to translate the IP addresses that are found in data packets into the MAC address of the hardware device.

Each device on the network performs ARP and keeps track of matching IP and MAC addresses in an ARP cache. ARP does not have a specific port number.

####    Telnet 

Telnet is an application layer protocol that allows a device to communicate with another device or server. Telnet sends all information in clear text. It uses command line prompts to control another device similar to secure shell (SSH), but Telnet is not as secure as SSH. Telnet can be used to connect to local or remote devices and uses TCP port 23. 

####    Secure shell

Secure shell protocol (SSH) is used to create a secure connection with a remote system. This application layer protocol provides an alternative for secure authentication and encrypted communication. SSH operates over the TCP port 22 and is a replacement for less secure protocols, such as Telnet.

####    Post office protocol

Post office protocol (POP) is an application layer (layer 4 of the TCP/IP model) protocol used to manage and retrieve email from a mail server. Many organizations have a dedicated mail server on the network that handles incoming and outgoing mail for users on the network. User devices will send requests to the remote mail server and download email messages locally. If you have ever refreshed your email application and had new emails populate in your inbox, you are experiencing POP and internet message access protocol (IMAP) in action. Unencrypted, plaintext authentication uses TCP/UDP port 110 and encrypted emails use Secure Sockets Layer/Transport Layer Security (SSL/TLS) over TCP/UDP port 995.  When using POP, mail has to finish downloading on a local device before it can be read and it does not allow a user to sync emails.

####    Internet Message Access Protocol (IMAP)

IMAP is used for incoming email. It downloads the headers of emails, but not the content. The content remains on the email server, which allows users to access their email from multiple devices. IMAP uses TCP port 143 for unencrypted email and TCP port 993 over the TLS protocol. Using IMAP allows users to partially read email before it is finished downloading and to sync emails. However, IMAP is slower than POP3.

####    Simple Mail Transfer Protocol

Simple Mail Transfer Protocol (SMTP) is used to transmit and route email from the sender to the recipient’s address. SMTP works with Message Transfer Agent (MTA) software, which searches DNS servers to resolve email addresses to IP addresses, to ensure emails reach their intended destination. SMTP uses TCP/UDP port 25 for unencrypted emails and TCP/UDP port 587 using TLS for encrypted emails. The TCP port 25 is often used by high-volume spam. SMTP helps to filter out spam by regulating how many emails a source can send at a time.

####    Protocols and port numbers

Remember that port numbers are used by network devices to determine what should be done with the information contained in each data packet once they reach their destination. Firewalls can filter out unwanted traffic based on port numbers. For example, an organization may configure a firewall to only allow access to TCP port 995 (POP3) by IP addresses belonging to the organization.

As a security analyst, you will need to know about many of the protocols and port numbers mentioned in this course. They may be used to determine your technical knowledge in interviews, so it’s a good idea to memorize them. You will also learn about new protocols on the job in a security position.

#### Introduction to wireless communication protocols

![img8](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/xRV4czFOTUeQoV2vrMyMeg_d23346290329425da28d901333b11af1_KRMIlg0NE-hyueu8ieJBVc92c_gZAut6oOyRG0iOjP58SBeS6AojyB3piYq3ZOtOCf1kwrG62COp1ei3Uih_CcoNT2_QdtdaHyEchUsGTcmreFbywK_tUWZJGhMD3Tji9hxIUjH-yQAD8RSKpTbtJDHXD88IOpsqzlu8MCJotlno6JixxiW8pmiYFuzqHZ1bZhfT3cMFIZxI3sPnCh_BnizMW3y21VJuVZcX?expiry=1706054400000&hmac=jppzO9I1duHKcqJBK--H9lNR6SSLdoMwIpsjeLe1gqE)

Many people today refer to wireless internet as Wi-Fi. **Wi-Fi** refers to a set of standards that define communication for wireless LANs. Wi-Fi is a marketing term commissioned by the Wireless Ethernet Compatibility Alliance (WECA). WECA has since renamed their organization Wi-Fi Alliance.

Wi-Fi standards and protocols are based on the 802.11 family of internet communication standards determined by the Institute of Electrical and Electronics Engineers (IEEE). So, as a security analyst, you might also see Wi-Fi referred to as IEEE 802.11.

Wi-Fi communications are secured by wireless networking protocols. Wireless security protocols have evolved over the years, helping to identify and resolve vulnerabilities with more advanced wireless technologies.

In this reading, you will learn about the evolution of wireless security protocols from WEP to WPA, WPA2, and WPA3. You’ll also learn how the Wireless Application Protocol was used for mobile internet communications.

#### Wired Equivalent Privacy

Wired equivalent privacy (WEP) is a wireless security protocol designed to provide users with the same level of privacy on wireless network connections as they have on wired network connections. WEP was developed in 1999 and is the oldest of the wireless security standards.

WEP is largely out of use today, but security analysts should still understand WEP in case they encounter it. For example, a network router might have used WEP as the default security protocol and the network administrator never changed it. Or, devices on a network might be too old to support newer Wi-Fi security protocols. Nevertheless, a malicious actor could potentially break the WEP encryption, so it’s now considered a high-risk security protocol.

#### Wi-Fi Protected Access

Wi-Fi Protected Access (WPA) was developed in 2003 to improve upon WEP, address the security issues that it presented, and replace it. WPA was always intended to be a transitional measure so backwards compatibility could be established with older hardware.

The flaws with WEP were in the protocol itself and how the encryption was used. WPA addressed this weakness by using a protocol called Temporal Key Integrity Protocol (TKIP). WPA encryption algorithm uses larger secret keys than WEPs, making it more difficult to guess the key by trial and error.

WPA also includes a message integrity check that includes a message authentication tag with each transmission. If a malicious actor attempts to alter the transmission in any way or resend at another time, WPA’s message integrity check will identify the attack and reject the transmission.

Despite the security improvements of WPA, it still has vulnerabilities. Malicious actors can use a key reinstallation attack (or KRACK attack) to decrypt transmissions using WPA. Attackers can insert themselves in the WPA authentication handshake process and insert a new encryption key instead of the dynamic one assigned by WPA. If they set the new key to all zeros, it is as if the transmission is not encrypted at all.

Because of this significant vulnerability, WPA was replaced with an updated version of the protocol called WPA2.

#### WPA2 & WPA3

#### WPA2

The second version of Wi-Fi Protected Access—known as WPA2—was released in 2004. WPA2 improves upon WPA by using the Advanced Encryption Standard (AES). WPA2 also improves upon WPA’s use of TKIP. WPA2 uses the Counter Mode Cipher Block Chain Message Authentication Code Protocol (CCMP), which provides encapsulation and ensures message authentication and integrity. Because of the strength of WPA2, it is considered the security standard for all Wi-Fi transmissions today. WPA2, like its predecessor, is vulnerable to KRACK attacks. This led to the development of WPA3 in 2018.

#### Personal

WPA2 personal mode is best suited for home networks for a variety of reasons. It is easy to implement, initial setup takes less time for personal than enterprise version. The global passphrase for WPA2 personal version needs to be applied to each individual computer and access point in a network. This makes it ideal for home networks, but unmanageable for organizations.

#### Enterprise

WPA2 enterprise mode works best for business applications. It provides the necessary security for wireless networks in business settings. The initial setup is more complicated than WPA2 personal mode, but enterprise mode offers individualized and centralized control over the Wi-Fi access to a business network. This means that network administrators can grant or remove user access to a network at any time. Users never have access to encryption keys, this prevents potential attackers from recovering network keys on individual computers.

####    WPA3

-   WPA3 is a secure Wi-Fi protocol and is growing in usage as more WPA3 compatible devices are released. These are the key differences between WPA2 and WPA3:

-   WPA3 addresses the authentication handshake vulnerability to KRACK attacks, which is present in WPA2.

-   WPA3 uses Simultaneous Authentication of Equals (SAE), a password-authenticated, cipher-key-sharing agreement. This prevents attackers from downloading data from wireless network connections to their systems to attempt to decode it.

-   WPA3 has increased encryption to make passwords more secure  by using 128-bit encryption, with WPA3-Enterprise mode offering optional 192-bit encryption.

### Glossary

**Address Resolution Protocol (ARP)**: A network protocol used to determine the MAC address of the next router or device on the path

**Cloud-based firewalls:** Software firewalls that are hosted by the cloud service provider

**Controlled zone:** A subnet that protects the internal network from the uncontrolled zone

**Domain Name System (DNS):** A networking protocol that translates internet domain names into IP addresses

**Encapsulation:** A process performed by a VPN service that protects your data by wrapping sensitive data in other data packets

**Firewall:** A network security device that monitors traffic to or from your network

**Forward proxy server:** A server that regulates and restricts a person’s access to the internet

**Hypertext Transfer Protocol (HTTP):** An application layer protocol that provides a method of communication between clients and website servers

**Hypertext Transfer Protocol Secure (HTTPS):** A network protocol that provides a secure method of communication between clients and servers

**IEEE 802.11 (Wi-Fi):** A set of standards that define communication for wireless LANs

**Network protocols:** A set of rules used by two or more devices on a network to describe the order of delivery of data and the structure of data

**Network segmentation:** A security technique that divides the network into segments

**Port filtering:** A firewall function that blocks or allows certain port numbers to limit unwanted communication

**Proxy server:** A server that fulfills the requests of its clients by forwarding them to other servers

**Reverse proxy server:** A server that regulates and restricts the internet's access to an internal server

**Secure File Transfer Protocol (SFTP):** A secure protocol used to transfer files from one device to another over a network

**Secure shell (SSH):** A security protocol used to create a shell with a remote system 

**Security zone:** A segment of a company’s network that protects the internal network from the internet

**Simple Network Management Protocol (SNMP):** A network protocol used for monitoring and managing devices on a network

**Stateful:** A class of firewall that keeps track of information passing through it and proactively filters out threats 

**Stateless:** A class of firewall that operates based on predefined rules and does not keep track of information from data packets

**Subnetting:** The subdivision of a network into logical groups called subnets

**Transmission Control Protocol (TCP):** An internet communication protocol that allows two devices to form a connection and stream data

**Uncontrolled zone:** The portion of the network outside the organization

**Virtual private network (VPN):** A network security service that changes your public IP address and masks your virtual location so that you can keep your data private when you are using a public network like the internet

**Wi-Fi Protected Access (WPA):** A wireless security protocol for devices to connect to the internet