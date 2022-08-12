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
 && nvim --headless -c 'autocmd User PackerComplete quitall' -c 'PackerSync'\
 && nvim --headless -c 'autocmd User PackerComplete quitall' -c 'PackerSync'\
 && pip install neovim\
 && npm install -g neovim\
 && sudo mkdir /workspace/.pers\
 && sudo touch /workspace/.pers/.bash_history\
 && sudo echo "HISTFILE = /workspace/.pers/.bash_history" >> /home/gitpod/.bash_profile
