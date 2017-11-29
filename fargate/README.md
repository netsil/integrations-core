# Fargate Integration

## Overview

Get metrics from fargate service in real time to:

* Visualize and monitor fargate states
* Be notified about fargate failovers and events.

## Installation

Install the `dd-check-fargate` package manually or with your favorite configuration manager

## Configuration

Edit the `fargate.yaml` file to point to your server and port, set the masters to monitor

## Validation

When you run `datadog-agent info` you should see something like the following:

    Checks
    ======

        fargate
        -----------
          - instance #0 [OK]
          - Collected 39 metrics, 0 events & 7 service checks

## Compatibility

The fargate check is compatible with all major platforms
