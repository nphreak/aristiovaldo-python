import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.15
import QtQuick.Controls.Material 2.15


ApplicationWindow{
    id: window
    width: 800
    height: 500
    visible:true
    title: qsTr("Aristiovaldo")

    // set flags
    flags: Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint | Qt.CustomizeWindowHint | Qt.MSWindowsFixedSizeDialogHint | Qt.WindowTitleHint


    // set material styles
    Material.theme: Material.Dark
    Material.accent: Material.LightBlue

    Rectangle{
        id: topBar
        height: 40
        color: Material.color(Material.Blue)
        anchors{
            left: parent.left
            right: parent.right
            top: parent.top
            margins: 10
        }
        radius: 5

        Text {
            text: qsTr("Aristiovaldo por Pedro nPhreak Rodrigues - Pedrin")
            anchors.verticalCenter: parent.verticalCenter
            verticalAlignment: Text.AlignVCenter
            horizontalAlignment: Text.AlignHCenter
            color: "#ffffff"            
            anchors.horizontalCenter: parent.horizontalCenter
            
        }

    }
    
    Rectangle{
        id: connectionArea
        width: 200
        height: 200
        color: "#20ffffff"
        anchors {
            top: topBar.bottom
            left: parent.left
            margins: 10
        }
        ComboBox {
            id: portSelect
            model: ["Selecionar"]
            height: 40
            anchors {
                top: parent.top
                left: parent.left
                right: parent.right
                margins: 5
            }
            
        }
        Button {
            id: searchPortsButton
            height: 40
            Text {
                text: qsTr("Search Ports")
                anchors.verticalCenter: parent.verticalCenter
                verticalAlignment: Text.AlignVCenter
                horizontalAlignment: Text.AlignHCenter
                color: "#ffffff"            
                anchors.horizontalCenter: parent.horizontalCenter
            }
            anchors{
                top: portSelect.bottom
                right: parent.right
                left: parent.left
                margins: 5
            }
            onPressed: {
                backend.port_list(portSelect.model[0])
            }

        }

        Button {
            id: connectButton
            height: 40
            width: 90
            Text {
                text: qsTr("Conectar")
                anchors.verticalCenter: parent.verticalCenter
                verticalAlignment: Text.AlignVCenter
                horizontalAlignment: Text.AlignHCenter
                color: "#ffffff"            
                anchors.horizontalCenter: parent.horizontalCenter            
            }
            
            anchors{
                top: searchPortsButton.bottom
                left: parent.left
                margins: 5
            }
            onPressed: {
                backend.connect(portSelect.currentText)
            }

        }

        Button {
            id: disconnectButton
            height: 40
            width: 90
            Text {
                text: qsTr("Disconnect")
                anchors.verticalCenter: parent.verticalCenter
                verticalAlignment: Text.AlignVCenter
                horizontalAlignment: Text.AlignHCenter
                color: "#ffffff"            
                anchors.horizontalCenter: parent.horizontalCenter
            }
            anchors{
                top: searchPortsButton.bottom
                right: parent.right
                margins: 5
            }
            onPressed: {
                backend.disconnect(portSelect.currentText)
            }

        }

        Text {
            id: statusString
            text: qsTr("esperando")
            color: "#ffffff"
            height: 40
            anchors{
                top: connectButton.bottom
                horizontalCenter: parent.horizontalCenter
                margins: 5
            }
            verticalAlignment: Text.AlignVCenter
            horizontalAlignment: Text.AlignHCenter
        }
    }
    
    Connections {
        target: backend
        
        function onSetPortList(port_list) {
            var split_list = port_list.split(",")
            portSelect.model = split_list
        }

        function onConnectToSerialPort(text) {
            statusString.text = text
        }

        function onDisconnectSerialPort(text) {
            statusString.text = text
        }
    }
    
}