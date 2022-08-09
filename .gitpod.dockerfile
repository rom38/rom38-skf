FROM gitpod/workspace-full

RUN sudo apt-get update \
 && sudo apt-get install -y \
    mc ncdu \
 && sudo rm -rf /var/lib/apt/lists/*\
 && sudo wget https://github.com/neovim/neovim/releases/download/nightly/nvim-linux64.deb \
 && sudo apt install ./nvim-linux64.deb