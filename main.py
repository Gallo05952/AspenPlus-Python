from Funzioni import *
import numpy as np
import os
# DEFINIZIONE DEL PATH DEL FILE ASPEN E APERTURA DELL'APPLICAZIONE
try:
    path=r"C:\Users\galloni\OneDrive - unibs.it\AB\Liquefazione\L_G\DISCO2VERY Prototipo.apwz"
    path_salvataggio=r"C:\Users\galloni\OneDrive - unibs.it\Corsi\Python\AspenPlus-Python\Risultati"
    aspen=AperturaAspen().apertura(path, visible=False)
except Exception as e:
    print("Errore nell'apertura di Aspen: ", e)

# DEFINIZIONE DELLE CONDIZIONI DI PROVA
portata_ingresso =np.linspace(150, 300, 11)
T_cond=-36
p_cond=np.linspace(14, 18, 11)
da_scrivere=[]
# CICLO DI SIMULAZIONE
Input(aspen).InserimentoTemperaturaCond(T_cond)
for portata in portata_ingresso:
    for pressione in p_cond:
        # INSERIMENTO DEI VALORI NEL FILE ASPEN
        Input(aspen).InserimentoMassaIn(portata)
        Input(aspen).InserimentoPressioneIn(pressione)

        # REINIZIALIZZAZIONE DELLA SIMULAZIONE E RUN
        try:
            aspen.Reinit()
            aspen.Engine.Run2()
            verifica_massa=Input(aspen).VerificaMassa(portata)
            if verifica_massa == False:
                print("Errore nell'inserimento della massa")
                break
            verifica_pressione=Input(aspen).VerificaPressione(pressione)
            if verifica_pressione == False:
                print("Errore nell'inserimento della pressione")
                break
        except Exception as e:
            print("Errore nel run della simulazione: ", e)
            break

        # RECUPERO DEI RISULTATI
        
        try:
            risultati=Output(aspen).RecuperoRisultati()
            if risultati==False:
                print("Errore nel recupero dei risultati")
                da_scrivere.append(None)
                break
            else:
                da_scrivere.append(risultati)
                print(risultati)
        except Exception as e:
            print("Errore nel recupero dei risultati: ", e)
            break

# STAMPA DEI RISULTATI SU UN FILE JSON E SU UN FILE EXCEL
try:
    base_name = f"Risultati_T={T_cond}_CO2in=5_"
    nome_file = DatiOut().generate_filename(base_name,path_salvataggio)
    nome_file = os.path.join(path_salvataggio, nome_file)
    DatiOut().StampaJson(nome_file,da_scrivere)
    DatiOut().StampaExcel(nome_file,da_scrivere)
except Exception as e:
    print("Errore nella scrittura dei risultati: ", e)
# CHIUSURA DEL FILE ASPEN
AperturaAspen().close(aspen)
