"""This plugin is for Lesson 1: Sequence."""

from __future__ import print_function
from collections import Counter
from kelpplugin import KelpPlugin
import os
import sys
import kurt
import PIL

'''How to run this plugin:
    hairball -d. -p sequenceViewer.Sequence test.sb
'''


class Sequence(KelpPlugin):
    def __init__(self):
        super(Sequence, self).__init__

    def analyze(self, scratch):
        if not getattr(scratch, 'kelp_prepared', False):
            KelpPlugin.tag_reachable_scripts(scratch)

        seq = dict()
        # store the screen
        seq['screen'] = KelpPlugin.save_png(projectName, scratch.thumbnail, 'screen');

        #store the values for the variables level and points, if they exist
        level = False
        points = False

        for name, var in scratch.variables.items():
            if name == 'level' or name == 'Level':
                level = True
                seq[name] = var.value
            elif name == 'points' or name == 'Points':
                points = True
                seq[name] = var.value

        # If they don't exist, store them with the value of -1
        if level == False:
            seq['level'] = '-1'
        if points == False:
            seq['points'] = '-1'

        # show the display
        self.SequenceDisplay(seq)


	def SequenceDisplay(self, seq):
		# stylesheet
        fil.write('<link rel="stylesheet" type="text/css" href="style.css">')

        # print the screen
        fil.write('<h1>Screenshot of Octopi Project</h1>')
        fil.write('<img src="{0}" border="1" heigh="240" width="320">'.format(seq['screen']))

        # variables
        for var in ['level', 'points']:
        	if seq[var] == '-1': #if they don't exist don't print them out
        		fil.write('<p>The variable <b>' + name + ' </b>does not exist</p>')
        	else:
        		fil.write('<p>{0}: {1}</p>'.format(var, seq[var]))

        fil.close()
        return 0
