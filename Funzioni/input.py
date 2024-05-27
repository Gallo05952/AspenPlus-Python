class Input:

    def __init__(self, aspen):
        self.aspen=aspen

    def InserimentoMassaIn(self,Massa_ingresso):
        In_massa=self.aspen.Tree.FindNode(r"\Data\Streams\IN\Input\TOTFLOW\MIXED")
        In_massa.Value = Massa_ingresso

    def VerificaMassa(self,Massa_ingresso):
        MassaIn=self.aspen.Tree.FindNode(r"\Data\Streams\IN\Output\MASSFLMX\MIXED").Value
        if MassaIn==Massa_ingresso:
            return True
        else:
            return False
        
    def InserimentoPressioneIn(self,Pressione_ingresso):
        In=self.aspen.Tree.FindNode(r"\Data\Blocks\COMP\Input\PRES")
        In.Value = Pressione_ingresso

    def VerificaPressione(self,Pressione_ingresso):
        PressioneIn=self.aspen.Tree.FindNode(r"\Data\Streams\S9\Output\PRES_OUT\MIXED").Value
        if PressioneIn==Pressione_ingresso:
            return True
        else:
            return False
        
    def InserimentoTemperaturaCond(self,Temperatura_ingresso):
        In=self.aspen.Tree.FindNode(r"\Data\Blocks\COND\Input\VALUE")
        In.Value = Temperatura_ingresso


