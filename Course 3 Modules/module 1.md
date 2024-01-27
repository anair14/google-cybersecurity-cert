## Network components, devices and diagrams

In this section of the course,  you will learn about network architecture.

Once you have a foundational understanding of network architecture, sometimes referred to as network design, you will learn about security vulnerabilities inherent in all networks and how malicious actors attempt to exploit them. In this reading, you will review network devices and connections and investigate a simple network diagram similar to those used every day by network security professionals. Essential tasks of a security analyst include setting up the tools, devices, and protocols used to observe and secure network traffic.

#### Devices on a network

Network devices are the devices that maintain information and services for users of a network. These devices connect over wired and wireless connections. After establishing a connection to the network, the devices send data packets. The data packets provide information about the source and the destination of the data.

![img](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/URorDIh9TNiq7e481RWHmQ_85911828bd7c43b38761dd2b520e8df1_CS_R-041_-Edited-S34G001-1-.png?expiry=1705968000000&hmac=Flc_YDFjcnLMgiOmfEfk3h_nyDl5dLDZAV1M5EHoehQ)

#### Devices and desktop computers

Most internet users are familiar with everyday devices, such as personal computers, laptops, mobile phones, and tablets. Each device and desktop computer has a unique MAC address and IP address, which identify it on the network, and a network interface that sends and receives data packets. These devices can connect to the network via a hard wire or a wireless connection.

#### Firewalls

A **firewall** is a network security device that monitors traffic to or from your network. Firewalls can also restrict specific incoming and outgoing network traffic. The organization configures the security rules. Firewalls often reside between the secured and controlled internal network and the untrusted network resources outside the organization, such as the internet.

#### Servers

Servers provide a service for other devices on the network. The devices that connect to a server are called clients. The following graphic outlines this model, which is called the client-server model. In this model, clients send requests to the server for information and services. The server performs the requests for the clients. Common examples include DNS servers that perform domain name lookups for internet sites, file servers that store and retrieve files from a database, and corporate mail servers that organize mail for a company.

![img2](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/FI4hBJhWTEyWNXoKI9EgsA_5a3867623fe5482aa3cb88b2e17fd3f1_m11tx1zMlcjG_2VzVR5QC6doDnVW9U6b0n04lmDZCi1BdjEjt-owNV78CEYLQeX_OoblVT1iYfESmwKKY7KkWUA-CB_bQXn--BroYC9c6GVbiZT1DJimU5CCOfNOz8HTQJUVivm8pNKK7NHRzv3W9INsegVffLpT23LJ2sXvgAdmHUwchtuJksNQwLqw70E?expiry=1705968000000&hmac=DvQPWlyt7ZZN3o0F-CtA4gpQlmPUySgMukDS0A3b-jA)

#### Hubs and switches

Hubs and switches both direct traffic on a local network. A hub is a device that provides a common point of connection for all devices directly connected to it. Hubs additionally repeat all information out to all ports. From a security perspective, this makes hubs vulnerable to eavesdropping. For this reason, hubs are not used as often on modern networks; most organizations use switches instead.

A switch forwards packets between devices directly connected to it. It maintains a MAC address table that matches MAC addresses of devices on the network to port numbers on the switch and forwards incoming data packets according to the destination MAC address.

#### Routers

Routers sit between networks and direct traffic, based on the IP address of the destination network. The IP address of the destination network is contained in the IP header. The router reads the header information and forwards the packet to the next router on the path to the destination. This continues until the packet reaches the destination network. Routers can also include a firewall feature that allows or blocks incoming traffic based on information in the transmission. This stops malicious traffic from entering the private network and damaging the local area network.

#### Modems and wireless access points

#### Modems

Modems usually interface with an internet service provider (ISP). ISPs provide internet connectivity via telephone lines, coaxial cables, fiber-optic cables, or satellites. Modems receive transmissions from the internet and translate them into digital signals that can be understood by the devices on the network. Usually, modems connect to a router that takes the decoded transmissions and sends them on to the local network.

**Note:** Enterprise networks used by large organizations to connect their users and devices often use other broadband technologies to handle high-volume traffic, instead of using a modem.

