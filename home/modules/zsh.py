import os 
def main():
    """Module to install ZSH, OhmyZSH and its plugins"""
    print("#### ZSH ####")
    os.system(
        '''
        chsh -s /usr/bin/zsh &&
        sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)";
        cd $HOME/build &&
        git clone https://github.com/zsh-users/zsh-syntax-highlighting.git $HOME/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting &&
        git clone https://github.com/zsh-users/zsh-autosuggestions.git $HOME/.oh-my-zsh/custom/plugins/zsh-autosuggestions 
        ''')
    