# DIY Bluetooth Mechanical Keyboard

## 1. Description

The DIY Bluetooth Mechanical Keyboard is a custom-designed 3D printed wireless keyboard with an ergonomic 6 degree tilt, a slide potentiometer for analog input, USB Type-C connectivity, and hot-swappable MX-style switches. It includes a detachable wrist rest for comfort and features embedded passive NFC tags that can be used for mobile automations or other creative integrations.  

This keyboard was made to be easily built and remixed by others. The entire design uses mostly through-hole components. Only the diodes are surface-mount, which makes it much easier to assemble without needing any special tools.

---

## 2. Why I Made This Project

I designed this keyboard for myself with daily use in mind. I wanted something compact, reliable, and comfortable to use, especially during long sessions. Most wireless keyboards don't come with embedded passive NFC tags and some still even use micro USB for charging and wired mode. This one uses USB Type-C and Bluetooth, and can also be recharged easily.

The project also gave me a chance to learn about PCB layout, 3D CAD, component sourcing, and firmware setup. I wanted to build something I could be proud of and share with others who might want to build their own.

---

## Project Gallery

---

### 3D CAD Model  
![cad_model](images/3D%20Model.avif)

---

### PCB Design  
![pcb_layout](images/PCB.avif)

---

### Wiring Diagram  
![wiring_diagram](images/Schematics.avif)

---

## Bill of Materials (BOM)

| No. | Category            | Item                   | Qty    | Est. Price (USD) | Description / Notes                                     | Link |
|-----|---------------------|------------------------|--------|------------------|---------------------------------------------------------|------|
| 1   | Switch & Keycap     | Gateron Milky Yellow Pro | 64 pcs | 12               | Smooth linear switches with factory lube                | https://www.tokopedia.com/mechkeyboardsid/gateron-g-pro-yellow-switch-linear-plate-mount?utm_source=salinlink&utm_medium=share&utm_campaign=PDP-266238606-2999811194-130725-RKdhUE |
| 2   | Switch & Keycap     | Kailh Hot Swap Sockets | 64 pcs | 5                | For hot-swappable MX-style switches                     | https://www.tokopedia.com/mechkeyboardsid/kailh-hot-swap-mechanical-keyboard-pcb-socket-black?utm_source=salinlink&utm_medium=share&utm_campaign=PDP-266238606-2198706891-130725-RKdhUE |
| 3   | Switch & Keycap     | Keycap Set             | 1 set  | 20               | Full keycap set, likely PBT                             | https://tk.tokopedia.com/ZSBVvFJGR/ |
| 4   | Switch & Keycap     | Stabilizer Set         | 1 set  | 10               | For spacebar, shift, enter, etc.                        | https://tk.tokopedia.com/ZSBpk1MKy/ |
| 5   | Electronics         | Nice!Nano V2 (Clone)   | 2 pcs  | 8                | Wireless controller with ZMK support                    | https://tk.tokopedia.com/ZSSLQ4ugF/ |
| 6   | Electronics         | MCP23017 E/SP          | 1 pc   | 7                | GPIO Expander                                           | https://www.tokopedia.com/iibuuffeellaaa/ic-chips-mcp23017-e-sp-dip-28-mcp23017-16-bit-i-o-expander-with-i2c-interface-ic-original-integrated-circuits-1731233355557078588?utm_source=salinlink&utm_medium=share&utm_campaign=PDP-266238606-100273252298-270725-RKdhUE |
| 7   | Electronics         | LiPo Battery           | 1 pc   | 4                | Powers the keyboard wirelessly                          | https://tk.tokopedia.com/ZSBpAFa1Y/ |
| 8   | Electronics         | JST Connector          | 1 pc   | 1                | Connects battery to PCB                                 | https://tk.tokopedia.com/ZSBpAYkm3/ |
| 9   | Electronics         | 1N4148 Diodes (SOD-123) | 100 pcs | 1               | For keyboard matrix                                     | https://www.tokopedia.com/i2c-parts/in4148-1n4148-1n4148ws-sod123-switching-diode-sod-123-dioda?utm_source=salinlink&utm_medium=share&utm_campaign=PDP-266238606-1509220482-130725-RKdhUE |
| 10  | Electronics         | 10K Slide Potentiometers | 10 pcs | 1               | For analog controls like volume                         | https://www.tokopedia.com/innovtronic/b10k-mono-slide-potentio-75mm-high-quality?utm_source=salinlink&utm_medium=share&utm_campaign=PDP-266238606-344656821-130725-RKdhUE |
| 11  | Fasteners           | M2.5 6mm Heat Inserts  | 6 pcs  | 1                | For securing threaded parts in plastic                  | https://tk.tokopedia.com/ZSBqKcnqk/ |
| 12  | Fasteners           | M2.5 8mm Screws        | 6 pcs  | 1                | For case and PCB mounting                               | https://www.tokopedia.com/archive-lapaktukang/baut-komputer-laptop-m2-5x4-m2-5x5-m2-5x6-m2-5x8-m2-5x10-m2-5x8-mm-hitam-d5-7f72b?utm_source=salinlink&utm_medium=share&utm_campaign=PDP-266238606-14063028572-140725-RKdhUE |
| 13  | Damping & Isolation | EVA Foam 3mm           | 1 pc   | 2                | For internal case dampening                             | https://www.tokopedia.com/tentakey/eva-foam-untuk-case-plate-foam-modding-mechanical-keyboard-25x30-2mm-26c32?utm_source=salinlink&utm_medium=share&utm_campaign=PDP-266238606-8737440897-140725-RKdhUE |
| 14  | Damping & Isolation | Non-slip Feet          | 1 set  | 1                | Anti-slip support                                       | https://tk.tokopedia.com/ZSBqsCjBn/ |
| 15  | Assembly            | Solder Wire            | 1 pc   | 2                | For assembling components                               | https://tk.tokopedia.com/ZSAR33vra/ |
| 16  | Assembly            | Solder Paste           | 1 pc   | 3                | For assembling components (SMD)                         | https://tk.tokopedia.com/ZSAR3KArf/ |
| 17  | Assembly            | Flux                   | 1 pc   | 1                | Improves solder quality, especially for SMD components  | |
| 18  | PCB & Electronics   | Custom PCB             | 5 pcs  | 16               | Custom-designed keyboard circuit board                  | — |
| 19  | Case Components     | Case                   | 1 pc   | 3                | One-piece keyboard case (price is reserved for shipping, tentative) | — |
| 20  | Case Components     | Wristrest              | 1 pc   | 3                | Wristrest (price is reserved for shipping, tentative)   | — |
| 21  | Feature Add-on      | Passive NFC Tags       | 1 pack | 4                | Embedded for automation (e.g. launch phone shortcut)    | https://tk.tokopedia.com/ZSBVtqGWa/ |

Total: $106 USD

> Prices are rounded up to the next whole dollar.
