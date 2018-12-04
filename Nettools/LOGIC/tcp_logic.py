from PyQt5 import QtWidgets
import socket,logging
import threading
import sys
from Nettools.UI import tcp_clientUI, tcp_serverUI
import ctypes
import inspect

# logging.basicConfig(filename='tcp.log',level=logging.DEBUG,format=' %(asctime)s - %(levelname)s- %(message)s')
logging.basicConfig(level=logging.DEBUG,format=' %(asctime)s - %(levelname)s- %(message)s')

class stopThreading():
    def __init__(self):
        pass

    def _async_raise(self,tid, exc_type):
        tid = ctypes.c_long(tid)
        if not inspect.isclass(exc_type):
            exc_type = type(exc_type)
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exc_type))
        if res == 0:
            raise ValueError("invalid thread id")
        elif res != 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
            raise SystemError("PyThreadState_SetAsyncExc failed")


    # 强制关闭线程的方法
    def stop_thread(self,thread):
        self._async_raise(thread.ident, SystemExit)



class TcpserverLogic(QtWidgets.QWidget, tcp_serverUI.Ui_serverUI):
    def __init__(self):
        super(TcpserverLogic, self).__init__()
        self.setupUi(self)
        self.tcp_socket = None
        self.sever_th = None
        self.client_socket_list = list()

        self.link = False  # 用于标记是否开启了连接


    def tcp_server_start(self):
        """
        功能函数，TCP服务端开启的方法
        :return: None
        """
        #创建套接字
        self.tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try:
            port = int(self.portlineEdit.text())
            self.tcp_socket.bind(('',port))
        except Exception as ret:
            msg = '请检查端口号\n'
            logging.debug(msg)
        else:
            self.tcp_socket.listen()
            self.server_th = threading.Thread(target=self.tcp_server_action)
            self.server_th.start()
            msg =  'TCP服务端正在监听端口:%s\n' % str(port)
            logging.debug(msg)

    def tcp_server_action(self):
        """
        功能函数，供创建线程的方法；
        使用子线程用于监听并创建连接，使主线程可以继续运行，以免无响应
        使用非阻塞式并发用于接收客户端消息，减少系统资源浪费，使软件轻量化
        :return:None
        """
        while True:
            try:
                client_socket,client_address = self.tcp_socket.accept()
            except Exception as ret:
                logging.debug(ret)
            else:
                # 将创建的客户端套接字存入列表,client_address为ip和端口的元组
                self.client_socket_list.append((client_socket,client_address))
                msg = 'TCP服务端已连接IP:%s端口:%s\n' % client_address
                logging.debug(msg)
            # 轮询客户端套接字列表，接收数据
            for client,address in self.client_socket_list:
                try:
                    recv_msg = client.recv(1024)
                except Exception as ret:
                    logging.debug(ret)
                else:
                    if recv_msg:
                        msg = recv_msg.decode('utf-8')
                        msg = '来自IP:{}端口:{}:\n{}\n'.format(address[0], address[1], msg)
                        logging.debug(msg)
                    else:
                        client.close()
                        self.client_socket_list.remove((client,address))


    def tcpserver_send(self):
        """
        功能函数，用于TCP服务端和TCP客户端发送消息
        :return: None
        """
        try:
            send_msg = (str(self.send_plainTextEdit.toPlainText())).encode('utp-8')
            for client,address in self.client_socket_list:
                client.send(send_msg)
            msg = 'TCP服务端已发送\n'
            logging.debug(msg)
        except Exception as ret:
            msg = '发送失败\n'
            logging.debug(msg)

    def tcpserver_close(self):
        """
        功能函数，关闭网络连接的方法
        :return:
        """
        try:
            for client, address in self.client_socket_list:
                client.close()
            self.tcp_socket.close()
            if self.link is True:
                msg = '已断开网络\n'
                logging.debug(msg)
        except Exception as ret:
            logging.debug(ret)
        try:
            stopThreading.stop_thread(self.sever_th)
        except Exception:
            pass
        try:
            stopThreading.stop_thread(self.client_th)
        except Exception:
            pass



class TcpclientLogic(QtWidgets.QWidget, tcp_clientUI.Ui_clientUI):
    def __init__(self):
        super(TcpclientLogic, self).__init__()
        self.setupUi(self)
        self.tcp_socket = None
        self.client_th = None
        self.link = False  # 用于标记是否开启了连接

    def tcp_client_start(self):
        """
        功能函数，TCP客户端连接其他服务端的方法
        :return:
        """
        self.tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try:
            address = (str(self.iplineEdit.text()),int(self.portlineEdit.text()))
        except Exception as ret:
            msg = '请检查目标IP，目标端口\n'
            logging.debug(msg)
        else:
            try:
                msg = '正在连接目标服务器\n'
                logging.debug(msg)
                self.tcp_socket.connect(address)
            except Exception as ret:
                msg = '无法连接目标服务器\n'
                logging.debug(msg)
            else:
                self.client_th = threading.Thread(target=self.tcp_client_action)
                self.client_th.start()
                msg = 'TCP客户端已连接IP:%s端口:%s\n' % address
                logging.debug(msg)

    def tcp_client_action(self,address):
        """
        功能函数，用于TCP客户端创建子线程的方法，阻塞式接收
        :return:
        """
        while True:
            recv_msg = self.tcp_socket.recv(1024)
            if recv_msg:
                msg = recv_msg.decode('utf-8')
                msg = '来自IP:{}端口:{}:\n{}\n'.format(address[0], address[1], msg)
                logging.debug(msg)
            else:
                self.tcp_socket.close()
                self.reset()
                msg = '从服务器断开连接\n'
                logging.debug(msg)
                break


    def tcpclient_send(self):
        """
        功能函数，用于TCP客户端和TCP服务端发送消息
        :return: None
        """
        try:
            send_msg = (str(self.send_plainTextEdit.toPlainText())).encode('utp-8')
            self.tcp_socket.send(send_msg)
            msg = 'TCP客户端已发送\n'
            logging.debug(msg)
        except Exception as ret:
            msg = '发送失败\n'
            logging.debug(msg)

    def tcpclient_close(self):
        """
        功能函数，关闭网络连接的方法
        :return:
        """
        try:
            self.tcp_socket.close()
            if self.link is True:
                msg = '已断开网络\n'
                logging.debug(msg)
        except Exception as ret:
            logging.debug(ret)
        try:
            stopThreading.stop_thread(self.sever_th)
        except Exception:
            pass
        try:
            stopThreading.stop_thread(self.client_th)
        except Exception:
            pass





if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = TcpclientLogic()
    ui.show()
    sys.exit(app.exec_())