class RlGeneratorView:
    def __init__(self, mainUI):
        self.ui = mainUI
        # connect generateLabelButton to display pageGenerateLabel page
        self.ui.generateRLBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.pageGenerateRL))
