*This project has been created as part of the 42 curriculum by nadoho.*

## Description

**NetPractice** is a general practical exercise designed to introduce the basics of computer networking.

The goal of this project is to configure small-scale networks by solving networking problems so they function correctly. Each level presents a topology (hosts, switches, routers) with some fields already set and others left blank or incorrect. The objective is to determine and fill in the missing or wrong values — IP addresses, subnet masks, gateways — so that all devices on the network can communicate properly.

Through this project, you learn to:
- Configure IP addresses and subnet masks correctly for a given topology
- Connect devices through switches and routers
- Understand the role of a default gateway within a network
- Reason about how packets are routed between different subnets

## Instructions

### Execution

To launch the training interface:

1. Download the project files and extract them to a folder of your choice.
2. Run the `run.sh` script to launch a local web server and open the interface in your browser:
   ```bash
   ./run.sh
   ```
   *Note: if the script doesn't work, start the server manually with:*
   ```bash
   python3 -m http.server 49242
   ```
   *then navigate to `http://localhost:49242`.*

### Usage and Exporting Configurations

- Enter your login in the training interface to use your personal configuration.
- For each of the 10 levels, modify the unshaded (editable) fields until the network configuration is correct — i.e., until the interface confirms that every device can reach the others as expected.
- Once a level is completed, use the **Get my config** button to export the corresponding configuration file.

### Submission Requirements

- 10 exported configuration files (one per level) must be placed at the root of the Git repository.
- Make sure your login was entered in the interface **before** exporting each configuration, otherwise the file won't be linked to your account.

## Resources

Networking concepts studied in this project:
- **TCP/IP addressing**
- **Subnet masks** (CIDR notation, calculating network/broadcast addresses)
- **Default gateways**
- **Routers and switches** (their respective roles in a topology)

References used to understand these concepts:
- [NetPractice Guide & Video](https://youtu.be/HQUw0CfQWAM?si=8dEaWssLcNbL0lFk)
- [tblaase's NetPractice Repository](https://github.com/tblaase/Net_Practice)

### AI Usage

AI (Claude) was used as a learning aid, specifically to:
- Get detailed explanations of subnetting logic (how to calculate valid host ranges from a given mask)
- Clarify the difference between a switch's and a router's role when a level involved multiple subnets
- Double-check reasoning on gateway configuration before validating a level in the interface

AI was not used to generate the network configurations themselves — each level's solution was worked out manually in the training interface.