![img3](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/5cpm9ICmSJCX3MLFfqT6kw_a636fcf868104322ad316bc98fabc3f1_S34G002.png?expiry=1705968000000&hmac=1TbJ0h2b_ijqYrDQ0LB_mQW3woQBgP5M8_Y9K7QT0u0)

#### Wireless access points

A wireless access point sends and receives digital signals over radio waves creating a wireless network. Devices with wireless adapters connect to the access point using Wi-Fi. Wi-Fi refers to a set of standards that are used by network devices to communicate wirelessly. Wireless access points and the devices connected to them use Wi-Fi protocols to send data through radio waves where they are sent to routers and switches and directed along the path to their final destination.

![img4](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/dI_SIruhQeuOZZVnzI6fmA_36c5e1379c0f4990a6fe0ac0c27763f1_S34G003.png?expiry=1705968000000&hmac=NdNjtOQVlK6UilNqlogdq7Jlp9J5pQ4MCe4GgtWXFyU)

#### Using network diagrams as a security analyst

Network diagrams allow network administrators and security personnel to imagine the architecture and design of their organization’s private network.

Network diagrams are topographical maps that show the devices on the network and how they connect. Network diagrams use small representative graphics to portray each network device and dotted lines to show how each device connects to the other. Security analysts use network diagrams to learn about network architecture and how to design networks.

![img5](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/WFixdsOUTMWCAFe3Dwv5tg_062b3fcba27b48acbe496f2aeb68def1_image.png?expiry=1705968000000&hmac=T7aEhqux2Mms6rOaNobxTd2jafDsxdw9uY0lrNPEp5o)

### TCP/IP Model

In this reading, you will build on what you have learned about the Transmission Control Protocol/Internet Protocol (TCP/IP) model, consider the differences between the Open Systems Interconnection (OSI) model and TCP/IP model, and learn how they’re related. Then, you’ll review each layer of the TCP/IP model and go over common protocols used in each layer.

As a security professional, it's important that you understand the TCP/IP model because all communication on a network is organized using network protocols. Network protocols are a language that systems use to communicate with each other. In order for two network systems to successfully communicate with each other, they need to use the same protocol. The two most common models available are the TCP/IP and the OSI model. These models are a representative guideline of how network communications work together and move throughout the network and the host. The examples provided in this course will follow the TCP/IP model.

#### The TCP/IP model

The TCP/IP model is a framework used to visualize how data is organized and transmitted across a network. This model helps network engineers and network security analysts conceptualize processes on the network and communicate where disruptions or security threats occur.

The TCP/IP model has four layers: network access layer, internet layer, transport layer, and application layer. When troubleshooting issues on the network, security professionals can analyze and deduce which layer or layers an attack occurred based on what processes were involved in an incident.

![img6](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/H9jj1YSsSDKlU8c8qzOgsQ_89f77799b50040b08911a8de1012e2f1_CS_R-210_S33G011-edited.png?expiry=1705968000000&hmac=WaAle77IzJp33MSD__PeUq44UEGJuQi21_5EQ-7HeD0)

#### Network access layer

The network access layer, sometimes called the data link layer, deals with the creation of data packets and their transmission across a network. This layer corresponds to the physical hardware involved in network transmission. Hubs, modems, cables, and wiring are all considered part of this layer. The address resolution protocol (ARP) is part of the network access layer. ARP assists IP with directing data packets on the same physical network by mapping IP addresses to MAC addresses on the same physical network.

#### Internet layer

The internet layer, sometimes referred to as the network layer, is responsible for ensuring the delivery to the destination host, which potentially resides on a different network. It ensures IP addresses are attached to data packets to indicate the location of the sender and receiver. The internet layer also determines which protocol is responsible for delivering the data packets and ensures the delivery to the destination host. Here are some of the common protocols that operate at the internet layer:

Internet Protocol (IP). IP sends the data packets to the correct destination and relies on the Transmission Control Protocol/User Datagram Protocol (TCP/UDP) to deliver them to the corresponding service. IP packets allow communication between two networks. They are routed from the sending network to the receiving network. The TCP/UDP retransmits any data that is lost or corrupt.
Internet Control Message Protocol (ICMP). The ICMP shares error information and status updates of data packets. This is useful for detecting and troubleshooting network errors. The ICMP reports information about packets that were dropped or that disappeared in transit, issues with network connectivity, and packets redirected to other routers.
Transport layer

