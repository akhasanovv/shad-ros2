"""STUDENT FILE. Implement the search state machine. No ROS calls in this module.
Use raster() and drive_to(); never read simulator internals or web /state.
Return Outcome('absent') ONLY after covering the entire requested area.
Return Outcome('found', x, y) after measuring the rectangle centre.
"""
from math import pi

from course_lab.world import Area, Sample, Decision, Outcome
from course_lab.navigation import drive_to, raster
from course_lab.probe import RectangleProbe

class Mission:
    def __init__(self, area: Area):
        self.area = area
        self.waypoints = raster(area)
        self.index = 0
        self.rp = None

    def step(self, sample: Sample) -> Decision:
        if sample.green and self.rp is None and self.area.contains(sample.x, sample.y):
            self.rp = RectangleProbe(self.area, sample)
            return self.rp.step(sample)

        if self.rp is not None:
            return self.rp.step(sample)
        
        v, w, reached = drive_to(sample, self.waypoints[self.index])
        while reached:
            self.index += 1
            if self.index == len(self.waypoints):
                return Decision(0.0, 0.0, Outcome('absent'))
            v, w, reached = drive_to(sample, self.waypoints[self.index])

        return Decision(v, w)
        

        
