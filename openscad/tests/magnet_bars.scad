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

include <../vitamins/magnet_bars.scad>

module magnet_bars()
{
    depth = mth_depth(magnetbars[0]);
    posx1 = mth_width(magnetbars[0]) / 2;
    posx2 = mth_width(magnetbars[0]) + 10 + mth_width(magnetbars[1] / 2);
    posx3 = mth_width(magnetbars[2]) / 2;

    posxyz = [[posx1, 2 * depth + 10, 0], [posx2, 2 * depth + 10, 0], [posx3, depth, 0]];

    for (i = [0:len(magnetbars) - 1])
    {
        translate(posxyz[i])
        {
            magnet_bar(magnetbars[i]);
        }
    }
}

if ($preview)
    magnet_bars();
