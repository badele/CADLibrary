//
// CADLibrary Copyright Bruno Adelé 2024
// brunoadele@gmail.com
// blog.jesuislibre.org
//
// This file is part of CADLibrary.
//
// CADLibrary is free software: you can redistribute it and/or modify it under the terms of the
// GNU General Public License as published by the Free Software Foundation, either version 3 of
// the License, or (at your option) any later version.
//
// CADLibrary is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
// without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
// See the GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License along with CADLibrary.
// If not, see <https://www.gnu.org/licenses/>.
//

include <../vitamins/screwdriver.scad>
include <NopSCADlib/utils/core/core.scad>

module screwdrivers()
{
    screwdriver(270, 150, 37.5, 25, 17, 8);
    translate([ 45, 0, 0 ]) screwdriver(240, 125, 34.5, 23, 15.5, 5.5);
    translate([ 90, 0, 0 ]) screwdriver(210, 100, 28.5, 19, 14.2, 4.5);
    translate([ 130, 0, 0 ]) screwdriver(210, 100, 28.5, 19, 13.5, 4.5);
    translate([ 170, 0, 0 ]) screwdriver(210, 100, 28.5, 19, 13.5, 4.5);
}

if ($preview)
    screwdrivers();
