##               █      █                                                     ##
##               ████████                                                     ##
##             ██        ██                                                   ##
##            ███  █  █  ███        splash_screen.py                          ##
##            █ █        █ █        Game_RamIt                                ##
##             ████████████                                                   ##
##           █              █       Copyright (c) 2016                        ##
##          █     █    █     █      AmazingCow - www.AmazingCow.com           ##
##          █     █    █     █                                                ##
##           █              █       N2OMatt - n2omatt@amazingcow.com          ##
##             ████████████         www.amazingcow.com/n2omatt                ##
##                                                                            ##
##                  This software is licensed as GPLv3                        ##
##                 CHECK THE COPYING FILE TO MORE DETAILS                     ##
##                                                                            ##
##    Permission is granted to anyone to use this software for any purpose,   ##
##   including commercial applications, and to alter it and redistribute it   ##
##               freely, subject to the following restrictions:               ##
##                                                                            ##
##     0. You **CANNOT** change the type of the license.                      ##
##     1. The origin of this software must not be misrepresented;             ##
##        you must not claim that you wrote the original software.            ##
##     2. If you use this software in a product, an acknowledgment in the     ##
##        product IS HIGHLY APPRECIATED, both in source and binary forms.     ##
##        (See opensource.AmazingCow.com/acknowledgment.html for details).    ##
##        If you will not acknowledge, just send us a email. We'll be         ##
##        *VERY* happy to see our work being used by other people. :)         ##
##        The email is: acknowledgment_opensource@AmazingCow.com              ##
##     3. Altered source versions must be plainly marked as such,             ##
##        and must not be misrepresented as being the original software.      ##
##     4. This notice may not be removed or altered from any source           ##
##        distribution.                                                       ##
##     5. Most important, you must have fun. ;)                               ##
##                                                                            ##
##      Visit opensource.amazingcow.com for more open-source projects.        ##
##                                                                            ##
##                                  Enjoy :)                                  ##
##----------------------------------------------------------------------------##

################################################################################
## Imports                                                                    ##
################################################################################
## Pygame ##
import pygame;
## Game_RamIt ##
import assets;
import director;
from constants import *;
from cowclock  import *;

class SplashScreen:
    ############################################################################
    ## Init                                                                   ##
    ############################################################################
    def __init__(self):
        director.set_clear_color(COLOR_WHITE);

        ## Logo
        self._logo     = assets.load_image("AmazingCow_Logo.png");
        logo_size      = self._logo.get_size();
        self._logo_pos = (GAME_WIN_WIDTH  * 0.5 - logo_size[0] * 0.5,
                          GAME_WIN_HEIGHT * 0.5 - logo_size[1] * 0.5);

        self._visible = False;

        ## Timer
        self._timer = CowClock(0.3, 5, self._on_timer_tick, self._on_timer_done);
        self._timer.start();


    ############################################################################
    ## Update / Draw                                                          ##
    ############################################################################
    def update(self, dt):
        self._timer.update(dt);

    def draw(self, surface):
        if(self._visible):
            surface.blit(self._logo, self._logo_pos);

    ############################################################################
    ## Timer Callbacks                                                        ##
    ############################################################################
    def _on_timer_tick(self):
        self._visible = True;

    def _on_timer_done(self):
        director.go_to_menu();
