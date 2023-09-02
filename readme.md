# chia_space_optimizer

This code will calculate with your given compression the best match to fill your chia space.

<div style="display: flex; align-items: center;">
  <a href="https://lafermedumineur.fr/chia-pool-stats/">
    <img src="assets/LFDM.png" alt="Image 1" style="float: left; margin-right: 20px; width: 100px">
  </a>
  <a href="https://discord.gg/G6zN82jJdp">
    <img src="assets/discord.png" alt="Image 2" style="float: left ; margin-top: 10px; margin-right: 20px;">
  </a>
  <p>This code has been build with love by LFDM teams. If you want to join us, click us</p>

</div>

## Install

Ensure you have python & [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git). then run in terminal

````shell
git clone https://github.com/CryptoLFDM/chia_space_optimizer.git
cd chia_space_optimizer
python3 -m venv .
source bin/activate
pip install requierement.txt
````

## Edit config file

there is a `config.yml` in `config` folder. Please edit and replace with your information. Please keep in mind that compression level 6 or + need gpu for farming. 5 is the maximum for cpu.


````yaml
---
compression_level: 5

directories_to_calculate:
  - U:\
  - V:\
  - W:\
  - X:\
  - Y:\
  - Z:\

````

## Run it

in the same shell as above

````shell
python main.py
````

You will see log like

````shell
Disk: U:\
Disk Size (GiB): 16623.89 GiB
Total GiB Used: 16616.30 GiB (99.95%)
Best Combination: [('k35', 23), ('k34', 1), ('k32', 1)]
K32 comparaison
Total K32 GiB Used: 16585.20 GiB (99.77%) with 204 K32 plots

Disk: V:\
Disk Size (GiB): 7311.73 GiB
Total GiB Used: 7288.30 GiB (99.68%)
Best Combination: [('k35', 10), ('k33', 1), ('k32', 1)]
K32 comparaison
Total K32 GiB Used: 7235.70 GiB (98.96%) with 89 K32 plots

Disk: W:\
Disk Size (GiB): 9167.72 GiB
Total GiB Used: 9152.00 GiB (99.83%)
Best Combination: [('k35', 13)]
K32 comparaison
Total K32 GiB Used: 9105.60 GiB (99.32%) with 112 K32 plots

Disk: X:\
Disk Size (GiB): 11039.88 GiB
Total GiB Used: 10984.30 GiB (99.50%)
Best Combination: [('k35', 15), ('k34', 1), ('k32', 1)]
K32 comparaison
Total K32 GiB Used: 10975.50 GiB (99.42%) with 135 K32 plots

Disk: Y:\
Disk Size (GiB): 14765.92 GiB
Total GiB Used: 14757.00 GiB (99.94%)
Best Combination: [('k35', 20), ('k34', 1), ('k33', 2)]
K32 comparaison
Total K32 GiB Used: 14715.30 GiB (99.66%) with 181 K32 plots

Disk: Z:\
Disk Size (GiB): 14767.48 GiB
Total GiB Used: 14766.00 GiB (99.99%)
Best Combination: [('k35', 20), ('k34', 2)]
K32 comparaison
Total K32 GiB Used: 14715.30 GiB (99.65%) with 181 K32 plots

````