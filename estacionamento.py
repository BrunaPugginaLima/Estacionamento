class Veiculo:
    def __init__(self, placa, estacionado):
        self.placa = placa
        self.estacionado = True
    def estacionar(self):
        self.estacionado = True
        print(f'Veículo da placa {self.placa} estacionado')  
    def sair_da_vaga(self):
        self.estacionado = False
        print(f'Veículo da placa {self.placa} saiu da vaga')    

class Carro(Veiculo):
    def __init__(self, placa, estacionado):
        super().__init__(placa, estacionado)  

class Moto(Veiculo):
    def __init__(self, placa, estacionado):
        super().__init__(placa, estacionado)  

class Vaga(Veiculo):
    def __init__(self, id, tipo, livre, placa) :
        self.id = id
        self.tipo = tipo
        self.livre = True
        self.placa = placa
    
    def ocupar(self,placa,tipo): 
        self.livre = False
        self.placa = placa
        self.tipo = tipo
        if tipo != 'Carro' and tipo != 'Moto' :
            print('Tipo não identificado')
        else:  
            print(f'Veículo do tipo {self.tipo}, de placa {self.placa} ocupou a vaga {self.id}')   

    def desocupar(self,placa,tipo): 
        self.livre = True
        self.placa = placa
        self.tipo = tipo
        if tipo != 'Carro' and tipo != 'Moto' :
            print('Tipo não identificado')
        else:  
            print(f'Veículo do tipo {self.tipo}, de placa {self.placa} saiu da vaga {self.id}')

class Estacionamento:
    def __init__(self,vagas_de_carro,vagas_de_moto,carro_para_vaga,moto_para_vaga,total_vagas_livres_carro,total_vagas_livres_moto):
        self.vagas_de_carro = int(vagas_de_carro)
        self.vagas_de_moto = int(vagas_de_moto)
        self.carro_para_vaga = int(carro_para_vaga)
        self.moto_para_vaga = int(moto_para_vaga)
        self.total_vagas_livres_carro = int(total_vagas_livres_carro)
        self.total_vagas_livres_moto = int(total_vagas_livres_moto)
    
    def estacionar_carro(self, carro: Carro):
        self.total_vagas_livres_carro = self.total_vagas_livres_carro -1
        if self.total_vagas_livres_carro <= 0 :
            self.total_vagas_livres_carro = 0
            print("Lamentamos o inconveniente, mas estamos sem vagas livres para carro!")
        else :
            print("Carro estacionado!")

    def estacionar_moto(self,veiculo: Veiculo):
        self.total_vagas_livres_moto = self.total_vagas_livres_moto -1
        if self.total_vagas_livres_moto <= 0 :
            self.total_vagas_livres_moto = 0
            if self.total_vagas_livres_carro > 0 :
                print("Moto estacionada em uma vaga para carro!") 
                self.total_vagas_livres_carro = self.total_vagas_livres_carro -1 
            else :
                print("Lamentamos o inconveniente, mas estamos sem vagas livres") 
        else :
            print("Moto estacionada!")
        
    def remover_carro(self):
        self.total_vagas_livres_carro = self.total_vagas_livres_carro +1
    def remover_moto(self):
        self.total_vagas_livres_moto = self.total_vagas_livres_moto +1
    def estado_do_estacionamento(self): 
        if self.total_vagas_livres_moto == 0 and self.total_vagas_livres_carro == 0 :
            print("ESTADO DO ESTACIONAMENTO : Estamos sem vagas livres") 
        else :
            print(f'ESTADO DO ESTACIONAMENTO : Estamos com {self.total_vagas_livres_carro} vagas para carro e {self.total_vagas_livres_moto} vagas para moto')

Moto1 = Moto('AAA0001', '') 
Moto1.sair_da_vaga() 
Carro1 = Carro('BBB0002', '') 
Carro1.estacionar()
Carro2 = Carro('CCC0003','')
Moto2 = Moto('DDD0004','')
Carro2.estacionar()
Carro2.sair_da_vaga()
Moto2.estacionar()

#Carro2 = Vaga('1','Carro','','AAA0002')
#Moto2 = Vaga('2','Moto','','BBB0001')
##Carro2.ocupar(Carro2.placa,Carro2.tipo)
#Moto2.desocupar(Moto2.placa,Moto2.tipo)

Este_estacionamento = Estacionamento('25', '25', '2', '3', '2', '0')
Este_estacionamento.estado_do_estacionamento()
Este_estacionamento.estacionar_carro(Carro1)
#Este_estacionamento.estacionar_carro(Carro2)
Este_estacionamento.estacionar_moto(Moto2)
Este_estacionamento.estado_do_estacionamento()