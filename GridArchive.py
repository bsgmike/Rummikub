"""
This class implements a saved queue of grid states. It allows queued grid states
to be retrieved so that player moves can be "undone".
"""

class GridArchive():
    def __init__(self):
        print("started a new grid archive")
        self.gridQueue = []

    def addGridToArchive(self, gridToSave):
        print("added a grid to the list")
        self.gridQueue.append(gridToSave)

    def getGridFromArchive(self):
        if len(self.gridQueue) > 0:
            return self.gridQueue.pop()
        else:
            return

    def getArchiveSize(self):
        return len(self.gridQueue)

    def isEmpty(self):
        if len(self.gridQueue) > 0:
            return False
        else:
            return True


class GridArchiveManager():
    player1Grid = None
    player2Grid = None
    gameBoard = None

    def __init__(self, p1Grid, p2Grid, gbGrid):
        GridArchiveManager.player1Grid = p1Grid
        GridArchiveManager.player2Grid = p2Grid
        GridArchiveManager.gameBoard = gbGrid

        self.player1Log = GridArchive()
        self.player2Log = GridArchive()
        self.boardLog = GridArchive()

    def saveGameState(self):
        p1 = GridArchiveManager.player1Grid.getGridState()
        self.player1Log.addGridToArchive(p1)

        p2 = GridArchiveManager.player2Grid.getGridState()
        self.player2Log.addGridToArchive(p2)

        gB = GridArchiveManager.gameBoard.getGridState()
        self.boardLog.addGridToArchive(gB)

    def restoreGameState(self):
        if self.player1Log.isEmpty() or self.player2Log.isEmpty() or self.boardLog.isEmpty():
            print("Error - no saved state to restore", "   P1 = ", self.player1Log.getArchiveSize(), "P2 = ", self.player1Log.getArchiveSize(), "GB = ", self.boardLog.getArchiveSize())
            return
        else:
            p1Grid = self.player1Log.getGridFromArchive()
            GridArchiveManager.player1Grid.restoreGridState(p1Grid)

            p2Grid = self.player2Log.getGridFromArchive()
            GridArchiveManager.player2Grid.restoreGridState(p2Grid)

            gBGrid = self.boardLog.getGridFromArchive()
            GridArchiveManager.gameBoard.restoreGridState(gBGrid)




