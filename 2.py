import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import pandas as pd
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QFormLayout, QWidget, QLineEdit, QPushButton


class TableModel(QtCore.QAbstractTableModel):

    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            value = self._data.iloc[index.row(), index.column()]

            return str(value)

    def rowCount(self, index):
        return self._data.shape[0]

    def columnCount(self, index):
        return self._data.shape[1]

    def flags(self, index):
        if not index.isValid():
            return Qt.ItemIsEnabled

        return super().flags(index) | Qt.ItemIsEditable  # add editable flag.

    def headerData(self, section, orientation, role):
        # section is the index of the column/row.
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._data.columns[section])

            if orientation == Qt.Vertical:
                return str(self._data.index[section])

    def setData(self, index, value, role):
        if role == Qt.InputMethod:
            print(1)
        if role == Qt.EditRole:
            # Set the value into the frame.
            self._data.iloc[index.row(), index.column()] = value
            print(value)
            return True

        return False

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("2")
        self.resize(700, 500)
        self.table = QtWidgets.QTableView()

        # data = pd.DataFrame([
        #   [1, 9, 2],
        #   [1, 0, -1],
        #   [3, 5, 2],
        #   [3, 3, 2],
        #   [5, 8, 9],
        # ], columns = ['A', 'B', 'C'], index=['Row 1', 'Row 2', 'Row 3', 'Row 4', 'Row 5'])

        Z_1 = [(1, 10),(4, 10),(8, 7),(1, 3),(5, 3),(2, 9),(3, 6),(7, 12)]
        Z_2 = [(2, 6),(7, 5),(9, 7),(4, 8),(4, 10),(3, 6),(5, 8),(4, 9)]
        Z_3 = [(3, 6),(6, 4),(3, 2),(2, 6),(2, 6),(3, 12),(5, 7),(7, 7)]
        Z_4 = [(2, 4),(4, 8),(5, 3),(2, 5),(3, 4),(4, 8),(3, 11),(4, 8)]
        xz_lst = list(zip(Z_1, Z_2, Z_3, Z_4))

        xz_df_1 = pd.DataFrame(xz_lst, columns = ['Z1', 'Z2','Z3','Z4'],
                index=["X1","X2","X3","X4","X5","X6","X7","X8"])

        df = pd.DataFrame\
        (
            {'Z1': [(1, 10),(4, 10),(8, 7),(1, 3),(5, 3),(2, 9),(3, 6),(7, 12)],
             'Z2': [(2, 6),(7, 5),(9, 7),(4, 8),(4, 10),(3, 6),(5, 8),(4, 9)],
             'Z3': [(3, 6),(6, 4),(3, 2),(2, 6),(2, 6),(3, 12),(5, 7),(7, 7)],
             'Z4': [(2, 4),(4, 8),(5, 3),(2, 5),(3, 4),(4, 8),(3, 11),(4, 8)]
            }, index=["X1","X2","X3","X4","X5","X6","X7","X8"]
        )

        self.model = TableModel(df)
        self.table.setModel(self.model)

        # self.table.verticalHeader().setStyleSheet("QHeaderView::section{background-color: #e5cbcb; text-align: center;}");

        outerLayout = QVBoxLayout()
        #outerLayout.addWidget(self.table)
        # Create a form layout for the label and line edit
        topLayout = QFormLayout()
        topLayout.addWidget(self.table)
        # Create a layout for the checkboxes
        optionsLayout = QVBoxLayout()

        button = QPushButton()
        optionsLayout.addWidget(button)

        # Nest the inner layouts into the outer layout
        outerLayout.addLayout(topLayout)
        outerLayout.addLayout(optionsLayout)

        widget = QWidget()
        widget.setLayout(outerLayout)
        self.setCentralWidget(widget)



app=QtWidgets.QApplication(sys.argv)
window=MainWindow()
window.show()
app.exec()