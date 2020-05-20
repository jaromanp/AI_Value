import pandas as pd

def main():
    df = pd.read_csv('InterpolatedWithCAPEX2.csv')

    max = {'D REVENUE':df['D REVENUE'].max(), 'U CR':df['U CR'].max(), 'D OE':df['D OE'].max(), 
       'D NOI':df['D NOI'].max(),'U CAPEX':df['U CAPEX'].max(), 'U CWK':df['U CWK'].max()} 
    min = {'D REVENUE':df['D REVENUE'].min(), 'U CR':df['U CR'].min(), 'D OE':df['D OE'].min(), 
       'D NOI':df['D NOI'].min(),'U CAPEX':df['U CAPEX'].min(), 'U CWK':df['U CWK'].min()} 
    filas, columnas = df.count()-1, len(df.columns)-1
    D_FCF = df.iloc[filas, columnas]
    print(D_FCF)

    #print(max['D REVENUE'])



if __name__ == "__main__":
    main()
     