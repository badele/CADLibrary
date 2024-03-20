//! # CADLibrary
//!
//! I would share here my OpenSCAD designs, generally related to woodworking.
//!
//! I draw inspiration from the excellent [NopSCADlib](https://github.com/nophead/NopSCADlib) project by nophead.
//! ## Installation
//!
//! Install requirements
//!
//! - `direnv` - direnv execute a command when enter on this folder project
//! - `nix` package manager for all systems ( Linux, MacOS, Windows)
//!
//! Once `direnv` and `nix` are installed, you just need to enter the project directory,
//! and then this project will configure itself automatically (see bellow tasks)
//!
//! - Clone the NoptCADlib repository
//! - Install requirement packages
//! - Create python virtualenv
//!
//! ## Usage
//!
//! ```bash
//! just inventories # Generate all vitamins
//! just projects    # Generate all projects
//! ```
//!
//!  <img src="libtest.png" width="100%"/>
//!
//! ## Projects
//!
//! | | |
//! |-|-|
//! | ![screwdrivers_store](./projects/screwdrivers_store/assemblies/main_assembly.png)| ![phone holder](./projects/phone_holder/assemblies/main_assembly.png) |
//! | [screwdrivers store](./projects/screwdrivers_store) | [phone holder](./projects/phone_holder) |
//!
//
// This file shows all the parts in the library.

use <tests/french_cleats.scad>;
use <tests/magnet_bars.scad>;
use <tests/plywoods.scad>;
use <tests/screwdrivers.scad>;
use <tests/wood_cylinder.scad>;

magnet_bars();
translate([ 53, 210, 9 ]) plywoods();
translate([ 165, 210, 9 ]) rotate([ 0, 90, 0 ]) wood_cylinders();
translate([ 165, 135, 9 ]) french_cleats();
translate([ 250, 80, 10 ]) rotate(-90, [ 1, 0, 0 ]) screwdrivers();
