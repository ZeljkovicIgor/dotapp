from os.path import expanduser, expandvars
from dot import Dot

SYSTEMPATH = "./test/system/"
REPOPATH = "./test/repo/"

DATA = [
    {
        "text": "Test",
        "class": Dot,
        "files": [{"path": SYSTEMPATH, "repo_path": REPOPATH, "name": ".testrc"}],
        "dependencies": [],
    }
]

REALDATA = [
    {
        "text": "Airline Theme",
        "class": Dot,
        "files": [
            {
                "path": expanduser(
                    "~/.local/share/nvim/plugged/vim-airline-themes/autoload/airline/themes/"
                ),
                "repo_path": "./",
                "name": "igor.vim",
            }
        ],
        "dependencies": [],
    },
    {
        "text": "Coc.nvim",
        "class": Dot,
        "files": [
            {
                "path": expanduser("~/.config/coc/extensions/"),
                "repo_path": "./",
                "name": "package.json",
            }
        ],
        "dependencies": [],
    },
    {
        "name": "vim",
        "text": "Vim",
        "class": Dot,
        "files": [{"path": expanduser("~/"), "repo_path": "./", "name": ".vimrc"}],
        "dependencies": [],
    },
    {
        "name": "nvim",
        "text": "Neovim",
        "class": Dot,
        "files": [
            {
                "path": expanduser("~/.config/nvim/plugins/"),
                "repo_path": "./nvim/plugins/",
            },
            {"path": expanduser("~/.config/nvim/"), "repo_path": "./nvim/"},
            {
                "name": ".nvimrc",
                "path": expanduser("~/"),
                "repo_path": "./",
            },
        ],
        "dependencies": [],
    },
    {
        "name": "kitty",
        "text": "Kitty",
        "class": Dot,
        "files": [{"path": expanduser("~/.config/kitty/"), "repo_path": "./kitty/"}],
        "dependencies": [],
    },
    {
        "name": "rofi",
        "text": "Rofi",
        "class": Dot,
        "files": [
            {
                "path": expanduser("~/.config/rofi/"),
                "repo_path": "./rofi/",
                "name": "config.rasi",
            },
            {
                "path": "/usr/share/rofi/themes/",
                "repo_path": "./rofi/",
                "name": "onedark-igor.rasi",
            },
        ],
        "dependencies": [],
    },
    {
        "name": "zsh",
        "text": "Zsh",
        "class": Dot,
        "files": [{"path": expanduser("~/"), "repo_path": "./", "name": ".zshrc"}],
        "dependencies": [
            {
                "alias": "omz",
                "text": "Oh My Zsh",
                "prerequisites": ["curl", "git"],
                "commands": {
                    "install": [
                        "sh -c '$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)'"
                    ],
                    "update": [],
                },
            },
            {
                "alias": "p10k",
                "text": "Powerlevel10k",
                "prerequisites": ["omz"],
                "commands": {
                    "install": [
                        expandvars(
                            "git -C ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k pull"
                        )
                    ],
                    "update": [],
                },
            },
            {
                "path": expanduser(
                    "${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting"
                ),
                "text": "zsh-syntax-highlighting",
                "prerequisites": [],
                "commands": {
                    "install": [
                        expanduser(
                            "git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting"
                        )
                    ],
                    "update": [],
                },
            },
            {
                "path": expanduser(
                    "${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions"
                ),
                "text": "zsh-autosuggestions",
                "prerequisites": [],
                "commands": {
                    "install": [
                        expanduser(
                            "git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions"
                        )
                    ],
                    "update": [],
                },
            },
            {
                "path": expanduser(
                    "${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/auto-ls"
                ),
                "text": "auto-ls",
                "prerequisites": [],
                "commands": {
                    "install": [
                        expanduser(
                            "git clone https://github.com/ZeljkovicIgor/auto-ls.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/auto-ls"
                        )
                    ],
                    "update": [],
                },
            },
            {
                "alias": "bat",
                "text": "bat",
                "prerequisites": [],
                "commands": {"install": ["pacman -S bat"], "update": []},
            },
        ],
    },
]
