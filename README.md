# PC Setup

Ansible playbook for setting up my PC

> [!IMPORTANT]
> This playbook is tailored to my personal preferences and may not work for everyone. It is intended to set up a Fedora Silverblue environment for a developer like me.

## Installation

1. Modify the roles in the [`site.yml`](site.yml) that you would like to apply
   to the PC.
2. [Optional] Change the host name in the [`site.yml`](site.yml) and
   [`inventory`](inventory) files
3. Install requirements:
    - `ansible`
    - `zenity`
4. Update download sources:
    - [sops](./roles/fedora-base/tasks/rpm-ostree.yml#L110-111)
    - [nerd-fonts](./roles/fedora-base/tasks/configs.yml#L164-165)
5. Run the [`install.sh`](install.sh) script:
   ```shell
   . ./install.sh
   ```

## Repository Structure

```text
.
├── roles/
│   ├── fedora-base/
│   │   ├── files/
│   │   │   └── …
│   │   └── tasks/
│   │       ├── main.yml
│   │       └── …
│   ├── fedora-gnome/
│   │   ├── files/
│   │   │   └── …
│   │   └── tasks/
│   │       ├── main.yml
│   │       └── …
│   ├── fedora-intel-graphics/
│   │   ├── files/
│   │   │   └── …
│   │   └── tasks/
│   │       ├── main.yml
│   │       └── …
│   └── …
├── install.sh
├── inventory
├── README.md
└── site.yml
```

The `roles` folder contains the configurations for the different roles (see
[Roles](#roles) for more details). Each role contains some `tasks` and
optionally some `files` that are used to set up the PC. Tasks are usually
grouped into `dnfs`, `flatpaks` and `configs` the contents of which is applied
through the corresponding `main.yml`. Change the contents of these tasks to
make changes to how the PC is set up.

The `install.sh` script is used to start the PC setup installation

The `inventory` file contains the hosts and their location on which the Ansible
setup runs. Since this is a local installation the location of the host is
"localhost". The name of the host may be changed, but beware that the name also
needs to be changed in the `site.yml`.

The `README.md` is this README.

The `site.yml` is the file that specifies which roles should be applied to which
host. If your PC setup changes in a major way (e.g. different desktop
environment or GPU hardware), apply different roles here (they would of course
need to be defined in the `roles` directory).

### Roles

#### fedora-base

This is the base role for every fedora setup, independent of desktop
environment and graphics stack, installing what I consider are must have
applications and adjusting the necessary configurations.

#### fedora-gnome

This installs gnome specific applications and modifies the environment to fit my
liking.

#### fedora-intel-graphics

This installs packages and configurations required for seamless usage of Intel
GPU hardware on a fedora system.

## Troubleshooting

You can test the Ansible Playbook using the `--check` flag when calling the
Ansible Playbook command, like so:

```bash
ansible-playbook site.yml --inventory inventory --ask-become-pass --check
```
