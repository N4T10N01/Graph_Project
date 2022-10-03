import sys
sys.path.append('..\\l1-graph-lab')



import time


class KPI:
    def __init__(self, objWithKPI):
        self.obj=objWithKPI
        self.kpis=objWithKPI.giveKPIs()

    def calcIndicators(self, func, arguments) -> dict:
        t=self._time(func, arguments)
        self.kpis.update({'executionTime':t})
        return self.kpis

    def _time(self, func, arguments) -> float:
        ti=time.time()
        func(*arguments)
        tf=time.time()
        return tf-ti
        



