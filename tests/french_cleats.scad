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

include <NopSCADlib/utils/core/core.scad>
use <NopSCADlib/utils/layout.scad>

include <../vitamins/french_cleats.scad>

module french_cleats()
{
    depth = 15;
    height = 60;
    space = 1;

    // Standard french cleats
    translate([ height / 2, 0, 0 ]) rotate([ 0, 0, -90 ])
        french_cleat(french_cleats[0], height = height, depth = depth, width = 20, bottom = true);
    translate([ height / 2, 0, 0 ]) rotate([ 0, 0, -90 ]) translate([ 0, height - depth + space, 0 ])
        french_cleat(french_cleats[0], height = height, depth = 15, width = 20, bottom = false);

    // simple french cleats
    translate([ height / 2, depth + space, 0 ]) rotate([ 0, 0, -90 ])
        french_cleat(french_cleats[1], height = height, depth = depth, width = 20, bottom = true);
    translate([ height / 2, depth + space, 0 ]) rotate([ 0, 0, -90 ]) translate([ 0, height - depth + space, 0 ])
        french_cleat(french_cleats[1], height = height, depth = 15, width = 20, bottom = false);
}

if ($preview)
    french_cleats();
