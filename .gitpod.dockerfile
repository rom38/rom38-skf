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
 && sudo git clone https://github.com/rom38/Neovim-from-scratch .\
 && sudo git switch dev\
 && nvim +PackerInstall +qa\
 && nvim +PackerUpdate +qa\
 && pip install neovim\
 && pip install pyright\
 && pip install ipykernel\
 && npm install -g neovim