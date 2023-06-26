
import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from ui_main import Ui_Form
import os
import pandas as pd
import numpy as np
import ast
import requests

# OWNER = 'uyounggong'
# REPO = 'test_0626'
# API_SERVER_URL = f"https://api.github.com/repos/{OWNER}/{REPO}"
# MY_API_KEY = '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'
#
# res = requests.get(f"{API_SERVER_URL}/releases/latest", auth=(OWNER, MY_API_KEY))
# if res.status_code != 200:
#     print("실패")

test = "version2"


class CenteredCheckBoxWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.checkbox = QCheckBox()
        layout = QHBoxLayout(self)
        layout.addWidget(self.checkbox)
        layout.setAlignment(Qt.AlignCenter)
        layout.setContentsMargins(0,0,0,0)
        self.checkbox.setCheckState(Qt.Unchecked)
        self.setLayout(layout)

    def paintEvent(self, event):
        pass

class CheckBoxHeader(QHeaderView):
    def __init__(self, parent=None):
        super().__init__(Qt.Horizontal, parent)
        self.setSectionResizeMode(QHeaderView.Stretch)
        self.setDefaultAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.setSectionsClickable(True)

        self.checkBox = QCheckBox()
        self.checkBox.stateChanged.connect(self.checkBoxClicked)

    def paintSection(self, painter, rect, logicalIndex):
        painter.save()
        super().paintSection(painter, rect, logicalIndex)
        painter.restore()

        if logicalIndex == 0:
            option = QStyleOptionButton()
            option.rect = QRect(rect.x() + rect.width() / 2 - 8, rect.y() + rect.height() / 2 - 8, 16, 16)
            if self.checkBox.isChecked():
                option.state = QStyle.State_On
            else:
                option.state = QStyle.State_Off
            self.style().drawControl(QStyle.CE_CheckBox, option, painter)

    def checkBoxClicked(self, state):
        for i in range(self.parent().rowCount()):
            widget = self.parent().cellWidget(i, 0)
            if widget is not None:
                checkbox = widget.checkbox
                if checkbox:
                    checkbox.setCheckState(self.checkBox.checkState())
        self.updateSection(0)


    def mousePressEvent(self, event):
        point = event.position().toPoint()
        if self.checkBox.geometry().contains(point):
            if self.checkBox.checkState() == Qt.Checked:
                self.checkBox.setCheckState(Qt.Unchecked)
            else:
                self.checkBox.setCheckState(Qt.Checked)
            self.updateSection(0)  # And this line
            return
        super().mousePressEvent(event)


class TableWidget(QTableWidget):
    def __init__(self, *args, **kwargs):
        super(TableWidget, self).__init__(*args, **kwargs)

        self.setAcceptDrops(True)
        self.setRowCount(0)
        self.setColumnCount(2)
        self.setHorizontalHeaderLabels(['', 'Filename'])

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

            for url in event.mimeData().urls():
                if url.isLocalFile():
                    self.addRow(url.toLocalFile())
        else:
            event.ignore()

    def addRow(self, text):
        row = self.rowCount()
        self.insertRow(row)
        checkBox = CenteredCheckBoxWidget()
        self.setCellWidget(row, 0, checkBox)
        self.setItem(row, 1, QTableWidgetItem(text))

class DnDLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            urls = event.mimeData().urls()
            for url in urls:
                file_path = url.toLocalFile()  # convert QUrl to local path
                self.window().add_to_table(file_path)


column_list = ["법정동코드", "시도명", "시군구명", "법정읍면동명", "법정리명", "산여부", "지번본번", "지번부번", "도로명코드", "도로명", "지하여부", "건물본번", "건물부번",
               "건축물대장건물명", "상세건물명", "건물관리번호", "읍면동일련번호", "행정동코드", "행정동명", "우편번호", "우편일련번호", "다량배달처명", "이동사유코드",
               "고시일자", "변동전도로명주소", "시군구용건물명", "공동주택여부", "기초구역여부", "상세주소여부", "비고1", "비고"]


