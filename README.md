# workspace

Workspace is a command line application to automate development startup.

## Installation

### curl

```
sh -c "$(curl -fsSL https://raw.githubusercontent.com/giancarlorocha/workspace/master/tools/install.sh)"
```

### wget

```
sh -c "$(wget -O- https://raw.githubusercontent.com/giancarlorocha/workspace/master/tools/install.sh)"
```

## Features

- [ ] `wsp <workspace>` open workspace folder using configured `$EDITOR`
- [ ] `wsp create <name>` create workspace inside `$HOME/.wsp/`
- [ ] read configuration from `$HOME/.wsp/config.yml`
- [ ] `wsp watch` wait a pid to terminate and shutdown a workspace
- [ ] `wsp clone` clone a repository to your `$WSP_HOME` and creates a new workspace for it
- [ ] install script

## Workspaces

Workspaces are defined using yaml.

```yaml
root: /home/user/repositories/project
editor: code # optional
startup:
  - docker-compose up
shutdown:
  - docker-compose down
```

> shutdown can be implemented in linux like this:

```bash
$EDITOR <workspace> & wsp watch $! -s <workspaces>
```
