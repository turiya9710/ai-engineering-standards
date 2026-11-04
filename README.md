# AI Engineering Standards

**Portable engineering standards and AI agent configuration for Claude Code and OpenAI Codex.**

A Git-based engineering standards system designed to provide consistent development practices across macOS, Windows 11, WSL2 Ubuntu, EC2 and other Linux environments.

The repository provides shared engineering principles, agent-specific instructions and cross-platform bootstrap scripts.

## Objectives

- Maintain consistent engineering standards across development environments.
- Support Claude Code and OpenAI Codex.
- Separate personal engineering preferences from organization-specific standards.
- Provide repeatable, Git-based configuration.
- Support both Linux/macOS Bash and Windows PowerShell.
- Integrate with Superpowers, OpenSpec and Git-based development workflows.
- Keep engineering standards portable and independent of any particular AI vendor.

## Architecture

The repository is the source of truth for engineering standards.

Each development environment maintains a local Git checkout and uses bootstrap scripts to install the appropriate global instructions.

|Environment|Bootstrap|
|---|---|
|macOS|Bash|
|WSL2 Ubuntu|Bash|
|EC2 Ubuntu/Linux|Bash|
|Windows 11|PowerShell|
|Linux containers/VMs|Bash|

Bash is used for Unix-like bootstrap automation. Users do not need to change their default interactive shell.

## Repository structure

text

```
ai-engineering-standards/
│
├── README.md
├── VERSION
├── LICENSE
├── .gitignore
│
├── standards/
│   ├── common/
│   ├── personal/
│   └── organizations/
│
├── agents/
│   ├── claude/
│   └── codex/
│
├── workflows/
│
├── integrations/
│   ├── superpowers/
│   ├── openspec/
│   └── github/
│
├── templates/
│
└── scripts/
    ├── render-instructions.py
    ├── bootstrap-unix.sh
    └── bootstrap-windows.ps1
```

## Supported AI agents

### Claude Code

Global instructions:

text

```
~/.claude/CLAUDE.md
```

### OpenAI Codex

Global instructions:

text

```
~/.codex/AGENTS.md
```

The Python renderer generates managed instruction sections while preserving content outside those sections.

Existing non-empty instruction files are backed up before their first modification.

## Prerequisites

### Unix-like environments

- Git
- Python 3
- Bash

### Windows

- Git for Windows
- Python 3
- PowerShell

Claude Code and Codex must be installed separately.

Their respective plugins and skills must also be installed and enabled independently.

## Installation

### Clone the repository

bash

```
mkdir -p ~/github
cd ~/github

git clone git@github.com:turiya9710/ai-engineering-standards.git

cd ai-engineering-standards
```

### macOS, Ubuntu, WSL2 and EC2

Run:

bash

Alternatively:

bash

```
chmod +x scripts/bootstrap-unix.sh
./scripts/bootstrap-unix.sh
```

The bootstrap defaults to the personal profile and both AI agents.

### Windows 11 PowerShell

powershell

```
.\scripts\bootstrap-windows.ps1
```

## Configuration profiles

The intended profile model supports:

|Profile|Purpose|
|---|---|
|Personal|Individual engineering preferences|
|Organization|Organization-specific engineering policies|
|Combined|Common, personal and organization standards|

Organization-specific profile support requires the corresponding organization instruction files and should be validated before use.

Never commit employer-confidential information or credentials to a personal repository without authorization.

## Configuration and updates

Pull the latest standards:

bash

```
cd ~/github/ai-engineering-standards
git pull --ff-only
```

Reapply the configuration:

bash

```
bash scripts/bootstrap-unix.sh
```

The bootstrap is designed to be repeatable and idempotent.

## Shell compatibility

The project supports Bash scripts without requiring Bash to be the user's default shell.

For example, users running tcsh can execute:

tcsh

```
bash scripts/bootstrap-unix.sh
```

Interactive shell preferences remain independent of bootstrap automation.

## Current implementation status

### Implemented and verified

- Shared engineering standards foundation.
- Personal engineering profile.
- Claude Code global instruction generation.
- Codex global instruction generation.
- Python instruction renderer.
- Unix bootstrap script.
- Windows PowerShell bootstrap script.
- Managed instruction sections.
- Backup of existing instruction files.
- Repeatable bootstrap execution.

### Validated environment

Initial validation was performed on:

- Windows 11
- WSL2 Ubuntu
- Bash 5.2.21
- Python 3.12.3
- Git 2.43.0
- Claude Code 2.1.317
- Codex CLI 0.166.0

Claude Superpowers 7.0.0 was confirmed enabled.

Codex Superpowers activation and the non-WSL platform bootstraps remain to be validated.

## Roadmap

### Milestone 2 — Agent integrations

- Verify Superpowers activation in Claude and Codex.
- Integrate OpenSpec workflows.
- Establish common development workflows.
- Document agent-specific behavior.

### Milestone 3 — Project-level configuration

- Generate project-level `CLAUDE.md`.
- Generate project-level `AGENTS.md`.
- Support repository-specific standards.
- Support project technology profiles.

### Milestone 4 — Cross-platform validation

- Validate macOS bootstrap.
- Validate Windows PowerShell bootstrap.
- Validate EC2 deployment.
- Validate container and cloud VM scenarios.

### Milestone 5 — Automation and quality

- Add GitHub Actions.
- Add automated tests.
- Add configuration validation.
- Add dry-run and check modes.
- Add versioned standards releases.

### Milestone 6 — Organization support

- Organization-specific standards overlays.
- Multiple organization profiles.
- Separate organization-owned standards repositories.
- Secure standards distribution and governance.

## Design principles

1. Git is the source of truth.
2. Configuration must be portable.
3. Personal and organization standards must remain separate.
4. Existing user configuration must be preserved.
5. Bootstrap operations must be repeatable.
6. Secrets and credentials must never be committed.
7. AI agents must report actual verification results.
8. Project-level instructions take precedence for project-specific requirements, subject to applicable higher-level policies.

## Version

Current milestone: **v0.1.0**

Release: Cross-platform AI engineering standards bootstrap foundation.

## Repository

GitHub: https://github.com/turiya9710/ai-engineering-standards

---

This project is intended to evolve into a reusable, version-controlled engineering playbook for human developers and AI coding agents.