The transport layer is responsible for delivering data between two systems or networks and includes protocols to control the flow of traffic across a network. TCP and UDP are the two transport protocols that occur at this layer.

####    Transmission Control Protocol

The Transmission Control Protocol (TCP) is an internet communication protocol that allows two devices to form a connection and stream data. It ensures that data is reliably transmitted to the destination service. TCP contains the port number of the intended destination service, which resides in the TCP header of a TCP/IP packet.

####    User Datagram Protocol

The User Datagram Protocol (UDP) is a connectionless protocol that does not establish a connection between devices before transmissions. It is used by applications that are not concerned with the reliability of the transmission. Data sent over UDP is not tracked as extensively as data sent using TCP. Because UDP does not establish network connections, it is used mostly for performance sensitive applications that operate in real time, such as video streaming.

####    Application layer

The application layer in the TCP/IP model is similar to the application, presentation, and session layers of the OSI model. The application layer is responsible for making network requests or responding to requests. This layer defines which internet services and applications any user can access. Protocols in the application layer determine how the data packets will interact with receiving devices. Some common protocols used on this layer are:

-   Hypertext transfer protocol (HTTP)

-   Simple mail transfer protocol (SMTP)

-   Secure shell (SSH)

-   File transfer protocol (FTP)

-   Domain name system (DNS)

-   Application layer protocols rely on underlying layers to transfer the data across the network.

-   TCP/IP model versus OSI model

####    The TCP/IP model next to the OSI model

![img7](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/RbNt47PDRTGJZ6q_QtaNMg_9b9098ac04e84c2d8ad04b220c5456f1_CS_R-210_TCP-vs-OSI.png?expiry=1705968000000&hmac=Kn8t8FsVxhY_lfvHRS5le0s0N4K_kRM9Af98O3m3lks)

The OSI visually organizes network protocols into different layers. Network professionals often use this model to communicate with each other about potential sources of problems or security threats when they occur.

The TCP/IP model combines multiple layers of the OSI model. There are many similarities between the two models. Both models define standards for networking and divide the network communication process into different layers. The TCP/IP model is a simplified version of the OSI model.

#### Glossary

**Bandwidth:** The maximum data transmission capacity over a network, measured by bits per second

**Cloud computing:** The practice of using remote servers, application, and network services that are hosted on the internet instead of on local physical devices

**Cloud network:** A collection of servers or computers that stores resources and data in remote data centers that can be accessed via the internet

**Data packet:** A basic unit of information that travels from one device to another within a network

**Hub:** A network device that broadcasts information to every device on the network

**Internet Protocol (IP):** A set of standards used for routing and addressing data packets as they travel between devices on a network

**Internet Protocol (IP) address:** A unique string of characters that identifies the location of a device on the internet

**Local Area Network (LAN):** A network that spans small areas like an office building, a school, or a home

**Media Access Control (MAC) address:** A unique alphanumeric identifier that is assigned to each physical device on a network

**Modem:** A device that connects your router to the internet and brings internet access to the LAN

**Network:** A group of connected devices

**Open systems interconnection (OSI) model:** A standardized concept that describes the seven layers computers use to communicate and send data over the network

**Packet sniffing:** The practice of capturing and inspecting data packets across a network

**Port:** A software-based location that organizes the sending and receiving of data between devices on a network

**Router:** A network device that connects multiple networks together

**Speed:** The rate at which a device sends and receives data, measured by bits per second

**Switch:** A device that makes connections between specific devices on a network by sending and receiving data between them

**TCP/IP model:** A framework used to visualize how data is organized and transmitted across a network

**Transmission Control Protocol (TCP):** An internet communication protocol that allows two devices to form a connection and stream data

**User Datagram Protocol (UDP):** A connectionless protocol that does not establish a connection between devices before transmissions

**Wide Area Network (WAN):** A network that spans a large geographic area like a city, state, or country

