<a name="TOP"></a>
# Screwdrivers Store

screwdrivers support

It's my first project in OpenSCAD. I wanted to create a support for my screwdrivers.


![Main Assembly](assemblies/main_assembled.png)

<span></span>

---
## Table of Contents
1. [Parts list](#Parts_list)
1. [Wall Frenchcleat Assembly](#wall_frenchcleat_assembly)
1. [Screwdriver Support Assembly](#screwdriver_support_assembly)
1. [Wall Support Assembly](#wall_support_assembly)
1. [Support Assembly](#support_assembly)
1. [Frenchcleat Assembly](#frenchcleat_assembly)
1. [Main Assembly](#main_assembly)

<span></span>
[Top](#TOP)

---
<a name="Parts_list"></a>
## Parts list
| <span style="writing-mode: vertical-rl; text-orientation: mixed;">Wall&nbsp;Frenchcleat</span> | <span style="writing-mode: vertical-rl; text-orientation: mixed;">Screwdriver&nbsp;Support</span> | <span style="writing-mode: vertical-rl; text-orientation: mixed;">Support</span> | <span style="writing-mode: vertical-rl; text-orientation: mixed;">Frenchcleat</span> | <span style="writing-mode: vertical-rl; text-orientation: mixed;">Main</span> | <span style="writing-mode: vertical-rl; text-orientation: mixed;">TOTALS</span> |  |
|---:|---:|---:|---:|---:|---:|:---|
|  |  |  |  |  | | **Vitamins** |
| &nbsp;&nbsp;1&nbsp; | &nbsp;&nbsp;.&nbsp; | &nbsp;&nbsp;.&nbsp; | &nbsp;&nbsp;.&nbsp; | &nbsp;&nbsp;.&nbsp; |  &nbsp;&nbsp;1&nbsp; | &nbsp;&nbsp; Bottom french cleat optimised 280x50x15 |
| &nbsp;&nbsp;.&nbsp; | &nbsp;&nbsp;.&nbsp; | &nbsp;&nbsp;.&nbsp; | &nbsp;&nbsp;2&nbsp; | &nbsp;&nbsp;.&nbsp; |  &nbsp;&nbsp;2&nbsp; | &nbsp;&nbsp; Screw 6-32 pan x 25mm |
| &nbsp;&nbsp;.&nbsp; | &nbsp;&nbsp;.&nbsp; | &nbsp;&nbsp;2&nbsp; | &nbsp;&nbsp;.&nbsp; | &nbsp;&nbsp;.&nbsp; |  &nbsp;&nbsp;2&nbsp; | &nbsp;&nbsp; Screw 6-32 pan x 40mm |
| &nbsp;&nbsp;.&nbsp; | &nbsp;&nbsp;.&nbsp; | &nbsp;&nbsp;.&nbsp; | &nbsp;&nbsp;.&nbsp; | &nbsp;&nbsp;1&nbsp; |  &nbsp;&nbsp;1&nbsp; | &nbsp;&nbsp; Screwdriver 210x100 |
| &nbsp;&nbsp;.&nbsp; | &nbsp;&nbsp;.&nbsp; | &nbsp;&nbsp;.&nbsp; | &nbsp;&nbsp;.&nbsp; | &nbsp;&nbsp;2&nbsp; |  &nbsp;&nbsp;2&nbsp; | &nbsp;&nbsp; Screwdriver 210x100 |
| &nbsp;&nbsp;.&nbsp; | &nbsp;&nbsp;.&nbsp; | &nbsp;&nbsp;.&nbsp; | &nbsp;&nbsp;.&nbsp; | &nbsp;&nbsp;1&nbsp; |  &nbsp;&nbsp;1&nbsp; | &nbsp;&nbsp; Screwdriver 240x125 |
| &nbsp;&nbsp;.&nbsp; | &nbsp;&nbsp;.&nbsp; | &nbsp;&nbsp;.&nbsp; | &nbsp;&nbsp;.&nbsp; | &nbsp;&nbsp;1&nbsp; |  &nbsp;&nbsp;1&nbsp; | &nbsp;&nbsp; Screwdriver 270x150 |
| &nbsp;&nbsp;.&nbsp; | &nbsp;&nbsp;.&nbsp; | &nbsp;&nbsp;1&nbsp; | &nbsp;&nbsp;.&nbsp; | &nbsp;&nbsp;.&nbsp; |  &nbsp;&nbsp;1&nbsp; | &nbsp;&nbsp;7 Plies plywood plank 280x100x15mm |
| &nbsp;&nbsp;.&nbsp; | &nbsp;&nbsp;1&nbsp; | &nbsp;&nbsp;.&nbsp; | &nbsp;&nbsp;.&nbsp; | &nbsp;&nbsp;.&nbsp; |  &nbsp;&nbsp;1&nbsp; | &nbsp;&nbsp;7 Plies plywood plank 280x70x15mm |
| &nbsp;&nbsp;1&nbsp; | &nbsp;&nbsp;.&nbsp; | &nbsp;&nbsp;.&nbsp; | &nbsp;&nbsp;.&nbsp; | &nbsp;&nbsp;.&nbsp; |  &nbsp;&nbsp;1&nbsp; | &nbsp;&nbsp;7 Plies plywood plank 50x280x15mm |
| &nbsp;&nbsp;2&nbsp; | &nbsp;&nbsp;1&nbsp; | &nbsp;&nbsp;3&nbsp; | &nbsp;&nbsp;2&nbsp; | &nbsp;&nbsp;5&nbsp; | &nbsp;&nbsp;13&nbsp; | &nbsp;&nbsp;Total vitamins count |

<span></span>
[Top](#TOP)

---
<a name="wall_frenchcleat_assembly"></a>
## Wall Frenchcleat Assembly
### Vitamins
|Qty|Description|
|---:|:----------|
|1| Bottom french cleat optimised 280x50x15|
|1|7 Plies plywood plank 50x280x15mm|


### Assembly instructions
![wall_frenchcleat_assembly](assemblies/wall_frenchcleat_assembly_tn.png)


1. cut the plywood and external cut at 45°


![wall_frenchcleat_assembled](assemblies/wall_frenchcleat_assembled_tn.png)

<span></span>
[Top](#TOP)

---
<a name="screwdriver_support_assembly"></a>
## Screwdriver Support Assembly
### Vitamins
|Qty|Description|
|---:|:----------|
|1|7 Plies plywood plank 280x70x15mm|


### Assembly instructions
![screwdriver_support_assembly](assemblies/screwdriver_support_assembly_tn.png)


1. cut the plywood
1. drill holes


![screwdriver_support_assembled](assemblies/screwdriver_support_assembled_tn.png)

<span></span>
[Top](#TOP)

---
<a name="wall_support_assembly"></a>
## Wall Support Assembly
### Vitamins
|Qty|Description|
|---:|:----------|
|1|7 Plies plywood plank 280x100x15mm|


### Assembly instructions
![wall_support_assembly](assemblies/wall_support_assembly_tn.png)

![wall_support_assembled](assemblies/wall_support_assembled_tn.png)

<span></span>
[Top](#TOP)

---
<a name="support_assembly"></a>
## Support Assembly
### Vitamins
|Qty|Description|
|---:|:----------|
|2| Screw 6-32 pan x 40mm|


### Sub-assemblies

| 1 x screwdriver_support_assembly | 1 x wall_support_assembly |
|---|---|
| ![screwdriver_support_assembled](assemblies/screwdriver_support_assembled_tn.png) | ![wall_support_assembled](assemblies/wall_support_assembled_tn.png) 



### Assembly instructions
![support_assembly](assemblies/support_assembly_tn.png)


1. Center the screwdriver support on the wall support
1. Tighten screws


![support_assembled](assemblies/support_assembled_tn.png)

<span></span>
[Top](#TOP)

---
<a name="frenchcleat_assembly"></a>
## Frenchcleat Assembly
### Vitamins
|Qty|Description|
|---:|:----------|
|2| Screw 6-32 pan x 25mm|


### Sub-assemblies

| 1 x support_assembly | 1 x wall_frenchcleat_assembly |
|---|---|
| ![support_assembled](assemblies/support_assembled_tn.png) | ![wall_frenchcleat_assembled](assemblies/wall_frenchcleat_assembled_tn.png) 



### Assembly instructions
![frenchcleat_assembly](assemblies/frenchcleat_assembly_tn.png)


1. Attach french cleat to the wall


![frenchcleat_assembled](assemblies/frenchcleat_assembled_tn.png)

<span></span>
[Top](#TOP)

---
<a name="main_assembly"></a>
## Main Assembly
### Vitamins
|Qty|Description|
|---:|:----------|
|1| Screwdriver 210x100|
|2| Screwdriver 210x100|
|1| Screwdriver 240x125|
|1| Screwdriver 270x150|


### Sub-assemblies

| 1 x frenchcleat_assembly |
|---|
| ![frenchcleat_assembled](assemblies/frenchcleat_assembled_tn.png) 



### Assembly instructions
![main_assembly](assemblies/main_assembly_tn.png)


Assembly instructions in Markdown format in front of each module that makes an assembly.


![main_assembled](assemblies/main_assembled_tn.png)

<span></span>
[Top](#TOP)
