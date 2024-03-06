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

include <../vitamins/french_cleats.scad>
include <NopSCADlib/utils/core/core.scad>

module french_cleats()
{
    width = 100;
    height = 60;
    depth = 15;

    cutspace = 2;
    space = 5;

    // Standard french cleats
    translate([ (height - depth + cutspace) / 2, 0, 0 ]) rotate([ 180, 0, 0 ])
        french_cleat(frenchcleat_std, width, height, depth, true);
    translate([ -(height - depth + cutspace) / 2, 0, 0 ]) rotate([ 180, 0, 0 ])
        french_cleat(frenchcleat_std, width, height, depth, false);

    // simple french cleats
    translate([ (depth - 3 * height - space) / 2, 0, 0 ]) rotate([ 180, 0, 0 ])
        french_cleat(frenchcleat_opt, width, height, depth, true);

    translate([ -cutspace + (3 * depth - 5 * height - space) / 2, 0, 0 ]) rotate([ 180, 0, 0 ])
        french_cleat(frenchcleat_opt, width, height, depth, false);
}

if ($preview)
    french_cleats();
