# Troubleshooting

## VIM Frozen
Generally happens when stopping terminal output with control flow.

``` vim
ctrl+s  # stops terminal output (causes freeze) (XON).
ctrl+q  # starts terminal output (XOFF).
```

