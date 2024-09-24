import serial
import time

class simple_sender:
    def __init__(self):
        try:
            self.ar = serial.Serial('COM5', 9600)
            print('connecting to arduino')
            time.sleep(2)
            print('connected.....')
        except serial.SerialException as e:
            print(f'Arduino is not found. SerialException: {e}')
        except Exception as e:
            print(f'An unexpected error occurred: {e}')

    def send(self, ar, s):
        ar.write(str.encode(s))
        time.sleep(0.5)

    def navi(self, data):
        print(f'data = {data}')

        if data == 'nb':
            self.send(self.ar, 'a') #Nyalakan lampu balkon
        elif data == 'mb':
            self.send(self.ar, 'b') #Matikan lampu balkon
        elif data == 'nd':
            self.send(self.ar, 'c') #Nyalakan lampu dapur
        elif data == 'md':
            self.send(self.ar, 'd') #Matikan lampu dapur
        elif data == 'nk':
            self.send(self.ar, 'e') #Nyalakan lampu kamar
        elif data == 'mk':
            self.send(self.ar, 'f') #Matikan lampu kamar
        elif data == 'np':
            self.send(self.ar, 'p') #Nyalakan proyektor
        elif data == 'mp':
            self.send(self.ar, 'q') #Matikan proyektor
        elif data == 'ns':
            self.send(self.ar, 's') #Nyalakan kipas
        elif data == 'ms':
            self.send(self.ar, 't') #Matikan kipas
        else:
            print('invalid')
    
    def num(self, data):
        for i in data:
            self.send(self.ar, i)

    def simple_run(self, data):
        print(data)
        if 'e' in data:
            print('closing capytant')
            self.ar.close()
            return '###'
        else:
            self.navi(data)
            return f'send {data}'
        
if '__name__' == '__main__':
    remote = simple_sender()