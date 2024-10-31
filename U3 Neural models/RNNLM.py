import graphviz as G

# boolean variables to denote dense or sparse connections between layers
DENSE = True
SPARSE = False


TIMESTEPS = 5
TIME_OFFSET = 3
words=['&lt;s&gt;','the','house','is','blue','.']

unrolled = G.Digraph(node_attr={'shape':'circle', 'fixedsize':'true'}, graph_attr={'style':'invis', 'rankdir':'BT', 'color':'transparent'})

i=0
for step in range(TIMESTEPS+2):
    if step == 0 or step == TIMESTEPS+1:
        with unrolled.subgraph(name='cluster_'+str(i)) as c:
            c.node('a'+str(step), '', color='transparent')
            c.node('b'+str(step), '', color='transparent')
            c.node('c'+str(step), '', color='transparent') 
            c.node('d'+str(step), '', color='transparent')
            c.edge('a'+str(step), 'b'+str(step), style='invis') 
            c.edge('b'+str(step), 'c'+str(step), style='invis')
            c.edge('c'+str(step), 'd'+str(step), style='invis')
    else:
        with unrolled.subgraph(name='cluster_'+str(i)) as c:
            c.node('a'+str(step), words[TIMESTEPS-step], color='transparent');
            c.node('b'+str(step), 'WE')
            #c.node('c'+str(step), 't'+'{:=+d}'.format(TIME_OFFSET-step) if TIME_OFFSET-step else 't')
            c.node('c'+str(step), '')
            c.node('d'+str(step), 'SM');
            #c.node('e'+str(step), '<w<sub>'+'t'+'{:=+d}'.format(TIME_OFFSET-step+1)+'</sub>>' if TIME_OFFSET-step+1 else '<w<sub>'+'t'+'</sub>>', color='transparent');
            c.node('e'+str(step), words[TIMESTEPS-step+1], color='transparent');
            c.edge('a'+str(step), 'b'+str(step), label='<w<sub>'+'t'+'{:=+d}'.format(TIME_OFFSET-step)+'</sub>>' if TIME_OFFSET-step else '<w<sub>'+'t'+'</sub>>'); 
            c.edge('b'+str(step), 'c'+str(step), label='<e<sub>'+'t'+'{:=+d}'.format(TIME_OFFSET-step)+'</sub>>' if TIME_OFFSET-step else '<e<sub>'+'t'+'</sub>>'); 
            c.edge('c'+str(step), 'd'+str(step), label='<a<sub>'+'t'+'{:=+d}'.format(TIME_OFFSET-step)+'</sub>>' if TIME_OFFSET-step else '<a<sub>'+'t'+'</sub>>');
            c.edge('d'+str(step), 'e'+str(step), label='<y<sub>'+'t'+'{:=+d}'.format(TIME_OFFSET-step+1)+'</sub>>' if TIME_OFFSET-step+1 else '<y<sub>'+'t'+'</sub>>');
            
for step in range(1, TIMESTEPS+1):
    unrolled.edge('c'+str(step-1), 'c'+str(step), label='<h<sub>'+'t'+'{:=+d}'.format(TIME_OFFSET-step)+'</sub>>' if TIME_OFFSET-step else '<h<sub>'+'t'+'</sub>>', constraint='false', dir='back', color='black')

unrolled.render(filename='RNNLM', format='svg');
