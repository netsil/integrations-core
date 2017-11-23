# Ecs Integration

## Overview

Get metrics from ecs service in real time to:

* Visualize and monitor ecs states
* Be notified about ecs failovers and events.

## Installation

Install the `dd-check-ecs` package manually or with your favorite configuration manager

## Configuration

Edit the `ecs.yaml` file to point to your server and port, set the masters to monitor

## Validation

When you run `datadog-agent info` you should see something like the following:

    Checks
    ======

        ecs
        -----------
          - instance #0 [OK]
          - Collected 39 metrics, 0 events & 7 service checks

## Compatibility

The ecs check is compatible with all major platforms
