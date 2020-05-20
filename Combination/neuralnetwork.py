import pandas as pd

def main():
   df = pd.read_csv('InterpolatedWithCAPEX2.csv')
   df_N = pd.read_csv('InterpolatedNum.csv')
   max_D = {'D REVENUE':df['D REVENUE'].max(), 'U CR':df['U CR'].max(), 'D OE':df['D OE'].max(), 
      'D NOI':df['D NOI'].max(),'U CAPEX':df['U CAPEX'].max(), 'U CWK':df['U CWK'].max()} 
   min_D = {'D REVENUE':df['D REVENUE'].min(), 'U CR':df['U CR'].min(), 'D OE':df['D OE'].min(), 
      'D NOI':df['D NOI'].min(),'U CAPEX':df['U CAPEX'].min(), 'U CWK':df['U CWK'].min()}
   max_N = {'U REVENUE':df_N['U REVENUE'].max(), 'D CR':df_N['D CR'].max(), 'U OE':df_N['U OE'].max(), 
      'U NOI':df_N['U NOI'].max(),'D CAPEX':df_N['D CAPEX'].max(), 'D CWK':df_N['D CWK'].max()} 
   min_N = {'U REVENUE':df_N['U REVENUE'].min(), 'D CR':df_N['D CR'].min(), 'U OE':df_N['U OE'].min(), 
      'U NOI':df_N['U NOI'].min(),'D CAPEX':df_N['D CAPEX'].min(), 'D CWK':df_N['D CWK'].min()}
   
   filas_d, columnas_d = df.count()-1, len(df.columns)-1
   dataset_D = df.values
   #Variables a pasar a la funcion generate_population
   d_fcf = dataset_D[filas_d, columnas_d][1]
   filas_n, columnas_n = df_N.count()-1, len(df_N.columns)-1
   dataset_N = df_N.values
   u_fcf = dataset_N[filas_d, columnas_d][1]
   ##Falta idear una forma en la que se pueda pasar u_fcf y d_fcf a apply function que no se por parametro

   ##Calculo de las x
   x1 = df_N['U REVENUE'].corr(df_N['U FCF'])
   x2 = df_N['D CR'].corr(df_N['U FCF'])
   x3 = df_N['U OE'].corr(df_N['U FCF'])
   x4 = df_N['U NOI'].corr(df_N['U FCF'])
   x5 = df_N['D CAPEX'].corr(df_N['U FCF'])
   x6 = df_N['D CWK'].corr(df_N['U FCF'])
   x7 = df['D REVENUE'].corr(df['D FCF'])
   x8 = df['U CR'].corr(df['D FCF'])
   x9 = df['D OE'].corr(df['D FCF'])
   x10 = df['D NOI'].corr(df['D FCF'])
   x11 = df['U CAPEX'].corr(df['D FCF'])
   x12 = df['U CWK'].corr(df['D FCF'])

   print(u_fcf)



if __name__ == "__main__":
    main()
     