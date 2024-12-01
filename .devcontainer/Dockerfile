FROM ubuntu:24.04

# Install dependencies
RUN apt-get update && \
    apt-get install -y \
    software-properties-common \
    wget \
    curl \
    sudo \
    zsh \
    git \
    tzdata \
    fonts-powerline \
    vim && \
    rm -rf /var/lib/apt/lists/*
    
RUN add-apt-repository ppa:deadsnakes/ppa -y
RUN apt-get update && \
    apt-get install -y \
    python3.13 \
    python-is-python3 

RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.13 1

RUN curl https://bootstrap.pypa.io/get-pip.py | python

RUN ln -sf /usr/share/zoneinfo/Africa/Casablanca /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata


# Install Oh My Zsh and Powerlevel10k theme
RUN curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh | bash -s -- --unattended && \
    git clone --depth=1 https://github.com/romkatv/powerlevel10k.git $ZSH_CUSTOM/themes/powerlevel10k

# Set default shell to zsh for root
RUN chsh -s /bin/zsh root

# Create 'dev' user, set zsh as default shell, and give sudo privileges
RUN useradd -m -s /bin/zsh dev && \
    echo "dev ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/dev

# Copy Powerlevel10k configuration file
COPY .p10k.zsh /home/dev/.p10k.zsh
COPY .p10k.zsh /root/.p10k.zsh

# Install Oh My Zsh and Powerlevel10k theme for 'dev' user
USER dev
RUN curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh | bash -s -- --unattended && \
    git clone --depth=1 https://github.com/romkatv/powerlevel10k.git /home/dev/.oh-my-zsh/themes/powerlevel10k && \
    echo 'source $HOME/.oh-my-zsh/themes/powerlevel10k/powerlevel10k.zsh-theme' >>~/.zshrc && \
    echo '[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh' >> ~/.zshrc

# Set the working directory and ensure dev has the correct permissions
WORKDIR /workspace
RUN chown -R dev:dev /workspace

# Switch to 'dev' user and set zsh as default shell
# USER dev
CMD ["zsh"]
