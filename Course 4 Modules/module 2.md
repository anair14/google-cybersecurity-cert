### Package managers for installing applications

Previously, you learned about Linux distributions and that different distributions derive from different sources, such as Debian or Red Hat Enterprise Linux distribution. You were also introduced to package managers, and learned that Linux applications are commonly distributed through package managers. In this reading, you’ll apply this knowledge to learn more about package managers. 

#### Introduction to package managers

A package is a piece of software that can be combined with other packages to form an application. Some packages may be large enough to form applications on their own. 

Packages contain the files necessary for an application to be installed. These files include dependencies, which are supplemental files used to run an application. 

Package managers can help resolve any issues with dependencies and perform other management tasks. A package manager is a tool that helps users install, manage, and remove packages or applications. Linux uses multiple package managers. 

*Note:* It’s important to use the most recent version of a package when possible. The most recent version has the most up-to-date bug fixes and security patches. These help keep your system more secure.

#### Types of package managers

Many commonly used Linux distributions are derived from the same parent distribution. For example, KALI LINUX ™, Ubuntu, and Parrot all come from Debian. CentOS comes from Red Hat.

This knowledge is useful when installing applications because certain package managers work with certain distributions. For example, the Red Hat Package Manager (RPM) can be used for Linux distributions derived from Red Hat, and package managers such as dpkg can be used for Linux distributions derived from Debian.

Different package managers typically use different file extensions. For example, Red Hat Package Manager (RPM) has files which use the `.rpm` file extension, such as `Package-Version-Release_Architecture.rpm`. Package managers for Debian-derived Linux distributions, such as dpkg, have files which use the `.deb` file extension, such as `Package_Version-Release_Architecture.deb`.

#### Package management tools

In addition to package managers like RPM and dpkg, there are also package management tools that allow you to easily work with packages through the shell. Package management tools are sometimes utilized instead of package managers because they allow users to more easily perform basic tasks, such as installing a new package. Two notable tools are the Advanced Package Tool (APT) and Yellowdog Updater Modified (YUM).

#### Advanced Package Tool (APT)

APT is a tool used with Debian-derived distributions. It is run from the command-line interface to manage, search, and install packages.

#### Yellowdog Updater Modified (YUM)

YUM is a tool used with Red Hat-derived distributions. It is run from the command-line interface to manage, search, and install packages. YUM works with `.rpm` files.

### Glossary

Application: A program that performs a specific task

Bash: The default shell in most Linux distributions

CentOS: An open-source distribution that is closely related to Red Hat

Central Processing Unit (CPU): A computer’s main processor, which is used to perform general computing tasks on a computer

Command: An instruction telling the computer to do something

Digital forensics: The practice of collecting and analyzing data to determine what has happened after an attack

Directory: A file that organizes where other files are stored

Distributions: The different versions of Linux

File path: The location of a file or directory

Filesystem Hierarchy Standard (FHS): The component of the Linux OS that organizes data

Graphical user interface (GUI): A user interface that uses icons on the screen to manage different tasks on the computer

Hard drive: A hardware component used for long-term memory

Hardware: The physical components of a computer

Internal hardware: The components required to run the computer

Kali Linux ™: An open-source distribution of Linux that is widely used in the security industry

Kernel: The component of the Linux OS that manages processes and memory

Linux: An open source operating system

Package: A piece of software that can be combined with other packages to form an application

Package manager: A tool that helps users install, manage, and remove packages or applications

Parrot: An open-source distribution that is commonly used for security

Penetration test (pen test): A simulated attack that helps identify vulnerabilities in systems, networks, websites, applications, and processes

Peripheral devices: Hardware components that are attached and controlled by the computer system

Random Access Memory (RAM): A hardware component used for short-term memory

Red Hat® Enterprise Linux® (also referred to simply as Red Hat in this course): A subscription-based distribution of Linux built for enterprise use

Shell: The command-line interpreter 

Standard error: An error message returned by the OS through the shell

Standard input: Information received by the OS via the command line

Standard output: Information returned by the OS through the shell

String data: Data consisting of an ordered sequence of characters

Ubuntu: An open-source, user-friendly distribution that is widely used in security and other industries

User: The person interacting with a computer