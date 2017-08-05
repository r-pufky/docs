""
"" If python (or any files) are tabbing incorrectly, modify the
"" /usr/share/vim/vim74/ftplugin/(filetype).vim file and comment out the
"" setlocal expandtab shiftwidth=4 softtabstop=4 tabstop=8
""
set nocompatible
set ruler
set viminfo='50,\"1000,:0

set popt+=syntax:y " Printing options
set mouse=a        " mouse will be on all the time

filetype on        "Enable filetype settings
filetype plugin on
filetype indent on

set hlsearch       "Highlight my search matches
set background=dark
set guioptions=agirt  "no menu, no toolbar
set guifont=Lucida\ Terminal

""  CONSOLE AND GUI OPTIONS:
""  -----------------------
set vb t_vb=          "turn beeping off
set tabstop=2
set softtabstop=2
set shiftwidth=2
set expandtab         "Convert tabs to spaces
set backspace=2       "This makes backspace work

"" STATUSBAR:
"" ---------
set laststatus=2
set statusline=
set statusline+=%-3.3n\                      " buffer number
set statusline+=%f\                          " file name
set statusline+=%h%m%r%w                     " flags
set statusline+=\[%{strlen(&ft)?&ft:'none'}, " filetype
set statusline+=%{&encoding},                " encoding
set statusline+=%{&fileformat}]              " file format
set statusline+=%=                           " right align
set statusline+=0x%-8B\                      " current char
set statusline+=%-14.(%l,%c%V%)\ %<%P        " offset

syntax on

"" COMMENTING:
"" ----------
map ,# :s/^/#/<CR>:nohlsearch<CR> 
map ,/ :s/^/\/\//<CR>:nohlsearch<CR> 
map ,> :s/^/> /<CR>:nohlsearch<CR> 
map ," :s/^/\"/<CR>:nohlsearch<CR> 
map ,% :s/^/%/<CR>:nohlsearch<CR> 
map ,! :s/^/!/<CR>:nohlsearch<CR> 
map ,; :s/^/;/<CR>:nohlsearch<CR> 
map ,- :s/^/--/<CR>:nohlsearch<CR> 
map ,c :s/^\/\/\\|^--\\|^> \\|^[#"%!;]//<CR>:nohlsearch<CR> 
" wrapping comments 
map ,* :s/^\(.*\)$/\/\* \1 \*\//<CR>:nohlsearch<CR> 
map ,( :s/^\(.*\)$/\(\* \1 \*\)/<CR>:nohlsearch<CR> 
map ,< :s/^\(.*\)$/<!-- \1 -->/<CR>:nohlsearch<CR> 
map ,d :s/^\([/(]\*\\|<!--\) \(.*\) \(\*[/)]\\|-->\)$/\2/<CR>:nohlsearch<CR> 

""---------------- OPTIONS YOU PROBABLY DON"T WANT TO PLAY WITH -------------
" When editing a file, always jump to the last known cursor position.
" Don't do it when the position is invalid or when inside an event handler
" (happens when dropping a file on gvim).
autocmd BufReadPost *
\ if expand("<afile>:p:h") !=? $TEMP |
\   if line("'\"") > 0 && line("'\"") <= line("$") |
\     exe "normal g`\"" |
\     let b:doopenfold = 1 |
\   endif |
\ endif
" Need to postpone using "zv" until after reading the modelines.
autocmd BufWinEnter *
\ if exists("b:doopenfold") |
\   unlet b:doopenfold |
\   exe "normal zv" |
\ endif 

" If we're in a wide window, enable line numbers.
fun! <SID>WindowWidth()
    if winwidth(0) > 90
        setlocal number
    else
        setlocal nonumber
    endif
endfun

" Always do a full syntax refresh
autocmd BufEnter * syntax sync fromstart
""---------------------------------------------------------------------------
