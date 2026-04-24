# SDN Topology Change Detector

## Description
This project implements a topology change detection system using Software Defined Networking (SDN). It uses the POX controller and Mininet to monitor changes in network topology such as switch connection/disconnection and link failures.

## Features
- Detect switch connection (ConnectionUp)
- Detect switch disconnection (ConnectionDown)
- Detect link up/down (LinkEvent)
- Real-time logging of topology changes

## Tools Used
- POX Controller
- Mininet
- OpenFlow Protocol

## Topology
Linear topology with switches and hosts.

Example:
h1 — s1 — s2 — s3 — h3

## How to Run

### Start Controller# sdn-topology-change-detector
Topology change detection using POX and Mininet
