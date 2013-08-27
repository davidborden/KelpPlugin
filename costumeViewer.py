"""This plugin is for Lesson 4: Costume Changes."""

from __future__ import print_function
from collections import Counter
from kelpplugin import KelpPlugin
from broadcastViewer import Broadcast
from initializationViewer import Initialization
import os
import sys
import kurt

'''How to run this plugin:
    hairball -d. -p costumeViewer.Costumes test.sb
'''

class Costumes(KelpPlugin):

    def __init__(self):
        super(Costumes, self).__init__

    def costumes(self, scratch):
        projectName = scratch.name
        costumes = dict()
        costumes['Stage'] = set()
        index = 0
        for background in scratch.stage.backgrounds:
            costumes['Stage'].add(KelpPlugin.save_png(projectName, background, index, 'Stage'))
            index += 1
        for sprite in scratch.sprites:
            index = 0
            costumes[sprite.name] = set()
            for costume in sprite.costumes:
                costumes[sprite.name].add(KelpPlugin.save_png(projectName, costume, index, sprite.name))
                index += 1
        self.costumes = costumes

    def analyze(self, scratch):
        if not getattr(scratch, 'kelp_prepared', False):
            KelpPlugin.tag_reachable_scripts(scratch)


        #call broadcast
        self.Broadcast = Broadcast()
        self.Broadcast.analyze(scratch)

        #call initialization
        self.Init = Initialization()
        self.Init.analyze(scratch)

        #costumes
        self.costumes(scratch)
        self.CostumeDisplay(self.costumes, fil)

    def CostumeDisplay(self, cost, fil):
		file = KelpPlugin.html_view("costume", "Costumes")
        file.write('<body>')

        # Displays sprite names and costumes
        file.write('<p>COSTUMES</p>')
        file.write('<table>')
        file.write('  <tr>')
        for sprite, value in cost.items():
            #if sprite != 'Stage':
            file.write('    <th>{0}</th>'.format(sprite))
        file.write('  </tr>')
        file.write('  <tr>')
        for sprite, values in cost.items():
            file.write('<td>')
            for value in values:
                #if sprite != 'Stage':
                file.write('    <p><img src="{0}" height="100" width="100"></p>'.format(value))
                #file.write('<p><img src="{0}"></p>'.format(value))
            file.write('</td>')
        file.write('  </tr>')
        file.write('</table>')

        self.Broadcast.BroadcastDisplay(self.Broadcast.help, KelpPlugin.thumbnails, fil)
        self.Init.initializationDisplay(self.Init.changes, self.Init.events);

        file.write('</body>')
        file.write('</html>')

        file.close()
        return 0
