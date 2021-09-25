import numpy as np
import matplotlib.pyplot as plt
import click
CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.group(context_settings=CONTEXT_SETTINGS)

@click.version_option(version='1.0.0')

def cli():

    """
    This command line tool can be used to perform polynomial fitting experiments 
    as well as polynomial overfitting experiments. 
    Optionally, a *.txt file containing two columns of data can be 
    provided or the fitting experiments can be performed by choosing to 
    generate simulated random data.
    
    python poly_fit.py [OPTIONS] COMMAND [ARGS]

    """
    
    pass

@cli.command(context_settings=CONTEXT_SETTINGS)
@click.option('-method', default='0', required=True,
                type=click.Choice(['0', '1']), prompt=True, 
                help='Choose how the data is generated, 0 for Randomly generated data for fitting experiments 1 for data read form filename'
                )

@click.argument('orders', nargs=-1)
@click.option('--filename', default=' ', 
              help='Data source filename when method=1')

def fit(method,orders,filename):
    """
    Perform data fitting.\n
    method: Data source, \n
    orders: Polynomial orders to fit, \n
    filename:*.txt for data source
    if method==1
    
    """
    if method=='1':

        try:
            data=np.loadtxt(filename)
            x=data[:,0]
            y=data[:,1]
        except (IndexError,OSError,FileNotFoundError):
            click.echo(click.style(

            'Please input true filename',
            fg='red',bold=True))
        
            return
    else:
        x=np.linspace(0,1,num=64)
        gen_order=np.random.randint(3,8)
        p=np.random.randint(0,5,size=gen_order)
        
        if p[0]==0:
            p[0]=1
        p=np.poly1d(p)
        y=p(x)
        y=y+np.random.randn(len(x))*np.max(y)*0.1
        click.echo(click.style(

            'The polynomial order used to generate data this time is %d.\n'%gen_order,
            
            fg='green',bold=True))
    figure=plt.figure(figsize=(8,6))
    plt.scatter(x,y,alpha=0.5)
    if method=='0':
        plt.plot(x,p(x),label="True")
        
    for i in range(len(orders)):
        param=np.polyfit(x,y,int(orders[i]))
        p=np.poly1d(param)
        plt.plot(x,p(x),label="Fit order %s"%orders[i])
        
    plt.legend()
    plt.xlabel("x",fontsize=16)
    plt.ylabel("y",fontsize=16)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.legend(fontsize=16)
    plt.savefig("result.png",dpi=600)
    plt.show()
        
        
        



  

if __name__ == '__main__':

    cli()


