# encoding: utf-8
from suds.client import Client

class ConsumirAPI(object):    
    def consultarCEP(self, cep):
        url = "https://apps.correios.com.br/SigepMasterJPA/AtendeClienteService/AtendeCliente?wsdl"            
        cliente = Client(url)        
        
        try:
            retorno = cliente.service.consultaCEP(cep)
        except:
            retorno = ""
            
        return dict(retorno)