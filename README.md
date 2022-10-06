# workspace

Workspace is a command line application to automate development startup.

## Features

- [ ] `wsp <workspace>` open workspace folder using configured `$EDITOR`
- [ ] `wsp create <name>` create workspace inside `$WSP_HOME`
- [ ] read configuration from `$WSP_HOME/config.yml`
- [ ] `wsp watch` wait a pid to terminate and shutdown a workspace

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
