"" https://dougblack.io/words/a-good-vimrc.html#colors
set nocompatible                             " Do not use vi compatible settings
set viminfo=%,'50,\"1000,/50,:0,h,f0,n~/.vim/.viminfo
"           | |   |      |   |  | |  + viminfo file path
"           | |   |      |   |  | + File marks 0-9,A-Z 0=NOT stored
"           | |   |      |   |  + Disable 'hlsearch' loading viminfo
"           | |   |      |   + Max command-line history saved
"           | |   |      + Max search history saved
"           | |   + Max register lines saved
"           | + lines saved for each register
"           + save/restore buffer list
"" https://stackoverflow.com/questions/23012391/how-and-where-is-my-viminfo-option-set

"" COLOR SCHEME:
"" -------------
set t_Co=256                                 " Use 256 colors. termguicolors (24bit) doesn't work with tmux
colorscheme monokai                          " Use custom monokai theme
syntax enable                                " Use colorscheme syntax highlighting
set printoptions+=syntax:y                   " Use colorscheme syntax highlighting when printing to paper
highlight ColorColumn ctermbg=235 guibg=#2c2d27                              " Vertical column highlighting
highlight VertSplit ctermfg=222 ctermbg=238 guifg=#ffd787 guibg=#444444      " Vertical split highlighting
highlight User1 ctermfg=010 ctermbg=241 guifg=#00ff00 guibg=#626262          " %1* color
highlight User6 ctermfg=241 ctermbg=239 guifg=#626262 guibg=#4e4e4e          " %6* color (inverted %1*)
highlight User2 ctermfg=009 ctermbg=239 guifg=#ff0000 guibg=#4e4e4e          " %2* color
highlight User7 ctermfg=239 ctermbg=237 guifg=#4e4e4e guibg=#3a3a3a          " %7* color (inverted %7*)
highlight User3 ctermfg=222 ctermbg=237 guifg=#ffd787 guifg=#3a3a3a          " %3* color
highlight User8 ctermfg=237 ctermbg=235 guifg=#3a3a3a guifg=#262626          " %8* color (inverted %3*)
highlight User4 ctermfg=239 ctermbg=235 guifg=#4e4e4e guifg=#262626          " %4* color
highlight User9 ctermfg=235 ctermbg=233 guifg=#262626 guifg=#121212          " %9* color (inverted %4*)

"" FILE OPTIONS:
"" -------------
"" If python (or any files) are tabbing incorrectly, modify the
"" /usr/share/vim/vim74/ftplugin/(filetype).vim file and comment out the
"" setlocal expandtab shiftwidth=4 softtabstop=4 tabstop=8
filetype on                                  " Enable filetype detection
filetype indent on                           " Load type specific indent files

"" SEARCHING:
"" ----------
set incsearch                                " Search as characters are entered
set hlsearch                                 " Highlight search matches
set ignorecase                               " Ignore case when searching
set smartcase                                " If search contains a captial letter, make search case-sensitive
nnoremap <silent> \ :nohlsearch<CR>          " \ clears search highlights

"" GUI OPTIONS:
"" ------------
set guioptions=agirt                         " No menu or toolbar in GUI
set guifont=SF\ Mono                         " Use SF Mono font in GUI

"" CONSOLE OPTIONS:
"" ----------------
set mouse=a                                  " Mouse will be on all the time
set belloff=all                              " Turn off visual/audio bells
set encoding=utf8                            " Encode non-ASCII to UTF8
set tabstop=2                                " Tab control characters are rendered with 5 spaces
set softtabstop=2                            " Number of spaces inserted when inserting a tab control character
set expandtab                                " Expand tab control character to spaces
set shiftwidth=2                             " Shifting (<< >>) is 2 spaces
set backspace=2                              " Make backspace behave like other editors
set textwidth=0                              " Disable hard text wrapping
set wrapmargin=0                             " Disable soft text wrapping
set wildmenu                                 " Visual autocomplete for command menus
set number                                   " Enable lines numbers by default (nonumber disable)
set showcmd                                  " Continue to show last command until new one is entered
set cursorline                               " Highlight current cursor line
set showmatch                                " Showing matching closure
set ruler                                    " Display position information
set autoread                                 " Auto-reload files if they change on disk
set autoindent                               " Copy indentation from current line when starting new line

"" SPLIT MANAGEMENT:
"" -----------------
set splitbelow                               " Horizontal splits always created below
set splitright                               " Vertical splits always created on right
nnoremap <silent> <leader>\| :vsplit<CR>     " \| Create vertical split
nnoremap <silent> <leader>- :split<CR>       " - Create horizontal split
nnoremap <silent> <leader><left>  <c-w><c-h> " left arrow select split left
nnoremap <silent> <leader><right> <c-w><c-l> " right arrow select split right
nnoremap <silent> <leader><up>    <c-w><c-k> " up arrow select split up
nnoremap <silent> <leader><down>  <c-w><c-j> " down arrow select split down
set fillchars+=vert:│                        " Use solid line for vertical split 