class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        # 타이틀바 없애기
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.clickPosition = None
        self.show()


        # 최소화 / 닫기
        self.ui.btn_mini.clicked.connect(self.showMinimized)
        self.ui.btn_close.clicked.connect(self.close)
        self.ui.btn_close.setCursor(Qt.PointingHandCursor)
        self.ui.btn_mini.setCursor(Qt.PointingHandCursor)

        # 버튼 클릭 커서
        self.ui.btn_process.setCursor(Qt.PointingHandCursor)
        self.ui.btn_mapping.setCursor(Qt.PointingHandCursor)
        self.ui.btn_upload.setCursor(Qt.PointingHandCursor)
        self.ui.btn_run.setCursor(Qt.PointingHandCursor)

        # '전처리' or '매핑' 상단 메뉴 오고가기
        self.buttons = [self.ui.btn_process, self.ui.btn_mapping]
        self.ui.btn_process.clicked.connect(self.btn_menu)
        self.ui.btn_mapping.clicked.connect(self.btn_menu)

        sizePolicy1 = self.ui.label_3.sizePolicy()

        self.ui.label_3.setParent(None)
        self.ui.label_3 = DnDLabel(self.ui.frame_13)
        self.ui.label_3.setObjectName(u"label_3")
        self.ui.label_3.setSizePolicy(sizePolicy1)
        self.ui.label_3.setStyleSheet(u"padding-right : 10px;")
        self.ui.label_3.setPixmap(QPixmap(u":/images/upload.png"))
        self.ui.label_3.setAlignment(Qt.AlignCenter)
        self.ui.verticalLayout_7.addWidget(self.ui.label_3)

        self.ui.tableWidget.setColumnCount(2)
        self.ui.tableWidget.setHorizontalHeaderLabels(["", "File Path"])
        self.ui.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.ui.tableWidget.setColumnWidth(0, 5)
        self.ui.tableWidget.verticalHeader().setVisible(False)
        # 도대체가 왜 컬럼 헤드에 체크박스가 안들어가냐??
        # self.ui.tableWidget.setHorizontalHeader(CheckBoxHeader(self))

        self.ui.btn_run.clicked.connect(self.run_process)

        self.ui.btn_upload.clicked.connect(self.select_file)

        self.ui.progressBar.setValue(0)

        self.ui.pushButton.clicked.connect(self.select_all)
        self.ui.pushButton.setCursor(Qt.PointingHandCursor)

        self.ui.btn_load_file.clicked.connect(self.load_file)
        self.ui.btn_load_file.setCursor(Qt.PointingHandCursor)
        self.ui.lineEdit_mapping.setPlaceholderText("파일을 넣어주세요.")
        self.ui.lineEdit_mapping.setReadOnly(True)

        #############################
        # Create a new instance of TableWidget
        self.myTableWidget = TableWidget(self)
        # Remove the original tableWidget from the layout
        self.ui.verticalLayout_12.removeWidget(self.ui.tableWidget_mapping)
        # Delete the original tableWidget
        self.ui.tableWidget_mapping.deleteLater()
        self.ui.tableWidget_mapping = None
        # Add the new tableWidget to the layout
        self.ui.verticalLayout_12.addWidget(self.myTableWidget)
        # Set header for new tableWidget
        self.myTableWidget.setHorizontalHeader(CheckBoxHeader(self.myTableWidget))
        header = self.myTableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.myTableWidget.verticalHeader().setVisible(False)


        # mapping button click
        self.ui.btn_run_mapping.clicked.connect(self.mapping_list)
        self.ui.btn_run_mapping.setCursor(Qt.PointingHandCursor)

        # 삭제 버튼 클릭
        self.ui.btn_delete.clicked.connect(self.delete_list)
        self.ui.btn_delete.setCursor(Qt.PointingHandCursor)
        self.ui.progressBar_2.setValue(0)

    #     def moveWindow(e):
    #         if e.buttons() == Qt.LeftButton:
    #             self.move(self.pos() + e.globalPosition().toPoint() - self.clickPosition)
    #             self.clickPosition = e.globalPosition().toPoint()
    #             e.accept()
    #
    #     self.ui.frame.mousePressEvent = moveWindow
    #
    # def mousePressEvent(self, event):
    #     self.clickPosition = event.globalPosition().toPoint()

        self.oldPos = None

    def mousePressEvent(self, event):
        self.oldPos = event.globalPosition()

    def mouseMoveEvent(self, event):
        if self.oldPos:
            delta = event.globalPosition() - self.oldPos
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPosition()

    def mouseReleaseEvent(self, event):
        self.oldPos = None

    def delete_list(self):
        for i in reversed(range(self.myTableWidget.rowCount())):
            widget = self.myTableWidget.cellWidget(i, 0)
            if widget is not None:
                checkbox = widget.checkbox
                if checkbox and checkbox.isChecked():
                    self.myTableWidget.removeRow(i)

    def mapping_list(self):
        input_file = self.ui.lineEdit_mapping.text()

        row_total = []
        for i in range(self.myTableWidget.rowCount()):
            checkbox_widget = self.myTableWidget.cellWidget(i, 0)
            checkbox = checkbox_widget.checkbox
            if checkbox and checkbox.isChecked():
                row_items = [self.myTableWidget.item(i, j).text() for j in
                             range(1, self.myTableWidget.columnCount())]
                row_total.append(row_items)

        if not row_total or not input_file:
            return

        saveFile = QFileDialog.getSaveFileName(self, "파일저장" , '' ,'Excel (*.xlsx)')
        selected_file, _ = saveFile

        if not selected_file:
            return


        df_input = pd.read_excel(input_file)
        input_cols = df_input.columns

        df_result = df_input
        result = pd.DataFrame()
        for index, data in enumerate(row_total):
            self.setCursor(Qt.WaitCursor)
            QApplication.processEvents()
            self.ui.progressBar_2.setValue( (index + 1) / len(row_total) * 100)
            try:
                df = pd.read_csv(data[0], encoding='cp949', low_memory=False)

                temp_df = pd.merge(df_result, df, how='left', left_on='sgg_road', right_on='sgg_road')
                matched = temp_df.dropna(subset=['PNU'], how='any', axis=0)
                unmatched = temp_df[temp_df['PNU'].isna()]

                if not unmatched.empty:
                    df_result = unmatched[input_cols]

                if not matched.empty:
                    result = pd.concat([result, matched])
                    self.setCursor(Qt.WaitCursor)
                    QApplication.processEvents()
            except Exception as e:
                QMessageBox.warning(self, "경고", data[0] + "\n파일을 확인해주세요.\n또는 Input 파일을 확인해 주세요.")


        if result.empty:
            QMessageBox.about(self, "알림", "결과가 없습니다.")
            return


        result[['nm_san', 'nm_bonbun', 'nm_bubun']] = result['PNU'].apply(self.split_pnu)
        result = result.sort_index()

        columns = ['n', 'nm_san', 'nm_bonbun', 'nm_bubun']

        for column in columns:
            result[column] = result[column].astype(int)

        result.to_excel(selected_file, index=False, float_format='%.0f')
        self.unsetCursor()
        QMessageBox.about(self,"알림", "작업이 완료되었습니다.")
        self.ui.progressBar_2.setValue(0)

        path = os.path.realpath('/'.join(selected_file.split('/')[:-1]))
        os.startfile(path)




    def split_pnu(self, pnu):
        try:
            pnu_str = str(pnu).split('-')[1]
            nm_san = pnu_str[0]
            nm_bonbun = pnu_str[1:5]
            nm_bubun = pnu_str[5:]
        except IndexError:
            nm_san = nm_bonbun = nm_bubun = None
        return pd.Series([nm_san, nm_bonbun, nm_bubun])

    def load_file(self):
        window_user_name = os.path.expanduser('~')
        self.file = f'{window_user_name}/Desktop/'
        fname = QFileDialog.getOpenFileName(self, None, self.file)
        file = str(fname[0])

        if not file:
            return

        self.ui.lineEdit_mapping.setText(file)


    def select_all(self):
        if self.ui.pushButton.text() == '전체선택':
            for i in range(self.ui.tableWidget.rowCount()):
                widget = self.ui.tableWidget.cellWidget(i, 0)
                if widget is not None:  # This check is to ensure the widget is not None
                    self.ui.pushButton.setText("선택해제")
                    checkbox = widget.layout().itemAt(0).widget()
                    checkbox.setCheckState(Qt.Checked)
                else:
                    print("none")
                    return
        else:
            for i in range(self.ui.tableWidget.rowCount()):
                widget = self.ui.tableWidget.cellWidget(i, 0)
                if widget is not None:  # This check is to ensure the widget is not None
                    self.ui.pushButton.setText("전체선택")
                    checkbox = widget.layout().itemAt(0).widget()
                    checkbox.setCheckState(Qt.Unchecked)
                else:
                    print("none")
                    return

    def select_file(self):
        window_user_name = os.path.expanduser('~')
        self.file = f'{window_user_name}/Desktop/'
        fname = QFileDialog.getOpenFileNames(self, None, self.file)
        file = str(fname[0])

        if not file:
            return

        file_list = ast.literal_eval(file)
        for i in file_list:
            self.insert_row(i)
    def run_process(self):

        row_total = []
        row_items = []
        for i in range(self.ui.tableWidget.rowCount()):
            checkbox_widget = self.ui.tableWidget.cellWidget(i, 0)
            if checkbox_widget:
                layout = checkbox_widget.layout()
                checkbox = layout.itemAt(0).widget()
                if checkbox.isChecked():
                    row_items = [self.ui.tableWidget.item(i, j).text() for j in
                                 range(1, self.ui.tableWidget.columnCount())]
                    # print(row_items)
                    row_total.append(row_items)


        if len(row_total) ==0:
            return

        savefolder = QFileDialog.getExistingDirectory(self, '파일저장', 'C:/Users/Admin/Desktop')
        if not savefolder:
            print("비었음")
            return

        QApplication.processEvents()
        for index, i in enumerate(row_total):
            try:
                self.setCursor(Qt.WaitCursor)
                QApplication.processEvents()
                self.ui.lbl_fileName.setText(i[0].split('/')[-1])
                self.setCursor(Qt.WaitCursor)
                QApplication.processEvents()
                # self.ui.progressBar.setValue(index/len(row_total) * 100)
                if len(row_total) == index + 1:
                    self.ui.progressBar.setValue(100)
                else:
                    self.ui.progressBar.setValue((index + 1)/len(row_total) * 100)
                self.setCursor(Qt.WaitCursor)
                QApplication.processEvents()
                new_name = "Preprocessing_" + i[0].split('/')[-1]
                new_dir = savefolder + "/" + new_name
                data = pd.read_csv(i[0], sep='|', encoding='cp949', names=column_list, header=None, index_col=False, low_memory=False)
                data = self.process(data)
                data.to_csv(new_dir, index = False)
                self.setCursor(Qt.WaitCursor)
                QApplication.processEvents()
            except Exception as e:
                QMessageBox.warning(self, "경고", i[0].split('/')[-1] + "\n파일의 형식이 잘못되었습니다.\n확인해주세요.")


        self.unsetCursor()
        QMessageBox.about(self, "알림", "작업이 완료되었습니다.")
        self.ui.progressBar.setValue(0)
        os.startfile(savefolder)
        for i in range(self.ui.tableWidget.rowCount()):
            widget = self.ui.tableWidget.cellWidget(i, 0)
            if widget is not None:  # This check is to ensure the widget is not None
                self.ui.pushButton.setText("전체선택")
                checkbox = widget.layout().itemAt(0).widget()
                checkbox.setCheckState(Qt.Unchecked)
            else:
                print("none")
                return


    def process(self, data):
        # region PNU만들기
        # 산여부 + 1
        self.ui.progressBar.setValue(10)
        data['산여부'] = data['산여부'] + 1
        data['산여부'] = data['산여부'].astype(str)
        # 지번본번 0000 4자리로
        self.ui.progressBar.setValue(20)
        data['지번본번'] = data['지번본번'].astype(str).str.zfill(4)
        # 지번부번 0000 4자리로
        data['지번부번'] = data['지번부번'].astype(str).str.zfill(4)
        # PNU = 법정동코드-(산여부+1)+지번본번+지번부번
        self.ui.progressBar.setValue(30)
        data['법정동코드'] = data['법정동코드'].astype(str)
        data['PNU'] = data['법정동코드'] + '-' + data['산여부'] + data['지번본번'] + data['지번부번']
        # endregion

        # region 도로명주소 만들기
        self.ui.progressBar.setValue(40)
        data['도로명주소'] = data['시도명'] + ' ' + data['시군구명'] + ' ' + data['도로명'] + ' ' + np.where(
            data['지하여부'].astype(str) == '1', 'B', '') + data['건물본번'].astype(str) + np.where(
            data['건물부번'].astype(str) == '0',
            '',
            '-' + data['건물부번'].astype(str))
        # endregion

        # region 필요한 컬럼만 추출
        self.ui.progressBar.setValue(50)
        data2 = data[['도로명주소', 'PNU', '시도명', '시군구명', '법정읍면동명', '법정리명', '도로명코드', '이동사유코드', '고시일자']].copy()
        # endregion

        # rename column
        self.ui.progressBar.setValue(60)
        data2.rename(
            columns={'도로명주소': 'sgg_road', '시도명': 'nm_sido', '시군구명': 'nm_sgg', '법정읍면동명': 'nm_umd', '법정리명': 'nm_ri',
                     '도로명코드': 'cd_road', '이동사유코드': 'cd_change', '고시일자': 'date'}, inplace=True)

        self.ui.progressBar.setValue(70)
        # 중복확인
        temp = data2.groupby('sgg_road').size().reset_index(name='n')
        self.ui.progressBar.setValue(80)
        data2 = pd.merge(data2, temp, on='sgg_road', how='left')

        # 중복제거
        self.ui.progressBar.setValue(90)
        data2 = data2.drop_duplicates()
        self.ui.progressBar.setValue(100)
        data2 = data2.reset_index(drop=True)

        return data2

    def add_to_table(self, file_path):
        # row = self.ui.tableWidget.rowCount()
        # self.ui.tableWidget.insertRow(row)
        # # Adding the checkbox widget in the first column
        # checkbox = QCheckBox()
        # checkbox.setCheckState(Qt.Unchecked)
        # cellWidget = QWidget()
        # layoutCB = QHBoxLayout(cellWidget)
        # layoutCB.addWidget(checkbox)
        # layoutCB.setAlignment(Qt.AlignCenter)
        # layoutCB.setContentsMargins(0, 0, 0, 0)
        # cellWidget.setLayout(layoutCB)
        # self.ui.tableWidget.setCellWidget(row, 0, cellWidget)
        # # Add the file_path in the second column
        # self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(file_path))
        self.insert_row(file_path)


    def insert_row(self, path):
        row = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(row)
        checkbox = QCheckBox()
        checkbox.setCheckState(Qt.Unchecked)
        cellWidget = QWidget()
        layoutCB = QHBoxLayout(cellWidget)
        layoutCB.addWidget(checkbox)
        layoutCB.setAlignment(Qt.AlignCenter)
        layoutCB.setContentsMargins(0, 0, 0, 0)
        cellWidget.setLayout(layoutCB)
        self.ui.tableWidget.setCellWidget(row, 0, cellWidget)
        self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(path))


    def btn_menu(self):
        btn= self.sender()
        btnName = btn.objectName()

        index_mapping = {
            "btn_process" : 0,
            "btn_mapping" : 1
        }

        if btnName in index_mapping:
            self.ui.stackedWidget.setCurrentIndex(index_mapping[btnName])
            self.update_button_style(btn)

    def update_button_style(self, active_button):
        active_style = "border : none; border-bottom : 2px solid rgb(55, 95, 245)"
        inactive_style = "border : none;"

        for button in self.buttons:
            button.setStyleSheet(active_style if button == active_button else inactive_style)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec())