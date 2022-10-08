#!/bin/bash

WSP="${WSP:-$HOME/.wsp}"
REMOTE="https://github.com/giancarlopro/workspace"

main() {
  if [ -d "$WSP" ]; then
    echo "Workspace already installed"
    exit 1
  fi

  git clone "$REMOTE" "$WSP"

  cd "$WSP" && \
  pipenv requirements > requirements.txt && \
  python -m pip install -r requirements.txt
}

main "$@"
