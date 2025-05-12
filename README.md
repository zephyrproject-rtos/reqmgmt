# Zephyr Project Requirements

This repository contains a preliminary work on the Zephyr Project requirements.

The requirements are captured using
[StrictDoc](https://github.com/strictdoc-project/strictdoc).

See the [Zephyr Safety Working Group Wiki](https://github.com/zephyrproject-rtos/zephyr/wiki/Safety-Working-Group) for information on connecting to the team.

The guidelines around writing requirements are located here: [Safety Requirements](https://docs.zephyrproject.org/latest/safety/safety_requirements.html)

## Deployed Documentation

The requirements documentation is available online at:
[https://zephyrproject-rtos.github.io/reqmgmt](https://zephyrproject-rtos.github.io/reqmgmt)

## System requirements

The requirements shall be browsable and editable on all major operating systems
that have Python 3.7+.

## Getting started

To install the requirements management tool:

```shell
pip install strictdoc
```

To generate the requirements documentation in HTML format:

```shell
strictdoc export .
```

To browse/edit the requirements using StrictDoc's web interface:

```shell
strictdoc server .
```

To generate uid's for new written requirements use the command:
```shell
strictdoc manage auto-uid .
```
