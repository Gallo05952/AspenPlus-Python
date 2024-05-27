class DatiOut:

    def __init__(self):
        pass


    def StampaJson(self,nome_file,dati):
        import json
        file_json=nome_file+".json"
        with open(file_json, 'w') as file:
            json.dump(dati, file, indent=4)

    def StampaExcel(self,nome_file,dati):
        import pandas as pd
        file_excel=nome_file+".xlsx"
        # Define your column names here
        column_names = ["T Cond [°C]", "P Comp [barg]", "Portata in [kg/h]", "FT123 [kg/h]", "FT120 [kg/h]", "FT201 [kg/h]", "QReb Scaldiglia [kW]", "QReb Fascio [kW]", "QCond [kW]", "CapFactor", "CO2 Purity", "L/G Ratio"]

        df = pd.DataFrame(dati, columns=column_names)
        df.to_excel(file_excel, index=False)

    def generate_filename(self,base_name,path):
        import os
        counter = 0
        while True:
            filename = f"{base_name}V{counter}"
            json_file = os.path.join(path, f"{filename}.json")
            excel_file = os.path.join(path, f"{filename}.xlsx")
            if not os.path.exists(json_file) and not os.path.exists(excel_file):
                return filename
            counter += 1