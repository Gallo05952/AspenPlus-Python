class Output:

    def __init__(self, aspen):
        self.aspen=aspen

    def RecuperoRisultati(self):
        #check if the simulation is converged
        # converged=self.aspen.Engine.Converged
        # if converged==False:
        #     print("Errore: la simulazione non è convergente")
        #     return False
        # else:
            #recupero dei risultati
        try:
            P_out=self.aspen.Tree.FindNode(r"\Data\Streams\S9\Output\PRES_OUT\MIXED").Value
            Massa_out=self.aspen.Tree.FindNode(r"\Data\Streams\IN\Output\MASSFLMX\MIXED").Value
            T_out=self.aspen.Tree.FindNode(r"\Data\Streams\REFLUX\Output\TEMP_OUT\MIXED").Value
            FT123=self.aspen.Tree.FindNode(r"\Data\Streams\RIC-COL\Output\MASSFLMX\MIXED").Value
            FT120=self.aspen.Tree.FindNode(r"\Data\Streams\S6\Output\MASSFLMX\MIXED").Value
            FT201=self.aspen.Tree.FindNode(r"\Data\Streams\REFLUX\Output\MASSFLMX\MIXED").Value
            QReb_Scaldiglia=self.aspen.Tree.FindNode(r"\Data\Blocks\COLONNA\Output\REB_DUTY").Value/1000 #in kW
            QReb_Fascio=-(self.aspen.Tree.FindNode(r"\Data\Blocks\REB\Output\QCALC").Value/1000) #in kW    
            QCond=self.aspen.Tree.FindNode(r"\Data\Blocks\COND\Output\HX_DUTY").Value/1000 #in kW
            CapFactor=self.CapacityFactor()
            CO2_purity=self.aspen.Tree.FindNode(r"\Data\Streams\CO2LIQ\Output\MOLEFRAC\MIXED\CARBO-01").Value
            L_G=FT201/FT123
            risultati=[T_out, P_out, Massa_out, FT123, FT120, FT201, QReb_Scaldiglia, QReb_Fascio, QCond, CapFactor, CO2_purity, L_G]
            return risultati
        except Exception as e:
            print("Errore nel recupero dei risultati: ", e)
            return False
        
    def NumeroStadi(self):
        Numero_Stadi= self.aspen.Tree.FindNode(r"\Data\Blocks\COLONNA\Input\NSTAGE")
        NstadiV = Numero_Stadi.Value
        return NstadiV
    
    def CapacityFactor(self):
        Nstadi=self.NumeroStadi()
        CapN=self.aspen.Tree.FindNode(r"\Data\Blocks\COLONNA\Output\CA_FLD_FAC3\INT-1\CS-1").Elements.Item(Nstadi-2)
        Capacity1=self.aspen.Tree.FindNode(r"\Data\Blocks\COLONNA\Output\CA_FLD_FAC3\INT-1\CS-1").Elements.Item(0)
        CapN=CapN.Value
        Capacity1=Capacity1.Value
        CF=min(Capacity1,CapN)
        return CF