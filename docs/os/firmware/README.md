# Firmware


## [Disable AMT][a]
Intel Active Management Technology runs a separate linux instance on the
management engine. It has [active real-world exploits][b].

* Press **F10** to get to AMT screen.
* Default password **admin**.
* New password constraints:
    * Minimum **8** characters
    * One **uppercase** character
    * One **lowercase** character
    * One number (**0-9**)
    * One symbol (**!@#$% ...** etc)
* Disable.

[a]: https://community.frame.work/t/intel-management-engine-me-active-management-technology-amt-instructions/6521
[b]: https://kakaroto.ca/2019/11/exploiting-intels-management-engine-part-1-understanding-pts-txe-poc