"" NETRW FILE BROWSER:
"" -------------------
"" https://shapeshed.com/vim-netrw/#netrw---the-unloved-directory-browser
let g:netrw_liststyle=3                      " Tree view as default list view (i to rotate through)
let g:netrw_sort_sequence='[\/]$,*'          " List directories on top, files below
let g:netrw_browse_split=3                   " Open files in previous window (was 3, tab)
let g:netrw_altv=1                           " Open files in vertical split
let g:netrw_banner=0                         " Disable the starting banner
let g:netrw_winsize=25                       " Only use 25% of screen for netrw

"" STATUSBAR:
"" ---------
"" Match coloring from tmux status bar
set laststatus=2                             " Always show the status bar
set statusline=                              " Clear status line
set statusline+=%1*%f%6*                    " File path
set statusline+=%2*\ %{&encoding}%7*        " File encoding
set statusline+=%3*\ %{&fileformat}%8*      " File format
set statusline+=%4*\ %m%r%9*                " [+] (modified file), [RO] (readonly)
set statusline+=%=                           " Items before this are left-aligned, after right-aligned
set statusline+=%9*%4*0x%B\                 " Hex code of character under cursor
set statusline+=%8*%3*%c\                   " column number
set statusline+=%7*%2*%p%%\                 " Percent through the file
set statusline+=%6*%1*[%l/%L]               " Show current line, total lines

"" FOLDING:
"" --------
set foldenable                               " Enable code folding
set foldlevelstart=10                        " Open 10 levels of folds by default
set foldnestmax=10                           " Max 10 nested fold level
set foldmethod=indent                        " Fold based on indentation level

"" COMMENTING:
"" ----------
map ,# :s/^/#/<CR>:nohlsearch<CR>            " Add # comment start block
map ,/ :s/^/\/\//<CR>:nohlsearch<CR>         " Add // comment start block
map ,> :s/^/> /<CR>:nohlsearch<CR>           " Add > comment start block
map ," :s/^/\"/<CR>:nohlsearch<CR>           " Add " comment start block
map ,% :s/^/%/<CR>:nohlsearch<CR>            " Add % comment start block
map ,! :s/^/!/<CR>:nohlsearch<CR>            " Add ! comment start block
map ,; :s/^/;/<CR>:nohlsearch<CR>            " Add ; comment start block
map ,- :s/^/--/<CR>:nohlsearch<CR>           " Add -- comment start block
map ,c :s/^\/\/\\|^--\\|^> \\|^[#"%!;]//<CR>:nohlsearch<CR>                  " Clear comment start block
"" Wrapping comments
map ,* :s/^\(.*\)$/\/\* \1 \*\//<CR>:nohlsearch<CR>                          " Insert /* */ for line
map ,( :s/^\(.*\)$/\(\* \1 \*\)/<CR>:nohlsearch<CR>                          " Insert (* *) for line
map ,< :s/^\(.*\)$/<!-- \1 -->/<CR>:nohlsearch<CR>                           " Insert <!-- --> for line
map ,d :s/^\([/(]\*\\|<!--\) \(.*\) \(\*[/)]\\|-->\)$/\2/<CR>:nohlsearch<CR> " Clear wrapped comment

let mapleader=' '                            " Use space instead of \ for leader key
nnoremap <silent> <leader>h :source ~/.vimrc<CR>                             " h to reload .vimrc
nnoremap <silent> <leader>r :set relativenumber!<CR>                         " m Toggle relative line numbers
nnoremap <silent> <leader>n :set number!<CR>                                 " n Toggle line numbers on/off
nnoremap <silent> <leader>s :call StripTrailingWhitespace()<CR>              " s Strip EOL/EOF trailing whitespace
nnoremap <silent> <leader>g :call ColorRightGutters()<CR>                    " g Toggle right gutter highlighting
nnoremap <silent> <Leader><Leader> :e#<CR>                                   "   Toggle between last opened file
nnoremap <silent> <leader>f za                                               " f open/closes fold

"" Jump to last known position when opening file.
autocmd BufReadPost *
\ if expand("<afile>:p:h") !=? $TEMP |
\   if line("'\"") > 0 && line("'\"") <= line("$") |
\     exe "normal g`\"" |
\     let b:doopenfold = 1 |
\   endif |
\ endif

"" When in GVIM don't do it when the position is invalid or when inside an event
"" handler, delay using "zv" until after reading the modelines.
autocmd BufWinEnter *
\ if exists("b:doopenfold") |
\   unlet b:doopenfold |
\   exe "normal zv" |
\ endif

"" Always do a full syntax refresh when loading
autocmd BufEnter * syntax sync fromstart

"" Strip EOL/EOF trailing whitespace
function! StripTrailingWhitespace()
  let save_cursor = getpos('.')
  silent! %s/\s\+$//e                        " EOL whitespace
  silent! %s#\($\n\)\+\%$##                  " EOF whitespace
  call setpos('.', save_cursor)
endfunction

"" Toggle right gutter highlighting
function! ColorRightGutters()
  if &colorcolumn == ""
    let &colorcolumn=join(range(81,120),",").join(range(120,999),",")
  else
    set colorcolumn=
  endif
endfunction
