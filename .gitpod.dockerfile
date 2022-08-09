FROM gitpod/workspace-full

RUN sudo apt-get update \
 && sudo apt-get install -y \
    mc ncdu \
 && sudo rm -rf /var/lib/apt/lists/*\
 && sudo wget https://github.com/neovim/neovim/releases/download/nightly/nvim-linux64.deb \
 && sudo apt install -y ./nvim-linux64.deb\
 && sudo rm  ./nvim-linux64.deb\
 && pyenv install 3.9.13\
 && pyenv global 3.9.13\
 && sudo mkdir .config/nvim\
 && cd .config/nvim\
 && git clone https://github.com/rom38/Neovim-from-scratch .\
 && git switch dev\
 && nvim +PackerUpdate +qa\
 && pip install neovim\
 && pip install pyright\
 && npm install -g neovim