//! # CADLibrary
//!
//! I would share here my OpenSCAD designs, generally related to woodworking.
//!
//! I draw inspiration from the excellent [NopSCADlib](https://github.com/nophead/NopSCADlib) project by nophead.
//!
//!  <img src="libtest.png" width="100%"/>
// This file shows all the parts in the library.

use <tests/french_cleats.scad>;
use <tests/magnet_bars.scad>;
use <tests/plywoods.scad>;

space = 2;

magnet_bars();
translate([ 165, 135, 9 ]) french_cleats();
